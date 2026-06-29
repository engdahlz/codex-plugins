# Autodesk Fusion Developer Codex Plugin

Autodesk Fusion Developer makes Codex behave like a high-autonomy, evidence-driven Fusion API, APS, MCP, and CAD automation assistant.

## Design goals

1. Use official Autodesk/OpenAI/MCP sources before coding.
2. Keep Product Help MCP, Fusion Desktop MCP, and Fusion Data MCP enabled by default.
3. Run runtime doctor checks before live Fusion work.
4. Let Codex act inside the user's stated task scope without repeated confirmation prompts.
5. Record an evidence ledger for autonomous runs.
6. Query the official Fusion API reference, Python stubs, and C++ headers before writing symbol-sensitive API code.
7. Treat Fusion Insider as a test channel, not a public baseline.
8. Verify results and report blocked platform/auth/runtime steps honestly.

## Included skills

See [`SKILLS.md`](SKILLS.md) for the full skill index.

## MCP profiles

- `autodesk-product-help` is enabled by default for Autodesk documentation research and uses `approve` tool approval.
- `autodesk-fusion-desktop` is enabled by default and points to `http://127.0.0.1:27182/mcp`.
- `autodesk-fusion-data` is enabled by default and points to `https://developer.api.autodesk.com/fusion/mcp`.
- All bundled MCP profiles are `required: false` so the plugin still installs when Fusion is closed or Autodesk OAuth is not available yet.

## Recommended autonomous run

```bash
python plugins/autodesk-fusion/scripts/fusion_doctor.py
python plugins/autodesk-fusion/scripts/evidence_ledger.py init --task "Describe the Fusion task"
python plugins/autodesk-fusion/scripts/query_fusion_api_reference.py --symbol adsk.fusion.Design
```

Then let Codex execute the requested work, verify the result, and finalize the ledger.

## Key references

- `references/runtime-doctor.md`
- `references/evidence-ledger.md`
- `references/api-reference-rag.md`
- `references/codex-high-autonomy-config.md`
- `references/computer-use-fusion.md`
- `references/workflow-mcp.md`
- `references/source-watcher.md`
- `references/official-sources.md`
- `references/insider-compatibility.md`
- `references/runtime-protocol.md`
- `references/security.md`
