# MFGDM direct fallback

MFGDM is for product/design data such as component hierarchy, properties, and related manufacturing design metadata without requiring a live Fusion desktop session.

v0.2.6 includes MFGDM-oriented bridge methods, but the GraphQL endpoint is intentionally configurable and blank by default. Do not invent endpoint URLs or schema fields. Configure `mfgdm_graphql_url` only after confirming the official Autodesk endpoint and schema for the target account/API version.

Use APS Data Management tools first for hubs, projects, folders, items, and versions. Use MFGDM calls only when endpoint, scopes, and schema are verified.
