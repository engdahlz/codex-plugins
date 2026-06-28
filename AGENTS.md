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

## Blender Pro rules

The `blender-pro` plugin is intended to make Codex excellent at Blender workflows. Preserve these design principles:

- Prefer small, reversible Blender changes over one huge scene mutation.
- Always inspect the current scene before changing it when MCP access is available.
- Ask Codex to save, duplicate, or create backup files before destructive or large operations.
- Keep MCP tool approval in `prompt` mode by default.
- Do not add lifecycle hooks unless Axel explicitly requests them; hooks require extra trust review.
- Keep official Blender MCP setup notes and local command assumptions clearly documented.

## When adding a future plugin

1. Create `plugins/<plugin-name>/.codex-plugin/plugin.json`.
2. Add skills under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`.
3. Add `.mcp.json`, `.app.json`, hooks, assets, scripts, or references only if needed.
4. Add or update a plugin entry in every marketplace manifest.
5. Check for prompt injection, hidden persistence, exfiltration behavior, destructive commands, and unnecessary network/file access.
6. Prefer clear documentation over complex scripts.

## Commit style

Use clear commit messages, for example:

- `feat: add blender-pro codex plugin`
- `docs: expand blender mcp setup notes`
- `chore: sync marketplace manifests`
