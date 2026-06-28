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

## Live operation protocol

1. Inspect current state.
2. Create a small plan.
3. Ask approval for each mutation class.
4. Mutate only the approved smallest step.
5. Verify through independent semantic and visual evidence when possible.
6. Save or export only after separate approval.

## Always check

- active document/product/viewport may be null.
- design units and database units.
- occurrence context versus native objects.
- event handler lifetime and cleanup.
- preview API status.
- whether actions touch files, cloud state, CAM, posts, or user preferences.
