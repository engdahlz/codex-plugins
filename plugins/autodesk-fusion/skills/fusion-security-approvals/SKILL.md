---
name: fusion-security-approvals
description: Apply the Autodesk Fusion plugin's high-autonomy policy while respecting secrets, platform prompts, MCP trust boundaries, hooks, and destructive-action risk.
---

# Fusion autonomy and security

Use before enabling live tools or publishing.

## Autonomy policy

Axel has requested that the Fusion plugin work as freely as possible without repeated confirmation prompts. Treat the current task as authorization for ordinary reads, writes, model edits, code changes, tests, and verification steps inside the stated scope.

## Do not pause for

- routine Fusion API reads.
- routine MCP inspection.
- model edits clearly requested by the task.
- code edits, validation, tests, and documentation updates inside the current repository task.
- routine save/export/post steps explicitly included in the user's request.

## Pause only for

- ambiguous destructive targets.
- missing credentials or OAuth authorization.
- unavoidable Codex, macOS, Autodesk, GitHub, or external platform approvals.
- actions outside the user's stated task scope.
- secrets, private CAD files, NDA Insider artifacts, or customer data that would be committed or exposed.
