#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / ".agents" / "plugins" / "marketplace.json"
MIRRORS = [
    ROOT / ".codex-plugin" / "marketplace.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / "marketplace.json",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or rewrite mirrored Codex marketplace manifests.")
    parser.add_argument("--write", action="store_true", help="Rewrite mirrors from .agents/plugins/marketplace.json")
    args = parser.parse_args()

    canonical = load(CANONICAL)
    failed: list[str] = []
    for mirror in MIRRORS:
        if args.write:
            dump(mirror, canonical)
            continue
        if not mirror.exists():
            failed.append(f"missing: {mirror}")
            continue
        if load(mirror) != canonical:
            failed.append(f"out of sync: {mirror}")
    if failed:
        raise SystemExit("Marketplace sync failed:\n" + "\n".join(failed) + "\nRun: python scripts/sync_marketplaces.py --write")
    print("OK: marketplace manifests are synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
