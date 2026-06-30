from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import os
import stat
import tempfile
import time

SENSITIVE_EXACT = {
    "access_token",
    "refresh_token",
    "id_token",
    "client_secret",
    "authorization",
    "code_verifier",
    "verifier",
    "password",
}


def _private_file_mode() -> int:
    return stat.S_IRUSR | stat.S_IWUSR


class TokenStore:
    def __init__(self, root: Path):
        self.root = root
        self.path = root / "autodesk_tokens.json"

    def ensure_root(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(self.root, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        except OSError:
            pass

    def exists(self) -> bool:
        return self.path.exists()

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            return {"_store_corrupt": True, "_store_error": str(exc)}

    def save(self, tokens: dict[str, Any]) -> None:
        self.ensure_root()
        now = time.time()
        payload = {**tokens, "updated_at": now}
        payload.setdefault("created_at", now)
        self.write_private_json(self.path, payload)

    def write_private_json(self, path: Path, payload: dict[str, Any]) -> None:
        self.ensure_root()
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, indent=2, sort_keys=True)
                handle.write("\n")
            os.chmod(tmp_name, _private_file_mode())
            os.replace(tmp_name, path)
            try:
                os.chmod(path, _private_file_mode())
            except OSError:
                pass
        finally:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)

    def read_private_json(self, path: Path) -> dict[str, Any]:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            return {"_store_corrupt": True, "_store_error": str(exc)}

    def clear(self) -> bool:
        if self.path.exists():
            self.path.unlink()
            return True
        return False

    def redacted(self) -> dict[str, Any]:
        return redact(self.load())


def _is_sensitive_key(key: str, value: Any) -> bool:
    lower = key.lower().replace("-", "_")
    if lower in SENSITIVE_EXACT:
        return True
    if not isinstance(value, str):
        return False
    return lower.endswith("_token") or lower.endswith("token") or "secret" in lower or "password" in lower or "authorization" in lower or "verifier" in lower


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if _is_sensitive_key(str(key), item):
                out[key] = "<redacted>" if item else ""
            else:
                out[key] = redact(item)
        return out
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value
