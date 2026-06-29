---
name: fusion-live-mcp
description: Inspect and operate an active Autodesk Fusion desktop session through Fusion Desktop MCP with high autonomy.
---

# Fusion live MCP

Use for active Fusion desktop inspection or live operations.

## Autonomy defaults

- Fusion Desktop MCP is enabled by default in this plugin.
- Start with read-only inspection, then proceed with routine operations inside the user's stated task scope.
- Avoid repeated confirmation prompts for model edits, checks, code changes, and verification steps that are clearly implied by the user's request.
- Identify active document, active product, units, save state, target component, and expected side effects.
- Execute in small reliable batches and verify after mutations.
- Pause only for ambiguous targets, missing credentials, unavoidable platform prompts, or operations outside the stated task scope.
