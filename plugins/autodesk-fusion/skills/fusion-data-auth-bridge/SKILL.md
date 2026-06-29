---
name: fusion-data-auth-bridge
description: Use when direct Autodesk Fusion Data MCP auth fails in Codex or when read-only APS/MFGDM cloud data access should go through the local stdio bridge.
---

# Fusion Data Auth Bridge

Use `autodesk-fusion-data-bridge` when direct `autodesk-fusion-data` auth is blocked by Codex/OAuth/CIMD compatibility.

Workflow:

1. Call `doctor`.
2. Call `auth_status`.
3. If not configured, request `AUTODESK_CLIENT_ID` or report blocked.
4. Use `start_login` and `complete_login_if_needed` to create local bridge tokens.
5. Use read-only tools: hubs, projects, folders, item versions, version metadata, and verified MFGDM calls.

Rules:

- Do not mutate Autodesk cloud data in v0.2.6.
- Do not expose or print tokens.
- Do not reuse tokens from other apps.
- If auth is unavailable, fall back to Desktop MCP or report blocked clearly.
