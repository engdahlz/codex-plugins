# Reality Composer Pro field guide

## Recommended workflow

1. Inspect the Xcode project, packages, `.realitycomposerpro`, `.rkassets`, USD, image, audio, and video assets.
2. Identify target platform: visionOS, iOS, or shared RealityKit package.
3. Use official Apple docs or WWDC references for SDK-sensitive code.
4. For UI-authored RCP work, produce exact editor steps and file-safe handoff notes.
5. For code-authored work, isolate changes in Swift packages or shared RealityKit modules.
6. Validate with Xcode build, asset audit, and device/simulator preview.

## Boundary

Do not claim Codex can directly drive the RCP app unless a real automation or MCP endpoint is present. The included MCP server is local helper tooling only.
