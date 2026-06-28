# Blender Python patterns

Use these patterns when Codex needs to generate or execute `bpy` code.

## General script shape

```python
import bpy
from mathutils import Vector

PLUGIN_TAG = "blender_pro"


def ensure_collection(name: str) -> bpy.types.Collection:
    collection = bpy.data.collections.get(name)
    if collection is None:
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
    return collection


def link_to_collection(obj: bpy.types.Object, collection_name: str) -> None:
    collection = ensure_collection(collection_name)
    for existing in obj.users_collection:
        existing.objects.unlink(obj)
    collection.objects.link(obj)


def create_material(name: str, color=(1, 1, 1, 1), roughness=0.5, metallic=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
    return mat
```

## Create object safely

```python
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
obj = bpy.context.object
obj.name = "geo_demo_cube"
obj["created_by"] = PLUGIN_TAG
link_to_collection(obj, "GEO_demo")
```

## Add bevel and weighted normals

```python
bevel = obj.modifiers.new("soft_edge_bevel", "BEVEL")
bevel.width = 0.05
bevel.segments = 3

weighted_normals = obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
weighted_normals.keep_sharp = True
```

## Create camera looking at target

```python
import mathutils

camera_data = bpy.data.cameras.new("camera_final_data")
camera = bpy.data.objects.new("camera_final", camera_data)
bpy.context.scene.collection.objects.link(camera)
camera.location = (5, -7, 4)

target = Vector((0, 0, 1))
direction = target - Vector(camera.location)
camera.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
camera.data.lens = 45
bpy.context.scene.camera = camera
```

## Add studio lights

```python
def add_area_light(name, location, power, size):
    data = bpy.data.lights.new(name + "_data", type="AREA")
    data.energy = power
    data.size = size
    obj = bpy.data.objects.new(name, data)
    bpy.context.scene.collection.objects.link(obj)
    obj.location = location
    return obj

key = add_area_light("light_key_softbox", (4, -5, 5), 650, 4)
fill = add_area_light("light_fill_soft", (-4, -3, 3), 120, 5)
rim = add_area_light("light_rim_edge", (0, 5, 4), 300, 3)
```

## Render settings

```python
scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.samples = 128
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.view_settings.view_transform = "Filmic"
scene.view_settings.look = "Medium High Contrast"
```

## Code review before execution

Before executing generated Python, check:

- Does it operate only on the intended objects/collections?
- Does it avoid unrelated file-system/network access?
- Does it avoid hidden persistence?
- Does it name new data-blocks clearly?
- Does it avoid destructive deletes unless explicitly requested?
- Does it verify or print enough result information?
