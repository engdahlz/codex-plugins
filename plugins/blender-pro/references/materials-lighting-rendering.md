# Materials, lighting, and rendering reference

## Material strategy

Start with the visual goal:

- Product render: clean materials, controlled roughness, bevels, studio lighting.
- Game asset: optimized materials, baked detail, packed textures, scale-aware texel density.
- Concept scene: bold silhouettes, readable color palette, fast iteration.
- Photoreal scene: real-world scale, physically plausible lights, measured materials, camera exposure.

## Principled BSDF defaults

- Plastic: metallic 0.0, roughness 0.35–0.65.
- Brushed metal: metallic 1.0, roughness 0.25–0.55, anisotropic if available.
- Glass: transmission/alpha depending on engine, roughness 0.0–0.15, IOR around 1.45.
- Rubber: metallic 0.0, roughness 0.65–0.9, dark base color.
- Ceramic: metallic 0.0, roughness 0.25–0.55, subtle bevels.

## Lighting patterns

### Studio product lighting

- Large area key light front/side above subject.
- Weak fill light opposite side.
- Rim light behind or above to separate silhouette.
- Optional white/gray floor plane for contact shadows.

### Cinematic scene lighting

- Define motivation: sun, window, neon, lamp, fire, monitor, moon.
- Use contrast intentionally.
- Keep silhouette readable from final camera.
- Use volumetrics only when needed.

### Isometric/explainer lighting

- Orthographic camera.
- Soft shadows.
- Clean ambient/fill.
- Saturated but controlled materials.

## Camera checklist

- Is the subject framed clearly?
- Does focal length match intent?
- Are clipping ranges correct?
- Is depth of field desired or distracting?
- Are resolution and aspect ratio set?
- Is the camera named `camera_final` or otherwise obvious?

## Render readiness

- Check render engine.
- Check samples and denoising.
- Check color management.
- Check resolution.
- Check transparent background if needed.
- Check output path before rendering to disk.
- Check all visible helper objects are intended.
