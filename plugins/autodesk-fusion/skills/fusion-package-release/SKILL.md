---
name: fusion-package-release
description: Package, validate, and release Autodesk Fusion Codex plugin changes with marketplace hygiene, source links, and safety checks.
---

# Fusion package release

Use before publishing plugin changes.

## Checklist

- JSON manifests validate.
- all marketplace mirrors list the same plugins.
- skill frontmatter is valid.
- live MCP profiles default to safe approval modes.
- no secrets, `.fusion-private/`, customer CAD, or Insider-only details are committed.
- README and changelog describe the release accurately.
