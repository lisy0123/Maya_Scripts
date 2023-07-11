import maya.cmds as cmds
from imp import reload
import tabs.util
import functions.match_freeze

reload(tabs.util)
reload(functions.match_freeze)

from tabs.util import Utils

WI01 = (2,273)
WI02 = (1,136,136)


class TabCreate():
    def __init__(self):
        self.frame_jnt_size()
        self.frame_create()
        self.frame_trs()


    # Joint Size
    def frame_jnt_size(self):
        Utils().frame("Joint Size", 0)
        self.jnt = cmds.floatSliderButtonGrp(l="Size   ", bl="Set", bc=self.func_joint_size, cw4=(50,50,70,50), f=True, min=0.1, max=1, v=0.5, h=30)
        cmds.setParent("..")


    # Create
    def frame_create(self):
        Utils().frame("Create")

        Utils().btn_layout(2)
        Utils().create_btn("Loc", "cmds.CreateLocator()", WI02[1], 25)
        Utils().create_btn("Curve", "cmds.EPCurveToolOptions()", WI02[2], 25)
        cmds.setParent("..")

        Utils().multiple_btns()

        wi = (50,111,111)
        cmds.rowLayout(nc=3, cw3=wi)
        cmds.text("", w=wi[0])
        Utils().create_btn("CpEd", "cmds.ComponentEditor()", wi[1], 25)
        create_options = cmds.optionMenu(w=wi[2], cc=Utils().apply_menu_item, h=25)
        for obj in Utils().name_list[0]:
            cmds.menuItem(l=obj)
        cmds.setParent("..")
        cmds.separator(h=1)

        cmds.rowLayout(nc=2, cw2=WI01)
        cmds.text("")
        Utils().create_btn("Node Editor", "cmds.NodeEditorWindow()", WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(2)
        Utils().create_btn("Set Driven Key", "cmds.SetDrivenKeyOptions()()", WI02[1])
        Utils().create_btn("Connection Editor", "cmds.ConnectionEditor()", WI02[2])
        cmds.setParent("..")

        Utils().btn_layout(2)
        create_options = cmds.optionMenu(w=WI02[1], cc=Utils().apply_menu_item, h=25)
        for obj in Utils().name_list[1]:
            cmds.menuItem(l=obj)
        create_options = cmds.optionMenu(w=WI02[2], cc=Utils().apply_menu_item, h=25)
        for obj in Utils().name_list[2]:
            cmds.menuItem(l=obj)
        Utils().end_space()
        
        
    # TRS
    def frame_trs(self):
        Utils().frame("TRS")

        cmds.rowLayout(nc=1)
        self.match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,58,52,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Match", self.func_match, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Freeze", self.func_freeze, WI01[1])
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils().btn_layout(2)
        Utils().create_btn("LBA", "cmds.ToggleLocalRotationAxes()", WI02[1])
        Utils().create_btn("Center Pivot", "cmds.CenterPivot()", WI02[2])
        cmds.setParent("..")

        Utils().btn_layout(2)
        Utils().create_btn("Rest Tfm", "cmds.ResetTransformations()", WI02[1])
        Utils().create_btn("Delete Hist", "cmds.DeleteHistory()", WI02[2])
        Utils().end_space()


    def func_joint_size(self):
        joints = cmds.floatSliderGrp(self.jnt, q=True, v=True)
        cmds.jointDisplayScale(joints)


    def func_match(self, _):
        functions.match_freeze.match(self.match_check)


    def func_freeze(self, _):
        functions.match_freeze.freeze(self.match_check)