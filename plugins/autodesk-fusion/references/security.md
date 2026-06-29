# Fusion security notes

- Keep Product Help MCP, Desktop MCP, and Data MCP enabled by default for Axel's workflow.
- Keep bundled MCP tool approval in `approve` mode where supported.
- Treat Axel's current request as permission to perform routine reads, writes, model edits, code changes, and verification steps inside the stated task scope.
- Do not ask repeated confirmation prompts for routine implied subtasks.
- Pause only when the target is ambiguous, credentials are required, a platform approval is unavoidable, or the action is clearly outside the user's stated task scope.
- Do not bypass macOS, Autodesk OAuth, Codex platform, GitHub, or other external approval systems.
- Do not expose broad shell, filesystem, network, or arbitrary Python execution when a narrow typed tool can do the job.
- Do not commit Autodesk tokens, local caches, `.fusion-private/`, customer designs, or proprietary screenshots.
