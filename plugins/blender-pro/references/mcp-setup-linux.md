# Blender MCP setup on Linux

## Checklist

1. Install Blender.
2. Install `uv` according to your distribution or the official uv installer.
3. Confirm `uvx` is visible:

```bash
which uvx
```

4. If Codex cannot find `uvx`, use the absolute path returned by `which uvx` in `.mcp.json`.
5. Open Blender and enable/start the Blender MCP add-on/server.
6. Confirm host and port are aligned, usually `localhost` and `9876`.
7. Restart Codex after any MCP config change.
8. Test with an inspect-only Blender Pro prompt.

## Notes

- Some desktop launchers do not inherit shell PATH.
- Wayland/X11 differences generally should not affect the MCP server, but Blender UI automation may differ by environment.
- Prefer small scene operations when running on low-power machines or remote sessions.
