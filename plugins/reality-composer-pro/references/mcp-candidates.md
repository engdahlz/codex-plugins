# MCP candidates for Apple documentation

The bundled `reality-composer-pro` helper remains the default because it is local, narrow, and purpose-built for this plugin.

Public third-party Apple documentation MCP/RAG candidates found during research:

- `kimsungwhee/apple-docs-mcp`
- `MightyDillah/apple-doc-mcp`
- `BingoWon/apple-rag-mcp`
- `Ahrentlov/appledeepdoc-mcp`

Review any third-party MCP server before enabling it in the plugin: install command, maintenance status, data-source freshness, output quality, and Codex compatibility.

Recommended path:

1. Keep the local helper enabled.
2. Add an optional Apple docs MCP profile only after a candidate is tested in a disposable workspace.
3. Prefer official Apple docs, WWDC transcripts, installed SDK headers, and Apple's Reality Composer Pro package over third-party cached summaries.
4. Document the exact version or commit of any external MCP server before enabling it.
