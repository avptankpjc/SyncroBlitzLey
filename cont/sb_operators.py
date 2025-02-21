
import bpy
from ..utils.sb_help_fun import sync_object_and_data, sync_material_with_object, apply_prefix_suffix


#+++++++++++++++++++++++++++++++++++
# Area - Operators
#+++++++++++++++++++++++++++++++++++

#------------------------------------
# Oper_SyncNames
#------------------------------------
class SyncNamesOperator(bpy.types.Operator):

    bl_idname = "object.sync_names_om"
    bl_label = "Sync Object and Data Names"
    bl_description = "Sync the object's name with its mesh(and optionally material) names."
    bl_options = {"UNDO"}


    sync_materials: bpy.props.BoolProperty(
        name="Sync Materials",
        description="If enabled, also sync materials name with the object",
        default=False
    )#type: ignore

    def execute(self, context):
        for obj in context.selected_objects:
            
            #Save the original name, if not exists
            if "orig_name" not in obj:
                obj["orig_name"] = obj.name

            else:
                if obj.name != obj["orig_name"]:
                    obj["orig_name"] = obj.name
            
            #Syncro the name object with data
            sync_object_and_data(obj)

            if self.sync_materials:
                sync_material_with_object(obj)

                for slot in obj.material_slots:
                    if slot.material and "base_name" not in slot.material:
                        slot.material["base_name"] = slot.material.name
        return {"FINISHED"}
    
    def invoke(self, context, event):
        res = context.window_manager.invoke_props_dialog(self)
        return res
    

class SyncAddPrefixSuffixOperator(bpy.types.Operator):
    """
        Adde o replace an prefix/suffix in the 
        current object name 
    """
    bl_idname = "object.add_prefix_suffix"
    bl_label = "Add/Replace Prefix or Suffix"
    bl_description = "Add or replace a prefix/suffix for selected objects and/or materials"
    bl_options = {"UNDO"}

    text: bpy.props.StringProperty(
        name="Text Prefix/Suffix",
        description="Text to add as prefix or suffix",
        default=""
    )#type: ignore

    is_prefix: bpy.props.BoolProperty(
        name="Is Prefix",
        description="If enabled, add as prefix, otherwise as suffix",
        default=True
    )#type: ignore

    affect_materials: bpy.props.BoolProperty(
        name="Affect Materials",
        description="If enabled, apply the change only to the object's materials",
        default=False
    )#type: ignore

    enumerate: bpy.props.BoolProperty(
        name="Enumerate",
        description="Add a sequential number to the text",
        default=False
    )#type: ignore

    
    def invoke(self, context, event):
        res = context.window_manager.invoke_props_dialog(self)
        return res

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "text")
        layout.prop(self, "is_prefix")
        layout.prop(self, "affect_materials")
        layout.prop(self, "enumerate")

    def execute(self, context):
        counter = 1

        for obj in context.selected_objects:
            if not self.affect_materials:

                current_name = obj.name
                new_txt = self.text.strip().replace(" ", "_")

                if self.enumerate: 
                    new_txt += f"{counter:02d}"

                if self.is_prefix: 
                    obj.name = apply_prefix_suffix(current_name, prefix=new_txt)
                else:
                    obj.name = apply_prefix_suffix(current_name, suffix=new_txt)

                
            if self.affect_materials:
                if obj.material_slots:
                    local_count = 1
                    for slot in obj.material_slots:
                        if slot.material:
                            material_name = slot.material.name
                            new_txt = self.text.strip().replace(" ", "_")

                            if self.enumerate: 
                                new_txt += f"{local_count:02d}"

                            if self.is_prefix:
                                slot.material.name = apply_prefix_suffix(material_name, prefix=new_txt)
                            else:
                                slot.material.name = apply_prefix_suffix(material_name, suffix=new_txt) 

                            local_count += 1

            counter += 1    
        return {"FINISHED"}
    


