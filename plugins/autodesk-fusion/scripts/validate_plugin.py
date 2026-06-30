#!/usr/bin/env python3
"""Passive validation helper for Fusion Developer."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLUGIN = ROOT / "plugins" / "autodesk-fusion"
BRIDGE = PLUGIN / "mcp" / "fusion-data-auth-bridge"
VERSION = (PLUGIN / "VERSION").read_text(encoding="utf-8").strip()

required = [
    PLUGIN / "VERSION",
    PLUGIN / ".codex-plugin" / "plugin.json",
    PLUGIN / ".mcp.json",
    PLUGIN / "skills",
    BRIDGE / "server.py",
    BRIDGE / "auth.py",
    BRIDGE / "token_store.py",
    BRIDGE / "aps_client.py",
    BRIDGE / "mfgdm_client.py",
    BRIDGE / "schemas.py",
    BRIDGE / "config.example.json",
    ROOT / ".agents" / "plugins" / "marketplace.json",
    ROOT / ".codex-plugin" / "marketplace.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "marketplace.json",
    ROOT / "scripts" / "sync_marketplaces.py",
    PLUGIN / "assets" / "icon.png",
    PLUGIN / "assets" / "logo.png",
    PLUGIN / "assets" / "screenshot-marketplace.png",
]

for path in required:
    if not path.exists():
        raise SystemExit(f"Missing: {path}")

if not re.match(r"^\d+\.\d+\.\d+$", VERSION):
    raise SystemExit(f"Invalid VERSION: {VERSION}")

plugin = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
mcp = json.loads((PLUGIN / ".mcp.json").read_text())
canonical = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())

if plugin["name"] != "autodesk-fusion":
    raise SystemExit("Unexpected plugin name")
if plugin.get("version") != VERSION:
    raise SystemExit(f"Plugin version {plugin.get('version')} does not match VERSION {VERSION}")
if plugin.get("mcpServers") != "./.mcp.json":
    raise SystemExit("Plugin manifest must reference bundled ./.mcp.json")
if plugin.get("interface", {}).get("displayName") != "Fusion Developer":
    raise SystemExit("Expected displayName Fusion Developer")

servers = mcp.get("mcp_servers", {})
for name in ["autodesk-product-help", "autodesk-fusion-desktop", "autodesk-fusion-data", "autodesk-fusion-data-bridge"]:
    if name not in servers:
        raise SystemExit(f"Missing MCP server: {name}")
    if not servers[name].get("enabled"):
        raise SystemExit(f"Expected MCP server enabled: {name}")

bridge = servers["autodesk-fusion-data-bridge"]
if bridge.get("command") not in {"python3", "python"}:
    raise SystemExit("Bridge MCP server must use Python stdio command")
args = bridge.get("args") or []
if args != ["./mcp/fusion-data-auth-bridge/server.py"]:
    raise SystemExit(f"Bridge args must be plugin-relative, got: {args}")
if bridge.get("env", {}).get("AUTODESK_FUSION_DATA_BRIDGE_CONFIG") != "./mcp/fusion-data-auth-bridge/config.example.json":
    raise SystemExit("Bridge config env path must be plugin-relative")
if any(str(arg).startswith("./plugins/autodesk-fusion") for arg in args):
    raise SystemExit("Bridge MCP args must not assume the repository root")
if "enabled_tools" not in bridge or "doctor" not in bridge["enabled_tools"]:
    raise SystemExit("Bridge MCP server should expose an explicit tool allowlist")

for mirror in [ROOT / ".codex-plugin" / "marketplace.json", ROOT / ".claude-plugin" / "marketplace.json", ROOT / "marketplace.json"]:
    if json.loads(mirror.read_text()) != canonical:
        raise SystemExit(f"Marketplace mirror out of sync: {mirror}")
if "autodesk-fusion" not in [entry["name"] for entry in canonical["plugins"]]:
    raise SystemExit("autodesk-fusion missing from canonical marketplace")

skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
skill_names = [path.parent.name for path in skill_files]
if "fusion-data-auth-bridge" not in skill_names:
    raise SystemExit("Missing fusion-data-auth-bridge skill")
for skill in skill_files:
    text = skill.read_text()
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"Invalid skill frontmatter: {skill}")
    declared = next((line.split(":", 1)[1].strip() for line in text.splitlines() if line.startswith("name:")), "")
    if declared != skill.parent.name:
        raise SystemExit(f"Skill folder/name mismatch: {skill}")

ignore = (ROOT / ".gitignore").read_text()
for forbidden in [".fusion-auth/", ".fusion-private/", ".fusion-runs/", ".fusion-api-reference/"]:
    if forbidden not in ignore:
        raise SystemExit(f".gitignore missing {forbidden}")
    if (ROOT / forbidden.rstrip("/")).exists():
        raise SystemExit(f"Generated/private folder must not be committed: {forbidden}")

print(f"OK: Autodesk Fusion v{VERSION} with {len(skill_files)} skills and bundled Fusion Data Auth Bridge validated")
