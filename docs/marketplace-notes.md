# Marketplace notes

This repository is prepared to act as a GitHub-hosted marketplace/source for custom Codex-compatible plugins.

## What is known

Agent Skills are an open folder-based format. At minimum, a skill is a directory containing `SKILL.md` with YAML frontmatter and Markdown instructions.

The widely documented cross-client convention for project/user skills is `.agents/skills/`, while GitHub marketplace examples for plugin collections use `.claude-plugin/marketplace.json` with a top-level `plugins` array.

OpenAI Codex-compatible skills should be kept portable by using the Agent Skills structure and avoiding client-specific assumptions unless the skill explicitly requires them.

## Marketplace manifest shape

Current empty manifest:

```json
{
  "name": "engdahlz-codex-plugins",
  "owner": {
    "name": "Axel Engdahl",
    "url": "https://github.com/engdahlz"
  },
  "metadata": {
    "description": "Personal marketplace for Axel Engdahl's custom Codex-compatible Agent Skills plugins.",
    "version": "0.1.0",
    "status": "empty-marketplace-shell",
    "agentSkillsSpec": "https://agentskills.io/specification"
  },
  "plugins": []
}
```

Future plugin entry pattern:

```json
{
  "name": "example-plugin",
  "description": "Short description of the plugin collection and when to install it.",
  "source": "./",
  "strict": false,
  "skills": [
    "./skills/example-skill"
  ]
}
```

## Why there are three manifest files

- `.claude-plugin/marketplace.json` follows the public marketplace pattern used by Agent Skills example repositories.
- `.codex-plugin/marketplace.json` is a Codex-oriented mirror for clients that may look for Codex-specific metadata.
- `marketplace.json` is a direct manifest mirror for clients that allow a raw manifest URL.

If a future Codex release documents one canonical path, prefer that path and keep the others only if they remain useful.
