import maya.cmds as cmds
from tabs.util import Utils

Utils = reload(Utils)

WI01 = (2,273)
WI02 = (1,136,136)


class TabAdvance():
    # ing
    # FK, IK, Ribbon setup
    def frame_setup(self):
        self.frame("Rigging Setup")

        wi = (120,150)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="                        Name : ")
        setup_name = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        setup_check = cmds.checkBoxGrp(l="   Options :  ", ncb=3, cw4=(125,40,40,10), la3=["FK","IK","Ribbon"], v1=True, v2=True, h=25)
        cmds.setParent("..")

        wi = (120,150)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l=" Ribbon Joint Number:")
        ribbon_num = cmds.intField(w=wi[1], v=9, h=25)
        cmds.setParent("..")

        self.btn_layout(1)
        cmds.button(l="Create", c="fkIkRibbon()", w=WI01[1], h=30)
        self.end_space()

    # ing
    # Motion path
    def frame_motion_path(self):
        self.frame("Motion Path")

        wi = (100,170)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="                  Name : ")
        mp_name = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        wi = (100,170)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="  Locator Number : ")
        mp_loc_num = cmds.intField(w=wi[1], v=5, h=25)
        cmds.setParent("..")

        self.btn_layout(1)
        cmds.button(l="Create", c="motionPath()", w=WI01[1], h=30)
        self.end_space()

    # ing
    # Rivet
    def frame_rivet(self):
        self.frame("Rivet")

        cmds.rowLayout(nc=1)
        rivet_check = cmds.radioButtonGrp(l="Check : ", cw3=(50,90,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        self.btn_layout(1)
        cmds.button(l="Rivet", c="rivet()", w=WI01[1], h=30)
        self.end_space()

    # ing
    # Copy Weight