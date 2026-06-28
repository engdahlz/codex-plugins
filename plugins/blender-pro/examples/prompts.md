# Blender Pro prompt examples

## Inspect without changing

```text
Use Blender Pro. Inspect my current Blender scene through MCP and report objects, collections, cameras, lights, units, render engine, frame range, and the top five quality issues. Do not change anything.
```

## Create a scene

```text
Use Blender Pro to create a clean low-poly sci-fi maintenance bay in Blender. Work in small batches, create named collections, add materials, lighting, camera, and render settings. Verify the scene after each batch.
```

## Product render

```text
Use Blender Pro to turn the selected object into a professional studio product render. Preserve the original object, improve materials, add bevel/weighted normals if appropriate, create three-point lighting, set a final camera, and prepare Cycles render settings.
```

## Safe Python automation

```text
Use Blender Pro to write Blender Python that creates a reusable procedural shelf system with adjustable dimensions. Explain the script first, then run it through MCP only after checking that it does not delete existing objects.
```

## Animation

```text
Use Blender Pro to animate a camera orbit around the main object from frame 1 to 120. Use a target empty, smooth interpolation, and verify the frame range/camera composition.
```

## Quality review

```text
Use Blender Pro to review this scene for production readiness: naming, collections, scale, transforms, materials, lighting, camera, render settings, and safety concerns. Give me a prioritized fix list.
```

## MCP troubleshooting

```text
Use Blender Pro MCP setup. Codex cannot connect to Blender. Walk me through checking uvx, the bundled .mcp.json, Blender add-on state, host/port, and Codex /mcp status.
```
