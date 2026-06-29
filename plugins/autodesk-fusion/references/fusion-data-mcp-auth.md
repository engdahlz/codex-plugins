# Fusion Data MCP authentication

Autodesk Fusion Data MCP is a remote Streamable HTTP MCP server. Codex can try direct OAuth with:

```bash
codex mcp login autodesk-fusion-data
```

If direct login fails with client metadata, CIMD, dynamic registration, redirect URI, or unsupported auth-flow errors, use the local bridge:

```text
autodesk-fusion-data-bridge
```

The bridge avoids relying on Codex remote OAuth support by presenting a local stdio MCP server to Codex and handling Autodesk OAuth locally.

Do not copy tokens from other MCP clients. Use a separate Autodesk OAuth flow for the bridge.
