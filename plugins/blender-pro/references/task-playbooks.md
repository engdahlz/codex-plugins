# Blender task playbooks

## Create a complete scene from a prompt

1. Restate the scene goal and style.
2. Create collections for environment, hero objects, props, lights, cameras, and helpers.
3. Block out shapes with simple primitives.
4. Add scale anchors and composition camera.
5. Add materials with readable names.
6. Add lighting.
7. Add details only after the silhouette and composition work.
8. Review from the final camera.

## Improve an existing scene

1. Inspect objects, collections, materials, cameras, lights, units, render engine, and frame range.
2. Identify top issues by impact.
3. Propose a ranked plan.
4. Save/duplicate before changing.
5. Fix organization first if it blocks work.
6. Improve lighting/camera before fine materials if the goal is a render.
7. Review with the quality checklist.

## Product visualization

1. Confirm product dimensions and target style.
2. Clean geometry and apply bevel/weighted normals.
3. Create realistic materials.
4. Add studio lighting and a clean background.
5. Use a camera focal length that avoids distortion.
6. Render test, adjust reflections/shadows, then final render.

## Procedural asset generation

1. Define parameters: dimensions, counts, random seed, material palette.
2. Generate objects in a named collection.
3. Add non-destructive modifiers.
4. Keep the script reusable and parameterized.
5. Verify counts and bounding boxes.
6. Save the script in the project if the user wants reproducibility.

## Troubleshoot Blender MCP

1. Check if Blender is open.
2. Check if the Blender-side MCP add-on/server is enabled and connected.
3. Check if Codex sees the `blender` MCP server.
4. Check `uvx` path and Python version.
5. Check host/port.
6. Restart Blender and Codex after config changes.
