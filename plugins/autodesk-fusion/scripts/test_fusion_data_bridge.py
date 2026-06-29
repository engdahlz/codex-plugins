#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "mcp" / "fusion-data-auth-bridge"
sys.path.insert(0, str(BRIDGE))

from auth import AutodeskOAuth
from schemas import BridgeConfig
from token_store import TokenStore, redact
from server import call_tool, TOOLS


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        cfg = BridgeConfig(token_store_dir=tmp)
        store = TokenStore(Path(tmp))
        oauth = AutodeskOAuth(cfg, store)
        status = oauth.auth_status()
        assert status["ok"] is True
        assert status["configured"] is False
        store.save({"access_token": "secret-access", "refresh_token": "secret-refresh", "expires_in": 3600})
        redacted = store.redacted()
        assert redacted["access_token"] == "<redacted>"
        assert redacted["refresh_token"] == "<redacted>"
        assert "doctor" in TOOLS
        assert "list_hubs" in TOOLS
        result = call_tool("auth_status", {})
        assert "secret-access" not in json.dumps(result)
    print("OK: fusion-data-auth-bridge offline tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
