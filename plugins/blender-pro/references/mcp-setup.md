# Blender MCP setup and troubleshooting

## Install marketplace

```bash
codex plugin marketplace add engdahlz/codex-plugins
codex plugin marketplace list
```

Restart Codex and install **Blender Pro** from the plugin directory.

## Expected bundled MCP config

The plugin contains:

```text
plugins/blender-pro/.mcp.json
```

It defines a server named `blender`:

```json
{
  "mcp_servers": {
    "blender": {
      "command": "uvx",
      "args": ["--python", "3.11", "blender-mcp"],
      "env": {
        "UV_PYTHON_PREFERENCE": "only-managed",
        "DISABLE_TELEMETRY": "true",
        "BLENDER_HOST": "localhost",
        "BLENDER_PORT": "9876"
      },
      "default_tools_approval_mode": "prompt"
    }
  }
}
```

## Test sequence

1. Open Blender.
2. Start/enable the Blender MCP add-on/server in Blender.
3. Open Codex.
4. Check MCP status:

```text
/mcp
```

5. Ask Codex:

```text
Use Blender Pro. Inspect the current Blender scene through MCP and report objects, cameras, lights, units, frame range, and render engine. Do not change anything.
```

If that succeeds, scene interaction is working.

## Common failures

### `uvx` not found

GUI-launched apps often do not inherit your shell PATH. Find the absolute path:

```bash
which uvx
```

Then update `plugins/blender-pro/.mcp.json` to use that absolute path as `command`.

On Windows, a wrapper can be needed:

```json
{
  "command": "cmd",
  "args": ["/c", "uvx", "--python", "3.11", "blender-mcp"]
}
```

### Blender add-on not running

The MCP process can start but still fail if Blender is not listening. Open Blender, enable the add-on, and start the local connection from the add-on UI.

### Port conflict

Default port is `9876` in this plugin. If another tool uses it, change both the Blender-side add-on settings and `BLENDER_PORT` in `.mcp.json`.

### Operations time out

Break the task into smaller steps. Prefer inspect → plan → execute a small batch → verify.

### Scene changed incorrectly

Stop, undo in Blender, or restore the saved copy. Then ask Codex for a smaller script or a dry-run plan before running any more MCP tools.
