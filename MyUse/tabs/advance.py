import maya.cmds as cmds
from imp import reload
import tabs.util

reload(tabs.util)

from tabs.util import Utils

WI01 = (2,273)
WI02 = (1,136,136)


class TabAdvance():
    def __init__(self):
        self.frame_setup()
        self.frame_motion_path()
        self.frame_rivet()


    # ing
    # FK, IK, Ribbon setup
    def frame_setup(self):
        Utils().frame("Rigging Setup")

        wi = (120,150)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="                        Name : ")
        self.setup_name = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.check_setup = cmds.checkBoxGrp(l="   Options :  ", ncb=3, cw4=(125,40,40,10), la3=["FK","IK","Ribbon"], v1=True, v2=True, h=25)
        cmds.setParent("..")

        wi = (120,150)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l=" Ribbon Joint Number:")
        self.ribbon_num = cmds.intField(w=wi[1], v=9, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Create", c="fkIkRibbon()", w=WI01[1], h=30)
        Utils().end_space()

    # ing
    # Motion path
    def frame_motion_path(self):
        Utils().frame("Motion Path")

        wi = (100,170)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="                  Name : ")
        self.mp_name = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        wi = (100,170)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="  Locator Number : ")
        self.mp_loc_num = cmds.intField(w=wi[1], v=5, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Create", c="motionPath()", w=WI01[1], h=30)
        Utils().end_space()

    # ing
    # Rivet
    def frame_rivet(self):
        Utils().frame("Rivet")

        cmds.rowLayout(nc=1)
        self.check_rivet = cmds.radioButtonGrp(l="Check : ", cw3=(50,90,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Rivet", c="rivet()", w=WI01[1], h=30)
        Utils().end_space()

    # ing
    # Copy Weight