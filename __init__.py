#    <SyncroBlitzLey, Blender addon for syncing object and mesh names.>
#    Copyright (C) <2025> <AvpTankPowerJC>
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.


    
bl_info = {
    "name":"SyncroBlitzLey",
    "author":"AvpTankPowerJc",
    "version":(1,0,0),
    "blender":(2,80,0),
    "location": "View3D > Sidebar (key N)",
    "description":"Sync Objetc's Name to Data Mesh",
    "category":"Object",
    "wiki_url":"https://github.com/avptankpjc/SyncroBlitzLey",
}



import bpy

from .cont.sb_operators import SyncNamesOperator, SyncAddPrefixSuffixOperator
from .view.sb_panel import SyncToolPanel


s_classes = [
    SyncNamesOperator,
    SyncAddPrefixSuffixOperator,
    SyncToolPanel
]

def register():
    for cls in s_classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(s_classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

