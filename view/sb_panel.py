import bpy

class SyncToolPanel(bpy.types.Panel):

    """Creates the Side Panel in the 3D Viewport"""
    bl_label        = "SyncroBlitzLey"
    bl_idname       = "VIEW3D_PT_sync_names_om"
    bl_space_type   = "VIEW_3D"
    bl_region_type  = "UI"
    bl_category     = "SyncroBlitzLey"

    def draw(self, context):
        """Draw Layout Panel"""
        layout = self.layout
        layout.label(text="Sync Names:")
        layout.operator("object.sync_names_om", text="Sync Selected Objects")
        
        layout.separator()

        layout.label(text="Add Prefix/Suffix:")
        layout.operator("object.add_prefix_suffix", text="Add/Replace Prefix-Suffix")


