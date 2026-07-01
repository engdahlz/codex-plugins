# codex-plugins

Personal GitHub marketplace for custom Codex plugins.

This repository is a Codex marketplace. Add the repository URL to Codex and install plugins exposed through `.agents/plugins/marketplace.json`.

## Available plugins

### Blender Pro

A professional Blender workflow plugin for Codex.

### Fusion Developer

An Autodesk Fusion workflow plugin for Fusion API, MCP, APS/Fusion Data workflows, Insider compatibility, CAD automation, evidence capture, and local bridge fallback workflows.

### RealityComposerPro

An Apple Reality Composer Pro and RealityKit workflow plugin for Codex.

RealityComposerPro v0.2.1 includes:

- Codex plugin manifest at `plugins/reality-composer-pro/.codex-plugin/plugin.json`.
- Bundled local MCP helper configuration at `plugins/reality-composer-pro/.mcp.json`.
- Skills mapped to the Apple Reality Composer Pro documentation sidebar.
- Release-note workflow for known issues, workarounds, fixed versions, and SDK-specific behavior.
- Local helper tools for reference search, project doctor, asset audit, Swift scaffolding, workflow checklists, task planning, and gitignore suggestions.
- Updated cube-and-cursor logo artwork.

## Install this marketplace in Codex

```bash
codex plugin marketplace add engdahlz/codex-plugins --ref main
codex plugin marketplace list
```

Then restart Codex, open `/plugins`, choose **Engdahlz Codex Plugins**, and install **RealityComposerPro**.

## Development rules

- Do not add plugins unless Axel explicitly requests them.
- Treat skills and MCP configuration as code.
- Keep plugin manifests and marketplace entries accurate.
- Keep skills focused and easy for Codex to select.
