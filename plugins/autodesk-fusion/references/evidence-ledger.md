# Evidence ledger

High autonomy works best when Codex leaves an audit trail.

Use `.fusion-runs/<timestamp>/evidence.json` for local run evidence. Do not commit `.fusion-runs/` because it may contain document names, project names, screenshots, or runtime details.

Recommended lifecycle:

```bash
python plugins/autodesk-fusion/scripts/evidence_ledger.py init --task "Fusion task"
python plugins/autodesk-fusion/scripts/evidence_ledger.py source .fusion-runs/<id>/evidence.json https://help.autodesk.com/... --symbol adsk.fusion.Design
python plugins/autodesk-fusion/scripts/evidence_ledger.py add .fusion-runs/<id>/evidence.json actions "Created command scaffold"
python plugins/autodesk-fusion/scripts/evidence_ledger.py add .fusion-runs/<id>/evidence.json verification "Validated SKILL.md frontmatter"
```

Capture:

- source URLs and symbols used.
- runtime state before and after work.
- actions performed.
- verification evidence.
- blocked platform/OAuth/runtime steps.
- warnings and assumptions.
