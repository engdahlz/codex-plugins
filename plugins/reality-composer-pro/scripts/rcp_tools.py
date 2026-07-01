#!/usr/bin/env python3
from __future__ import annotations

import json
import os
from pathlib import Path

ASSET_EXTS = {".usd", ".usda", ".usdc", ".usdz", ".reality", ".png", ".jpg", ".jpeg", ".heic", ".exr", ".hdr", ".mp3", ".wav", ".mp4", ".mov", ".obj", ".fbx", ".gltf", ".glb"}
SKIP_DIRS = {".git", ".build", "DerivedData", "node_modules", ".swiftpm", "__pycache__"}
SIDEBAR = {
    "Essentials": ["Linking an Xcode project", "Configuring the project workspace", "Navigating the Reality Composer Pro workspace", "Adding entities and assets to a scene", "Working with the Graph Editor", "Reusing assets with prototypes and instances"],
    "Materials": ["Building materials in Reality Composer Pro", "Applying materials to an asset", "Designing materials with Shader Graph"],
    "Particle Emitter": ["Creating particle systems in Reality Composer Pro"],
    "Script graph": ["Getting started with script graphs"],
    "Character Intelligence": ["Animation Graph", "Behavior Tree", "Navigation Mesh", "Character interactions"]
}
RELEASE_SOURCES = [
    ("Reality Composer Pro docs", "https://developer.apple.com/documentation/realitycomposerpro/"),
    ("Apple updates", "https://developer.apple.com/documentation/Updates"),
    ("Xcode release notes", "https://developer.apple.com/documentation/xcode-release-notes/"),
    ("visionOS release notes", "https://developer.apple.com/documentation/visionos-release-notes/"),
    ("iOS and iPadOS release notes", "https://developer.apple.com/documentation/ios-ipados-release-notes/"),
    ("macOS release notes", "https://developer.apple.com/documentation/macos-release-notes/"),
    ("RealityKit docs", "https://developer.apple.com/documentation/realitykit/")
]
MCP_CANDIDATES = ["kimsungwhee/apple-docs-mcp", "MightyDillah/apple-doc-mcp", "BingoWon/apple-rag-mcp", "Ahrentlov/appledeepdoc-mcp"]


def root() -> Path:
    env = os.environ.get("RCP_PLUGIN_ROOT")
    return Path(env).expanduser().resolve() if env and "PLUGIN_ROOT" not in env else Path(__file__).resolve().parents[1]


def load_docs():
    path = root() / "references" / "docs_index.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def search_docs(query: str = "Reality Composer Pro", limit: int = 8) -> str:
    terms = [t.lower() for t in (query or "").replace("/", " ").replace("-", " ").split()]
    scored = []
    for entry in load_docs():
        hay = json.dumps(entry, ensure_ascii=False).lower()
        score = sum(3 if t in str(entry.get("title", "")).lower() else 1 for t in terms if t in hay)
        if score:
            scored.append((score, entry))
    if not scored:
        scored = [(0, e) for e in load_docs()]
    scored.sort(key=lambda item: (-item[0], item[1].get("title", "")))
    out = [f"# RealityComposerPro reference search: {query}", ""]
    for _, entry in scored[: max(1, min(int(limit or 8), 20))]:
        out += [f"## {entry.get('title', 'Untitled')} (`{entry.get('id', 'unknown')}`)", f"URL: {entry.get('url', '')}", f"Why relevant: {entry.get('summary', '')}", ""]
    return "\n".join(out).rstrip()


def reference_get(ref_id: str) -> str:
    for entry in load_docs():
        if entry.get("id") == ref_id:
            return json.dumps(entry, indent=2, ensure_ascii=False)
    return f"Reference id not found: {ref_id}"


def sidebar_map() -> str:
    out = ["# Reality Composer Pro documentation sidebar map", ""]
    for section, pages in SIDEBAR.items():
        out += [f"## {section}", ""] + [f"- {page}" for page in pages] + [""]
    return "\n".join(out).rstrip()


def release_notes_plan(symptom: str = "") -> str:
    out = ["# Release notes check plan", "", f"Symptom: {symptom or 'not specified'}", "", "## Sources"]
    out += [f"- {name}: {url}" for name, url in RELEASE_SOURCES]
    out += ["", "## Extract", "- Platform and version", "- Component or tool area", "- Known issue wording", "- Workaround wording", "- Fixed version, if any", "- Impacted plugin skill", "- Last checked date"]
    return "\n".join(out)


def mcp_candidates() -> str:
    out = ["# Apple documentation MCP candidates", "", "Keep the bundled local helper as default. Review external servers before enabling them.", ""]
    out += [f"- {repo}" for repo in MCP_CANDIDATES]
    out += ["", "Review: install command, license, maintenance status, source freshness, output quality, Codex compatibility, and exact pinned version."]
    return "\n".join(out)


def mcp_candidate_report() -> str:
    return mcp_candidates()


def iter_files(path: Path):
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.endswith(".xcodeproj") and not d.endswith(".xcworkspace")]
        for name in filenames:
            yield Path(dirpath) / name


def inventory(path: str | None = None):
    base = Path(path or os.getcwd()).expanduser().resolve()
    info = {"root": str(base), "exists": base.exists(), "xcode_projects": [], "workspaces": [], "rkassets": [], "reality_composer_packages": [], "swift_files": 0, "assets": {}, "largest_assets": []}
    if not base.exists():
        return info
    largest = []
    for p in iter_files(base):
        rel = str(p.relative_to(base))
        if p.name.endswith(".xcodeproj"):
            info["xcode_projects"].append(rel)
        if p.name.endswith(".xcworkspace"):
            info["workspaces"].append(rel)
        if p.suffix == ".swift":
            info["swift_files"] += 1
        if p.suffix == ".rkassets":
            info["rkassets"].append(rel)
        if p.suffix == ".realitycomposerpro":
            info["reality_composer_packages"].append(rel)
        if p.suffix.lower() in ASSET_EXTS:
            size = p.stat().st_size
            bucket = info["assets"].setdefault(p.suffix.lower(), {"count": 0, "bytes": 0, "examples": []})
            bucket["count"] += 1; bucket["bytes"] += size
            if len(bucket["examples"]) < 5: bucket["examples"].append(rel)
            largest.append((size, rel))
    info["largest_assets"] = [{"path": rel, "bytes": size} for size, rel in sorted(largest, reverse=True)[:10]]
    return info


def project_doctor(path: str | None = None) -> str:
    data = inventory(path)
    out = ["# RealityComposerPro project doctor", "", f"Root: `{data['root']}`", f"Exists: `{data['exists']}`", ""]
    if not data["exists"]: return "\n".join(out + ["Path does not exist."])
    for title, key in [("Xcode projects", "xcode_projects"), ("Xcode workspaces", "workspaces"), ("RealityKit asset folders", "rkassets"), ("Reality Composer packages", "reality_composer_packages")]:
        out += [f"## {title}", ""] + ([f"- `{v}`" for v in data[key]] or ["- None detected"]) + [""]
    out += ["## Asset summary", ""]
    out += [f"- `{ext}`: {value['count']} file(s)" for ext, value in sorted(data["assets"].items())] or ["- No tracked asset extensions detected"]
    return "\n".join(out).rstrip()


def asset_audit(path: str | None = None) -> str:
    data = inventory(path)
    return json.dumps({"root": data["root"], "assets": data["assets"], "largest_assets": data["largest_assets"]}, indent=2, ensure_ascii=False)


def swift_scaffold(kind: str = "RealityView", type_name: str = "Example", module_name: str = "RealityContent") -> str:
    if "component" in (kind or "").lower():
        return f"import RealityKit\n\npublic struct {type_name}Component: Component, Codable {{\n    public var intensity: Float = 1\n}}\n"
    return f"import SwiftUI\nimport RealityKit\n\nstruct {type_name}RealityView: View {{\n    var body: some View {{\n        RealityView {{ content in\n            // Load Reality Composer Pro content here from {module_name}.\n        }}\n    }}\n}}\n"


def checklist(topic: str = "scene") -> str:
    items = ["Confirm target platform, RCP version, Xcode version, and device/simulator.", "Identify source-of-truth files before editing.", "Check relevant Apple release notes for known issues and workarounds.", "Create a branch or backup for large scene or asset changes.", "Validate in Xcode and Reality Composer Pro preview."]
    return "\n".join([f"# Checklist: {topic}", ""] + [f"- [ ] {item}" for item in items])


def generate_checklist(workflow: str = "scene", target: str = "Reality Composer Pro scene") -> str:
    return checklist(f"{workflow} for {target}")


def plan_task(task: str, target_platform: str = "visionOS", autonomy: str = "high") -> str:
    return "\n".join(["# RealityComposerPro implementation plan", "", f"Task: {task}", f"Target platform: {target_platform}", f"Autonomy: {autonomy}", "", "1. Inspect project and assets.", "2. Search official/bundled references.", "3. Check release notes for known issues and workarounds.", "4. Decide what is RCP-editor work versus Swift/RealityKit code.", "5. Implement small reversible changes.", "6. Validate and record manual editor steps."])


def gitignore_suggestions(root_path: str | None = None) -> str:
    return """# Suggested RealityComposerPro git hygiene
.DS_Store
*.xcuserstate
xcuserdata/
DerivedData/
.build/
.swiftpm/
# Generated runtime/export outputs. Keep only if they are source of truth.
*.reality
""".rstrip()
