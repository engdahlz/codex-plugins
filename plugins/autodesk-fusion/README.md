# Autodesk Fusion Developer Codex Plugin

Autodesk Fusion Developer makes Codex behave like a high-autonomy Fusion API, APS, MCP, and CAD automation assistant.

## Design goals

1. Use official Autodesk/OpenAI/MCP sources before coding.
2. Keep Product Help MCP, Fusion Desktop MCP, and Fusion Data MCP enabled by default.
3. Let Codex act inside the user's stated task scope without repeated confirmation prompts.
4. Keep Fusion Data MCP and APS cloud workflows conceptually separate from live desktop API workflows.
5. Treat Fusion Insider as a test channel, not a public baseline.
6. Verify results and report blocked platform/auth/runtime steps honestly.
7. Keep preview and Insider-only functionality out of public marketplace release paths.

## Included skills

See [`SKILLS.md`](SKILLS.md) for the full skill index.

## MCP profiles

- `autodesk-product-help` is enabled by default for Autodesk documentation research and uses `approve` tool approval.
- `autodesk-fusion-desktop` is enabled by default and points to `http://127.0.0.1:27182/mcp`; tool approval is set to `approve` in the bundled config.
- `autodesk-fusion-data` is enabled by default and points to `https://developer.api.autodesk.com/fusion/mcp`; tool approval is set to `approve` in the bundled config.

The MCP profiles are `required: false` so the plugin still installs when Fusion is closed or Autodesk OAuth is not available yet.

## High-autonomy live Fusion workflow

When MCP or Fusion Python access is available, Codex should:

1. Inspect the current document/product/units before mutation.
2. Treat the user's current task as approval for ordinary reads, writes, modeling steps, and code changes inside that task's scope.
3. Avoid repeated confirmation prompts for routine steps.
4. Execute in small reversible batches where possible.
5. Verify semantically and visually when possible.
6. Report platform, OAuth, OS, missing-server, or permission blocks honestly instead of claiming success.
7. Pause only when the requested target is ambiguous, credentials are required, a platform approval is unavoidable, or the action is clearly outside the user's stated task scope.

## Key references

- `references/official-sources.md`
- `references/insider-compatibility.md`
- `references/runtime-protocol.md`
- `references/security.md`
