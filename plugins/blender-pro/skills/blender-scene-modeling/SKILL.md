---
name: blender-scene-modeling
description: Use for Blender scene creation, object layout, scale, collections, transforms, modifiers, hard-surface modeling, procedural primitives, cleanup, and geometry organization.
license: Proprietary
metadata:
  plugin: blender-pro
  version: "0.2.0"
---

# Blender Scene Modeling

## Purpose

Create and improve Blender scenes with clean organization, readable scale, and maintainable geometry.

## Workflow

1. Inspect units, collections, object count, transforms, selected objects, and visible cameras/lights.
2. Block out the scene with simple primitives before adding detail.
3. Use collections such as `GEO_main`, `GEO_props`, `LIGHTS`, `CAMERAS`, and `SOURCE_originals`.
4. Keep originals when making major edits.
5. Prefer non-destructive modifiers while iterating: bevel, mirror, array, solidify, weighted normals, subdivision, or shrinkwrap as appropriate.
6. Apply transforms only when it helps modeling, rigging, export, or predictable modifiers.
7. Verify names, origins, dimensions, transforms, and modifier stacks before handoff.

## Modeling standards

- Use real-world scale when the user asks for realism, product work, CAD-like work, or export.
- Use bevels and weighted normals for hard-surface polish.
- Keep helper objects in a helper collection.
- Avoid unnecessary mesh density.
- Report any uncertain measurements or assumptions.

## References

- `../../references/professional-workflow.md`
- `../../references/task-playbooks.md`
- `../../references/quality-checklist.md`
