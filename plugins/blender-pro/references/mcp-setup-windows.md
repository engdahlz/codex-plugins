# Blender MCP setup on Windows

## Checklist

1. Install Blender.
2. Install `uv` using the official Windows installer or package manager used by the Blender MCP project.
3. Confirm `uvx` is visible:

```powershell
where uvx
```

4. If Codex cannot start `uvx`, use a `cmd` wrapper in MCP config:

```json
{
  "command": "cmd",
  "args": ["/c", "uvx", "--python", "3.11", "blender-mcp"]
}
```

5. Open Blender and enable/start the Blender MCP add-on/server.
6. Fully quit and restart Codex after PATH or config changes.
7. Test with an inspect-only Blender Pro prompt.

## Common Windows issue

GUI apps may not refresh PATH until restarted. If `uvx` works in PowerShell but not in Codex, use the wrapper or an absolute path.
