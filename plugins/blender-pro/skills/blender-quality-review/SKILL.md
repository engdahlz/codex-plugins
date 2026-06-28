---
name: blender-quality-review
description: Use for Blender quality review across scene organization, scale, transforms, topology, modifiers, materials, lighting, camera, render settings, animation, export readiness, and handoff risks.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Quality Review

## Purpose

Review a Blender scene before final handoff, rendering, export, or further automated editing.

## Review workflow

1. Inspect scene units, frame range, render engine, output settings, cameras, lights, collections, objects, materials, and modifiers.
2. Check scene organization: naming, collections, helper objects, and preserved source objects.
3. Check geometry: scale, transforms, origins, density, bevels, normals, duplicate objects, and z-fighting.
4. Check materials and textures: missing assets, plausible shader values, clear material names, and external source notes.
5. Check lighting and camera: readable subject, clipping, focal length, exposure, shadows, and composition.
6. Check render readiness: engine, samples, denoise, color management, resolution, output path, and transparency needs.
7. Check animation if present: frame range, keyframes, constraints, object drift, and camera movement.
8. Return a prioritized fix list with high-impact items first.

## Output format

- Summary of current state.
- Critical issues.
- Important improvements.
- Optional polish.
- Recommended next action.

## References

- `../../references/quality-checklist.md`
- `../../references/professional-workflow.md`
- `../../references/render-pipeline.md`
- `../../references/asset-pipeline.md`
