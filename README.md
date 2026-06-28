# codex-plugins

Personal GitHub marketplace for custom Codex plugins.

This repository is a Codex marketplace. Add the repository URL to Codex and install the plugins exposed through `.agents/plugins/marketplace.json`.

## Available plugins

### Blender Pro

A professional Blender workflow plugin for Codex.

Blender Pro packages:

- A Codex plugin manifest at `plugins/blender-pro/.codex-plugin/plugin.json`.
- A bundled Blender MCP configuration at `plugins/blender-pro/.mcp.json`.
- Seven focused Agent Skills for setup, scene work, modeling, materials/lighting, animation/rigging, Python automation, and quality review.
- Deep reference documentation for professional Blender workflows, safety, MCP setup, and Python patterns.
- Marketplace metadata so Codex can discover the plugin from this repository.

## Install this marketplace in Codex

```bash
codex plugin marketplace add engdahlz/codex-plugins
codex plugin marketplace list
```

Then restart Codex, open the plugin directory, choose **Engdahlz Codex Plugins**, and install **Blender Pro**.

Pinned version example:

```bash
codex plugin marketplace add engdahlz/codex-plugins --ref main
```

## Canonical marketplace files

Codex reads repo marketplaces from:

```text
.agents/plugins/marketplace.json
```

This repo also keeps compatibility mirrors at:

```text
.claude-plugin/marketplace.json
.codex-plugin/marketplace.json
marketplace.json
```

Keep all marketplace manifests synchronized.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json     # Canonical Codex repo marketplace
├── .claude-plugin/marketplace.json      # Legacy-compatible marketplace mirror
├── .codex-plugin/marketplace.json       # Compatibility mirror
├── docs/                                # Marketplace notes
├── plugins/
│   └── blender-pro/                     # First real plugin
│       ├── .codex-plugin/plugin.json    # Required Codex plugin manifest
│       ├── .mcp.json                    # Bundled Blender MCP server config
│       ├── skills/                      # Bundled Agent Skills
│       ├── references/                  # Documentation loaded on demand
│       ├── examples/                    # Prompt examples
│       ├── scripts/                     # Validation tools
│       └── assets/                      # Plugin icon/logo
├── templates/                           # Templates only, not active plugins
├── AGENTS.md                            # AI agent rules for this repository
└── SECURITY.md                          # Security policy for skills/plugins
```

## Development rules

- Do not add plugins unless Axel explicitly requests them.
- Treat skills and MCP configuration as code.
- Do not commit secrets, personal credentials, API keys, OAuth tokens, or generated auth files.
- Keep plugin manifests and marketplace entries accurate.
- Keep skills focused and front-load their descriptions so Codex can select the right skill.
