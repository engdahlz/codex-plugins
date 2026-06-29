# Runtime protocol

## Router

Use this routing model before implementation:

```text
Official docs and API facts          -> Autodesk Product Help MCP / official URLs
Active desktop model inspection      -> Fusion Desktop MCP / Fusion API
Hub, project, item, version metadata -> Fusion Data MCP / MFGDM
Headless cloud automation            -> APS Automation API for Fusion
Shop-floor production data           -> Fusion Operations API
Native Fusion dialogs and UI         -> Codex Computer Use / appshots
Palette or Viewer browser UI         -> Codex browser workflows
Repository-only plugin work          -> Codex file edits and tests
```

## High-autonomy live operation protocol

1. Inspect current state before mutation.
2. Treat the user's current request as authorization for ordinary operations inside the stated scope.
3. Do not ask repeated confirmation questions for routine subtasks.
4. Execute in the smallest reliable batches.
5. Verify through independent semantic and visual evidence when possible.
6. Report blocked platform, OAuth, OS, missing-server, permission, or runtime steps as blocked, not passed.
7. Pause only when the target is ambiguous, credentials are required, a platform approval is unavoidable, or the operation is clearly outside the user's stated scope.

## Always check

- active document/product/viewport may be null.
- design units and database units.
- occurrence context versus native objects.
- event handler lifetime and cleanup.
- preview API status.
- whether actions touch files, cloud state, CAM, posts, or user preferences.
