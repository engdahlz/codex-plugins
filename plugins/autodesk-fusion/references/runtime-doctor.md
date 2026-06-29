# Fusion runtime doctor

Use `scripts/fusion_doctor.py` before live Fusion tasks when practical.

The doctor is passive. It checks local Desktop MCP reachability, Product Help MCP reachability, Fusion Data MCP reachability, and records likely blockers without mutating the active design.

```bash
python plugins/autodesk-fusion/scripts/fusion_doctor.py --json-out /tmp/fusion-doctor.json
```

Interpretation:

- Desktop MCP TCP failure usually means Fusion is closed, MCP is disabled in Fusion preferences, or the port changed.
- Data MCP HTTP success does not mean Autodesk OAuth is complete.
- Product Help MCP is documentation-oriented and should normally be safe to use for research.

Doctor results should be copied into the evidence ledger for long autonomous runs.
