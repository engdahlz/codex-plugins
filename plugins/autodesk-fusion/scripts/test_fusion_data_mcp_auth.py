#!/usr/bin/env python3
"""Guided checks for direct Autodesk Fusion Data MCP auth in Codex."""

print("Direct test path:")
print("1. Ensure ~/.codex/config.toml contains a remote MCP server for https://developer.api.autodesk.com/fusion/mcp")
print("2. Run: codex mcp login autodesk-fusion-data")
print("3. In Codex TUI, run: /mcp")
print("If the login fails due to client metadata/CIMD/redirect registration, use autodesk-fusion-data-bridge instead.")
