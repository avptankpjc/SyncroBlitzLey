

    
bl_info = {
    "name":"SyncroBlitzLey",
    "author":"AvpTankPowerJc",
    "version":(1,0,0),
    "blender":(2,80,0),
    "location": "View3D > Sidebar (key N)",
    "description":"Sync Objetc's Name to Data Mesh",
    "category":"Object",
}



import bpy

from .cont.sb_operators import SyncNamesOperator
from .view.sb_panel import SyncNamesPanel


s_classes = [
    SyncNamesOperator,
    SyncNamesPanel
]

def register():
    for cls in s_classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in s_classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

