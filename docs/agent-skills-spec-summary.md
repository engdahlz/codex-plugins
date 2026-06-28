# Agent Skills spec summary

This is a practical summary for this repository. For the full standard, see https://agentskills.io/specification.

## Minimal skill layout

```text
skills/<skill-name>/
└── SKILL.md
```

Optional additions:

```text
skills/<skill-name>/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

## Required `SKILL.md` frontmatter

```markdown
---
name: skill-name
description: Clear description of what the skill does and when to use it.
---
```

## Naming rules

- 1–64 characters.
- Lowercase letters, numbers, and hyphens only.
- Must not start or end with a hyphen.
- Must not contain consecutive hyphens.
- Must match the parent directory name.

## Description rules

The description is what helps the agent decide when to activate the skill. It should explain:

- What the skill does.
- When to use it.
- Important keywords users are likely to mention.

## Body guidance

The Markdown body should include only the instructions needed when the skill activates. Keep it focused and move long material into `references/`.

Recommended sections:

- Purpose
- When to use
- Workflow
- Inputs and outputs
- Edge cases
- Safety constraints

## Progressive disclosure

Agents usually load skills in stages:

1. Catalog: only `name` and `description`.
2. Activation: full `SKILL.md`.
3. Resources: referenced scripts, docs, templates, or assets only when needed.

This is why concise descriptions and focused skill files matter.
