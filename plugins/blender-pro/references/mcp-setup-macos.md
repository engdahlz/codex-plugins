# Blender MCP setup on macOS

## Checklist

1. Install Blender.
2. Install `uv` if the MCP package uses `uvx`:

```bash
brew install uv
```

3. Confirm `uvx` is visible:

```bash
which uvx
```

4. If Codex cannot find `uvx`, replace `command: "uvx"` in `.mcp.json` with the absolute path returned by `which uvx`.
5. Open Blender and enable/start the Blender MCP add-on/server.
6. Restart Codex after changing plugin or MCP configuration.
7. Test with an inspect-only Blender Pro prompt.

## Common macOS issue

Apps launched from Finder/Dock may not inherit the same PATH as Terminal. Absolute paths are more reliable for MCP launchers.

## Recommended config shape

```json
{
  "command": "uvx",
  "args": ["--python", "3.11", "blender-mcp"],
  "env": {
    "UV_PYTHON_PREFERENCE": "only-managed",
    "DISABLE_TELEMETRY": "true",
    "BLENDER_HOST": "localhost",
    "BLENDER_PORT": "9876"
  }
}
```
