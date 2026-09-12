import bpy

def purge_button(self, context):
    self.layout.operator("outliner.orphans_purge", text="Purge Unsused Data", icon="ORPHAN_DATA")


def register():
    bpy.types.VIEW3D_HT_tool_header.prepend(purge_button)


def unregister():
    bpy.types.VIEW3D_HT_tool_header.remove(purge_button)


if __name__ == "__main__":
    register()