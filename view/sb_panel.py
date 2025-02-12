import bpy

class SyncNamesPanel(bpy.types.Panel):

    """Creates the Side Panel in the 3D Viewport"""
    bl_label        = "Syncro Obj2Dat Names "
    bl_idname       = "VIEW3D_PT_sync_names_om"
    bl_space_type   = "VIEW_3D"
    bl_region_type  = "UI"
    bl_category     = "SyncBzLey"

    def draw(self, context):
        """Draw Layout Panel"""
        layout = self.layout
        row = layout.row()
        row.operator("object.sync_names_om", text="Sync Selected Objects")


