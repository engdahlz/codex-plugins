# Fusion security notes

- Keep Product Help MCP read-oriented and enabled by default.
- Keep Desktop MCP enabled by default for Axel's workflow, but keep tool approval in `prompt` mode and require explicit approval before mutation.
- Keep Data MCP disabled by default because it requires Autodesk identity and cloud scopes.
- Human approval is required for model mutation, arbitrary script execution, filesystem deployment, save/saveAs/new version, export/overwrite, CAM/post output, permission/admin work, external system writes, and publication.
- Do not expose broad shell, filesystem, network, or arbitrary Python execution when a narrow typed tool can do the job.
- Do not commit Autodesk tokens, local caches, `.fusion-private/`, customer designs, or proprietary screenshots.
