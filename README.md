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

### Autodesk Fusion Developer

A high-autonomy, evidence-driven Autodesk Fusion workflow plugin for Codex.

Autodesk Fusion Developer v0.2.5 includes:

- Codex plugin manifest at `plugins/autodesk-fusion/.codex-plugin/plugin.json`.
- Product Help MCP, Fusion Desktop MCP, and Fusion Data MCP enabled by default in `plugins/autodesk-fusion/.mcp.json`.
- Runtime doctor tooling for Fusion Desktop MCP, Fusion Data MCP, local environment, and source status.
- Evidence ledger scripts for autonomous runs.
- Official Fusion API reference RAG guidance and local indexing/search helpers.
- Computer Use guidance for Fusion UI, dialogs, palettes, and appshots.
- Optional hook examples and Codex subagent prompts for large tasks.
- Expanded 2026 skills for Python 3.14, Design Intent, BOM/properties, assembly references, source watching, and large assemblies.

## Install this marketplace in Codex

```bash
codex plugin marketplace add engdahlz/codex-plugins
codex plugin marketplace list
```

Then restart Codex, open the plugin directory, choose **Engdahlz Codex Plugins**, and install **Blender Pro** or **Autodesk Fusion Developer**.

Pinned version example:

```bash
codex plugin marketplace add engdahlz/codex-plugins --ref main
```

Install Fusion directly after adding the marketplace:

```bash
codex plugin add autodesk-fusion@engdahlz-codex-plugins
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
│   ├── blender-pro/
│   └── autodesk-fusion/
│       ├── .codex-plugin/plugin.json
│       ├── .mcp.json
│       ├── .codex/agents/
│       ├── hooks/
│       ├── skills/
│       ├── references/
│       ├── examples/
│       ├── scripts/
│       └── assets/
├── templates/
├── AGENTS.md
└── SECURITY.md
```

## Development rules

- Do not add plugins unless Axel explicitly requests them.
- Treat skills and MCP configuration as code.
- Do not commit secrets, credentials, API keys, OAuth tokens, Autodesk tokens, private design files, `.env` files, or generated auth files.
- Keep plugin manifests and marketplace entries accurate.
- Keep skills focused and easy for Codex to select.
