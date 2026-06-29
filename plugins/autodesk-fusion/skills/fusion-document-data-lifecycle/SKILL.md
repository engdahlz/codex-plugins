---
name: fusion-document-data-lifecycle
description: Manage Fusion document lifecycle, file open context, cloud versions, save/export policy, and data panel interactions under the high-autonomy policy.
---

# Fusion document data lifecycle

Use for opening, saving, exporting, versioning, or cloud document workflows.

## Rules

- Identify document identity, save state, cloud item/version, and target path.
- Treat the user's current task as permission for document operations clearly inside that scope.
- Separate open, save, saveAs, export, upload, and publish conceptually in reports.
- Do not rely on document names alone for identity.
- Pause only for ambiguous targets, missing credentials, unavoidable platform prompts, or actions outside the stated scope.
