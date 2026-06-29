from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import os
import stat

SENSITIVE_KEYS = {"access_token", "refresh_token", "id_token", "client_secret"}


class TokenStore:
    def __init__(self, root: Path):
        self.root = root
        self.path = root / "autodesk_tokens.json"

    def exists(self) -> bool:
        return self.path.exists()

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, tokens: dict[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(tokens, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        try:
            os.chmod(self.path, stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass

    def clear(self) -> bool:
        if self.path.exists():
            self.path.unlink()
            return True
        return False

    def redacted(self) -> dict[str, Any]:
        return redact(self.load())


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key in SENSITIVE_KEYS:
                out[key] = "<redacted>" if item else ""
            else:
                out[key] = redact(item)
        return out
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value
