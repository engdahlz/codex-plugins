---
name: blender-render-pipeline
description: Use for Blender render setup, Cycles, Eevee, Workbench, samples, denoise, resolution, color management, camera output, file paths, render passes, transparency, and final render readiness.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Render Pipeline

## Purpose

Prepare Blender scenes for reliable test renders and final renders.

## Workflow

1. Inspect render engine, active camera, resolution, frame range, samples, denoise, color management, output path, and file format.
2. Confirm render intent: still image, animation, viewport preview, transparent PNG, product render, cinematic render, or technical render.
3. Set the camera and verify composition.
4. Choose engine settings that match the goal.
5. Check lighting, exposure, shadows, reflections, transparency, and background.
6. Run a low-cost preview workflow before final settings.
7. Report final settings and any remaining risks.

## Standards

- Use Cycles for higher realism when render time is acceptable.
- Use Eevee when speed or real-time look is more important.
- Use Workbench for fast technical/clay review.
- Do not overwrite important output paths without confirmation.
- Keep render settings documented in the handoff.

## References

- `../../references/render-pipeline.md`
- `../../references/materials-lighting-rendering.md`
- `../../references/quality-checklist.md`
