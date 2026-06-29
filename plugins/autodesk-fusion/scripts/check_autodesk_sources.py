#!/usr/bin/env python3
"""Passive source watcher for key Autodesk/OpenAI/MCP URLs."""

from __future__ import annotations

import json
from urllib import request, error

URLS = [
    "https://aps.autodesk.com/developer/overview/autodesk-fusion-api",
    "https://help.autodesk.com/view/fusion360/ENU/?contextId=APIWhatsNew",
    "https://github.com/AutodeskFusion360/FusionAPIReference",
    "https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW",
    "https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_KnowledgeMcp_autodesk_product_help_mcp_server_html",
    "https://help.autodesk.com/view/ADSKMCP/ENU/?guid=ADSKMCP_FusionCloudMcp_autodesk_fusion_data_mcp_server_html",
    "https://developers.openai.com/codex/plugins/build",
    "https://developers.openai.com/codex/mcp",
    "https://modelcontextprotocol.io/specification/2025-11-25"
]


def check(url: str) -> dict:
    try:
        req = request.Request(url, method="HEAD")
        with request.urlopen(req, timeout=10) as resp:
            return {"url": url, "ok": True, "status": resp.status, "etag": resp.headers.get("ETag"), "lastModified": resp.headers.get("Last-Modified")}
    except error.HTTPError as exc:
        return {"url": url, "ok": exc.code < 500, "status": exc.code}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "ok": False, "error": str(exc)}


print(json.dumps([check(url) for url in URLS], indent=2, sort_keys=True))
