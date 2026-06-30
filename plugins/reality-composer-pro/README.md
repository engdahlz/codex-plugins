# Reality Composer Pro Expert

Reality Composer Pro Expert is a Codex plugin for Apple Reality Composer Pro, RealityKit, visionOS, USD asset pipelines, and Reality Composer Pro 3 editor-extension workflows.

## Included

- Focused skills for RCP authoring, Xcode integration, USD assets, materials, Script Graph, animation, custom plugins, performance, and troubleshooting.
- Local stdio MCP helper for docs search, project inspection, asset audit, Swift scaffolding, checklists, gitignore guidance, and task planning.
- Official-source reference index for Apple Developer pages, WWDC sessions, and Apple sample/source repositories.
- Swift examples for RealityKit content loading and custom Reality Composer Pro editor plugin scaffolding.

## MCP tools

```bash
python3 ${PLUGIN_ROOT}/scripts/rcp_helper.py
```

Tools: `rcp_doc_search`, `rcp_reference_get`, `rcp_project_doctor`, `rcp_asset_audit`, `rcp_swift_scaffold`, `rcp_generate_checklist`, `rcp_plan_task`, `rcp_gitignore_suggestions`.

## Validate

```bash
python3 plugins/reality-composer-pro/scripts/validate_plugin.py .
```
