#!/usr/bin/env python3
"""Passive validation helper for Blender Pro."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PLUGIN = ROOT / "plugins" / "blender-pro"

required = [
    PLUGIN / ".codex-plugin" / "plugin.json",
    PLUGIN / ".mcp.json",
    PLUGIN / "skills",
    ROOT / ".agents" / "plugins" / "marketplace.json",
]

for path in required:
    if not path.exists():
        raise SystemExit(f"Missing: {path}")

json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
json.loads((PLUGIN / ".mcp.json").read_text())
json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())

skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
if not skill_files:
    raise SystemExit("No skills found")

for skill in skill_files:
    text = skill.read_text()
    if not text.startswith("---") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"Invalid skill frontmatter: {skill}")

print(f"OK: {len(skill_files)} Blender Pro skills validated")
