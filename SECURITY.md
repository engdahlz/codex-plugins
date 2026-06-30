# Security policy

Agent Skills and Codex plugins can influence how an AI agent reads files, runs tools, writes code, and follows workflows. Treat every skill, plugin manifest, MCP configuration, script, hook, and bridge server like executable code plus instructions.

## Never commit

- API keys, tokens, cookies, passwords, private SSH keys, OAuth refresh tokens, or `.env` files.
- Autodesk/APS access tokens, OAuth client secrets, local Fusion auth files, customer CAD files, NC/post outputs, or proprietary screenshots.
- `.fusion-auth/`, `.fusion-private/`, `.fusion-runs/`, `.fusion-api-reference/`, generated evidence with private design names, or local runtime snapshots.
- Hidden prompts that try to override system, developer, or user instructions.
- Scripts that exfiltrate files, browser data, credentials, repository contents, or tokens from other apps.

## Fusion Data Auth Bridge

The bridge performs its own Autodesk OAuth flow and stores tokens only under `.fusion-auth/` by default. It must not read tokens from Claude Desktop, VS Code, browsers, Autodesk apps, keychains owned by other clients, or unrelated config files.

v0.2.10 bridge cloud-data tools are read-only. They may read hubs, projects, folders, items, versions, and verified MFGDM data. They must not mutate Autodesk cloud data.

The bridge must validate OAuth state, expire pending login state, redact sensitive output fields, and keep local generated auth state out of Git.

External approvals, Autodesk OAuth, macOS permissions, GitHub permissions, and Codex platform controls must be honored. The plugin must not attempt to bypass them.
