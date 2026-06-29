# Fusion Data Auth Bridge

Local stdio MCP bridge for Autodesk Fusion cloud/design data workflows when Codex cannot complete Autodesk Fusion Data MCP's built-in auth/CIMD flow directly.

## Purpose

Codex talks to this server over local stdio. The bridge handles Autodesk OAuth locally and exposes narrow read-only tools for APS Data Management and MFGDM-oriented workflows.

## First-run

```bash
export AUTODESK_CLIENT_ID="your-public-aps-client-id"
python3 plugins/autodesk-fusion/mcp/fusion-data-auth-bridge/server.py
```

In Codex, use the bridge tools:

1. `doctor`
2. `auth_status`
3. `start_login`
4. Open the returned authorization URL.
5. Pass the returned `code` to `complete_login_if_needed`.
6. Use read-only tools such as `list_hubs`, `list_projects`, and `get_item_versions`.

## Token storage

Tokens are stored locally under `.fusion-auth/` by default. This folder is ignored and must not be committed.

## Scope

v0.2.6 is read-only. It does not mutate Autodesk cloud data.

## Why not steal tokens from another app?

Do not reuse Claude Desktop, VS Code, browser, Fusion, or keychain tokens. This bridge performs its own Autodesk OAuth flow and stores only its own local tokens.
