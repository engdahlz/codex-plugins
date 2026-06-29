---
name: fusion-evidence-ledger
description: Use for autonomous Fusion runs that need source evidence, runtime evidence, actions, verification, warnings, and blocked-step tracking.
---

# Fusion evidence ledger

Use `.fusion-runs/<timestamp>/evidence.json` for local run evidence. Do not commit `.fusion-runs/`.

Capture sources, runtime state, before/after snapshots, actions, verification, warnings, and blocked steps.

Evidence should support claims without forcing Axel to micromanage every step.
