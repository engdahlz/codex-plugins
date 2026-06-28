# Blender MCP tool contract

## Purpose

This document defines how Blender Pro should use Blender MCP tools.

## Operating contract

- Start with inspect-only when the scene state is unknown.
- State a short plan before changing the scene.
- Prefer small, reversible batches.
- Verify after each batch.
- Keep created objects, materials, lights, cameras, collections, and node groups clearly named.
- Preserve original objects when performing major edits.
- Avoid external asset downloads unless the user approves them.
- Track external asset source and license notes when assets are used.

## Approval posture

The bundled MCP config uses prompt approval mode by default. Keep this default unless Axel explicitly asks to change it.

## High-risk operations

Pause and ask for confirmation before:

- Replacing the whole scene.
- Removing many objects or collections.
- Applying irreversible changes across many objects.
- Writing output files over important paths.
- Enabling external asset downloads.
- Using stored credentials for third-party asset services.

## Result report

After tool use, report:

- What changed.
- What was verified.
- What was not verified.
- Recommended next step.
