#!/usr/bin/env python3
"""Fetch or refresh Autodesk's official Fusion API Reference repository."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

REPO = "https://github.com/AutodeskFusion360/FusionAPIReference.git"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", default=".fusion-api-reference")
    args = parser.parse_args()
    target = Path(args.target)
    if target.exists():
        run(["git", "-C", str(target), "pull", "--ff-only"])
    else:
        run(["git", "clone", "--depth", "1", REPO, str(target)])
    print(f"Fusion API reference ready: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
