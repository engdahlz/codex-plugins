# Official Blender MCP notes

Primary source requested for this plugin:

```text
https://www.blender.org/lab/mcp-server/
```

Use Blender Lab's official MCP server page as the source of truth for installation steps, Blender add-on details, supported Blender versions, and the current MCP server launcher command.

## Current bundled assumption

This plugin ships a standard Codex MCP config at `../.mcp.json` using:

```json
{
  "command": "uvx",
  "args": ["--python", "3.11", "blender-mcp"]
}
```

This is a practical default because many Blender MCP setups expose the server through `uvx blender-mcp`. If Blender Lab documents a different package name, command, port, transport, or add-on procedure, update `../.mcp.json` and this reference file before publishing the plugin broadly.

## Verification checklist

Before using this plugin heavily, verify the official page for:

- MCP package/launcher command.
- Blender add-on installation method.
- Default port and host.
- Whether the server uses stdio, HTTP, or another transport.
- Whether telemetry exists and how to disable it.
- Whether asset download tools require extra opt-in.
- Supported Blender versions.
- Known limitations and security warnings.

## Local connection model

Most Blender MCP setups use two local components:

1. A Blender-side add-on/server running inside Blender.
2. A Codex-launched MCP process that communicates with that Blender-side component.

Codex talks to the MCP process. The MCP process talks to Blender. If any piece is missing, live scene control will fail.

## Safe default policy

Keep MCP tool approval in prompt mode until the setup is trusted:

```toml
[plugins."blender-pro".mcp_servers.blender]
enabled = true
default_tools_approval_mode = "prompt"
```

For large scene edits, save the `.blend` file before running tools that execute Blender Python or delete/replace objects.
