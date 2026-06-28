---
name: blender-generalist
description: Use for broad Blender workflow coordination across MCP setup, scene inspection, modeling, materials, lighting, rendering, animation, asset pipeline, Geometry Nodes, bpy planning, and quality review.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Generalist

## Purpose

Coordinate Blender Pro workflows and route the task to the right specialized skill.

## Standard workflow

1. Identify the requested outcome: inspect, create, edit, render, animate, export, troubleshoot, or review.
2. If MCP is available, inspect the scene before changing it.
3. Write a short plan with collections, objects, materials, lighting, camera, and output targets.
4. Work in small batches and verify after each batch.
5. Use clear names for objects, materials, node groups, lights, cameras, and collections.
6. Finish with a quality review and a concise report of what changed.

## Skill routing

- Use `blender-mcp-setup` for connection and environment problems.
- Use `blender-scene-modeling` for layout, object creation, modifiers, and scale.
- Use `blender-materials-lighting` for shaders, lights, cameras, and look development.
- Use `blender-render-pipeline` for render engine, samples, color management, output, and final render readiness.
- Use `blender-animation-rigging` for timeline, keyframes, constraints, rigs, and motion review.
- Use `blender-geometry-nodes` for procedural node systems.
- Use `blender-asset-pipeline` for import, export, naming, units, provenance, and handoff.
- Use `blender-bpy-workflows` for planning and reviewing Blender scripting workflows.
- Use `blender-quality-review` before final handoff.

## References

- `../../references/professional-workflow.md`
- `../../references/safety.md`
- `../../references/quality-checklist.md`
- `../../examples/prompts.md`
