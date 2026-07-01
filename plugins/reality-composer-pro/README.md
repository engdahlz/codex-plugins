# RealityComposerPro

RealityComposerPro is a Codex plugin for Apple Reality Composer Pro, RealityKit, visionOS, USD asset pipelines, and Reality Composer Pro editor-extension workflows.

## Highlights

- Skills mapped to the Apple Reality Composer Pro documentation sidebar.
- Release-note triage workflow for known issues and workarounds.
- Local stdio MCP helper for docs lookup, project inspection, asset audit, Swift scaffolding, checklists, task planning, and gitignore suggestions.
- References for Reality Composer Pro, RealityKit, visionOS, WWDC sessions, custom editor plugins, release notes, and Apple-docs MCP candidates.
- Swift examples for `RealityView` loading and custom component/plugin scaffolding.

## Validate

```bash
python3 plugins/reality-composer-pro/scripts/validate_plugin.py .
python3 plugins/reality-composer-pro/scripts/rcp_helper.py --self-test
```

## Important boundary

The bundled helper is not an Apple-provided remote-control API for the Reality Composer Pro app. It is a local Codex helper for planning, inspection, references, scaffolding, and safe handoff.
