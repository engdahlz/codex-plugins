# Blender Pro Codex Plugin

Blender Pro makes Codex behave like a disciplined Blender professional: scene planner, modeler, materials/lighting artist, render technician, animator, rigger, Python automation assistant, and reviewer.

The plugin is designed around three ideas:

1. **Use MCP for live Blender control** when the Blender MCP server is configured and the Blender add-on/server is running.
2. **Use focused Agent Skills** so Codex chooses the right Blender workflow without bloating context.
3. **Use references and checklists** so complex Blender work is planned, executed, verified, and reviewed instead of guessed.

## What is included

```text
blender-pro/
├── .codex-plugin/plugin.json
├── .mcp.json
├── assets/
├── examples/
├── references/
├── scripts/
└── skills/
```

## Skills

- `blender-generalist` — orchestration skill for broad Blender work.
- `blender-mcp-setup` — setup/troubleshooting for Blender MCP.
- `blender-scene-modeling` — scene creation, layout, scale, collections, object modeling.
- `blender-materials-lighting` — materials, shaders, lighting, cameras, rendering.
- `blender-animation-rigging` — keyframes, timelines, constraints, rigs, camera animation.
- `blender-python-automation` — safe `bpy` automation and script generation.
- `blender-quality-review` — final review, cleanup, render readiness, production checklist.

## MCP server

The bundled `./.mcp.json` configures a local stdio Blender MCP server named `blender`.

Default command:

```json
{
  "command": "uvx",
  "args": ["--python", "3.11", "blender-mcp"]
}
```

The configuration intentionally keeps tool approval in prompt mode and disables telemetry by default:

```json
{
  "DISABLE_TELEMETRY": "true"
}
```

## Setup summary

1. Install Blender.
2. Install the official Blender MCP server/add-on from Blender Lab.
3. Install or verify `uvx` if the MCP server uses the `uvx blender-mcp` launcher.
4. Start Blender and enable/start the Blender MCP add-on/server inside Blender.
5. Install this marketplace in Codex:

```bash
codex plugin marketplace add engdahlz/codex-plugins
```

6. Install and enable **Blender Pro** in Codex.
7. Start a Blender task with one of the example prompts in `examples/prompts.md`.

## Professional workflow

When MCP is available, Codex should:

1. Inspect the current scene.
2. State a short plan.
3. Save or duplicate before destructive changes.
4. Execute changes in small batches.
5. Verify scene state after each batch.
6. Name objects/materials/collections clearly.
7. Review scale, topology, transforms, camera, lighting, render settings, and asset provenance.

When MCP is not available, Codex should not pretend to have modified Blender. It should provide a script, step-by-step instructions, or troubleshooting for the MCP connection.

## Why no hooks yet

Hooks can be powerful, but they require extra trust review. This first version deliberately ships without hooks. The plugin is skill/MCP/reference based, which is safer and easier to audit.
