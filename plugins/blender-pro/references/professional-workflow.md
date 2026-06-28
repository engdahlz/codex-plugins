# Professional Blender workflow for Codex

## Default loop

Use this loop for most Blender work:

1. **Clarify outcome**: What should the final scene/model/render/animation accomplish?
2. **Inspect**: If MCP is available, inspect the current scene before modifying it.
3. **Plan**: State a compact plan with object hierarchy, materials, lighting, camera, and render targets.
4. **Protect**: Save, duplicate, or work in a new collection before major edits.
5. **Execute**: Make changes in small batches.
6. **Verify**: Check scene state and report what changed.
7. **Refine**: Improve composition, scale, naming, material quality, lighting, render settings, and cleanup.
8. **Review**: Run the quality checklist before final output.

## Scene organization standards

Use clear collections:

```text
SCENE_main
GEO_environment
GEO_hero
GEO_props
LIGHTS
CAMERAS
MATERIAL_TESTS
SOURCE_originals
RENDER_helpers
```

Name objects descriptively:

```text
hero_robot_body_lowpoly
lamp_key_area_softbox
camera_final_35mm
mat_brushed_aluminum_dark
```

## Scale and units

- Confirm scene units before modeling.
- Use realistic dimensions when the user requests realism, CAD-like results, or product visualization.
- Apply transforms when appropriate, especially before booleans, bevels, rigging, or export.
- Keep origins intentional: world origin for layout, object base for props, joint locations for rig parts.

## Modeling standards

- Prefer simple primitives plus modifiers for quick procedural work.
- Use bevels and weighted normals for hard-surface assets.
- Use array/mirror/screw/solidify modifiers for repeatable geometry.
- Keep modifiers named and non-destructive until finalization.
- Avoid over-dense geometry unless detail is necessary.

## Materials standards

- Use Principled BSDF as the default material foundation.
- Name materials by look and purpose.
- Use roughness/metallic/transmission intentionally.
- For procedural materials, expose key values in the material name or reference notes.

## Lighting and camera standards

- Add a camera early for composition.
- Use focal length intentionally: wide for space, 50–85mm for product/portrait-like framing.
- Use key/fill/rim or HDRI/studio lighting depending on the style.
- Verify clipping distances, depth of field, resolution, and render engine.

## Reporting standard

After changes, report:

- What was changed.
- What was verified.
- What remains uncertain.
- Suggested next refinements.
