# Codex high-autonomy configuration for Fusion

The plugin sets all bundled Fusion MCP profiles to enabled and uses `approve` as the bundled tool approval default where supported.

This does not bypass platform controls. Codex, macOS, Autodesk OAuth, GitHub, or a missing Fusion MCP server may still require separate action.

Suggested profiles:

## Safe coding

- Use for repo-only plugin edits.
- Keep filesystem limited to the workspace.
- Network only when current source research is needed.

## Fusion live development

- Fusion open.
- Fusion MCP enabled in Preferences > General > API.
- Local endpoint reachable at `127.0.0.1:27182` or configured port.
- Product Help, Desktop, and Data MCP enabled.
- Evidence ledger active for long/mutating tasks.

## Local trusted lab

- Use only in a controlled local environment.
- Wider filesystem/network access may improve automation but increases risk.
- Do not use with private customer CAD unless the repository and evidence output paths are controlled.
