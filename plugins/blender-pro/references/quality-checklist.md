# Blender quality checklist

Run this before final handoff.

## Scene organization

- Objects have descriptive names.
- Materials have descriptive names.
- Collections are logical.
- Temporary objects are removed or placed in a helper collection.
- Original assets are preserved if destructive changes were made.

## Geometry

- Scale is intentional.
- Transforms are applied where necessary.
- Bevels/weighted normals are used for hard-surface quality.
- No obvious z-fighting.
- No duplicate accidental objects.
- Modifiers are named and intentional.

## Materials

- Materials match user intent.
- Metallic/roughness values are plausible.
- Texture/procedural scale looks correct.
- No missing image textures.
- Asset licenses are tracked when external assets are used.

## Lighting

- Main subject is readable.
- Shadows support the composition.
- Exposure is not clipped unless stylistic.
- Light names and types are clear.

## Camera/render

- Final camera is set.
- Resolution and aspect ratio match the deliverable.
- Render engine and samples are appropriate.
- Color management is intentional.
- Output path is safe if rendering to disk.

## Animation

- Frame range is correct.
- Motion is intentional.
- No unintended keys or object drift.
- Constraints/drivers work through the full range.

## MCP safety

- No unnecessary external downloads.
- No hidden credentials or API keys.
- No unrelated filesystem access.
- Destructive edits were explicitly requested or safely backed up.
