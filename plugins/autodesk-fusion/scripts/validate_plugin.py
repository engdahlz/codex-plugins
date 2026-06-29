#!/usr/bin/env python3
"""Passive validation helper for Autodesk Fusion Developer."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLUGIN = ROOT / "plugins" / "autodesk-fusion"

required = [
    PLUGIN / ".codex-plugin" / "plugin.json",
    PLUGIN / ".mcp.json",
    PLUGIN / "skills",
    ROOT / ".agents" / "plugins" / "marketplace.json",
    ROOT / ".codex-plugin" / "marketplace.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "marketplace.json",
]

for path in required:
    if not path.exists():
        raise SystemExit(f"Missing: {path}")

plugin = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
mcp = json.loads((PLUGIN / ".mcp.json").read_text())
canonical = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())

if plugin["name"] != "autodesk-fusion":
    raise SystemExit("Unexpected plugin name")
if "mcp_servers" not in mcp:
    raise SystemExit(".mcp.json must contain mcp_servers")
for name, server in mcp["mcp_servers"].items():
    if not server.get("enabled"):
        raise SystemExit(f"Expected high-autonomy MCP server enabled: {name}")
if "autodesk-fusion" not in [entry["name"] for entry in canonical["plugins"]]:
    raise SystemExit("autodesk-fusion missing from canonical marketplace")

skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
if len(skill_files) < 35:
    raise SystemExit("Too few Fusion skills found")
for skill in skill_files:
    text = skill.read_text()
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"Invalid skill frontmatter: {skill}")

for forbidden in [".fusion-private", ".fusion-runs", ".fusion-api-reference"]:
    if (ROOT / forbidden).exists():
        raise SystemExit(f"Private/generated folder must not be committed: {forbidden}")

print(f"OK: Autodesk Fusion v{plugin['version']} with {len(skill_files)} skills validated")
