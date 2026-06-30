// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "RealityComposerProCustomComponents",
    platforms: [.visionOS(.v2), .iOS(.v18), .macOS(.v15)],
    products: [
        .library(name: "RCPExampleShared", targets: ["RCPExampleShared"]),
        .library(name: "RCPExamplePlugin", targets: ["RCPExamplePlugin"])
    ],
    dependencies: [
        .package(url: "https://github.com/apple/reality-composer-pro-plugin", branch: "main")
    ],
    targets: [
        .target(name: "RCPExampleShared"),
        .target(name: "RCPExamplePlugin", dependencies: ["RCPExampleShared", .product(name: "RealityComposerProPlugin", package: "reality-composer-pro-plugin")])
    ]
)
