#!/usr/bin/env python3
"""Passive validation helper for Autodesk Fusion Developer."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLUGIN = ROOT / "plugins" / "autodesk-fusion"
BRIDGE = PLUGIN / "mcp" / "fusion-data-auth-bridge"

required = [
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
    PLUGIN / "assets" / "icon.png",
    PLUGIN / "assets" / "logo.png",
    PLUGIN / "assets" / "screenshot-marketplace.png",
]

for path in required:
    if not path.exists():
        raise SystemExit(f"Missing: {path}")

plugin = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
mcp = json.loads((PLUGIN / ".mcp.json").read_text())
canonical = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())

if plugin["name"] != "autodesk-fusion":
    raise SystemExit("Unexpected plugin name")
if plugin.get("version") != "0.2.8":
    raise SystemExit("Expected plugin version 0.2.8")
servers = mcp.get("mcp_servers", {})
for name in ["autodesk-product-help", "autodesk-fusion-desktop", "autodesk-fusion-data", "autodesk-fusion-data-bridge"]:
    if name not in servers:
        raise SystemExit(f"Missing MCP server: {name}")
    if not servers[name].get("enabled"):
        raise SystemExit(f"Expected MCP server enabled: {name}")
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

ignore = (ROOT / ".gitignore").read_text()
for forbidden in [".fusion-auth/", ".fusion-private/", ".fusion-runs/", ".fusion-api-reference/"]:
    if forbidden not in ignore:
        raise SystemExit(f".gitignore missing {forbidden}")
    if (ROOT / forbidden.rstrip("/")).exists():
        raise SystemExit(f"Generated/private folder must not be committed: {forbidden}")

print(f"OK: Autodesk Fusion v{plugin['version']} with {len(skill_files)} skills and Fusion Data Auth Bridge validated")
