import maya.cmds as cmds
from tabs.util import Utils

Utils = reload(Utils)

WI01 = (2,273)
WI02 = (1,136,136)


class TabCtrl():
    # Controller
    def frame_ctrl(self):
        Utils.frame("Controller")

        cmds.rowLayout(nc=1)
        ctrl_make = cmds.radioButtonGrp(l=" Make : ", cw3=(60,100,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        wi = (60,100)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text("      Shape :", w=wi[0])
        shapes = cmds.optionMenu(w=wi[1], h=25)
        cmds.menuItem(l="  Circle")
        cmds.menuItem(l="  Box")
        cmds.menuItem(l="  Ball")
        cmds.menuItem(l="  Diamond")
        cmds.menuItem(l="  Cross 1")
        cmds.menuItem(l="  Cross 2")
        cmds.menuItem(l="  Eyes")
        cmds.menuItem(l="  Handle")
        cmds.menuItem(l="  Arrow 1")
        cmds.menuItem(l="  Arrow 2")
        cmds.menuItem(l="  Arrow 4")
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        axes = cmds.radioButtonGrp(l="Axes : ", la3=["X","Y","Z"], nrb=3, cw4=(60,70,70,20), sl=1, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils.btn_layout(1)
        cmds.button(l="Create Controller", c="createController()", w=WI01[1], h=30)
        cmds.setParent("..")
        cmds.separator(h=1)


    # Text
    def frame_text(self):
        wi=(45,230)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="  Text : ", w=wi[0])
        tx = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        Utils.btn_layout(1)
        cmds.button(l="Create", c="text()", w=WI01[1], h=25)
        Utils.end_space()


    # Constraint
    def frame_const(self):
        Utils.frame("Constraint")

        Utils.btn_layout(2)
        mo_quick_check = cmds.checkBoxGrp(l="Quick: ", ncb=1, cw2=(55,10), h=25)
        mo_check = cmds.checkBoxGrp(l="Maintain offset : ", ncb=1, v1=True, cw2=(90,10), h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        axes_check = cmds.checkBoxGrp(l=" Axes: ", ncb=3, cw4=(60,60,60,10), la3=["X","Y","Z"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        mo_const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils.btn_layout(1)
        cmds.button(l="Constraint", c="const()", w=WI01[1], h=30)
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils.btn_layout(2)
        cmds.button(l="Aim Constraint", c="cmds.AimConstraintOptions()", w=WI02[1], h=30)
        cmds.button(l="PoleVector Constraint", c="cmds.poleVectorConstraint(w=1)", w=WI02[1], h=30)
        Utils.end_space()


    # Color Picker
    def frame_color_picker(self):
        Utils.frame("Color Picker", 0)

        wi=(45,45,45,45,45,45)
        cmds.rowLayout(nc=6, cw6=wi)
        cmds.button(l="", w=wi[0], c="colorPicker(13)", bgc=(1,0,0), h=30)
        cmds.button(l="", w=wi[1], c="colorPicker(17)",bgc=(1,1,0), h=30)
        cmds.button(l="", w=wi[2], c="colorPicker(6)", bgc=(0,0,1), h=30)
        cmds.button(l="", w=wi[3], c="colorPicker(18)", bgc=(0,1,1), h=30)
        cmds.button(l="", w=wi[4], c="colorPicker(20)", bgc=(1,0.75,0.75), h=30)
        cmds.button(l="More", w=wi[5], c="color()", h=30)
        cmds.setParent("..")
        cmds.setParent("..")