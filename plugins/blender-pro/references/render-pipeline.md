# Render pipeline reference

## Purpose

Use this reference to prepare reliable preview renders and final renders from Blender.

## Render setup checklist

- Active camera is set.
- Composition is checked from the active camera.
- Resolution and aspect ratio match the deliverable.
- Render engine matches the goal.
- Samples, denoise, shadows, and color management are intentional.
- Output path and file format are safe.
- Frame range is correct for animation.

## Engine guidance

- Cycles: best for physically plausible lighting, reflections, and product-style realism.
- Eevee: best for speed, stylized scenes, and real-time preview workflows.
- Workbench: best for fast technical, clay, and modeling reviews.

## Preview-first workflow

1. Set a low-cost preview resolution or samples.
2. Verify framing, exposure, and silhouette.
3. Fix lighting and materials before raising quality settings.
4. Check final output path.
5. Increase final samples/resolution only after the preview is correct.

## Final handoff

Report the engine, camera, resolution, samples, denoise state, color management, output path, and known issues.
