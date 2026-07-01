import SwiftUI
import RealityKit

struct RealityKitContentLoaderView: View {
    var body: some View {
        RealityView { content in
            do {
                let root = try await Entity(named: "Scene", in: realityKitContentBundle)
                content.add(root)
            } catch {
                print("Failed to load RealityKit content: \(error)")
            }
        }
    }
}
