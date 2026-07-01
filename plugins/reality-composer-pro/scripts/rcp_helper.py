#!/usr/bin/env python3
"""Standard-library stdio MCP helper for the RealityComposerPro Codex plugin."""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any

from rcp_tools import (
    asset_audit,
    generate_checklist,
    gitignore_suggestions,
    mcp_candidate_report,
    plan_task,
    project_doctor,
    reference_get,
    release_notes_plan,
    search_docs,
    sidebar_map,
    swift_scaffold,
)

PROTOCOL_VERSION = "2024-11-05"

TOOLS: dict[str, dict[str, Any]] = {
    "rcp_doc_search": {"description": "Search bundled RealityComposerPro references.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}, "limit": {"type": "integer", "default": 8}}, "required": ["query"]}},
    "rcp_reference_get": {"description": "Return one bundled reference entry by id.", "inputSchema": {"type": "object", "properties": {"topic_id": {"type": "string"}}, "required": ["topic_id"]}},
    "rcp_docs_sidebar_map": {"description": "Return the Reality Composer Pro documentation sidebar section map used by skills.", "inputSchema": {"type": "object", "properties": {}}},
    "rcp_release_notes_plan": {"description": "Return release-note sources and extraction checklist for a symptom.", "inputSchema": {"type": "object", "properties": {"symptom": {"type": "string", "default": ""}}}},
    "rcp_mcp_candidates": {"description": "List candidate third-party Apple documentation MCP/RAG servers and review criteria.", "inputSchema": {"type": "object", "properties": {}}},
    "rcp_project_doctor": {"description": "Inspect a local RCP/RealityKit/Xcode project.", "inputSchema": {"type": "object", "properties": {"root_path": {"type": "string", "default": "."}}}},
    "rcp_asset_audit": {"description": "Summarize USD, model, image, audio, video, and RealityKit assets.", "inputSchema": {"type": "object", "properties": {"root_path": {"type": "string", "default": "."}}}},
    "rcp_swift_scaffold": {"description": "Return Swift scaffolding snippets.", "inputSchema": {"type": "object", "properties": {"kind": {"type": "string", "default": "custom-component-plugin"}, "type_name": {"type": "string", "default": "Example"}, "module_name": {"type": "string", "default": "RealityContent"}}}},
    "rcp_generate_checklist": {"description": "Generate a workflow checklist.", "inputSchema": {"type": "object", "properties": {"workflow": {"type": "string", "default": "scene"}, "target": {"type": "string", "default": "Reality Composer Pro scene"}}}},
    "rcp_plan_task": {"description": "Turn a broad user task into a safe RCP implementation plan.", "inputSchema": {"type": "object", "properties": {"task": {"type": "string"}, "target_platform": {"type": "string", "default": "visionOS"}, "autonomy": {"type": "string", "default": "high"}}, "required": ["task"]}},
    "rcp_gitignore_suggestions": {"description": "Suggest git hygiene rules for RCP/RealityKit projects.", "inputSchema": {"type": "object", "properties": {"root_path": {"type": "string", "default": "."}}}},
}


def call_tool(name: str, args: dict[str, Any]) -> str:
    args = args or {}
    if name == "rcp_doc_search": return search_docs(str(args.get("query", "")), int(args.get("limit", 8)))
    if name == "rcp_reference_get": return reference_get(str(args.get("topic_id", "")))
    if name == "rcp_docs_sidebar_map": return sidebar_map()
    if name == "rcp_release_notes_plan": return release_notes_plan(str(args.get("symptom", "")))
    if name == "rcp_mcp_candidates": return mcp_candidate_report()
    if name == "rcp_project_doctor": return project_doctor(args.get("root_path") or ".")
    if name == "rcp_asset_audit": return asset_audit(args.get("root_path") or ".")
    if name == "rcp_swift_scaffold": return swift_scaffold(str(args.get("kind", "custom-component-plugin")), str(args.get("type_name", "Example")), str(args.get("module_name", "RealityContent")))
    if name == "rcp_generate_checklist": return generate_checklist(str(args.get("workflow", "scene")), str(args.get("target", "Reality Composer Pro scene")))
    if name == "rcp_plan_task": return plan_task(str(args.get("task", "")), str(args.get("target_platform", "visionOS")), str(args.get("autonomy", "high")))
    if name == "rcp_gitignore_suggestions": return gitignore_suggestions(args.get("root_path") or ".")
    raise ValueError("Unknown tool: " + str(name))


class Transport:
    def __init__(self) -> None:
        self.framed: bool | None = None

    def read(self) -> dict[str, Any] | None:
        line = sys.stdin.buffer.readline()
        while line in (b"\n", b"\r\n"):
            line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line.lower().startswith(b"content-length:"):
            self.framed = True
            length = int(line.split(b":", 1)[1].strip())
            while True:
                header = sys.stdin.buffer.readline()
                if header in (b"\r\n", b"\n", b""):
                    break
                if header.lower().startswith(b"content-length:"):
                    length = int(header.split(b":", 1)[1].strip())
            return json.loads(sys.stdin.buffer.read(length).decode("utf-8"))
        self.framed = False if self.framed is None else self.framed
        return json.loads(line.decode("utf-8"))

    def write(self, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        if self.framed:
            sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii") + body)
        else:
            sys.stdout.buffer.write(body + b"\n")
        sys.stdout.buffer.flush()


def handle(message: dict[str, Any]) -> dict[str, Any] | None:
    method = message.get("method")
    msg_id = message.get("id")
    if msg_id is None:
        return None
    params = message.get("params") or {}
    try:
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": msg_id, "result": {"protocolVersion": params.get("protocolVersion", PROTOCOL_VERSION), "capabilities": {"tools": {"listChanged": False}}, "serverInfo": {"name": "reality-composer-pro", "version": "0.2.0"}}}
        if method == "tools/list":
            return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": name, **meta} for name, meta in TOOLS.items()]}}
        if method == "tools/call":
            text = call_tool(str(params.get("name", "")), params.get("arguments") or {})
            return {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": text}], "isError": False}}
        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found: " + str(method)}}
    except Exception as exc:
        return {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32000, "message": str(exc)}}


def self_test() -> int:
    for req in [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "rcp_docs_sidebar_map", "arguments": {}}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "rcp_release_notes_plan", "arguments": {"symptom": "preview crash"}}},
    ]:
        print(json.dumps(handle(req), indent=2, ensure_ascii=False)[:4000])
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="RealityComposerPro Codex MCP helper")
    parser.add_argument("--self-test", action="store_true")
    parser.parse_known_args()
    if "--self-test" in sys.argv:
        return self_test()
    transport = Transport()
    while True:
        message = transport.read()
        if message is None:
            return 0
        response = handle(message)
        if response is not None:
            transport.write(response)

if __name__ == "__main__":
    raise SystemExit(main())
