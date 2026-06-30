#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "references" / "docs_index.json"
ASSET_EXTS = {".realitycomposerpro", ".rkassets", ".reality", ".usdz", ".usd", ".usda", ".usdc", ".png", ".jpg", ".jpeg", ".heic", ".exr", ".hdr", ".wav", ".aiff", ".mp3", ".mov", ".mp4"}

def load_docs() -> list[dict[str, Any]]:
    return json.loads(DOCS.read_text(encoding="utf-8")) if DOCS.exists() else []

def doc_search(query: str, limit: int = 8) -> list[dict[str, Any]]:
    q = query.lower().strip()
    docs = load_docs()
    if not q:
        return docs[:limit]
    scored = []
    for doc in docs:
        hay = " ".join(str(doc.get(k, "")) for k in ("id", "title", "summary", "kind")) + " " + " ".join(doc.get("tags", []))
        score = sum(1 for token in q.split() if token in hay.lower())
        if score:
            scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:limit]]

def reference_get(ref_id: str):
    return next((d for d in load_docs() if d.get("id") == ref_id), None)

def project_doctor(path: str):
    root = Path(path).expanduser().resolve()
    if not root.exists():
        return {"root": str(root), "ok": False, "findings": ["Path does not exist."], "signals": {}}
    files = [p for p in root.rglob("*") if p.is_file()]
    signals = {
        "xcode_projects": [str(p.relative_to(root)) for p in files if p.name.endswith(".xcodeproj")],
        "workspaces": [str(p.relative_to(root)) for p in files if p.name.endswith(".xcworkspace")],
        "swift_files": sum(1 for p in files if p.suffix == ".swift"),
        "reality_composer_packages": [str(p.relative_to(root)) for p in files if p.suffix == ".realitycomposerpro"],
        "rkassets": [str(p.relative_to(root)) for p in files if p.suffix == ".rkassets"],
        "usd_assets": sum(1 for p in files if p.suffix.lower() in {".usd", ".usda", ".usdc", ".usdz"})
    }
    findings = []
    if not signals["xcode_projects"] and not signals["workspaces"]:
        findings.append("No Xcode project or workspace detected.")
    if not signals["reality_composer_packages"] and not signals["rkassets"]:
        findings.append("No .realitycomposerpro or .rkassets package detected.")
    if not findings:
        findings.append("Project has expected Reality Composer Pro / RealityKit signals.")
    return {"root": str(root), "ok": True, "signals": signals, "findings": findings}

def asset_audit(path: str):
    root = Path(path).expanduser().resolve()
    counts = {}
    examples = {}
    if not root.exists():
        return {"root": str(root), "asset_counts": counts, "examples": examples}
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in ASSET_EXTS:
            ext = p.suffix.lower()
            counts[ext] = counts.get(ext, 0) + 1
            examples.setdefault(ext, [])
            if len(examples[ext]) < 5:
                examples[ext].append(str(p.relative_to(root)))
    return {"root": str(root), "asset_counts": counts, "examples": examples}

def swift_scaffold(kind: str) -> str:
    if "component" in kind.lower():
        return "import RealityKit\n\npublic struct ExampleComponent: Component, Codable { public var speed: Float = 1 }\n"
    return "import SwiftUI\nimport RealityKit\n\nstruct ContentView: View { var body: some View { RealityView { content in } } }\n"

def checklist(topic: str):
    return ["Inspect project structure and current assets.", "Check Apple docs or WWDC references for SDK-sensitive APIs.", "Make a branch or backup before large edits.", "Prefer small reversible edits.", "Validate in Xcode and Reality Composer Pro preview or device."]
