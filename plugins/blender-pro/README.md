# Blender Pro Codex Plugin

Blender Pro makes Codex behave like a disciplined Blender professional: scene planner, modeler, material and lighting artist, render technician, animator, rigger, asset-pipeline assistant, Geometry Nodes planner, bpy workflow reviewer, and final quality reviewer.

## Design goals

1. Use MCP for live Blender control when the Blender MCP server and Blender-side add-on are running.
2. Use focused Agent Skills so Codex chooses the right workflow without loading unnecessary context.
3. Use references and checklists so complex Blender work is planned, executed, verified, and reviewed.
4. Keep MCP tool approval in prompt mode by default.
5. Avoid hooks until there is a strong reason to add them.

## Included skills

- `blender-generalist` — broad Blender orchestration and skill routing.
- `blender-mcp-setup` — setup and troubleshooting for Blender MCP.
- `blender-scene-modeling` — scene layout, collections, transforms, modifiers, scale, and geometry cleanup.
- `blender-materials-lighting` — materials, shaders, lighting, cameras, and visual polish.
- `blender-animation-rigging` — keyframes, constraints, armatures, camera motion, and rig review.
- `blender-quality-review` — production-readiness review and prioritized fix lists.
- `blender-geometry-nodes` — procedural node-system planning and review.
- `blender-asset-pipeline` — imports, exports, naming, scale, handoff, and asset provenance.
- `blender-render-pipeline` — Cycles/Eevee/Workbench render setup and output checks.
- `blender-bpy-workflows` — safe Blender `bpy` workflow planning and script review.

## MCP server

The bundled `./.mcp.json` configures a local stdio Blender MCP server named `blender`.

Default command:

```json
{
  "command": "uvx",
  "args": ["--python", "3.11", "blender-mcp"]
}
```

The configuration keeps tool approval in prompt mode and disables telemetry by default:

```json
{
  "DISABLE_TELEMETRY": "true"
}
```

## Setup summary

1. Install Blender.
2. Install and enable the Blender MCP add-on/server in Blender.
3. Install or verify `uvx`.
4. Start Blender and start the Blender-side MCP connection.
5. Install this marketplace in Codex:

```bash
codex plugin marketplace add engdahlz/codex-plugins
```

6. Install and enable **Blender Pro** in Codex.
7. Start with an inspect-only prompt before making scene changes.

## Safe live-scene workflow

When MCP is available, Codex should:

1. Inspect the current scene.
2. State a short plan.
3. Save or duplicate before destructive changes.
4. Execute changes in small batches.
5. Verify scene state after each batch.
6. Name objects, materials, collections, lights, cameras, node groups, and helpers clearly.
7. Review scale, topology, transforms, materials, lighting, cameras, render settings, asset provenance, and output readiness.

When MCP is not available, Codex should provide setup help, step-by-step Blender instructions, or a reviewable script; it should not claim that it changed Blender.

## Key references

- `references/mcp-setup.md`
- `references/mcp-setup-macos.md`
- `references/mcp-setup-windows.md`
- `references/mcp-setup-linux.md`
- `references/mcp-troubleshooting.md`
- `references/mcp-tool-contract.md`
- `references/professional-workflow.md`
- `references/geometry-nodes.md`
- `references/asset-pipeline.md`
- `references/render-pipeline.md`
- `references/blender-bpy-workflows.md`
- `references/quality-checklist.md`

## Why no hooks yet

Codex plugins can include hooks, but hooks require extra trust review. Blender Pro v0.2.0 stays skill/MCP/reference based so it remains easier to audit.
