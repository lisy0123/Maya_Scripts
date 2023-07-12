import maya.cmds as cmds
import pymel.core as pm


if cmds.window(TOOLNAME, ex=True):
    cmds.deleteUI(TOOLNAME)


WINDOW = cmds.window(TOOLNAME, t=TOOLTITLE)
cmds.rowColumnLayout(w=285)


# UI1: Setting
frame("Setting")

wi = (10,56,60,80,60)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("")
arm_check = cmds.checkBox(l=" Arm : ", w=wi[1], v=True, h=25)
arm = cmds.intField(w=wi[2], v=1, h=25)
cmds.text(l="    Base Finger :  ", w=wi[3])
basefinger = cmds.intField(w=wi[4], v=5, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=5, cw5=wi)
cmds.text("")
leg_check = cmds.checkBox(l=" Leg : ", w=wi[1], v=True, h=25)
leg = cmds.intField(w=wi[2], v=1, h=25)
cmds.text(l="    Sub Finger : ", w=wi[3])
subfinger = cmds.intField(w=wi[4], v=3, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Create Basic Joints", c="JntCreate()", w=WI01[1], h=30)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Mirror / Orient Joints", c="JntMirror()", w=WI01[1], h=30)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Setting", c="Setting()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

cmds.showWindow(TOOLNAME)