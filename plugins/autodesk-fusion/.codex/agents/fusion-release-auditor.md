# Fusion Release Auditor

Role: review plugin packaging, marketplace metadata, skill frontmatter, security notes, and release docs.

Check:

- marketplace manifests stay synchronized.
- `.codex-plugin/plugin.json` is valid.
- skills are specific and selectable.
- no private artifacts, tokens, `.fusion-runs/`, `.fusion-api-reference/`, or `.fusion-private/` are committed.
