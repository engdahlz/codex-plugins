# Fusion Data Auth Bridge

Local stdio MCP bridge for Autodesk Fusion cloud/design data workflows when Codex cannot complete Autodesk Fusion Data MCP's built-in auth/CIMD flow directly.

## Purpose

Codex talks to this server over local stdio. The bridge handles Autodesk OAuth locally and exposes narrow read-only tools for APS Data Management and verified MFGDM-oriented workflows.

The plugin bundles this server through `plugins/autodesk-fusion/.mcp.json` using this plugin-relative command:

```json
{
  "command": "python3",
  "args": ["./mcp/fusion-data-auth-bridge/server.py"],
  "cwd": "."
}
```

## First run

```bash
export AUTODESK_CLIENT_ID="your-public-aps-client-id"
python3 plugins/autodesk-fusion/scripts/test_fusion_data_bridge.py
```

In Codex, use the bridge tools:

1. `doctor`
2. `auth_status`
3. `start_login`
4. Open the returned authorization URL.
5. Pass the returned `code` and `state` to `complete_login_if_needed`.
6. Use read-only tools such as `list_hubs`, `list_projects`, and `get_item_versions`.

## Local storage

Bridge sign-in data is stored locally under `.fusion-auth/` by default. This folder is ignored and must not be committed.

v0.2.10 writes the local store more defensively, handles corrupt JSON without crashing, redacts nested sensitive fields in outputs, and expires pending login state.

## Scope

v0.2.10 is read-only. It does not mutate Autodesk cloud data.

## MFGDM

MFGDM-style GraphQL is intentionally gated. Configure endpoint, schema version, and verification metadata only after checking current official Autodesk documentation.
