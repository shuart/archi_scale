bl_info = {
    "name": "Set Architectural Scale",
    "author": "Stephane Huart",
    "version": (0, 2),
    "blender": (2, 76, 0),
    "location": "Properties > Scene ",
    "description": "Set a scale for the render",
    "warning": "",
    "wiki_url": "",
    "category": "Render",
    }


import bpy

scnType = bpy.types.Scene
print("Scale calculation has been updated")

MyTest=str(0)
#MyCurrentOrthoScale = str(bpy.data.cameras[0].ortho_scale)

#MyCurrentOrthoScale = str(bpy.context.scene.camera.data.ortho_scale)

class MyFloatOperator(bpy.types.Operator):
    
    bl_idname = "bpt.another_thing_do_to"
    
    #MyCurrentOrthoScale = str(bpy.context.scene.camera.data.ortho_scale)
    
    def execute(self, context):
        print("MyFloatOperator.showValue was called.", context.scene.my_float_prop)
        #self.MyCurrentOrthoScale = str(bpy.context.scene.camera.data.ortho_scale)
        baseScale = (bpy.context.scene.camera.data.ortho_scale) *100
        print(baseScale)
        paperDistance= baseScale/context.scene.my_float_prop
        print(paperDistance)
        targetRes= paperDistance/2.56 * context.scene.my_DPI_prop
        print(targetRes)
        context.scene.render.resolution_x = targetRes
        context.scene.render.resolution_y = targetRes
        #return {'FINISHED'}
        
class MyDPI(bpy.types.Operator):
    
    bl_idname = "bpt.DPI"
    
    def showValue(self, context):
        print("DPI.showValue was called.", context.scene.my_float_prop)
        
FloatProperty = bpy.props.FloatProperty
    
scnType.my_float_prop = FloatProperty(name = "Scale : 1/", default = .5, min = 1, max = 10000, description = "Float Prop Desc", update = MyFloatOperator.execute)

scnType.my_DPI_prop = FloatProperty(name = "DPI", default = 150, min = 1, max = 10000, description = "Float Prop Desc", update = MyDPI.showValue)

class ArchitectureScalePanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Set architectural Scale"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create two columns
        split = layout.split()

        # Scale and DPI
        col = split.column(align=True)
        col.label(text="User values:")
        col.prop(scene, "my_float_prop")
        col.prop(scene, "my_DPI_prop")

        # Blender Props
        col = split.column(align=True)
        col.label(text="Scene props:")
        col.prop(scene.camera.data, "ortho_scale")
        col.prop(scene.render, "resolution_x")
        col.prop(scene.render, "resolution_y")
        col.prop(scene.render, "resolution_percentage")

        # Render Button
      
        row = layout.row()
        row.scale_y = 1.0
        row.operator("render.render")


def register():
    bpy.utils.register_class(ArchitectureScalePanel)


def unregister():
    bpy.utils.unregister_class(ArchitectureScalePanel)


if __name__ == "__main__":
    register()
