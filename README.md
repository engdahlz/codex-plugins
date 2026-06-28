# codex-plugins

Personal GitHub marketplace for my custom Codex / Agent Skills plugins.

This repository is intentionally set up as an empty marketplace shell. It contains the marketplace metadata, documentation, safety rules, and templates needed to add plugins later, but it does **not** contain any active plugins yet.

## What this repo is for

- Keep all custom Codex-compatible skills/plugins in one version-controlled place.
- Add this repository URL to Codex or another compatible agent client as a marketplace/source.
- Add future plugins as self-contained folders with clear instructions, resources, and optional scripts.
- Keep marketplace metadata in sync so one URL can expose all custom plugins.

## Current status

No plugins are published yet.

The marketplace files currently have an empty `plugins` array on purpose:

```json
"plugins": []
```

## Standards used

This repo is prepared around the Agent Skills format:

- A skill is a folder containing a required `SKILL.md` file.
- `SKILL.md` starts with YAML frontmatter, at minimum `name` and `description`.
- Skills may also include optional `scripts/`, `references/`, and `assets/` folders.

Marketplace compatibility files are included at:

- `.claude-plugin/marketplace.json` — known GitHub plugin marketplace layout used by Agent Skills examples.
- `.codex-plugin/marketplace.json` — compatibility mirror for Codex-oriented clients if they look for a Codex-specific marketplace folder.
- `marketplace.json` — root-level convenience mirror for clients that accept a direct marketplace manifest.

Keep these three files synchronized when adding or removing plugins.

## Intended marketplace URL

Use the repository URL when Codex asks for a marketplace/source URL:

```text
https://github.com/engdahlz/codex-plugins
```

For clients that use repository shorthand, use:

```text
engdahlz/codex-plugins
```

For clients with a slash-command marketplace flow, the equivalent pattern is usually:

```text
/plugin marketplace add engdahlz/codex-plugins
```

## Repository structure

```text
.
├── .claude-plugin/marketplace.json     # Marketplace manifest used by current Agent Skills examples
├── .codex-plugin/marketplace.json      # Codex-oriented compatibility mirror
├── docs/                               # Notes and operating rules
├── skills/                             # Future skill/plugin folders go here
├── templates/                          # Safe templates, not active plugins
├── AGENTS.md                           # Instructions for AI coding agents working in this repo
├── SECURITY.md                         # Safety rules for reviewing plugins
└── marketplace.json                    # Root-level manifest mirror
```

## Adding a plugin later

Do not add plugins casually. When I ask for one, follow this flow:

1. Create a new folder under `skills/<plugin-name>/`.
2. Add `skills/<plugin-name>/SKILL.md` with valid YAML frontmatter.
3. Add optional `scripts/`, `references/`, or `assets/` only if needed.
4. Add a plugin entry to all marketplace manifests.
5. Validate the skill and check for unsafe instructions or hidden behavior.
6. Commit the change with a clear message.

## Naming rules for skills

Use lowercase letters, numbers, and hyphens only:

```text
good: fusion-cad-review
bad: Fusion_CAD_Review
bad: fusion--cad
```

The folder name must match the `name` field in `SKILL.md`.

## Important safety rule

Skills are executable/contextual instructions for agents. Treat them like code. Do not add secrets, credentials, tokens, personal data, hidden commands, or instructions that try to override user/developer/system permissions.
