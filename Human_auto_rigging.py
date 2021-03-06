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
subfinger = cmds.intSliderGrp(l="Sub Finger  ", min=1, max=10, v=4, f=True, cw3=(70,50,50))
wi=(2,55,100,130)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="", w=wi[0])
cmds.button(l="Delete", h=30, w=wi[1], c="DeleteJoint()")
cmds.button(l="Default setting", h=30, w=wi[2], c="DefaultJntSetting()")
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
        print "Delete Jnts"
    else:
        cmds.warning("Already delete it!")

# Need to fix!
# Go back to Default Jnt Setting
def DefaultJntSetting():
    l = cmds.intSliderGrp(leg, q=True, v=True)
    cmds.intSliderGrp.setValue(l.setValue,v=1,)
    cmds.intSliderGrp(leg, v=1)
    cmds.intSliderGrp(arm, v=1)
    cmds.intSliderGrp(basefinger, v=5)
    cmds.intSliderGrp(subfinger, v=4)

# Create Basic Jnt
def CreateBaseJoint():
    if cmds.objExists("Root"):
        cmds.warning("Basic Jnts are already exists")
    else:
        root=cmds.joint(n="Root", p=(0,9.82,-0.17))
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
        JntLeg()
        
        a=cmds.circle(nr=(0,1,0), n="world_ctrl")
        cmds.scale(3,3,3, a)
        cmds.makeIdentity(a=True, t=True, r=True, s=True, n=0)
        cmds.DeleteHistory(a)
        cmds.parent("Root","world_ctrl")
        print "Create Base Jnts"

#---------------------------------------------------------------------------------------#

# Leg Jnt
def JntLeg():
    i = cmds.intSliderGrp(leg, q=True, v=True)
    print "Leg Jnt count: "+str(i)
    if i==1:
        JntLeg_sub(0,0,i)
    elif i==2:
        JntLeg_sub(0.3,0.5,i-1)
        JntLeg_sub(0.3,-0.5,i)
    else:
        JntLeg_sub(0,0,i-2)
        JntLeg_sub(0.4,-0.4,i-1)
        JntLeg_sub(0.4,0.4,i)

def JntLeg_sub(x,y,i):
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
    i = cmds.intSliderGrp(arm, q=True, v=True)
    print "Arm Jnt count: "+str(i)
    if i==1:
        JntArm_sub(0,0,i)
    elif i==2:
        JntArm_sub(0,0,i-1)
        JntArm_sub(0,0.8,i)
    else:
        JntArm_sub(0.2,-0.1,i-2)
        JntArm_sub(0,0.4,i-1)
        JntArm_sub(0.2,0.9,i)

def JntArm_sub(x,y,i):
    arms = cmds.intSliderGrp(arm, q=True, v=True)
    cmds.select("Chest")
    cmds.joint(n="L_Scapula_"+str(i), p=(0.4-x,13.7,-0.15-y))
    cmds.joint(n="L_Shoulder_"+str(i), p=(1.5-x,13.7,-0.15-y))
    cmds.joint(n="L_Elbow_"+str(i), p=(4-x,13.7,-0.3-y))
    cmds.joint(n="L_Wrist_"+str(i), p=(6.4-x,13.7,-0.15-y))
    JntFinger(i,y)

#---------------------------------------------------------------------------------------#

# Finger Jnt
def JntFinger(a,y):
    base = cmds.intSliderGrp(basefinger, q=True, v=True)
    sub = cmds.intSliderGrp(subfinger, q=True, v=True)
    wrist = "L_Wrist_"+str(a)
    finger = "L_Finger_"+str(a)
    print "Base Finger Jnt count: "+str(base)
    print "Sub Finger Jnt count: "+str(sub)
    x=1
    while x<=base:
        cmds.select(wrist)
        if x==1:
            for i in range(1,sub+1):
                cmds.joint(n=finger+"_Thumb"+str(i), p=(6.4+0.2*i,13.68-0.08*i,-0.175+0.15*i-y))
        if x==2:
            for i in range(1, sub+1):
                cmds.joint(n=finger+"_Index"+str(i), p=(7.08+0.2*i,13.71-0.01*i,0.03+0.05*i-y))
        if x==3:
            for i in range(1, sub+1):
                cmds.joint(n=finger+"_Mid"+str(i), p=(7.13+0.25*i,13.7,-0.173-0.003*i-y))
        if x==4:
            cmds.joint(n=finger+"_Cup", p=(6.6,13.7,-0.27-y))
            for i in range(1, sub+1):
                cmds.joint(n=finger+"_Ring"+str(i), p=(7.05+0.25*i,13.65,-0.37-0.03*i-y))
        if x==5:
            cmds.select(finger+"_Cup")
            for i in range(1, sub+1):
                cmds.joint(n=finger+"_Pinky"+str(i), p=(7.05+0.2*i ,13.68-0.03*i,-0.48-0.07*i-y))
        if x>=6:
            cmds.select(finger+"_Cup")
            for i in range(1, sub+1):
                cmds.joint(n=finger+"_Extra"+str(x-5)+"_"+str(i), p=(7.09+(0.2-0.03*(x-5))*i-0.1*(x-5),13.68-0.03*i-0.02*(x-5),-0.48-(0.1+0.012*(x-5))*i-0.1*(x-5)-y))
        x=x+1

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
    i = cmds.intSliderGrp(leg, q=True, v=True)
    for x in range(1, i+1):
        if cmds.objExists("R_Hip_"+str(x)):
            cmds.warning("R_Leg_"+str(x)+" is already exists")
        else:
            cmds.mirrorJoint("L_Hip_"+str(x),mirrorBehavior=True, myz=True, sr=("L_","R_"))
            print "Mirror Hip Jnts"
    
    j = cmds.intSliderGrp(arm, q=True, v=True)
    for y in range(1, j+1):
        if cmds.objExists("R_Scapula_"+str(y)):
            cmds.warning("R_Arm_"+str(y)+" is already exists")
        else:
            cmds.mirrorJoint("L_Scapula_"+str(y),mirrorBehavior=True, myz=True, sr=("L_","R_"))
            print "Mirror Arm Jnts"
    
    if cmds.objExists("R_Eye"):
        cmds.warning("R_Eye is already exists")
    else:
        cmds.mirrorJoint("L_Eye",mirrorBehavior=True, myz=True, sr=("L_","R_"))
        print "Mirror Eye Jnts"

# need to fix
# Orient Jnt
def JntOrient():
    cmds.makeIdentity("Root", a=True, t=True, r=True, s=True, n=0)
    print "Orient Jnts"

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

# Go back to Default Pose
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
    print "Change Jnts Size: "+str(j)



