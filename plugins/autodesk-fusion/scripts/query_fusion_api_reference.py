#!/usr/bin/env python3
"""Small local search helper for Autodesk Fusion API reference docs/stubs/headers."""

from __future__ import annotations

import argparse
from pathlib import Path

DEFAULT_ROOT = Path(".fusion-api-reference")
EXTS = {".html", ".htm", ".pyi", ".h", ".hpp", ".txt", ".md"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Missing {root}; run update_fusion_api_reference.py first")
    hits = []
    needle = args.symbol.lower()
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTS:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        idx = text.lower().find(needle)
        if idx >= 0:
            snippet = text[max(0, idx - 160): idx + 320].replace("\n", " ")
            hits.append((str(path), snippet))
            if len(hits) >= args.limit:
                break
    for path, snippet in hits:
        print(f"\n## {path}\n{snippet}")
    return 0 if hits else 1


if __name__ == "__main__":
    raise SystemExit(main())
