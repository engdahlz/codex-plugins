#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from aps_client import APSClient
from auth import AutodeskOAuth
from mfgdm_client import MFGDMClient
from schemas import BridgeConfig, blocked, ok
from token_store import TokenStore

CONFIG = BridgeConfig.load()
STORE = TokenStore(CONFIG.token_store_path)
AUTH = AutodeskOAuth(CONFIG, STORE)
APS = APSClient(CONFIG, AUTH.get_access_token)
MFGDM = MFGDMClient(CONFIG, AUTH.get_access_token)

TOOLS = {
    "auth_status": "Return local bridge auth/config status without exposing tokens.",
    "start_login": "Create an Autodesk OAuth PKCE authorization URL.",
    "complete_login_if_needed": "Complete OAuth token exchange from an authorization code.",
    "logout_local": "Remove only local bridge tokens and pending-login state.",
    "list_hubs": "Read Autodesk hubs through APS Data Management.",
    "list_projects": "Read projects for a hub_id.",
    "list_top_folders": "Read top folders for hub_id and project_id.",
    "list_folder_contents": "Read folder contents for project_id and folder_id.",
    "get_item_versions": "Read item versions for project_id and item_id.",
    "get_version_metadata": "Read version metadata for project_id and version_id.",
    "get_mfgdm_design_summary": "Read minimal MFGDM design summary when endpoint is configured.",
    "get_mfgdm_component_hierarchy": "Read MFGDM component hierarchy when endpoint/schema are configured.",
    "doctor": "Check bridge config, token status, and likely next steps."
}


def tool_schema(name: str, description: str) -> dict[str, Any]:
    props: dict[str, Any] = {}
    required: list[str] = []
    if name == "complete_login_if_needed":
        props = {"code": {"type": "string"}, "state": {"type": "string"}}
        required = ["code"]
    elif name == "list_projects":
        props = {"hub_id": {"type": "string"}}
        required = ["hub_id"]
    elif name == "list_top_folders":
        props = {"hub_id": {"type": "string"}, "project_id": {"type": "string"}}
        required = ["hub_id", "project_id"]
    elif name == "list_folder_contents":
        props = {"project_id": {"type": "string"}, "folder_id": {"type": "string"}}
        required = ["project_id", "folder_id"]
    elif name == "get_item_versions":
        props = {"project_id": {"type": "string"}, "item_id": {"type": "string"}}
        required = ["project_id", "item_id"]
    elif name == "get_version_metadata":
        props = {"project_id": {"type": "string"}, "version_id": {"type": "string"}}
        required = ["project_id", "version_id"]
    elif name in {"get_mfgdm_design_summary", "get_mfgdm_component_hierarchy"}:
        props = {"design_id": {"type": "string"}}
        required = ["design_id"]
    return {"name": name, "description": description, "inputSchema": {"type": "object", "properties": props, "required": required}}


def call_tool(name: str, args: dict[str, Any]) -> dict[str, Any]:
    if name == "auth_status":
        return AUTH.auth_status()
    if name == "start_login":
        return AUTH.start_login()
    if name == "complete_login_if_needed":
        return AUTH.complete_login(args.get("code"), args.get("state"))
    if name == "logout_local":
        return AUTH.logout_local()
    if name == "list_hubs":
        return APS.list_hubs()
    if name == "list_projects":
        return APS.list_projects(args.get("hub_id", ""))
    if name == "list_top_folders":
        return APS.list_top_folders(args.get("hub_id", ""), args.get("project_id", ""))
    if name == "list_folder_contents":
        return APS.list_folder_contents(args.get("project_id", ""), args.get("folder_id", ""))
    if name == "get_item_versions":
        return APS.get_item_versions(args.get("project_id", ""), args.get("item_id", ""))
    if name == "get_version_metadata":
        return APS.get_version_metadata(args.get("project_id", ""), args.get("version_id", ""))
    if name == "get_mfgdm_design_summary":
        return MFGDM.design_summary(args.get("design_id", ""))
    if name == "get_mfgdm_component_hierarchy":
        return MFGDM.component_hierarchy(args.get("design_id", ""))
    if name == "doctor":
        status = AUTH.auth_status()
        return ok({"config": {"apiBaseUrl": CONFIG.api_base_url, "tokenStore": str(CONFIG.token_store_path), "mfgdmConfigured": bool(CONFIG.mfgdm_graphql_url)}, "auth": status})
    return blocked("unknown_tool", f"Unknown tool: {name}")


def read_message() -> dict[str, Any] | None:
    header = b""
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        header += line
    length = None
    for raw in header.decode(errors="replace").splitlines():
        if raw.lower().startswith("content-length:"):
            length = int(raw.split(":", 1)[1].strip())
    if length is None:
        return None
    body = sys.stdin.buffer.read(length)
    return json.loads(body.decode())


def write_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, separators=(",", ":")).encode()
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode() + body)
    sys.stdout.buffer.flush()


def result(message_id: Any, value: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "result": value}


def error_response(message_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": message_id, "error": {"code": code, "message": message}}


def handle(msg: dict[str, Any]) -> dict[str, Any] | None:
    method = msg.get("method")
    message_id = msg.get("id")
    params = msg.get("params") or {}
    if method == "initialize":
        return result(message_id, {"protocolVersion": "2025-11-25", "capabilities": {"tools": {}}, "serverInfo": {"name": "autodesk-fusion-data-bridge", "version": "0.2.6"}})
    if method in {"notifications/initialized", "initialized"}:
        return None
    if method == "tools/list":
        return result(message_id, {"tools": [tool_schema(name, description) for name, description in TOOLS.items()]})
    if method == "tools/call":
        name = params.get("name", "")
        args = params.get("arguments") or {}
        payload = call_tool(name, args)
        return result(message_id, {"content": [{"type": "text", "text": json.dumps(payload, indent=2, sort_keys=True)}], "isError": not payload.get("ok", False)})
    return error_response(message_id, -32601, f"Unsupported method: {method}")


def main() -> int:
    while True:
        msg = read_message()
        if msg is None:
            return 0
        response = handle(msg)
        if response is not None and "id" in msg:
            write_message(response)


if __name__ == "__main__":
    raise SystemExit(main())
