# Fusion API reference RAG

Use Autodesk's official `AutodeskFusion360/FusionAPIReference` repository as the local source of truth for symbol-sensitive Fusion API work.

Recommended setup:

```bash
python plugins/autodesk-fusion/scripts/update_fusion_api_reference.py
python plugins/autodesk-fusion/scripts/query_fusion_api_reference.py --symbol adsk.fusion.Design
```

Retrieval policy:

1. Find exact symbol/signature evidence in Python stubs or C++ headers.
2. Pull behavior/lifecycle notes from the HTML docs.
3. Record the source URL or local path in the evidence ledger.
4. Generate code only after the exact class, method, property, event, enum, and argument semantics are known.
5. Do not mix old snippets with current signatures.

Keep `.fusion-api-reference/` out of Git. It is generated source material, not plugin source.
