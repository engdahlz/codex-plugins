# Official Blender MCP notes

Primary source for this plugin:

```text
https://www.blender.org/lab/mcp-server/
```

Use Blender Lab's official MCP server page as the source of truth for installation steps, Blender add-on details, supported Blender versions, and the current MCP server launcher command.

## Current bundled default

This plugin ships a Codex MCP config at `../.mcp.json` using:

```json
{
  "command": "uvx",
  "args": ["--python", "3.11", "blender-mcp"]
}
```

This is a practical default for Blender MCP setups that expose the server through `uvx blender-mcp`. If Blender Lab documents a different package name, command, port, transport, or add-on procedure, update `../.mcp.json` and this reference file.

## Verification checklist

Before relying on a new Blender MCP release, verify:

- MCP package or launcher command.
- Blender add-on installation method.
- Default port and host.
- Transport type.
- Telemetry controls.
- External asset download controls.
- Supported Blender versions.
- Security warnings and known limitations.

## Local connection model

Most Blender MCP setups use two local components:

1. A Blender-side add-on/server running inside Blender.
2. A Codex-launched MCP process that communicates with that Blender-side component.

Codex talks to the MCP process. The MCP process talks to Blender. If either side is missing, live scene control will fail.

## Safe default policy

Keep MCP tool approval in prompt mode until the setup is trusted:

```toml
[plugins."blender-pro".mcp_servers.blender]
enabled = true
default_tools_approval_mode = "prompt"
```

For large scene edits, save the `.blend` file before using tools that execute Blender-side code or change many objects.
