# codex-plugins

Personal GitHub marketplace for custom Codex plugins.

Add this repository URL to Codex, then install plugins from `.agents/plugins/marketplace.json`.

## Available plugins

### Blender Pro

A professional Blender workflow plugin for Codex with Blender MCP setup, scene inspection, modeling, materials, lighting, render workflow, animation, geometry nodes, asset pipelines, Python/bpy workflows, and review skills.

### Fusion Developer

An Autodesk Fusion workflow plugin for Fusion API, Product Help MCP, Fusion Desktop MCP, APS/Fusion Data workflows, Insider compatibility, CAD automation, evidence capture, and local bridge fallback workflows.

### Reality Composer Pro Expert

An Apple Reality Composer Pro and RealityKit workflow plugin for Codex. It includes skills, references, Swift examples, and a local MCP server for Reality Composer Pro 3, visionOS/iOS spatial content, `.realitycomposerpro`, `.rkassets`, USD/USDZ asset hygiene, Xcode integration, RealityView loading, components, systems, actions, Shader Graph, Script Graph, Compute Graph, Animation Graph, Sequencer, Behavior Trees, Navigation Mesh, and custom editor plugins.

## Install in Codex

```bash
codex plugin marketplace add engdahlz/codex-plugins --ref main
codex plugin marketplace list
```

Then open `/plugins` and install the plugin you want.
