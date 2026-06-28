# Blender bpy workflows reference

## Purpose

Use this reference for planning and reviewing Blender bpy workflows before applying them through MCP.

## Safe workflow

1. Inspect the current scene.
2. Define the exact target objects, collections, materials, lights, cameras, or node groups.
3. Plan the change in small steps.
4. Explain the intended result.
5. Apply only one small batch at a time.
6. Verify the result after each batch.
7. Report what changed and what remains uncertain.

## Review checklist

- Scope is clear.
- Names are clear.
- Created objects belong in known collections.
- Output can be verified in the scene.
- No credentials are stored.
- No unrelated local files are read.
- No broad scene removal happens without user approval.

## Common patterns

- Create a named collection.
- Create primitives with explicit dimensions and locations.
- Assign materials with descriptive names.
- Add cameras and lights with clear names.
- Check object count, dimensions, transforms, and render settings after changes.
