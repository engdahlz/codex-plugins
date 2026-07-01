#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def fail(msg: str):
    print(f"ERROR: {msg}")
    raise SystemExit(1)


def main():
    repo = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    plugin = repo / "plugins" / "reality-composer-pro"
    manifest = plugin / ".codex-plugin" / "plugin.json"
    if not manifest.exists():
        fail("missing plugin manifest")
    data = json.loads(manifest.read_text())
    if data.get("name") != "reality-composer-pro":
        fail("manifest name must be reality-composer-pro")
    if data.get("mcpServers") != "./.mcp.json":
        fail("manifest must point to ./.mcp.json")
    if "rcp_helper.py" not in (plugin / ".mcp.json").read_text():
        fail("mcp config must launch rcp_helper.py")
    skills = list((plugin / "skills").glob("*/SKILL.md"))
    if len(skills) < 8:
        fail("expected at least 8 skills")
    for skill in skills:
        text = skill.read_text()
        if not text.startswith("---") or "description:" not in text:
            fail(f"skill missing frontmatter: {skill}")
    markets = [repo / "marketplace.json", repo / ".agents/plugins/marketplace.json", repo / ".codex-plugin/marketplace.json", repo / ".claude-plugin/marketplace.json"]
    bodies = [p.read_text() for p in markets]
    if len(set(bodies)) != 1:
        fail("marketplace files are not synchronized")
    print("Reality Composer Pro plugin validation passed")

if __name__ == "__main__":
    main()
