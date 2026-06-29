# Changelog

## 0.2.9

- Renamed the plugin display name from `Autodesk Fusion Developer` to `Fusion Developer`.

## 0.2.8

- Replaced Autodesk Fusion Developer PNG logo and icon variants with the updated Fusion + Codex arrow artwork.

## 0.2.7

- Updated Autodesk Fusion Developer plugin visuals to use the new Fusion + Codex arrow PNG icon set.
- Added PNG icon, logo, 128px/256px variants, and marketplace screenshot asset.
- Updated plugin manifest to point `composerIcon`, `logo`, and `screenshots` to PNG assets for better Codex UI compatibility.

## 0.2.6

- Added `autodesk-fusion-data-bridge`, a local stdio MCP bridge for Codex-compatible Autodesk OAuth and read-only Fusion cloud data workflows.
- Added bridge modules for PKCE OAuth, local token storage/redaction, APS Data Management reads, configurable MFGDM placeholders, schemas, and stdio MCP server handling.
- Added bridge tests and direct Fusion Data MCP auth guidance.
- Added references for Fusion Data MCP auth, bridge architecture, and MFGDM direct fallback.
- Added `fusion-data-auth-bridge` skill and updated SKILLS index.
- Updated `.mcp.json`, README, SECURITY, AGENTS, `.gitignore`, validation helper, and file list.

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
