#!/usr/bin/env python3
"""Autodesk Fusion runtime doctor for Codex.

Passive checks only: no Fusion model mutation, no OAuth token capture.
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import time
from pathlib import Path
from urllib import request, error

DEFAULT_DESKTOP_URL = "http://127.0.0.1:27182/mcp"
DEFAULT_DATA_URL = "https://developer.api.autodesk.com/fusion/mcp"
PRODUCT_HELP_URL = "https://developer.api.autodesk.com/knowledge/public/v1/mcp"


def tcp_check(host: str, port: int, timeout: float = 2.0) -> dict:
    started = time.time()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return {"ok": True, "latencyMs": round((time.time() - started) * 1000)}
    except OSError as exc:
        return {"ok": False, "error": str(exc)}


def http_probe(url: str, timeout: float = 5.0) -> dict:
    started = time.time()
    req = request.Request(url, method="GET")
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return {"ok": True, "status": resp.status, "latencyMs": round((time.time() - started) * 1000)}
    except error.HTTPError as exc:
        return {"ok": exc.code < 500, "status": exc.code, "note": "HTTP response received"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--desktop-url", default=DEFAULT_DESKTOP_URL)
    parser.add_argument("--data-url", default=DEFAULT_DATA_URL)
    parser.add_argument("--product-help-url", default=PRODUCT_HELP_URL)
    parser.add_argument("--json-out", default=None)
    args = parser.parse_args()

    desktop = tcp_check("127.0.0.1", 27182)
    report = {
        "schemaVersion": "fusion-doctor-v1",
        "checks": {
            "fusionDesktopMcpTcp": desktop,
            "fusionDesktopMcpHttp": http_probe(args.desktop_url),
            "fusionDataMcpHttp": http_probe(args.data_url),
            "productHelpMcpHttp": http_probe(args.product_help_url),
        },
        "notes": [
            "Desktop MCP requires Fusion running and MCP enabled in Fusion Preferences > General > API.",
            "Data MCP may require Autodesk OAuth even when the HTTP endpoint is reachable.",
            "This script is passive and does not mutate Fusion documents."
        ]
    }

    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if args.json_out:
        Path(args.json_out).write_text(text + "\n", encoding="utf-8")
    return 0 if any(v.get("ok") for v in report["checks"].values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
