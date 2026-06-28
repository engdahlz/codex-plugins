---
name: fusion-addin-scaffold
description: Scaffold and review Autodesk Fusion Python add-ins with manifests, commands, events, cleanup, and deployment discipline.
---

# Fusion add-in scaffold

Use for Python add-in structure.

## Include

- `.manifest` and `.py` entry points.
- `run(context)` and `stop(context)` cleanup.
- Strong references for event handlers.
- Idempotent UI creation/removal.
- Zero Doc guards for `activeDocument`, `activeProduct`, and `activeViewport`.
- Separate domain logic from `adsk` adapters.
