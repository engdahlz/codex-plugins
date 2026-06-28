---
name: fusion-api-reference-rag
description: Build source-grounded Fusion API answers using official reference pages, Python stubs, C++ headers, and direct source URLs.
---

# Fusion API reference RAG

Use when Codex needs exact signatures or current API behavior.

## Strategy

1. Find exact symbol in official docs or stubs.
2. Pull 2-3 relevant reference passages.
3. Capture version/lifecycle status.
4. Generate code only after evidence is explicit.
5. Do not mix old snippets with current signatures.
