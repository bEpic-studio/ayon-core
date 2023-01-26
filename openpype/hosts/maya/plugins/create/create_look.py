from openpype.hosts.maya.api import (
    plugin,
    lib
)
from openpype.lib import (
    BoolDef,
    TextDef
)


class CreateLook(plugin.MayaCreator):
    """Shader connections defining shape look"""

    identifier = "io.openpype.creators.maya.look"
    label = "Look"
    family = "look"
    icon = "paint-brush"

    make_tx = True

    def get_instance_attr_defs(self):

        return [
            # TODO: This value should actually get set on create!
            TextDef("renderLayer",
                    # TODO: Bug: Hidden attribute's label is still shown in UI?
                    hidden=True,
                    default=lib.get_current_renderlayer(),
                    label="Renderlayer",
                    tooltip="Renderlayer to extract the look from"),
            BoolDef("maketx",
                    label="MakeTX",
                    tooltip="Whether to generate .tx files for your textures",
                    default=self.make_tx),
            BoolDef("forceCopy",
                    label="Force Copy",
                    tooltip="Enable users to force a copy instead of hardlink."
                            "\nNote: On Windows copy is always forced due to "
                            "bugs in windows' implementation of hardlinks.",
                    default=False)
        ]

    def get_pre_create_attr_defs(self):
        # Show same attributes on create but include use selection
        defs = super(CreateLook, self).get_pre_create_attr_defs()
        defs.extend(self.get_instance_attr_defs())
        return defs
