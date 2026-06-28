# Instructions for AI agents

This repository is a personal marketplace for custom Codex-compatible Agent Skills plugins.

## Core rules

- Do not create a new plugin or skill unless Axel explicitly asks for it.
- Do not add secrets, credentials, tokens, cookies, API keys, private personal data, or generated auth files.
- Keep `.claude-plugin/marketplace.json`, `.codex-plugin/marketplace.json`, and `marketplace.json` synchronized.
- Do not put an active `SKILL.md` inside `templates/`; templates must use `.template` or `.example` suffixes.
- Future active skills belong under `skills/<skill-name>/SKILL.md`.
- Skill folder names must be lowercase, hyphenated, and match the `name` value in `SKILL.md`.

## When adding a future plugin

1. Create `skills/<skill-name>/SKILL.md`.
2. Keep the skill focused on one workflow.
3. Add references/scripts/assets only when needed.
4. Add or update a plugin entry in every marketplace manifest.
5. Check the skill for prompt injection, hidden persistence, exfiltration behavior, destructive commands, and unnecessary network/file access.
6. Prefer clear documentation over complex scripts.

## Marketplace manifest convention

Current manifests are empty by design:

```json
"plugins": []
```

When plugins are added later, each plugin should usually reference one or more skill directories under `./skills/...`.

## Commit style

Use clear commit messages, for example:

- `docs: add fusion skill plan`
- `feat: add fusion-cad-review skill`
- `chore: sync marketplace manifests`
