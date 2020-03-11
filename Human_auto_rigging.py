import maya.cmds as cmds

win="HumanAutoRigging"
if cmds.window(win, ex=True):
    cmds.deleteUI(win)

cmds.window(win, t="Human Auto Rigging")
cmds.rowColumnLayout(w=300)

# Arm & Leg Setting UI
cmds.frameLayout(l="Arm & Leg & Spine Setting", cll=True)
leg = cmds.intSliderGrp(l="Leg      ", min=1, max=3, v=1, f=True, cw3=(70,50,50))
arm = cmds.intSliderGrp(l="Arm      ", min=1, max=3, v=1, f=True, cw3=(70,50,50))
basefinger = cmds.intSliderGrp(l="Base Finger ", min=1, max=10, v=5, f=True, cw3=(70,50,50))
subfiner = cmds.intSliderGrp(l="Sub Finger  ", min=1, max=10, v=5, f=True, cw3=(70,50,50))
spine = cmds.intSliderGrp(l="Spine     ", min=3, max=10, v=7, f=True, cw3=(70,50,50))
wi=(3,65,1,218)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="", w=wi[0])
cmds.button(l="Delete", h=30, w=wi[1], c="DeleteJoint()")
cmds.text(l="", w=wi[2])
cmds.button(l="Create Basic Joint", h=30, w=wi[3], c="CreateBaseJoint()")
cmds.setParent("..")
cmds.setParent("..")
cmds.rowLayout(nc=1)
cmds.setParent("..")
cmds.separator(h=3)
cmds.separator(h=3)

# Setting UI
cmds.frameLayout(l="Setting", cll=True)
cmds.rowLayout(nc=1)
colorsetting = cmds.radioButtonGrp(l="  Ctrl Color :  ", cw3=(80,100,5), la2=["Same (L=R)","Separate (L/R)"], nrb=2, sl=1, w=298)
cmds.setParent("..")
cmds.button(l="Setting", h=30, c="Setting()")
cmds.button(l="Select Bind Skin Joints", h=30, c="SelectJoints()")
wi=(1,144,144)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text(l="", w=wi[0])
cmds.button(l="Open Bind SKin Options", h=30, w=wi[1], c="OpenOptions()")
cmds.button(l="Bind Skin (Default)", h=30, w=wi[2], c="BindSkin()")
cmds.setParent("..")
cmds.setParent("..")
cmds.rowLayout(nc=1)
cmds.setParent("..")
cmds.separator(h=3)
cmds.separator(h=3)

# Ctrl setting UI
cmds.frameLayout(l="Control", cll=True)
cmds.rowLayout(nc=1)
cmds.setParent("..")
cmds.button(l="Default Pose", h=30, c="DefaultPose()")
keysave=cmds.checkBoxGrp(l="Key Save Options : ", ncb=1, cw2=(110,50), l1="Hierachy", v1=True)
cmds.button(l="Key Save", h=30, c="KeySave()")
keymirror = cmds.radioButtonGrp(l="    Key Mirror : ", cw3=(110,80,5), la2=["L->R","R->L"], nrb=2, sl=1, w=295)
cmds.button(l="Key Mirror", h=30, c="KeyMirror()")
cmds.setParent("..")
cmds.rowLayout(nc=1)
cmds.setParent("..")
cmds.separator(h=3)
cmds.separator(h=3)

# Jnt size
jnt=cmds.floatSliderButtonGrp(l="Joint Size ", bl="Set", bc="JointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)

cmds.showWindow(win)

#-------------------------------------- Active Code ------------------------------------#

# Delete All Jnt
def DeleteJoint():
    if cmds.objExists("world_ctrl"):
        cmds.delete("world_ctrl")
    else:
        cmds.warning("Already delete it!")

# Create Basic Jnt
def CreateBaseJoint():
    if cmds.objExists("Root"):
        cmds.warning("Basic Joints are already exists")
    else:
        root=cmds.joint(n="Root", p=(0,9.82,-0.17))
        JntLeg()
        cmds.select("Root")
        cmds.joint(n="Spine1", p=(0,11.5,-0.4))
        cmds.joint(n="Chest", p=(0,13,-0.55))
        cmds.joint(n="Neck", p=(0,14.1,-0.38))
        cmds.joint(n="Head", p=(0,15.7,-0.1))
        cmds.joint(n="HeadEnd", p=(0,17.1,-0.1))
        
        cmds.select("Head")
        cmds.joint(n="Jaw", p=(0,15.4,0.3))
        cmds.joint(n="JawEnd", p=(0,14.9,1.25))
        cmds.select("Head")
        cmds.joint(n="L_Eye", p=(0.34,15.9,0.9))
        cmds.joint(n="L_EyeEnd", p=(0.34,15.9,1.5))
        JntArm()
        cmds.select("Chest")
        cmds.joint(n="L_Scapula", p=(0.4,13.7,-0.15))
        cmds.joint(n="L_Shoulder", p=(1.5,13.7,-0.15))
        cmds.joint(n="L_Elbow", p=(4,13.7,-0.3))
        cmds.joint(n="L_Wrist", p=(6.4,13.7,-0.15))
        
        a=cmds.circle(nr=(0,1,0), n="world_ctrl")
        cmds.scale(3,3,3, a)
        cmds.makeIdentity(a=True, t=True, r=True, s=True, n=0)
        cmds.DeleteHistory(a)
        cmds.parent("Root","world_ctrl")

# Leg Jnt
def JntLeg():
    cmds.warning("JntLeg")
    i = cmds.intSliderGrp(leg, q=True, v=True)
    cmds.warning(i)
    if i==1:
        JntLeg_sub(0,0,i)
    elif i==2:
        JntLeg_sub(0.3,0.5,i-1)
        JntLeg_sub(0.3,-0.5,i)
    else:
        JntLeg_sub(0,0,i-2)
        JntLeg_sub(0.4,-0.4,i-1)
        JntLeg_sub(0.4,0.4,i)

def JntLeg_sub(x, y, i):
    cmds.select("Root")
    cmds.joint(n="L_Hip_"+str(i), p=(0.8-x,9.6,-0.2-y))
    cmds.joint(n="L_Knee_"+str(i),p=(0.98-x,4.7,0.2-y))
    cmds.joint(n="L_Ankle_"+str(i),p=(1.08-x,0.85,-0.05-y))
    cmds.joint(n="L_Heel_"+str(i),p=(1.08-x,0,-0.7-y))
    cmds.select("L_Ankle_"+str(i))
    cmds.joint(n="L_Toes_"+str(i),p=(1.08-x,0.2,1.3-y))
    cmds.joint(n="L_FootSideInner_"+str(i), p=(0.58-x,0,1.3-y))
    cmds.select("L_Toes_"+str(i))
    cmds.joint(n="L_FootSideOuter_"+str(i), p=(1.58-x,0,1.3-y))
    cmds.select("L_Toes_"+str(i))
    cmds.joint(n="L_ToesEnd_"+str(i), p=(1.08-x,0,2-y))

# Arm Jnt
def JntArm():
    cmds.warning("JntArm")

def JntArm_Sub():
    cmds.warning("JntArm_Sub")

# Finger Jnt
def Finger():
    cmds.warning("Finger")

# Spine Jnt
def JntSpine():
    cmds.warning("JntSpine")

#---------------------------------------------------------------------------------------#

# Setting
def Setting():
    # Jnt Setting
    JntMirror()
    JntOrient()
    JntFKCreate()
    JntIKCreate()
    JntSquashStretch()
    JntScale()
    JntSmoothMove()
    # Ctrl Setting
    CtrlSetting()
    cmds.warning("Fixing")

#---------------------------------------------------------------------------------------#

# Mirror Hip(leg), Scapula(Arm), Eye
def JntMirror():
    if cmds.objExists("R_Hip"):
        cmds.warning("R_Leg is already exists")
    else:
        cmds.mirrorJoint("L_Hip",mirrorBehavior=True, myz=True, sr=("L_","R_"))
    
    if cmds.objExists("R_Scapula"):
        cmds.warning("R_Arm is already exists")
    else:
        cmds.mirrorJoint("L_Scapula",mirrorBehavior=True, myz=True, sr=("L_","R_"))
    
    if cmds.objExists("R_Eye"):
        cmds.warning("R_Eye is already exists")
    else:
        cmds.mirrorJoint("L_Eye",mirrorBehavior=True, myz=True, sr=("L_","R_"))

# need to fix
# Orient Jnt
def JntOrient():
    cmds.makeIdentity("Root", a=True, t=True, r=True, s=True, n=0)

#---------------------------------------------------------------------------------------#

# Create FK Jnt
def JntFKCreate():
    cmds.warning("FKCreating")

# Create IK Jnt
def JntIKCreate():
    cmds.warning("IKCreting")

# Create Squash and Stretch Jnt
def JntSquashStretch():
    cmds.warning("SquashStretch")

# Make Jnt Scale
def JntScale():
    cmds.warning("Scaling")

# Make Jnt move smooth (During Squash and Stretch)
def JntSmoothMove():
    cmds.warning("SmoothMoving")

# R, L Color Setting + All Ctrl Setting
def CtrlSetting():
    cmds.warning("CtrlSetting")

#---------------------------------------------------------------------------------------#

# Select joints to bind skin
def SelectJoints():
    cmds.warning("SelectJnt")

# Open Bind Skin Options
def OpenOptions():
    cmds.warning("Open Bind Skin Options")

# Bind Skin
def BindSkin():
    cmds.warning("BindSkinning")

#---------------------------------------------------------------------------------------#

# Get back to Default Pose
def DefaultPose():
    cmds.warning("Default Pose")

# Save keys
def KeySave():
    cmds.warning("Save Key")

# Mirror keys
def KeyMirror():
    cmds.warning("Mirror Key")

#---------------------------------------------------------------------------------------#

def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)








