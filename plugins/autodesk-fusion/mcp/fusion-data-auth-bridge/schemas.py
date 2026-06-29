from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json
import os


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
    request_timeout_sec: int = 20

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
        return Path(self.token_store_dir)

    @classmethod
    def load(cls, path: str | None = None) -> "BridgeConfig":
        selected = path or os.environ.get("AUTODESK_FUSION_DATA_BRIDGE_CONFIG", "")
        if selected and Path(selected).exists():
            raw = json.loads(Path(selected).read_text(encoding="utf-8"))
            allowed = {field.name for field in cls.__dataclass_fields__.values()}
            return cls(**{key: value for key, value in raw.items() if key in allowed})
        return cls()


def ok(data: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"ok": True, **(data or {})}


def blocked(reason: str, next_step: str | None = None, **extra: Any) -> dict[str, Any]:
    payload: dict[str, Any] = {"ok": False, "blocked": True, "reason": reason}
    if next_step:
        payload["nextStep"] = next_step
    payload.update(extra)
    return payload
