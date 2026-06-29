# Security policy

Agent Skills and Codex plugins can influence how an AI agent reads files, runs tools, writes code, and follows workflows. Treat every skill, plugin manifest, MCP configuration, and script like executable code plus instructions.

## Never commit

- API keys, tokens, cookies, passwords, private SSH keys, OAuth refresh tokens, or `.env` files.
- Autodesk/APS access tokens, OAuth client secrets, local Fusion auth files, customer CAD files, NC/post outputs, or proprietary screenshots.
- Personal data that is not required for the plugin.
- Hidden prompts that try to override system, developer, or user instructions.
- Scripts that exfiltrate files, browser data, credentials, or repository contents.
- Destructive commands unless the plugin is explicitly about a safe, reviewed destructive workflow.

## Review checklist for every future plugin

Before adding a plugin to the marketplace:

- Confirm the plugin has a narrow, legitimate purpose.
- Read the full `plugin.json` and all `SKILL.md` files.
- Review bundled scripts, MCP configuration, references, and assets.
- Check for unnecessary network access.
- Check for hidden persistence, background processes, auto-update behavior, and lifecycle hooks.
- Check that file writes are limited and clearly described.
- Validate that marketplace manifests point only to intended plugin folders.

## Blender-specific concerns

Blender MCP may execute Blender Python inside a live Blender session. Save work before running large modifications, and do not execute code that reads unrelated files, uses the network unexpectedly, deletes many objects, or stores credentials.

## Fusion-specific concerns

Fusion Desktop MCP and Fusion Python can mutate live CAD documents. The Fusion plugin is configured for high autonomy because Axel explicitly requested minimal confirmation prompts. Codex should still inspect state first, operate inside the current task scope, prefer reversible batches, verify outcomes, and report blocked platform/auth/runtime steps honestly.

Autodesk Product Help MCP, Fusion Desktop MCP, and Fusion Data MCP are enabled by default. Their bundled tool approval is set to `approve` where supported. This does not bypass macOS, Autodesk OAuth, Codex platform, repository permission, or other external approval systems.

Fusion Insider artifacts and capability snapshots may contain NDA-only information. Keep them out of public commits and place private local snapshots under `.fusion-private/`, which must stay ignored.
