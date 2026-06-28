---
name: blender-asset-pipeline
description: Use for Blender import/export workflows, asset cleanup, naming, units, origins, transforms, texture paths, external asset provenance, licensing notes, glTF/FBX/USDZ/OBJ handoff, and production-ready asset organization.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Asset Pipeline

## Purpose

Prepare Blender assets for reliable import, export, reuse, and handoff.

## Workflow

1. Confirm target format and destination: Blender reuse, game engine, web viewer, CAD handoff, render-only, or archive.
2. Inspect units, scale, object origins, transforms, collections, modifiers, materials, textures, animations, and linked data.
3. Preserve source assets in a source collection before cleanup.
4. Normalize naming for objects, materials, textures, cameras, lights, and collections.
5. Check external asset source and license notes.
6. Prepare export settings and verify the exported result when possible.
7. Provide a handoff summary with assumptions and remaining risks.

## Format notes

- glTF/GLB: good for web and real-time workflows.
- FBX: common for DCC/game-engine interchange but can vary by importer.
- OBJ: simple static mesh exchange; limited materials.
- USD/USDZ: useful for Apple/AR and scene interchange.
- BLEND: best for preserving native Blender data.

## References

- `../../references/asset-pipeline.md`
- `../../references/quality-checklist.md`
- `../../references/safety.md`
