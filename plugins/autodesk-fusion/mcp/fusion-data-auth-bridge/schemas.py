from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
import ipaddress
import json
import os

PLUGIN_VERSION = "0.2.10"

ALLOWED_AUTODESK_HOSTS = {
    "developer.api.autodesk.com",
    "aps.autodesk.com",
}

BLOCKED_HOSTS = {
    "localhost",
    "0.0.0.0",
}


def _env_path(name: str) -> Path | None:
    value = os.environ.get(name, "").strip()
    if not value:
        return None
    return Path(os.path.expandvars(value)).expanduser()


def _default_plugin_root() -> Path:
    # schemas.py -> fusion-data-auth-bridge -> mcp -> autodesk-fusion
    return Path(__file__).resolve().parents[2]


def plugin_root() -> Path:
    return _env_path("PLUGIN_ROOT") or _env_path("CLAUDE_PLUGIN_ROOT") or _default_plugin_root()


def plugin_data() -> Path:
    return _env_path("PLUGIN_DATA") or _env_path("CLAUDE_PLUGIN_DATA") or plugin_root()


def resolve_config_path(path: str) -> Path:
    expanded = os.path.expandvars(path).replace("${PLUGIN_ROOT}", str(plugin_root())).replace("${PLUGIN_DATA}", str(plugin_data()))
    candidate = Path(expanded).expanduser()
    if not candidate.is_absolute():
        candidate = plugin_root() / candidate
    return candidate


@dataclass(frozen=True)
class BridgeConfig:
    client_id_env: str = "AUTODESK_CLIENT_ID"
    callback_port_env: str = "AUTODESK_CALLBACK_PORT"
    callback_port_default: int = 59595
    redirect_path: str = "/callback"
    auth_url: str = "https://developer.api.autodesk.com/authentication/v2/authorize"
    token_url: str = "https://developer.api.autodesk.com/authentication/v2/token"
    api_base_url: str = "https://developer.api.autodesk.com"
    scopes: list[str] = field(default_factory=lambda: ["data:read", "account:read"])
    token_store_dir: str = ".fusion-auth"
    mfgdm_graphql_url: str = ""
    mfgdm_schema_version: str = ""
    mfgdm_verified_at: str = ""
    mfgdm_allowed_queries_file: str = ""
    allow_unverified_urls: bool = False
    request_timeout_sec: int = 20
    retry_attempts: int = 2
    retry_base_delay_sec: float = 0.5
    page_limit_default: int = 50
    page_limit_max: int = 200
    pending_login_ttl_sec: int = 600

    @property
    def client_id(self) -> str:
        return os.environ.get(self.client_id_env, "").strip()

    @property
    def callback_port(self) -> int:
        value = os.environ.get(self.callback_port_env, "").strip()
        if value:
            return int(value)
        return int(self.callback_port_default)

    @property
    def redirect_uri(self) -> str:
        return f"http://127.0.0.1:{self.callback_port}{self.redirect_path}"

    @property
    def token_store_path(self) -> Path:
        raw = os.path.expandvars(self.token_store_dir)
        path = Path(raw).expanduser()
        if path.is_absolute():
            return path
        return plugin_data() / path

    @property
    def allowed_queries_path(self) -> Path | None:
        if not self.mfgdm_allowed_queries_file:
            return None
        return resolve_config_path(self.mfgdm_allowed_queries_file)

    @classmethod
    def load(cls, path: str | None = None) -> "BridgeConfig":
        selected = path or os.environ.get("AUTODESK_FUSION_DATA_BRIDGE_CONFIG", "")
        if selected:
            candidate = resolve_config_path(selected)
            if candidate.exists():
                raw = json.loads(candidate.read_text(encoding="utf-8"))
                allowed = {field.name for field in cls.__dataclass_fields__.values()}
                return cls(**{key: value for key, value in raw.items() if key in allowed})
        return cls()

    def validate_static_urls(self) -> dict[str, Any]:
        for label, value in {
            "auth_url": self.auth_url,
            "token_url": self.token_url,
            "api_base_url": self.api_base_url,
        }.items():
            verdict = validate_autodesk_url(value, allow_empty=False, allow_loopback=False)
            if not verdict["ok"]:
                return blocked("invalid_bridge_url", f"{label} is not an allowed Autodesk HTTPS URL.", field=label, value=value, validation=verdict)
        if self.mfgdm_graphql_url:
            verdict = validate_autodesk_url(value=self.mfgdm_graphql_url, allow_empty=True, allow_loopback=False, allow_unverified=self.allow_unverified_urls)
            if not verdict["ok"]:
                return blocked("invalid_mfgdm_url", "mfgdm_graphql_url must be an allowed Autodesk HTTPS URL unless allow_unverified_urls is explicitly true.", validation=verdict)
        return ok()

    def clamp_limit(self, value: Any | None) -> int:
        try:
            limit = int(value) if value is not None else int(self.page_limit_default)
        except (TypeError, ValueError):
            limit = int(self.page_limit_default)
        return max(1, min(limit, int(self.page_limit_max)))


def validate_autodesk_url(value: str, *, allow_empty: bool = False, allow_loopback: bool = False, allow_unverified: bool = False) -> dict[str, Any]:
    if not value:
        return ok() if allow_empty else blocked("empty_url")
    parsed = urlparse(value)
    if parsed.scheme != "https":
        if not (allow_loopback and parsed.scheme == "http" and parsed.hostname in {"127.0.0.1", "localhost"}):
            return blocked("non_https_url")
    host = (parsed.hostname or "").lower()
    if not host:
        return blocked("missing_host")
    if host in BLOCKED_HOSTS and not allow_loopback:
        return blocked("blocked_host")
    try:
        ip = ipaddress.ip_address(host)
        if not allow_loopback and (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved):
            return blocked("blocked_ip_range")
    except ValueError:
        pass
    if allow_unverified:
        return ok({"unverifiedUrlAllowed": True})
    if host not in ALLOWED_AUTODESK_HOSTS and not any(host.endswith(f".{suffix}") for suffix in ALLOWED_AUTODESK_HOSTS):
        return blocked("host_not_allowlisted", allowedHosts=sorted(ALLOWED_AUTODESK_HOSTS))
    return ok()


def ok(data: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"ok": True, **(data or {})}


def blocked(reason: str, next_step: str | None = None, **extra: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {"ok": False, "blocked": True, "reason": reason}
    if next_step:
        payload["nextStep"] = next_step
    payload.update(extra)
    return payload
