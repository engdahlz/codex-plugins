from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from urllib import parse, request, error
import base64
import hashlib
import json
import secrets
import time

from schemas import BridgeConfig, blocked, ok
from token_store import TokenStore, redact


@dataclass
class LoginState:
    verifier: str
    challenge: str
    state: str
    authorization_url: str


class AutodeskOAuth:
    def __init__(self, config: BridgeConfig, store: TokenStore):
        self.config = config
        self.store = store
        self._pending_path = store.root / "pending_login.json"

    def auth_status(self) -> dict[str, Any]:
        tokens = self.store.load()
        configured = bool(self.config.client_id)
        expires_at = tokens.get("expires_at")
        expired = bool(expires_at and time.time() > float(expires_at))
        return ok({
            "configured": configured,
            "clientIdEnv": self.config.client_id_env,
            "tokenPresent": bool(tokens.get("access_token")),
            "refreshTokenPresent": bool(tokens.get("refresh_token")),
            "expired": expired,
            "tokenStore": str(self.store.path),
            "tokens": redact(tokens)
        })

    def start_login(self) -> dict[str, Any]:
        if not self.config.client_id:
            return blocked(
                "missing_client_id",
                f"Set {self.config.client_id_env} to an Autodesk APS public OAuth client id."
            )
        verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).decode().rstrip("=")
        challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
        state = secrets.token_urlsafe(32)
        params = {
            "response_type": "code",
            "client_id": self.config.client_id,
            "redirect_uri": self.config.redirect_uri,
            "scope": " ".join(self.config.scopes),
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256"
        }
        url = f"{self.config.auth_url}?{parse.urlencode(params)}"
        self.store.root.mkdir(parents=True, exist_ok=True)
        self._pending_path.write_text(json.dumps({
            "verifier": verifier,
            "state": state,
            "redirect_uri": self.config.redirect_uri,
            "created_at": time.time()
        }, indent=2) + "\n", encoding="utf-8")
        return ok({
            "authorizationUrl": url,
            "redirectUri": self.config.redirect_uri,
            "state": state,
            "instructions": "Open authorizationUrl, sign in, then call complete_login_if_needed with the returned code and state. Tokens are stored locally and redacted from outputs."
        })

    def complete_login(self, code: str | None = None, state: str | None = None) -> dict[str, Any]:
        if not code:
            return blocked("missing_authorization_code", "Call start_login, authorize in browser, then pass the returned code.")
        if not self._pending_path.exists():
            return blocked("missing_pending_login", "Call start_login before completing login.")
        pending = json.loads(self._pending_path.read_text(encoding="utf-8"))
        if state and state != pending.get("state"):
            return blocked("state_mismatch", "Restart login; returned OAuth state did not match pending state.")
        data = parse.urlencode({
            "grant_type": "authorization_code",
            "client_id": self.config.client_id,
            "code_verifier": pending["verifier"],
            "code": code,
            "redirect_uri": pending["redirect_uri"]
        }).encode()
        req = request.Request(self.config.token_url, data=data, method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"})
        try:
            with request.urlopen(req, timeout=self.config.request_timeout_sec) as resp:
                tokens = json.loads(resp.read().decode())
        except error.HTTPError as exc:
            detail = exc.read().decode(errors="replace")[:1000]
            return blocked("token_exchange_failed", "Check Autodesk OAuth app redirect URI, scopes, and client id.", status=exc.code, detail=detail)
        except Exception as exc:  # noqa: BLE001
            return blocked("token_exchange_error", str(exc))
        if "expires_in" in tokens:
            tokens["expires_at"] = time.time() + int(tokens.get("expires_in", 0)) - 60
        self.store.save(tokens)
        self._pending_path.unlink(missing_ok=True)
        return ok({"tokenStored": True, "tokens": redact(tokens)})

    def get_access_token(self) -> str | None:
        tokens = self.store.load()
        token = tokens.get("access_token")
        if token and not self._is_expired(tokens):
            return token
        if tokens.get("refresh_token"):
            refreshed = self.refresh()
            if refreshed.get("ok"):
                return self.store.load().get("access_token")
        return token

    def refresh(self) -> dict[str, Any]:
        tokens = self.store.load()
        refresh_token = tokens.get("refresh_token")
        if not refresh_token:
            return blocked("missing_refresh_token", "Run start_login again.")
        data = parse.urlencode({
            "grant_type": "refresh_token",
            "client_id": self.config.client_id,
            "refresh_token": refresh_token
        }).encode()
        req = request.Request(self.config.token_url, data=data, method="POST", headers={"Content-Type": "application/x-www-form-urlencoded"})
        try:
            with request.urlopen(req, timeout=self.config.request_timeout_sec) as resp:
                updated = json.loads(resp.read().decode())
        except Exception as exc:  # noqa: BLE001
            return blocked("refresh_failed", str(exc))
        tokens.update(updated)
        if "expires_in" in updated:
            tokens["expires_at"] = time.time() + int(updated.get("expires_in", 0)) - 60
        self.store.save(tokens)
        return ok({"refreshed": True, "tokens": redact(tokens)})

    def logout_local(self) -> dict[str, Any]:
        removed = self.store.clear()
        self._pending_path.unlink(missing_ok=True)
        return ok({"removedLocalTokens": removed})

    @staticmethod
    def _is_expired(tokens: dict[str, Any]) -> bool:
        expires_at = tokens.get("expires_at")
        return bool(expires_at and time.time() > float(expires_at))
