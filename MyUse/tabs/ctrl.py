import maya.cmds as cmds
import pymel.core as pm
from imp import reload
import tabs.util
import functions.controller as funcs_ctrl
import functions.constraint as funcs_const
import functions.text_ctrl as funcs_text
import functions.color as funcs_color

reload(tabs.util)
reload(funcs_ctrl)
reload(funcs_const)
reload(funcs_text)
reload(funcs_color)

from tabs.util import Utils
from functions.color import Color

WI01 = (2,273)
WI02 = (1,136,136)


class TabCtrl():
    def __init__(self):
        self.frame_ctrl()
        self.frame_text()
        self.frame_const()
        self.frame_color_picker()


    # Controller
    def frame_ctrl(self):
        Utils().frame("Controller")

        cmds.rowLayout(nc=1)
        self.make = cmds.radioButtonGrp(l=" Make : ", cw3=(60,100,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        wi = (60,100)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text("      Shape :", w=wi[0])
        self.shapes = cmds.optionMenu(w=wi[1], h=25)
        cmds.menuItem(l="  Circle")
        cmds.menuItem(l="  Square")
        cmds.menuItem(l="  Box")
        cmds.menuItem(l="  Ball")
        cmds.menuItem(l="  Diamond")
        cmds.menuItem(l="  Polygon")
        cmds.menuItem(l="  Cross 1")
        cmds.menuItem(l="  Cross 2")
        cmds.menuItem(l="  Eyes")
        cmds.menuItem(l="  Handle")
        cmds.menuItem(l="  Arrow 1")
        cmds.menuItem(l="  Arrow 2")
        cmds.menuItem(l="  Arrow 4")
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.ctrl_axes = cmds.radioButtonGrp(l="Axes : ", la3=["X","Y","Z"], nrb=3, cw4=(60,70,70,20), sl=1, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.ctrl_const = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Create Controller", 
            lambda x: funcs_ctrl.create_ctrl(self.make, self.shapes, self.ctrl_axes, self.ctrl_const), WI01[1])
        Utils().end_space()


    # Text
    def frame_text(self):
        Utils().frame("Text")
        wi=(45,230)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="  Text : ", w=wi[0])
        self.txt = cmds.textField(w=wi[1], h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Create", self.func_text, WI01[1])
        Utils().end_space()


    # Constraint
    def frame_const(self):
        Utils().frame("Constraint")

        Utils().btn_layout(2)
        self.quick = cmds.checkBoxGrp(l="Quick : ", ncb=1, cw2=(60,10), h=25)
        self.mo = cmds.checkBoxGrp(l="Maintain offset : ", ncb=1, v1=True, cw2=(90,10), h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.cons_axes = cmds.checkBoxGrp(l="Axes : ", ncb=3, cw4=(63,60,60,10), la3=["X","Y","Z"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.cons_const = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Constraint", 
            lambda x: funcs_const.const(self.cons_axes, self.cons_const, self.quick, self.mo), WI01[1])
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils().btn_layout(2)
        Utils().create_btn("Aim Constraint", "cmds.AimConstraintOptions()", WI02[1])
        Utils().create_btn("PoleVector Constraint",
            lambda x: cmds.poleVectorConstraint(w=1), WI02[1])
        Utils().end_space()


    # Color Picker
    def frame_color_picker(self):
        Utils().frame("Color Picker", 0)

        wi=(45,45,45,45,45,45)
        cmds.rowLayout(nc=6, cw6=wi)
        cmds.button(l="", w=wi[0], c=lambda x: funcs_color.color_picker(13), bgc=(1,0,0), h=30)
        cmds.button(l="", w=wi[1], c=lambda x: funcs_color.color_picker(17),bgc=(1,1,0), h=30)
        cmds.button(l="", w=wi[2], c=lambda x: funcs_color.color_picker(6), bgc=(0,0,1), h=30)
        cmds.button(l="", w=wi[3], c=lambda x: funcs_color.color_picker(18), bgc=(0,1,1), h=30)
        cmds.button(l="", w=wi[4], c=lambda x: funcs_color.color_picker(20), bgc=(1,0.75,0.75), h=30)
        Utils().create_btn("More", Color, wi[5])
        cmds.setParent("..")
        cmds.setParent("..")

    
    def func_text(self, _):
        text = pm.textField(self.txt, q=True, tx=True)
        funcs_text.text(text)
