import maya.cmds as cmds

win="HumanAutoRigging"
if cmds.window(win, ex=True):
    cmds.deleteUI(win)

cmds.window(win, t="Human Auto Rigging")
cmds.rowColumnLayout(w=300)

#Arm & Leg Setting UI
cmds.frameLayout(l="Arm & Leg Setting", cll=True)
leg = cmds.intSliderGrp(l="Leg      ", min=1, max=5, v=1, f=True, cw3=(70,50,50))
arm = cmds.intSliderGrp(l="Arm      ", min=1, max=5, v=1, f=True, cw3=(70,50,50))
basefinger = cmds.intSliderGrp(l="Base Finger ", min=1, max=10, v=5, f=True, cw3=(70,50,50))
subfiner = cmds.intSliderGrp(l="Sub Finger  ", min=1, max=10, v=5, f=True, cw3=(70,50,50))
cmds.setParent("..")
cmds.setParent("..")

#Spine Setting UI
cmds.frameLayout(l="Spine Setting", cll=True)
spine = cmds.intSliderGrp(l="Spine     ", min=3, max=10, v=7, f=True, cw3=(70,50,50))
cmds.setParent("..")
cmds.rowLayout(nc=1)
cmds.setParent("..")
cmds.button(l="Create Basic Joint", h=30, c="CreateBaseJoint()")
cmds.separator(h=3)
cmds.separator(h=3)
colorsetting = cmds.radioButtonGrp(l="Ctrl Color     ", cw3=(80,100,10), la2=["Same (L=R)","Separate (L/R)"], nrb=2, sl=1, w=298)
cmds.button(l="Setting", h=30, c="Setting()")

#jnt size
cmds.separator(h=3)
cmds.separator(h=3)
jnt=cmds.floatSliderButtonGrp(l="Joint Size ", bl="Set", bc="JointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)

cmds.showWindow(win)

#-------------------------------------- Active Code ------------------------------------#

#Create basic Jnt
def CreateBaseJoint():
    if cmds.objExists("Root"):
        cmds.warning("Basic Joints are already exists")
    else:
        root=cmds.joint(n="Root", p=(0,10,0))
        cmds.joint(n="L_Hip", p=(0,9,-1))
        cmds.joint(n="L_Knee",p=(0,0,0))
        cmds.joint(n="L_Ankle",p=(0,0,0))
        cmds.joint(n="L_Heel",p=(1,0,0))
        cmds.joint(n="L_Toes",p=(0,0,0))
        cmds.joint(n="L_FootSideInner")
        cmds.joint(n="L_FootSideOuter")
        cmds.joint(n="L_ToesEnd")
        a=cmds.circle(nr=(0,1,0), n="world_ctrl")
        cmds.parent("Root",a)

#Mirror Jnt -> Orient Jnt -> Create Ctrl
def Setting():
    MirrorJoints()
    OrientJoints()
    cmds.warning("Fixing")

def Arm():
    cmds.warning("Arm")

def Leg():
    cmds.warning("Leg")

#---------------------------------------------------------------------------------------#

def MirrorJoints():
    if cmds.objExists("R_*"):
        cmds.warning("R is already exists")
    else:
        cmds.mirrorJoint("L_*",mirrorBehavior=True, myz=True, sr=("L_","R_"))


def OrientJoints():
    cmds.makeIdentity("Root", a=True, r=True)


def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)








