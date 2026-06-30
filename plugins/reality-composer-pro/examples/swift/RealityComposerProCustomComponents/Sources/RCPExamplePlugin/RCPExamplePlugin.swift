import RealityComposerProPlugin
import RCPExampleShared

@main
struct RCPExamplePlugin: RealityComposerProPlugin {
    var components: [any Component.Type] {
        [SpinComponent.self]
    }
}
