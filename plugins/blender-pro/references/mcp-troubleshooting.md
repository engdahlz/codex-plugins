# Blender MCP troubleshooting

## Quick diagnosis

1. Is Blender open?
2. Is the Blender MCP add-on enabled?
3. Is the Blender-side connection started?
4. Does Codex show the `blender` MCP server?
5. Can Codex run an inspect-only request?
6. Do host and port match on both sides?

## Common symptoms

### Codex cannot start the server

- Check `uvx` path.
- Use an absolute path if Codex was launched from a GUI.
- Pin Python 3.11 in the MCP config.
- Restart Codex after config changes.

### Server starts but Blender does not respond

- Start the Blender-side MCP add-on/server.
- Check `BLENDER_HOST` and `BLENDER_PORT`.
- Restart Blender and Codex.

### Operations time out

- Break the task into smaller steps.
- Run inspect-only first.
- Avoid huge scene-wide changes in one batch.
- Reduce viewport/render load before complex tasks.

### Scene changes are not as expected

- Stop and review the last change.
- Use Blender undo or restore a saved file.
- Ask Codex for a smaller plan and a verification step before continuing.
