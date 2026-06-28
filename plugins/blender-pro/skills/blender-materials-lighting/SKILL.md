---
name: blender-materials-lighting
description: Use for Blender materials, shaders, procedural textures, lighting, cameras, Cycles/Eevee look development, color management, exposure, and visual polish.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Materials Lighting

## Purpose

Make Blender scenes visually clear, intentional, and render-ready.

## Workflow

1. Inspect materials, shader nodes, textures, lights, cameras, render engine, color management, and resolution.
2. Identify the target style: studio product, cinematic, low-poly, photoreal, technical, game asset, or concept art.
3. Improve base materials first: color, roughness, metallic, alpha, normal/detail, and naming.
4. Set the final camera early and judge visual changes through that camera.
5. Add lighting with a clear motivation: studio key/fill/rim, HDRI, window, practical lights, emissive accents, or sun/sky.
6. Tune exposure, color management, shadows, reflections, and background.
7. Verify final camera framing, render engine, samples, resolution, and output intent.

## Standards

- Name materials by look and purpose, for example `mat_brushed_metal_dark`.
- Use physically plausible values when realism matters.
- Avoid external asset downloads unless the user approves them.
- Track texture/HDRI/model source and license when external assets are used.

## References

- `../../references/materials-lighting-rendering.md`
- `../../references/render-pipeline.md`
- `../../references/quality-checklist.md`
