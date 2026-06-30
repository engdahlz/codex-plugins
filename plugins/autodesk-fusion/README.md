# Fusion Developer Codex Plugin

Fusion Developer makes Codex behave like a high-autonomy, evidence-driven Fusion API, APS, MCP, and CAD automation assistant.

## v0.2.10 highlights

- Keeps direct Autodesk Fusion Data MCP enabled.
- Keeps Autodesk Product Help MCP and Fusion Desktop MCP bundled in the plugin MCP config.
- Fixes the local `autodesk-fusion-data-bridge` stdio path so it is plugin-relative and follows the plugin after installation.
- Adds a single `VERSION` source and stronger validation around manifest, marketplace, skills, MCP config, and private generated folders.
- Hardens the Fusion Data Auth Bridge token store with private directory/file permissions, atomic writes, corrupt-store handling, and deeper redaction.
- Tightens the local bridge OAuth flow by requiring returned state, expiring pending login state, and avoiding expired-token reuse after refresh failure.
- Adds marketplace sync tooling so `.agents`, `.codex-plugin`, `.claude-plugin`, and root marketplace files do not drift.

## MCP profiles

- `autodesk-product-help` is enabled by default for official Autodesk product/API help.
- `autodesk-fusion-desktop` is enabled by default for local live Fusion workflows when Fusion is running.
- `autodesk-fusion-data` is enabled by default for Autodesk-hosted Fusion Data MCP workflows.
- `autodesk-fusion-data-bridge` is enabled by default and runs locally over stdio from `./mcp/fusion-data-auth-bridge/server.py` relative to the plugin root.

## Fusion Data auth strategy

1. Try direct `autodesk-fusion-data` first.
2. If Codex cannot complete Autodesk auth/CIMD, use `autodesk-fusion-data-bridge`.
3. The bridge prefers direct APS Data Management reads.
4. MFGDM GraphQL is configurable and should only be enabled after official endpoint/schema verification.
5. No bridge tool mutates Autodesk cloud data in v0.2.10.

## First run

```bash
export AUTODESK_CLIENT_ID="your-public-aps-client-id"
python plugins/autodesk-fusion/scripts/validate_plugin.py
python plugins/autodesk-fusion/scripts/test_fusion_data_bridge.py
python plugins/autodesk-fusion/scripts/fusion_doctor.py
```

In Codex, call bridge tools:

```text
doctor -> auth_status -> start_login -> complete_login_if_needed -> list_hubs
```

`complete_login_if_needed` should receive both the returned authorization `code` and returned OAuth `state`.

## Marketplace maintenance

```bash
python scripts/sync_marketplaces.py
python scripts/sync_marketplaces.py --write
```

## Key references

- `references/fusion-data-auth-bridge.md`
- `references/fusion-data-mcp-auth.md`
- `references/mfgdm-direct-fallback.md`
- `references/runtime-doctor.md`
- `references/evidence-ledger.md`
- `references/api-reference-rag.md`
- `references/official-sources.md`
