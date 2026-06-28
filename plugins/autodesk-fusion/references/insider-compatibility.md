# Fusion Insider compatibility

Fusion Insider should be treated as a moving runtime capability set, not as the plugin minimum version.

## Rules

- Keep `public`, `insider`, `runtime availability`, `public lifecycle`, and `distribution decision` as separate fields.
- Never infer release status from `hasattr`, import success, MCP discovery, or a successful live call.
- Store private runtime snapshots under `.fusion-private/` and never commit them.
- Do not include NDA feature names, screenshots, documents, hub names, project names, customer data, or private build details in public issues or commits.
- Release builds must use public Autodesk documentation as the contract.

## Recommended snapshot flow

1. Run the runtime probe in public Fusion.
2. Run the same probe in Fusion Insider.
3. Compare allowlisted public capabilities only.
4. Report regressions separately from new Insider-only availability.
5. Promote a capability only after public documentation confirms release status.
