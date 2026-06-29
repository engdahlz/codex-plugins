# Fusion Developer Codex Plugin

Fusion Developer makes Codex behave like a high-autonomy, evidence-driven Fusion API, APS, MCP, and CAD automation assistant.

## v0.2.6 highlights

- Keeps direct Autodesk Fusion Data MCP enabled.
- Adds `autodesk-fusion-data-bridge`, a local stdio MCP fallback for Codex auth compatibility gaps.
- Adds APS Data Management read-only bridge tools for hubs, projects, folders, items, and versions.
- Adds configurable MFGDM placeholders that must only be enabled after endpoint/schema verification.
- Adds local OAuth PKCE flow with token redaction and ignored `.fusion-auth/` storage.

## MCP profiles

- `autodesk-product-help` is enabled by default.
- `autodesk-fusion-desktop` is enabled by default.
- `autodesk-fusion-data` is enabled by default.
- `autodesk-fusion-data-bridge` is enabled by default and runs locally over stdio.

## Fusion Data auth strategy

1. Try direct `autodesk-fusion-data` first.
2. If Codex cannot complete Autodesk auth/CIMD, use `autodesk-fusion-data-bridge`.
3. The bridge prefers direct APS Data Management reads.
4. MFGDM GraphQL is configurable and should only be enabled after official endpoint/schema verification.
5. No bridge tool mutates Autodesk cloud data in v0.2.6.

## First run

```bash
export AUTODESK_CLIENT_ID="your-public-aps-client-id"
python plugins/autodesk-fusion/scripts/test_fusion_data_bridge.py
python plugins/autodesk-fusion/scripts/fusion_doctor.py
```

In Codex, call bridge tools:

```text
doctor -> auth_status -> start_login -> complete_login_if_needed -> list_hubs
```

## Key references

- `references/fusion-data-auth-bridge.md`
- `references/fusion-data-mcp-auth.md`
- `references/mfgdm-direct-fallback.md`
- `references/runtime-doctor.md`
- `references/evidence-ledger.md`
- `references/api-reference-rag.md`
- `references/official-sources.md`
