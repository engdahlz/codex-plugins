#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "mcp" / "fusion-data-auth-bridge"
sys.path.insert(0, str(BRIDGE))

from auth import AutodeskOAuth
from schemas import BridgeConfig, PLUGIN_VERSION
from token_store import TokenStore, redact
from server import TOOLS, call_tool


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["PLUGIN_DATA"] = tmp
        cfg = BridgeConfig(token_store_dir=".fusion-auth", pending_login_ttl_sec=1)
        store = TokenStore(cfg.token_store_path)
        oauth = AutodeskOAuth(cfg, store)

        status = oauth.auth_status()
        assert status["ok"] is True
        assert status["configured"] is False
        assert status["needsLogin"] is True

        sample = redact({"nested": {"apiToken": "abc"}})
        assert sample["nested"]["apiToken"] == "<redacted>"

        assert "doctor" in TOOLS
        assert "list_hubs" in TOOLS

        missing_state = oauth.complete_login(code="abc", state=None)
        assert missing_state["reason"] == "missing_oauth_state"

        start_without_client = oauth.start_login()
        assert start_without_client["reason"] == "missing_client_id"

        store.write_private_json(oauth._pending_path, {"verifier": "v", "state": "expected", "redirect_uri": cfg.redirect_uri, "created_at": time.time() - 5})
        expired = oauth.complete_login(code="abc", state="expected")
        assert expired["reason"] == "pending_login_expired"

        assert PLUGIN_VERSION == "0.2.10"
        assert call_tool("auth_status", {})["ok"] is True
    print("OK: fusion-data-auth-bridge offline tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
