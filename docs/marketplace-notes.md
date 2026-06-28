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

## Current plugins

```text
plugins/blender-pro/
plugins/autodesk-fusion/
```

The Blender Pro plugin includes `.codex-plugin/plugin.json`, `.mcp.json`, `skills/`, `references/`, `examples/`, `scripts/`, and `assets/`.

The Autodesk Fusion Developer plugin includes `.codex-plugin/plugin.json`, `.mcp.json`, `skills/`, `references/`, `examples/`, `scripts/`, and `assets/`.

## Marketplace entry pattern

```json
{
  "name": "autodesk-fusion",
  "source": {
    "source": "local",
    "path": "./plugins/autodesk-fusion"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

## Install command

```bash
codex plugin marketplace add engdahlz/codex-plugins
codex plugin add autodesk-fusion@engdahlz-codex-plugins
```

## Maintenance checklist

After changing a plugin:

1. Validate JSON.
2. Validate every `SKILL.md` frontmatter block.
3. Check that plugin manifest paths start with `./` and resolve inside the plugin root.
4. Check that every marketplace mirror has the same plugin list.
5. Restart Codex or run marketplace upgrade before testing.
