# Changelog

## 0.2.5

- Added Fusion runtime doctor script and skill.
- Added evidence ledger script, reference, and skill for autonomous run audit trails.
- Added Fusion API Reference RAG helper scripts and reference documentation.
- Added Computer Use guide and skill for Fusion GUI workflows.
- Added high-autonomy Codex configuration guide.
- Added optional hook examples for session start, pre-MCP logging, and stop checks.
- Added Codex subagent prompt files for API research, implementation, runtime verification, release audit, and Insider regression checks.
- Added 2026-focused skills for Python 3.14, Design Intent, BOM/properties, assembly references, source watching, local workflow MCP, and large assembly performance.
- Updated README, AGENTS, SECURITY, SKILLS index, validation helper, and plugin manifest.

## 0.2.4

- Enabled Autodesk Product Help MCP, Fusion Desktop MCP, and Fusion Data MCP by default.
- Set bundled MCP tool approval to `approve` where supported so Codex can work with fewer confirmation prompts.
- Updated runtime, live MCP, security, CAM, and document-lifecycle skills for high-autonomy operation inside the user's stated task scope.
- Updated README, plugin manifest, agent rules, security notes, and runtime protocol to match the high-autonomy default.

## 0.2.3

- Enabled Autodesk Fusion Desktop MCP by default at `http://127.0.0.1:27182/mcp`.
- Kept Fusion Desktop MCP tool approval in `prompt` mode for live CAD safety.
- Updated README, agent rules, and security notes to match the new default.

## 0.2.2

- Added Autodesk Fusion Developer plugin to `engdahlz/codex-plugins` marketplace.
- Added MCP profiles for Autodesk Product Help, Fusion Desktop MCP, and Fusion Data MCP.
- Added focused Fusion skills for API research, live MCP, add-ins, 2026 API compatibility, Insider compatibility, Electronics read-only, APS cloud workflows, validation, and security.
- Added official-source reference notes and safe live-operation protocol.
