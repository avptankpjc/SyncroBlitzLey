
import bpy


class SyncNamesOperator(bpy.types.Operator):

    bl_idname = "object.sync_names_om"
    bl_label = "Sync Object and Data Names"
    bl_options = {"REGISTER", "UNDO"}


    def execute(self, context):
        self.syncObjectToDataNames(context.selected_objects)
        return {"FINISHED"}
    
    
    def syncObjectToDataNames(self,objects):
        """Synchronize the object names with their mesh data names"""
        for obj in objects:
            if obj.data:
                obj.data.name = obj.name
