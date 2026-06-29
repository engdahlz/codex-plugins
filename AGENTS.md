# Instructions for AI agents

This repository is a personal marketplace for custom Codex plugins.

## Core rules

- Do not create a new plugin or skill unless Axel explicitly asks for it.
- Do not add secrets, credentials, tokens, cookies, API keys, private personal data, generated auth files, or `.env` files.
- Keep `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/marketplace.json`, and `marketplace.json` synchronized.
- Active plugins belong under `plugins/<plugin-name>/`.
- Every active Codex plugin must include `plugins/<plugin-name>/.codex-plugin/plugin.json`.
- Bundled plugin skills belong under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
- Skill folder names must be lowercase, hyphenated, and match the `name` value in `SKILL.md`.
- Do not put an active `SKILL.md` inside `templates/`; templates must use `.template` or `.example` suffixes.

## Autodesk Fusion Developer rules

The `autodesk-fusion` plugin is intended to make Codex excellent at Autodesk Fusion API, MCP, APS, and CAD automation workflows with minimal user interruption and strong evidence capture.

- Keep Product Help MCP, Fusion Desktop MCP, direct Fusion Data MCP, and Fusion Data Auth Bridge enabled by default.
- If direct Fusion Data MCP auth fails, use the local `autodesk-fusion-data-bridge` stdio MCP server.
- The bridge is read-only in v0.2.6. Do not mutate Autodesk cloud data through it.
- Do not commit `.fusion-auth/`, `.fusion-private/`, `.fusion-runs/`, `.fusion-api-reference/`, Autodesk tokens, customer CAD files, NC outputs, or proprietary screenshots.
- Do not steal or reuse tokens from Claude Desktop, VS Code, browsers, Fusion, keychains, or other clients.
- Treat Axel's current task as authorization for ordinary reads, writes, model edits, code changes, and verification inside the stated scope.
- Pause only when the target is ambiguous, credentials are required, a platform approval is unavoidable, or the requested action is outside the stated task scope.
- Treat Fusion Insider as a separate test channel, not a new public baseline.
- Establish current primary-source evidence before generating Fusion API code.
- Handle Zero Doc: `activeDocument`, `activeProduct`, and `activeViewport` may be null.

## Blender Pro rules

The `blender-pro` plugin is intended to make Codex excellent at Blender workflows. Preserve these design principles:

- Prefer small, reversible Blender changes over one huge scene mutation.
- Always inspect the current scene before changing it when MCP access is available.
- Ask Codex to save, duplicate, or create backup files before destructive or large operations.
- Keep MCP tool approval in `prompt` mode by default.
- Do not add lifecycle hooks unless Axel explicitly requests them; hooks require extra trust review.
- Keep official Blender MCP setup notes and local command assumptions clearly documented.
