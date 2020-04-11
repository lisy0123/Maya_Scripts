import maya.cmds as cmds

win="WingAutoRigging"
if cmds.window(win, ex=True):
    cmds.deleteUI(win)

cmds.window(win, t="Wing Auto Rigging")
cmds.rowColumnLayout(w=280)

cmds.separator(h=5, w=280)
wi=(80,130,60)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text(l="Base Joint", w=wi[0])
basejnt=cmds.intField(w=wi[1], min=2, max=10, v=4)
cmds.button(l="Create", c="BaseJoint()", w=wi[2])
cmds.setParent("..")

cmds.separator(h=5, w=280)
wi=(80,130,60)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text(l="Sub Joint", w=wi[0])
subjnt=cmds.intField(w=wi[1], min=1, max=30, v=3)
cmds.button(l="Create",c="SubJoint()", w=wi[2])
cmds.setParent("..")

cmds.separator(h=3, w=280)
cmds.separator(h=3, w=280)
cmds.button(l="Mirror Joints", c="MirrorJoints()", h=40)
cmds.button(l="Orient Joints", c="OrientJoints()", h=40)
cmds.button(l="Create Controller", h=40)

cmds.separator(h=5, w=280)
jnt=cmds.floatSliderButtonGrp(l="Joint Size  ", bl="Set", bc="JointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)
cmds.separator(h=5, w=280)

cmds.showWindow(win)

#-------------------------------------- Active Code ------------------------------------#

def BaseJoint():
    if cmds.objExists("L_Wing_1"):
        cmds.warning("L_Wing_1 is already exists")
    else:
        cmds.circle(n="Wing_World", nr=(0,1,0))
        cmds.joint(n="Wing_Root", p=(0,0,0))
        for x in range(1, cmds.intField(basejnt, q=True, v=True)+1):
            cmds.joint(n="L_Wing_"+str(x), p=(5*x,0,0))



def SubJoint():
    print cmds.intField(subjnt, q=True, v=True)

#--------------------------------------------------------------------------------------------#

def MirrorJoints():
    if cmds.objExists("R_Wing_1"):
        cmds.warning("R_Wing_1 is already exists")
    else:
        cmds.mirrorJoint("L_Wing_1",mb=True, myz=True, sr=("L_","R_"))

def OrientJoints():
    cmds.makeIdentity("L_Wing_1", a=True, r=True)
    cmds.makeIdentity("R_Wing_1", a=True, r=True)

def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)
