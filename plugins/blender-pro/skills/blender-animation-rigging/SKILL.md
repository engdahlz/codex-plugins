---
name: blender-animation-rigging
description: Use for Blender animation, keyframes, timeline setup, interpolation, camera animation, constraints, armatures, rigging, pose checks, and motion review.
license: Proprietary
compatibility: Requires Blender and a configured Blender MCP server for live scene interaction.
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Animation Rigging

## Purpose

Create or review animation and rigging work in Blender with safe, inspectable steps.

## Workflow

1. Inspect frame range, FPS, animated objects, constraints, armatures, cameras, and existing keyframes.
2. Confirm animation goal, duration, camera target, and output format.
3. Save or duplicate before changing keyframes, constraints, armatures, or weights.
4. Build key poses first, then refine interpolation and timing.
5. For camera moves, use a target empty when appropriate.
6. For rigs, apply transforms where appropriate before binding and test representative poses.
7. Verify the whole frame range before final handoff.

## Standards

- Use clear names for rigs, bones, controls, constraints, actions, and cameras.
- Avoid unnecessary keys on unchanged channels.
- Use constraints and drivers when motion should remain procedural.
- Check start, middle, and end frames, not only frame 1.

## References

- `../../references/animation-rigging.md`
- `../../references/safety.md`
- `../../references/quality-checklist.md`
