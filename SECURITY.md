# Security policy

Agent Skills and Codex plugins can influence how an AI agent reads files, runs tools, writes code, and follows workflows. Treat every skill like executable code plus instructions.

## Never commit

- API keys, tokens, cookies, passwords, private SSH keys, OAuth refresh tokens, or `.env` files.
- Personal data that is not required for the skill.
- Hidden prompts that try to override system, developer, or user instructions.
- Scripts that exfiltrate files, browser data, credentials, or repository contents.
- Destructive commands unless the skill is explicitly about a safe, reviewed destructive workflow.

## Review checklist for every future skill

Before adding a plugin to the marketplace:

- Confirm the skill has a narrow, legitimate purpose.
- Read the full `SKILL.md`, not only the description.
- Review all bundled scripts and resources.
- Check for unnecessary network access.
- Check for hidden persistence, background processes, or auto-update behavior.
- Check that file writes are limited and clearly described.
- Check that any tool permissions are justified and as narrow as possible.
- Validate that the marketplace manifest points only to intended skill folders.

## Reporting problems

This is a personal repository. If a future plugin looks unsafe, remove it from all marketplace manifests first, then review or delete the underlying files.
