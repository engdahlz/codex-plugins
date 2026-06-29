---
name: fusion-source-watcher
description: Use to check official Autodesk, APS, OpenAI Codex, and MCP source drift before updating plugin behavior or API assumptions.
---

# Fusion source watcher

Use `scripts/check_autodesk_sources.py` to detect likely changes in official sources.

A source status change is a trigger to reread sources, not automatic proof that plugin behavior should change.
