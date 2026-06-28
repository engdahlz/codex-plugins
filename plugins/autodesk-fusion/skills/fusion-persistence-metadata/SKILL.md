---
name: fusion-persistence-metadata
description: Use Fusion attributes, entity tokens, naming, and external IDs for durable model metadata and recovery.
---

# Fusion persistence metadata

Use when an add-in must find or recover objects later.

## Rules

- Use attributes and stable naming for add-in-owned data.
- Treat entity tokens as recovery hints, not permanent universal IDs.
- Store versioned metadata schemas.
- Include cleanup and migration paths.
