---
name: fusion-workflow-mcp
description: Use when designing a local workflow MCP layer above Autodesk MCP servers for doctor, snapshot, plan, verify, API lookup, and evidence reporting.
---

# Fusion workflow MCP

Use for building a local orchestration layer, not replacing Autodesk MCP.

Expose narrow typed tools such as `fusion_doctor`, `fusion_snapshot`, `fusion_verify`, and `fusion_evidence_report`. Avoid arbitrary shell/Python execution when a typed workflow tool is enough.
