# Geometry Nodes reference

## Purpose

Use Geometry Nodes when the result should be procedural, adjustable, repeated, scattered, generated from curves/points, or reused with different parameters.

## Planning checklist

- What should the node group generate or modify?
- What parameters should be exposed?
- What inputs are objects, curves, meshes, collections, materials, or numeric values?
- What output should be visible in the viewport and render?
- What density or performance limits matter?

## Recommended node-group structure

1. Inputs and user parameters.
2. Source geometry or points.
3. Distribution or transformation logic.
4. Instance/object/material assignment.
5. Cleanup and realization only when needed.
6. Output geometry.

## Naming standards

- Node groups: `GN_descriptive_goal`.
- Modifier names: `gn_descriptive_goal`.
- Exposed inputs: use readable labels with units.
- Collections: separate sources, generated results, and helpers.

## Review checklist

- Inputs are meaningful and documented.
- Generated geometry has stable scale.
- Instance counts are reasonable.
- Materials are assigned intentionally.
- The node group can be reused without hidden assumptions.
- Viewport performance is acceptable.
