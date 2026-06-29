#!/usr/bin/env python3
"""Create and append evidence ledgers for autonomous Fusion runs."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd()
RUNS = ROOT / ".fusion-runs"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cmd_init(args: argparse.Namespace) -> int:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    data = {
        "schemaVersion": "fusion-evidence-ledger-v1",
        "runId": run_id,
        "task": args.task,
        "createdAt": now(),
        "sourcesUsed": [],
        "runtime": {},
        "before": {},
        "actions": [],
        "after": {},
        "verification": [],
        "blocked": [],
        "warnings": []
    }
    save(run_dir / "evidence.json", data)
    (run_dir / "summary.md").write_text(f"# Fusion run {run_id}\n\nTask: {args.task}\n", encoding="utf-8")
    print(run_dir)
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    path = Path(args.ledger)
    data = load(path)
    data.setdefault(args.section, []).append({"time": now(), "message": args.message})
    save(path, data)
    return 0


def cmd_source(args: argparse.Namespace) -> int:
    path = Path(args.ledger)
    data = load(path)
    data.setdefault("sourcesUsed", []).append({"time": now(), "url": args.url, "symbol": args.symbol, "lifecycle": args.lifecycle})
    save(path, data)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    init = sub.add_parser("init")
    init.add_argument("--task", required=True)
    init.set_defaults(func=cmd_init)
    add = sub.add_parser("add")
    add.add_argument("ledger")
    add.add_argument("section", choices=["actions", "verification", "blocked", "warnings"])
    add.add_argument("message")
    add.set_defaults(func=cmd_add)
    src = sub.add_parser("source")
    src.add_argument("ledger")
    src.add_argument("url")
    src.add_argument("--symbol", default="")
    src.add_argument("--lifecycle", default="unknown")
    src.set_defaults(func=cmd_source)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
