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
for mirror in [ROOT / ".codex-plugin" / "marketplace.json", ROOT / ".claude-plugin" / "marketplace.json", ROOT / "marketplace.json"]:
    json.loads(mirror.read_text())

if plugin["name"] != "autodesk-fusion":
    raise SystemExit("Unexpected plugin name")
if "mcp_servers" not in mcp:
    raise SystemExit(".mcp.json must contain mcp_servers")
if "autodesk-fusion" not in [entry["name"] for entry in canonical["plugins"]]:
    raise SystemExit("autodesk-fusion missing from canonical marketplace")

skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
if len(skill_files) < 10:
    raise SystemExit("Too few Fusion skills found")

for skill in skill_files:
    text = skill.read_text()
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"Invalid skill frontmatter: {skill}")

print(f"OK: {len(skill_files)} Autodesk Fusion skills validated")
