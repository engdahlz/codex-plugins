#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import rcp_tools

try:
    from mcp.server.fastmcp import FastMCP
except Exception as exc:
    raise SystemExit("Install Python package mcp to run this helper") from exc

app = FastMCP("reality-composer-pro")

@app.tool()
def rcp_doc_search(query: str, limit: int = 8):
    return rcp_tools.doc_search(query, limit)

@app.tool()
def rcp_reference_get(ref_id: str):
    return rcp_tools.reference_get(ref_id) or {"error": "not found"}

@app.tool()
def rcp_project_doctor(path: str = "."):
    return rcp_tools.project_doctor(path)

@app.tool()
def rcp_asset_audit(path: str = "."):
    return rcp_tools.asset_audit(path)

@app.tool()
def rcp_swift_scaffold(kind: str = "RealityView"):
    return rcp_tools.swift_scaffold(kind)

@app.tool()
def rcp_generate_checklist(topic: str = "project"):
    return rcp_tools.checklist(topic)

@app.tool()
def rcp_plan_task(task: str):
    return rcp_tools.checklist(task) + ["Implement the smallest safe change.", "Record files changed and manual RCP editor steps."]

@app.tool()
def rcp_gitignore_suggestions():
    return ["DerivedData/", ".build/", "*.xcuserstate", "*.xcuserdata/", "*.reality", ".DS_Store"]

if __name__ == "__main__":
    app.run()
