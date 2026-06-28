---
name: fusion-security-approvals
description: Review Fusion workflows for approvals, MCP trust, secrets, destructive actions, filesystem writes, cloud scopes, hooks, and publication risk.
---

# Fusion security and approvals

Use before enabling live tools or publishing.

## Require approval for

- model/CAM/cloud mutation.
- arbitrary Fusion script execution.
- save, saveAs, new version, export, or overwrite.
- NC/post output.
- permission/admin changes.
- external system writes.
- plugin hooks or lifecycle automation.
