# Local workflow MCP layer

Autodesk MCP servers should remain the source of truth for Autodesk data and live Fusion access. A local workflow MCP can sit above them to give Codex stable, typed orchestration tools.

Potential local tools:

- `fusion_doctor`
- `fusion_snapshot`
- `fusion_plan`
- `fusion_verify`
- `fusion_api_lookup`
- `fusion_source_check`
- `fusion_evidence_report`

Rules:

- Do not expose arbitrary filesystem, shell, or Python execution if a narrow typed tool is enough.
- Keep mutating workflow tools scoped to the current task.
- Log meaningful actions to the evidence ledger.
