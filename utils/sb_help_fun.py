
import bpy


###--------------------------------------------
### Area Functions
###--------------------------------------------


def apply_prefix_suffix(name, prefix="", suffix=""):
    """
        Applay prefix/suffix by provided prompt user.
    """
    parts = name.split("_")

    if len(parts) > 2:
        current_prefix, base_name, current_suffix = parts[0], parts[1], parts[-1]

    elif len(parts) == 2:
        current_prefix, base_name = parts[0], parts[1]
        current_suffix = ""

    else:
        current_prefix, base_name, current_suffix = "", parts[0], ""

    new_prefix = prefix if prefix else current_prefix
    new_suffix = suffix if suffix else current_suffix

    new_name = f"{new_prefix}_{base_name}_{new_suffix}".strip("_")

    return new_name


def sync_object_and_data(obj):

    """
        Synchronize the object names with their mesh 
        data names
    """
    if obj.data:
        obj.data.name = obj.name


def sync_material_with_object(obj):
    """
        Synchronize the object names with their  
        materials
    """
    if obj.material_slots:
        for slot in obj.material_slots:
            if slot.material:
                slot.material.name = obj.name




