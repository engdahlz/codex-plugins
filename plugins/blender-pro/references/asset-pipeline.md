# Asset pipeline reference

## Purpose

Use this reference when preparing Blender assets for reuse, export, rendering, or handoff to another tool.

## Intake checklist

- Target format and destination.
- Real-world dimensions and unit system.
- Required origin point and forward/up axes.
- Texture path requirements.
- Animation requirements.
- External asset sources and license notes.

## Cleanup workflow

1. Preserve originals in `SOURCE_originals`.
2. Rename objects and materials clearly.
3. Check units, scale, object origins, and transforms.
4. Review modifiers and decide what should stay live versus applied.
5. Pack, relink, or document textures.
6. Remove temporary helpers or move them to a helper collection.
7. Export a test file and inspect the result when possible.

## Handoff checklist

- Object names are readable.
- Materials are readable.
- Units and scale are documented.
- Export format and settings are documented.
- Texture paths are valid.
- Licenses and sources are noted.
- Known limitations are listed.
