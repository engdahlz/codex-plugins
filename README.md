# codex-plugins

Personal GitHub marketplace for custom Codex plugins.

This repository is a Codex marketplace. Add the repository URL to Codex and install plugins exposed through `.agents/plugins/marketplace.json`.

## Available plugins

### Blender Pro

A professional Blender workflow plugin for Codex.

Blender Pro v0.2.0 includes:

- Codex plugin manifest at `plugins/blender-pro/.codex-plugin/plugin.json`.
- Bundled Blender MCP configuration at `plugins/blender-pro/.mcp.json`.
- Focused skills for Blender setup, scene work, modeling, materials and lighting, render workflow, animation and rigging, Geometry Nodes, asset pipelines, bpy workflows, and quality review.
- Reference documentation for Blender MCP setup, safety, professional workflow, modeling, materials, lighting, rendering, asset handoff, and troubleshooting.
- Marketplace metadata, icon, logo, and SVG screenshots so Codex can present the plugin cleanly.

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
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
├── .codex-plugin/marketplace.json
├── docs/
├── plugins/
│   └── blender-pro/
│       ├── .codex-plugin/plugin.json
│       ├── .mcp.json
│       ├── skills/
│       ├── references/
│       ├── examples/
│       └── assets/
├── templates/
├── AGENTS.md
└── SECURITY.md
```

## Development rules

- Do not add plugins unless Axel explicitly requests them.
- Treat skills and MCP configuration as code.
- Do not commit secrets, credentials, API keys, OAuth tokens, or generated auth files.
- Keep plugin manifests and marketplace entries accurate.
- Keep skills focused and easy for Codex to select.
