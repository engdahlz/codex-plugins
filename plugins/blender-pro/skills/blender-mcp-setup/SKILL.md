---
name: blender-mcp-setup
description: Use for Blender MCP setup, uvx configuration, Blender add-on checks, Codex plugin MCP configuration, host/port troubleshooting, and connection validation.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender MCP Setup

## Purpose

Help Codex connect safely and reliably to Blender through the bundled Blender MCP server.

## Setup checklist

1. Confirm Blender is installed and opens normally.
2. Confirm the Blender-side MCP add-on/server is installed and enabled.
3. Confirm the local MCP launcher works, usually with `uvx --python 3.11 blender-mcp`.
4. Confirm Codex can see the bundled MCP server named `blender`.
5. Confirm host and port match on both sides, usually `localhost:9876`.
6. Run an inspect-only task before any scene edits.

## Common fixes

- If `uvx` is not found, use the absolute path from `which uvx` or `where uvx`.
- On Windows, a `cmd /c uvx ...` wrapper may be needed.
- If Python selection fails, keep `--python 3.11` and `UV_PYTHON_PREFERENCE=only-managed`.
- If Blender is not responding, restart Blender, start the add-on connection, then restart Codex.
- If operations time out, split the task into smaller batches.

## References

- `../../references/official-blender-mcp.md`
- `../../references/mcp-setup.md`
- `../../references/mcp-setup-macos.md`
- `../../references/mcp-setup-windows.md`
- `../../references/mcp-setup-linux.md`
- `../../references/mcp-troubleshooting.md`
