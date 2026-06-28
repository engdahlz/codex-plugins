---
name: fusion-assemblies-context
description: Handle Autodesk Fusion components, occurrences, proxies, native objects, assembly paths, and context-sensitive operations.
---

# Fusion assemblies context

Use when models contain components or occurrences.

## Rules

- Identify root component, active component, occurrence path, and native object.
- Distinguish native objects from occurrence-context proxies.
- Record transform context for geometry operations.
- Avoid mutating the wrong component due to active selection ambiguity.
