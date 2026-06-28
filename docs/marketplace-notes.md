# Marketplace notes

This repository is prepared as a GitHub-hosted marketplace/source for custom Codex plugins.

## Codex marketplace layout

The canonical repo marketplace is:

```text
$REPO_ROOT/.agents/plugins/marketplace.json
```

A marketplace is a JSON catalog with one entry per plugin. Each entry points to a plugin folder, usually under `./plugins/<plugin-name>`.

This repository also keeps compatibility mirrors at:

```text
.claude-plugin/marketplace.json
.codex-plugin/marketplace.json
marketplace.json
```

## Current plugin

```text
plugins/blender-pro/
```

The Blender Pro plugin includes:

- `.codex-plugin/plugin.json`
- `.mcp.json`
- `skills/`
- `references/`
- `examples/`
- `scripts/`
- `assets/`

## Marketplace entry pattern

```json
{
  "name": "blender-pro",
  "source": {
    "source": "local",
    "path": "./plugins/blender-pro"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Design"
}
```

## Install command

```bash
codex plugin marketplace add engdahlz/codex-plugins
```

## Maintenance checklist

After changing a plugin:

1. Validate JSON.
2. Validate every `SKILL.md` frontmatter block.
3. Check that plugin manifest paths start with `./` and resolve inside the plugin root.
4. Check that every marketplace mirror has the same plugin list.
5. Restart Codex or run marketplace upgrade before testing.
