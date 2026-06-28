# Autodesk Fusion Developer Codex Plugin

Autodesk Fusion Developer makes Codex behave like a disciplined Fusion API, APS, MCP, and CAD automation assistant.

## Design goals

1. Use official Autodesk/OpenAI/MCP sources before coding.
2. Use Product Help MCP for documentation and Fusion Desktop MCP for live desktop work when Fusion is running.
3. Keep Fusion Data MCP and APS cloud workflows separate from live desktop API workflows.
4. Treat Fusion Insider as a test channel, not a public baseline.
5. Use `inspect -> plan -> approve -> mutate -> verify` for all live CAD operations.
6. Keep preview and Insider-only functionality out of public marketplace release paths.

## Included skills

See [`SKILLS.md`](SKILLS.md) for the full skill index.

## MCP profiles

- `autodesk-product-help` is enabled by default for Autodesk documentation research.
- `autodesk-fusion-desktop` is enabled by default and points to `http://127.0.0.1:27182/mcp`; tool approval remains in `prompt` mode.
- `autodesk-fusion-data` is disabled by default and points to `https://developer.api.autodesk.com/fusion/mcp`.

## Safe live Fusion workflow

When MCP or Fusion Python access is available, Codex should:

1. Inspect the current document/product/units without mutation.
2. State the runtime and evidence sources.
3. Produce a mutation plan with expected object/timeline/file/cloud side effects.
4. Ask for approval before model, CAM, cloud, save, export, or filesystem mutation.
5. Execute the smallest approved step.
6. Verify semantically and visually when possible.
7. Report blocked live tests honestly.

## Key references

- `references/official-sources.md`
- `references/insider-compatibility.md`
- `references/runtime-protocol.md`
- `references/security.md`
