import RealityKit

public struct SpinComponent: Component, Codable {
    public var radiansPerSecond: Float

    public init(radiansPerSecond: Float = 1.0) {
        self.radiansPerSecond = radiansPerSecond
    }
}
