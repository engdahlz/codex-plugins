# Fusion Data Auth Bridge

The bridge exists because direct Autodesk Fusion Data MCP auth may require a built-in auth/CIMD flow that Codex does not expose clearly enough for reliable direct use.

Architecture:

```text
Codex -> local stdio MCP bridge -> Autodesk OAuth -> APS Data Management / MFGDM-style read APIs
```

The bridge is read-only in v0.2.6. It exposes narrow tools for auth status, login, logout, hubs, projects, folders, item versions, version metadata, and MFGDM placeholders.

Use direct `autodesk-fusion-data` first when Codex auth works. Use `autodesk-fusion-data-bridge` when direct auth fails.

Do not commit `.fusion-auth/`, `.fusion-private/`, `.fusion-runs/`, or `.fusion-api-reference/`.
