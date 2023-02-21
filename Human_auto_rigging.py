import maya.cmds as cmds
import pymel.core as pm

TOOLNAME = "HumanAutoRigging"
TOOLTITLE = "Human Auto Rigging"

WI01 = (2,273)
WI02 = (1,136,136)

TRANSLATE = ".translate"
ROTATE = ".rotate"
SCALE = ".scale"
AXISES = ["X", "Y", "Z"]
LFRT = ["L", "R"]

PLUSMIN = "plusMinusAverage"
MULDIV = "multiplyDivide"
REVERSE = "reverse"
BLENDTWO = "blendTwoAttr"
BLENDCOLORS = "blendColors"

CIRCLE = "circle"
SQUARE = "square"
ARROW1 = "arrow1"
ARROW4 = "arrow4"
DIA = "dia"
BOX = "box"
BALL = "ball"
DIAMOND = "diamond"
FKIK_CROSS = "cross1"
CROSS = "cross2"
EYE = "eye"

RED = "red"
YELLOW = "yellow"
BLUE = "blue"
SKYBLUE = "skyblue"
PINK = "pink"

def joint_name(type, body, num):
    types = {0: "RIG_", 1: "FK_", 2: "IK_", 3: "IK_non_", 4: "IK_stretch_",
            5: "IK_loc_"}
    return(types[type]+body+str(num))

def ctrlgrp(num=0):
    res = "_ctrl"
    if num == 1:
        res += "_grp"
    elif num == 2:
        res = "_grp"
    elif num == 3:
        res = "_loc"
    return(res)

def btn_layout(cnt):
    if cnt == 1:
        cmds.rowLayout(nc=2, cw2=WI01)
        cmds.text("")
    elif cnt == 2:
        cmds.rowLayout(nc=3, cw3=WI02)
        cmds.text("")

def frame(text, tmp=True):
    cmds.frameLayout(l=text, cll=True, w=285)
    if tmp:
        cmds.rowLayout(nc=1, h=1)
        cmds.setParent("..")

def endspace():
    cmds.setParent("..")
    cmds.separator(h=1)
    cmds.setParent("..")

if cmds.window(TOOLNAME, ex=True):
    cmds.deleteUI(TOOLNAME)

WINDOW = cmds.window(TOOLNAME, t=TOOLTITLE)
cmds.rowColumnLayout(w=285)


#----------------------------------------------------------------------------#


# Jnt size
frame("Joint Size", 0)
jnt = cmds.floatSliderButtonGrp(l="Size   ", bl="Set", bc="JointSize()", cw4=(50,50,70,50), f=True, min=0.1, max=1, v=0.5, h=30)
cmds.setParent("..")


# UI1: Rigging
frame("Rigging")

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
cmds.button(l="Setting Rigs", c="Setting()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

btn_layout(2)
cmds.button(l="Select Skin Joints", c="SelectJnt()", w=WI02[1], h=30)
cmds.button(l="Bind Skin Options", c="cmds.SmoothBindSkinOptions()", w=WI02[2], h=30)
endspace()


# UI2: Tools
frame("Tools")

btn_layout(2)
cmds.button(l="Loc", c="cmds.CreateLocator()", w=WI02[1], h=30)
cmds.button(l="LBA", c="cmds.ToggleLocalRotationAxes()", w=WI02[2], h=30)
cmds.setParent("..")

cmds.rowLayout(nc=1)
match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,58,52,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Match", c="matchFreeze()", w=WI01[1], h=30)
endspace()


# UI3: Lock
frame("Lock")

cmds.rowLayout(nc=1)
lock_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,60,60,60,10), la4=["Trans","Rot","Scale","Vis"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

btn_layout(2)
cmds.button(l="Lock", c="lockUnlock(True, True)", w=WI02[1], h=30)
cmds.button(l="UnKeyable", c="lockUnlock(True, False)", w=WI02[2], h=30)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Unlock + Keyable", c="lockUnlock(False, True)", w=WI01[1], h=30)
cmds.setParent("..")

btn_layout(2)
cmds.button(l="Lock Selected", c="lockUnlock(True, True, True)", w=WI02[1], h=30)
cmds.button(l="Unlock Selected", c="lockUnlock(False, True, True)", w=WI02[2], h=30)
endspace()


# UI4: Animation
frame("Animation")

btn_layout(1)
cmds.button(l="Back to Default Pose", c="DefaultPose()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

cmds.rowLayout(nc=1)
save_check = cmds.radioButtonGrp(l="Check : ", cw3=(75,70,10), la2=["Once","Hierarchy"], nrb=2, sl=2, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Save Keys", c="SaveKey()", w=WI01[1], h=30)
cmds.setParent("..")

btn_layout(1)
mirrorkey = cmds.radioButtonGrp(l="    Mirror Keys : ", cw3=(75,70,10), la2=["L => R","R => L"], nrb=2, sl=1, w=295, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Mirror Keys", c="MirrorKey()", w=WI01[1], h=30)
endspace()


cmds.showWindow(TOOLNAME)


#-------------------------------- Active Code ------------------------------#


# Create Basic Jnt
def JntCreate():
    if cmds.objExists("Root"):
        cmds.warning("Root is already exists")
    else:
        cmds.joint(n="Root", p=(0,9.82,-0.25))
        cmds.joint(n="Spine0", p=(0,9.82,-0.25))
        JntHead()
        if cmds.checkBox(arm_check, q=True, v=True):
            JntArmLeg("Arm")
        if cmds.checkBox(leg_check, q=True, v=True):
            cmds.joint("Root", n="Pelvic", p=(0,9.82,-0.25))
            JntArmLeg("Leg")
        
        world_ctrl = cmds.circle(nr=(0,1,0), n="World_ctrl")
        cmds.scale(3,3,3, world_ctrl)
        cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0)
        cmds.DeleteHistory(world_ctrl)
        cmds.parent("Root", "World_ctrl")
        print "Create Base Jnts"


# Head Jnt
def JntHead():
    cmds.joint("Spine0", n="Spine", p=(0,11.5,-0.15))
    cmds.joint(n="Chest1", p=(0,13,-0.3))
    cmds.joint(n="Neck1", p=(0,14.1,-0.2))
    cmds.joint(n="Head1", p=(0,15.7,-0.1))
    cmds.joint(n="Head1_end", p=(0,17.1,-0.1))
    cmds.joint("Spine0", e=True, oj="xyz", sao="zup", ch=True, zso=True)
    
    cmds.joint("Head1", n="Jaw1", p=(0,15.4,0.5))
    cmds.joint(n="Jaw1_end", p=(0,14.9,1.5))
    cmds.joint("Jaw1", e=True, oj="xyz", sao="ydown", ch=True, zso=True)
    
    cmds.joint("Head1", n="L_Eye1", p=(0.34,15.9,0.5))
    cmds.joint(n="L_Eye1_end", p=(0.34,15.9,1.5))
    cmds.joint("L_Eye1", e=True, oj="xyz", sao="zup", ch=True, zso=True)


# Arm & Leg Jnt
def JntArmLeg(obj):
    if obj == "Leg":
        num = cmds.intField(leg, q=True, v=True)
        func = JntLeg_sub
    elif obj == "Arm":
        num = cmds.intField(arm, q=True, v=True)
        func = JntArm_sub
    print obj + " Jnt count: " + str(num)
    if num == 0:
        cmds.warning(obj + " count is 0!")
        return
        
    tmp = 0
    if num != 1:
        tmp = num / 2
    for i in range(1, tmp+1):
        z_f = -num + i
        z_b = num - i
        if num % 2 == 0:
            z_f += 0.5*i
            z_b -= 0.5*i
        func((tmp-i)*0.3, z_f*0.3, i)
        func((tmp-i)*0.3, z_b*0.3, num-i+1)
    if num % 2 == 1:
        func(0, 0, num/2+1)


def JntLeg_sub(x,z,num):
    cmds.joint("Pelvic", n="L_Hip"+str(num), r=True, p=(1-x,-0.5,0.1-z))
    cmds.joint(n="L_Knee"+str(num), r=True, p=(0,-4.63,0.3))
    cmds.joint(n="L_Ankle"+str(num), r=True, p=(0,-3.85,-0.2))
    cmds.joint(n="tmp", r=True, p=(0,-1,0))
    cmds.joint("L_Hip"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
    cmds.delete("tmp")
    
    cmds.joint("L_Ankle"+str(num), n="L_Toes"+str(num), r=True, p=(0.54,-1.3,0))
    cmds.joint(n="L_Toes_end"+str(num), r=True, p=(0.3,-0.7,0))
    cmds.joint("L_Toes"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
    
    cmds.joint("L_Ankle"+str(num), n="L_Heel"+str(num), r=True, p=(0.84,1,0))
    cmds.joint("L_Toes_end"+str(num), n="L_FootSideInner"+str(num), r=True, p=(0,1,-0.5))
    cmds.joint("L_Toes_end"+str(num), n="L_FootSideOuter"+str(num), r=True, p=(0,1,0.5))
    cmds.parent("L_FootSide*"+str(num), w=True)
    cmds.parent("L_FootSide*"+str(num), "L_Toes"+str(num))


def JntArm_sub(x,z,num):
    cmds.joint("Chest1", n="L_Scapula"+str(num), p=(0.4-x,14,-0.1-z))
    cmds.joint(n="L_Shoulder"+str(num), p=(1.3-x,14,-0.1-z))
    cmds.joint(n="L_Elbow"+str(num), p=(4-x,14,-0.2-z))
    cmds.joint(n="L_Wrist"+str(num), p=(6.4-x,14,-z))
    cmds.joint(n="tmp", p=(7.4-x,14,-z))
    
    cmds.joint("L_Scapula"+str(num), e=True, oj="xyz", sao="ydown", ch=True, zso=True)
    cmds.delete("tmp")
    
    cmds.select("L_Wrist"+str(num))
    JntFinger(num,z)


# Finger Jnt
def JntFinger(num,y):
    num_basefinger = cmds.intField(basefinger, q=True, v=True)
    num_subfinger = cmds.intField(subfinger, q=True, v=True)+1
    wrist = "L_Wrist"+str(num)
    finger = "L_Finger"+str(num)+"_"
    print "Base Finger Jnt count: " + str(num_basefinger) + " / Sub Finger Jnt count: " + str(num_subfinger-1)
    
    for nb in range(1, num_basefinger+1):
        cmds.select(wrist)
        if nb == 1:
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(6.5+0.2*i,14-0.08*i,0.18*i-y))
        elif nb == 2:
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(7+0.2*i,14-0.01*i,0.1+0.05*i-y))
        elif nb == 3:
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(7.1+0.25*i,14,-y))
        elif nb == 4:
            cmds.joint(n=finger+"Cup", p=(6.7,14,-0.15-y))
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(7+0.25*i,14,-0.2-0.03*i-y))
        elif nb == 5:
            cmds.select(finger+"Cup")
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(7+0.2*i ,14-0.03*i,-0.3-0.07*i-y))
        elif nb >= 6:
            cmds.select(finger+"Cup")
            for i in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(nb)+"_"+str(i), p=(7+(0.2-0.03*(nb-5))*i-0.1*(nb-5),14-0.02*(nb-5),-0.3-(0.1+0.01*(nb-5))*i-0.1*(nb-5)-y))
    JntFingerOrient(num)


def JntFingerOrient(num):
    bf_int = cmds.intField(basefinger, q=True, v=True)
    for x in range(1, bf_int+1):
        cmds.select("L_Finger"+str(num)+"_"+str(x)+"_1")
        cmds.FreezeTransformations()
        if x == 1:
            cmds.joint(e=True, oj="xyz", sao="zdown", ch=True, zso=True)
        else:
            cmds.joint(e=True, oj="xyz", sao="ydown", ch=True, zso=True)
    cmds.makeIdentity("L_Wrist"+str(num), a=True, r=True)
    cmds.DeleteHistory("L_Wrist"+str(num))


#----------------------------------------------------------------------------#


# Mirror Hip(leg), Scapula(Arm), Eye
def JntMirror():
    if not cmds.objExists("L_*"):
        cmds.warning("No joints!")
        return
    if cmds.objExists("R_*"):
        cmds.warning("Already Mirrored!")
        return
        
    num_leg = cmds.intField(leg, q=True, v=True)
    num_arm = cmds.intField(arm, q=True, v=True)
    world_scale = cmds.getAttr("World_ctrl"+SCALE+"X")
    grp_for_scale = "scale_grp"
    
    JntOrient()
    if cmds.checkBox(arm_check, q=True, v=True):
        JntMirror_check(num_arm, "Scapula", "Arm")
    if cmds.checkBox(leg_check, q=True, v=True):
        JntMirror_check(num_leg, "Hip", "Leg")
    JntMirror_check(1, "Eye", "Eye")
    
    if not cmds.objExists(grp_for_scale):
        cmds.group(n=grp_for_scale, em=True)
        cmds.parent(grp_for_scale, "World_ctrl")
    cmds.scale(world_scale, world_scale, world_scale, grp_for_scale)


def JntMirror_check(end_num, obj, name):
    for num in range(1, end_num+1):
        if cmds.objExists("R_"+obj+str(num)):
            cmds.warning("R_"+name+str(num)+" is already exists")
        else:
            cmds.mirrorJoint("L_"+obj+str(num),mirrorBehavior=True, myz=True, sr=("L_", "R_"))
            print "Mirror "+name+" Jnts"


# Orient Jnt
def JntOrient():
    num_leg = cmds.intField(leg, q=True, v=True)
    num_arm = cmds.intField(arm, q=True, v=True)
    num_finger = cmds.intField(basefinger, q=True, v=True)

    cmds.select("World_ctrl")
    cmds.FreezeTransformations()
    
    if cmds.checkBox(leg_check, q=True, v=True):
        for num in range(1, num_leg+1):
            cmds.parent(["L_Toes"+str(num), "L_Heel"+str(num)], w=True)
            cmds.joint("L_Ankle"+str(num), n="leg_tmp"+str(num), r=True, p=(2, 0, 0))

    if cmds.checkBox(arm_check, q=True, v=True):
        idx_finger = num_finger if num_finger < 3 else 3
        for num in range(1, num_arm+1):
            for i in range(1, idx_finger+1):
                cmds.parent("L_Finger"+str(num)+"_"+str(i)+"_1", w=True)
            if num_finger > 3:
                cmds.parent("L_Finger"+str(num)+"_Cup", w=True)
            cmds.joint("L_Wrist"+str(num), n="wrist_tmp"+str(num), r=True, p=(2, 0, 0))

    cmds.joint("Spine0", e=True, oj="xyz", sao="zup", ch=True, zso=True)
    cmds.joint("Jaw1", e=True, oj="xyz", sao="ydown", ch=True, zso=True)
    cmds.joint("L_Eye1", e=True, oj="xyz", sao="zup", ch=True, zso=True)
    print "Orient Head Jnts"
    
    if cmds.checkBox(leg_check, q=True, v=True):
        for num in range(1, num_leg+1):
            cmds.joint("L_Hip"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
            cmds.joint("L_Toes"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
            cmds.delete("leg_tmp"+str(num))
            cmds.parent(["L_Toes"+str(num), "L_Heel"+str(num)], "L_Ankle"+str(num))
        print "Orient Hip Jnts"

    if cmds.checkBox(arm_check, q=True, v=True):
        for num in range(1, num_arm+1):
            cmds.joint("L_Scapula" + str(num), e=True, oj="xyz", sao="ydown", ch=True, zso=True)
            cmds.delete("wrist_tmp"+str(num))
            for i in range(1, idx_finger+1):
                cmds.parent("L_Finger"+str(num)+"_"+str(i)+"_1", "L_Wrist"+str(num))
            if num_finger > 3:
                cmds.parent("L_Finger"+str(num)+"_Cup", "L_Wrist"+str(num))
        print "Orient Arm Jnts"

    cmds.makeIdentity("Root", a=True, r=True)
    cmds.DeleteHistory("Root")


#----------------------------------------------------------------------------#


# !!! FIX: 아무것도 없을 때 warning
# Setting: FK, IK, Scale, SquashStretch
def Setting():
    if not cmds.objExists("R_*"):
        if not cmds.objExists("L_*"):
            cmds.warning("No joints!")
            return
        cmds.warning("Need to Mirror!")
        return
    if cmds.getAttr("World_ctrl"+SCALE+"X") != 1:
        cmds.warning("Need to Orient!")
        return
    if cmds.objExists("rig_grp"):
        cmds.warning("Already Done!")
        return
    
    rig_grp = "rig_grp"
    world_grp = "World_ctrl_grp"
    ik_grp = "IK_grp"
    fk_grp = "FK_grp"
    fkik_grp = "FKIK"+ctrlgrp(1)
    jnt_grp = "jnt_grp"
    extra_grp = "extra_grp"
    ctrl_grp = "ctrl_grp"
    
    ikjnt_grp = "IK_jnt_grp"
    ikctrl_grp = "IK"+ctrlgrp(1)
    ikcluster_grp = "IK_cluster"+ctrlgrp(1)
    ikspline_grp = "IK_spline"+ctrlgrp(1)
    ikstatic_grp = "IK_static"+ctrlgrp(1)
    ikfollow_grp = "IK_follow"+ctrlgrp(1)
    ikmessure_grp = "IK_messure"+ctrlgrp(1)
    
    grp_names = [rig_grp, world_grp, ik_grp, fk_grp, fkik_grp,
                jnt_grp, extra_grp, ctrl_grp, ikjnt_grp, ikctrl_grp,
                ikcluster_grp, ikspline_grp, ikstatic_grp, ikfollow_grp,
                ikmessure_grp]
    
    for grp_name in grp_names:
        cmds.group(n=grp_name, em=True)
    cmds.parent(ikjnt_grp, ikctrl_grp, ikcluster_grp, ikspline_grp,
                ikstatic_grp, ikfollow_grp, ikmessure_grp,
                ik_grp)
    cmds.parentConstraint("World_ctrl", ikstatic_grp, mo=True)
    cmds.scaleConstraint("World_ctrl", ikstatic_grp, mo=True)
    
    SettingRoot()
    SettingSpine()
    SettingHead()
    if cmds.checkBox(arm_check, q=True, v=True):
       SettingArm()
#       SettingHand()
    if cmds.checkBox(leg_check, q=True, v=True):
       SettingLeg()
#       SettingFoot()
#    SettingElse()
#    cmds.warning("Fixing")

    cmds.delete("scale_grp")
    cmds.parent("World_ctrl", world_grp)
    cmds.parent("Root", rig_grp)
    for grp_name in [fk_grp, ik_grp, fkik_grp, jnt_grp]:
        cmds.connectAttr("World_ctrl"+SCALE, grp_name+SCALE)
    cmds.parent(world_grp, "Root_ctrl_grp", fk_grp, ik_grp, fkik_grp, extra_grp, ctrl_grp)
    cmds.parent(jnt_grp, ctrl_grp, rig_grp)
                
#    for part in [ikjnt_grp, vis_grp]:
#        cmds.setAttr(part+".visibility", 0)


#----------------------------------------------------------------------------#

def SettingRoot():
    cmds.duplicate("Root", n="RIG_Root1", po=True)
    cmds.parent("RIG_Root1", "jnt_grp")
    
    CtrlCreate("RIG_Root1", ARROW1, 0, "Root", YELLOW)
    cmds.parent("Root"+ctrlgrp(1), "rig_grp")
    cmds.connectAttr("Root"+ctrlgrp()+SCALE, "RIG_Root1"+SCALE)
    
    cmds.parentConstraint("World_ctrl", "Root"+ctrlgrp(1), mo=True)
    cmds.connectAttr("World_ctrl"+SCALE, "Root"+ctrlgrp(1)+SCALE)
    
    for axis in ["sx", "sy", "sz"]:
        cmds.setAttr("Root_ctrl."+axis, lock=True, keyable=False, channelBox=False)
    root_follow()


########## !!! FIX 다리하고 다시 오기
def root_follow():
    follow = "Root_follow"
    follow_center = "Root_follow_center"
    follow_btw_legs = "Root_follow_btw_legs"
    
    add_attrs("Root"+ctrlgrp())
    add_attrs("Root"+ctrlgrp(), "follow_btw_legs", 2, 0, 0, 10)
    for grp_name in [follow, follow_center, follow_btw_legs]:
        cmds.group(n=grp_name, em=True)
    cmds.parent(follow_btw_legs, follow_center, follow)
    cmds.parentConstraint("World_ctrl", follow)
    cmds.scaleConstraint("World_ctrl", follow)
#    cmds.parentConstraint("IK_L_leg1_ctrl", "IK_R_leg1_ctrl", follow_btw_legs)

    cmds.parent(follow, "extra_grp")


#----------------------------------------------------------------------------#


def SettingSpine():
    Setting_prepare("Spine")
    SpineFK()
    SpineIK()
    Setting_vis("Spine")
    cmds.parent("RIG_Spine1", "FK_Spine1", "IK_Spine1", "RIG_Root1")
    print "Create Spine"


def SpineFK():
    def fk_spine(num):
        return(joint_name(1, "Spine", num))

    CtrlCreate(fk_spine(1), CIRCLE, 1, "FK_Pelvic", SKYBLUE)
    CtrlCreate(fk_spine(4), CIRCLE, 1, "FK_Spine", SKYBLUE)
    CtrlCreate(fk_spine(7), CIRCLE, 0, "FK_Chest", SKYBLUE)
    for num in [1, 4]:
        fk_ctrl = "FK_Pelvic" if num == 1 else "FK_Spine"
        cmds.connectAttr(fk_ctrl+ctrlgrp()+SCALE, fk_spine(num)+SCALE)
        cmds.connectAttr(fk_ctrl+ctrlgrp()+SCALE, fk_spine(num+1)+SCALE)
        cmds.connectAttr(fk_ctrl+ctrlgrp()+SCALE, fk_spine(num+2)+SCALE)
    cmds.connectAttr("FK_Chest"+ctrlgrp()+SCALE, fk_spine(7)+SCALE)
    
    fk_divide_ctrl(["FK_Pelvic", "FK_Spine"])
    fk_grouping(fk_spine, "Spine", [3, 6])
    

def SpineIK():
    def ik_spine(num):
        return(joint_name(2, "Spine", num))
 
    ik_spline_handle(ik_spine, "Spine", 7)
    ik_spline_handle_cluster(ik_spine, "Spine", 4, 7)

    tmp = [ik_spine(1), ik_spine(2), 2]
    num = [1, 0.5]
    for i in range(2):
        for idx in range(2):
            tmp_cluster = joint_name(2,"Spine",tmp[2]+idx)+"_cluster_grp"
            cmds.parentConstraint(tmp[0]+ctrlgrp(), tmp[1]+ctrlgrp(), tmp_cluster, mo=True)
            cmds.setAttr(tmp_cluster+"_parentConstraint1."+tmp[0]+"_ctrlW0", num[0])
            cmds.setAttr(tmp_cluster+"_parentConstraint1."+tmp[1]+"_ctrlW1", num[1])
            num = num[::-1]
        tmp = [ik_spine(2), ik_spine(3), 5]
    
    ik_twist("Spine")
    ik_hybrid("Spine")
    ik_middle_follow("Spine")
    ik_stretchy("Spine")
    ik_stiff("Spine")
    ik_volume("Spine")
    ik_grouping("Spine")


#----------------------------------------------------------------------------#

# !!! FIX
def SettingHead():
    Setting_prepare("Neck")
    NeckFK()
    NeckIK()
    Setting_vis("Neck")
    cmds.parent("RIG_Neck1", "FK_Neck1", "IK_Neck1", "RIG_Spine7")
    
    Setting_head()
    HeadFK()
    EyeAim()
    print "Create Hand"
    
    
def NeckFK():
    def fk_neck(num):
        return(joint_name(1, "Neck", num))
        
    CtrlCreate(fk_neck(1), CIRCLE, 1, "FK_Neck", SKYBLUE)
    CtrlCreate(fk_neck(5), CIRCLE, 9, "FK_Head", SKYBLUE)
    cmds.scale(0.7, 0.7, 0.7, "FK_Neck_ctrl.cv[0:7]", r=True, ocp=True)
    cmds.scale(0.7, 0.7, 0.7, "FK_Head_ctrl.cv[0:7]", r=True, ocp=True)
    
    cmds.connectAttr("FK_Neck"+ctrlgrp()+SCALE, fk_neck(1)+SCALE)
    cmds.connectAttr("FK_Neck"+ctrlgrp()+SCALE, fk_neck(2)+SCALE)
    cmds.connectAttr("FK_Neck"+ctrlgrp()+SCALE, fk_neck(3)+SCALE)
    cmds.connectAttr("FK_Neck"+ctrlgrp()+SCALE, fk_neck(4)+SCALE)
    
    fk_divide_ctrl(["FK_Neck"])
    fk_grouping(fk_neck, "Neck", [4])

    
def NeckIK():
    def ik_neck(num):
        return(joint_name(2, "Neck", num))
    
    ik_spline_handle(ik_neck, "Neck", 5)
    ik_spline_handle_cluster(ik_neck, "Neck", 3, 5)
    
    cmds.parentConstraint(ik_neck(1)+ctrlgrp(), ik_neck(2)+ctrlgrp(), ik_neck(2)+"_cluster_grp", mo=True)
    cmds.parentConstraint(ik_neck(2)+ctrlgrp(), ik_neck(3)+ctrlgrp(), ik_neck(4)+"_cluster_grp", mo=True)
        
    ik_twist("Neck")
    ik_hybrid("Neck")
    ik_middle_follow("Neck")
    ik_stretchy("Neck")
    ik_stiff("Neck")
    ik_volume("Neck")
    ik_grouping("Neck")
    
    for num in range(1, 4):
        cmds.scale(0.7, 0.7, 0.7, ik_neck(num)+"_ctrl.cv[0:15]", r=True, ocp=True)
        cmds.scale(0.7, 0.7, 0.7, "IK_Neck_Hybrid"+str(num)+"_ctrl.cv[0:16]", r=True, ocp=True)
    

def HeadFK():
    match_objs("RIG_Head1_end", "FK_Head"+ctrlgrp())
    cmds.setAttr("FK_Head"+ctrlgrp()+ROTATE+"Y", 0)
    cmds.select("FK_Head"+ctrlgrp())
    cmds.makeIdentity(a=True, t=1, r=1, n=0)
    cmds.ResetTransformations()
    cmds.parentConstraint("FK_Head"+ctrlgrp(), "FK_Neck5", mo=True)
    cmds.connectAttr("FK_Head"+ctrlgrp()+SCALE, "FK_Neck5"+SCALE)

    CtrlCreate("RIG_Jaw1", CIRCLE, 0, "FK_Jaw", SKYBLUE)
    CtrlCreate("RIG_L_Eye1", CIRCLE, 0, "FK_L_Eye", SKYBLUE)
    CtrlCreate("RIG_R_Eye1", CIRCLE, 0, "FK_R_Eye", SKYBLUE)
    
    for name in ["FK_Jaw", "FK_L_Eye", "FK_R_Eye"]:
        cmds.scale(0.25, 0.25, 0.25, name+ctrlgrp()+".cv[0:7]", r=True, ocp=True)
    cmds.connectAttr("FK_Jaw"+ctrlgrp()+SCALE, "RIG_Jaw1"+SCALE)
    cmds.connectAttr("FK_L_Eye"+ctrlgrp()+SCALE, "RIG_L_Eye1"+SCALE)
    cmds.connectAttr("FK_R_Eye"+ctrlgrp()+SCALE, "RIG_R_Eye1"+SCALE)
    
    fk_grouping(None, "Head", None)
    cmds.connectAttr("RIG_Neck5"+SCALE, "FK_Head"+ctrlgrp(2)+SCALE)


def EyeAim():
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    aim_l = "AIM_L_Eye"
    aim_r = "AIM_R_Eye"
    aim_all = "AIM_Eye"
    follow_on = aim_all+"_follow_on"
    follow_off = aim_all+"_follow_off"
    
    CtrlCreate("RIG_L_Eye1_end", CROSS, 9, aim_l, RED)
    CtrlCreate("RIG_R_Eye1_end", CROSS, 9, aim_r, BLUE)
    CtrlCreate("RIG_R_Eye1_end", CROSS, 9, aim_all, YELLOW)
    cmds.pointConstraint("RIG_L_Eye1_end", "RIG_R_Eye1_end", aim_all+ctrlgrp(1), n="tmp")
    cmds.delete("tmp")
    cmds.scale(1.5, 1.5, 1.5, aim_all+ctrlgrp(1))
    cmds.select(aim_l+ctrlgrp(1), aim_r+ctrlgrp(1), aim_all+ctrlgrp(1))
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parent(aim_l+ctrlgrp(1), aim_r+ctrlgrp(1), aim_all+ctrlgrp())
    cmds.setAttr(aim_all+ctrlgrp(1)+TRANSLATE+"Z", world_scale)
    for lr in LFRT:
        cmds.aimConstraint("AIM_"+lr+"_Eye"+ctrlgrp(), "FK_"+lr+"_Eye"+ctrlgrp(1), mo=True, u=[1,0,0])

    for name in [follow_on, follow_off]:
        cmds.group(n=name, em=True)
        match_objs(aim_all+ctrlgrp(1), name)
    cmds.group(n=follow_on+ctrlgrp(2), em=True)
    match_objs("RIG_Neck5", follow_on+ctrlgrp(2))
    cmds.parentConstraint("RIG_Neck5", follow_on+ctrlgrp(2), mo=True)
    cmds.parent(follow_on, follow_on+ctrlgrp(2))
    cmds.parentConstraint(follow_on, follow_off, aim_all+ctrlgrp(1), mo=True)

    add_attrs(aim_all+ctrlgrp())
    add_attrs(aim_all+ctrlgrp(), "follow", 2, 5, 0, 10)
    
    attr_follow_off = aim_all+ctrlgrp(1)+"_parentConstraint1."+follow_off+"W1"
    attr_follow_on = aim_all+ctrlgrp(1)+"_parentConstraint1."+follow_on+"W0"
    follow_attr(aim_all+ctrlgrp(), attr_follow_on, attr_follow_off, 10)
    
    cmds.group(n=aim_all+ctrlgrp(2), em=True)
    match_objs("RIG_Neck5", aim_all+ctrlgrp(2))
    cmds.parent(aim_all+ctrlgrp(1), follow_on+ctrlgrp(2), follow_off, aim_all+ctrlgrp(2))
    cmds.parent(aim_all+ctrlgrp(2), "FK_grp")
    cmds.connectAttr("RIG_Neck5"+SCALE, aim_all+ctrlgrp(2)+SCALE)
    
    
#----------------------------------------------------------------------------#


def SettingArm():
    end_num = cmds.intField(arm, q=True, v=True)
    
    Setting_scapula()
    Setting_prepare("Arm")
    ScapulaFK()
    ArmLegFKIK("Arm")
    Setting_vis_armleg("Arm")
    print "Create Arm"


def ScapulaFK():
    end_num = cmds.intField(arm, q=True, v=True)
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            rig_scapula = joint_name(0,lr+"_Scapula",num)
            rig_shoulder = joint_name(0,lr+"_Shoulder",num)
            fk_scapula = joint_name(1,lr+"_Scapula",num)
            attr_num = -1 if lr == "L" else 1
            
            CtrlCreate(rig_scapula, ARROW4, 9, fk_scapula, YELLOW)
            match_objs(rig_shoulder, fk_scapula+ctrlgrp())
            cmds.setAttr(fk_scapula+ctrlgrp()+TRANSLATE+"Y", attr_num*world_scale)
            cmds.select(fk_scapula+ctrlgrp())
            cmds.makeIdentity(a=True, t=1, r=1, n=0)
            cmds.ResetTransformations()
            cmds.parentConstraint(fk_scapula+ctrlgrp(), rig_scapula, mo=True)
            cmds.connectAttr(fk_scapula+ctrlgrp()+SCALE, rig_scapula+SCALE)


#----------------------------------------------------------------------------#


def SettingHand():
        print "Create Hand"


#----------------------------------------------------------------------------#


def SettingLeg():
    num_leg = cmds.intField(leg, q=True, v=True)
    
    cmds.duplicate("FK_Spine1", n="RIG_Pelvic1", po=True)
    Setting_prepare("Leg")
    PelvicFK()
    ArmLegFKIK("Leg")
    Setting_vis_armleg("Leg")
    print "Create Leg"
        
def PelvicFK():
    end_num = cmds.intField(leg, q=True, v=True)
    
    rig = "RIG_Pelvic1"
    fk = cmds.duplicate("FK_Spine1", n="FK_Pelvic1"+ctrlgrp(2), po=True)
    ik = cmds.duplicate("FK_Spine1", n="IK_Pelvic1"+ctrlgrp(2), po=True)
    
    spread(rig, fk, ik)
    cmds.connectAttr("FKIK_Spine_ctrl.FKIK", rig+".spread")
    cmds.pointConstraint("FK_Spine1", fk, mo=True)
    cmds.connectAttr("FK_Pelvic_Divide.output", fk[0]+ROTATE)
    cmds.parentConstraint("IK_Spine1_ctrl", ik, mo=True)

        
#----------------------------------------------------------------------------#


def SettingFoot():
    print "Create Foot"


#----------------------------------------------------------------------------#


def SettingElse():
    print "Create Else"


#----------------------------------------------------------------------------#


def Setting_prepare(part):
    def rig_spine(num):
        return(joint_name(0, "Spine", num))
    def rig_neck(num):
        return(joint_name(0, "Neck", num))

    if part in ["Spine", "Neck"]:
        body = [part]
        num_body = 1
    elif part == "Arm":
        body = ["L_Shoulder", "L_Elbow", "L_Wrist"]
        num_body = cmds.intField(arm, q=True, v=True)
    elif part == "Leg":
        body = ["L_Hip", "L_Knee", "L_Ankle"]
        num_body = cmds.intField(leg, q=True, v=True)
        
    for num in range(1, num_body+1):
        if part == "Spine":
            cmds.duplicate("Spine0", n=rig_spine(1), po=True)
            cmds.duplicate("Spine", n=rig_spine(4), po=True)
            cmds.duplicate("Chest1", n=rig_spine(7), po=True)
            cmds.parent("RIG_Spine*", w=True)
            Setting_spine(rig_spine(4), rig_spine(1), 2)
            Setting_spine(rig_spine(7), rig_spine(4), 5)
            cmds.parent(rig_spine(4), rig_spine(3))
            cmds.parent(rig_spine(7), rig_spine(6))
            cmds.select(rig_spine(1))
            cmds.FreezeTransformations()
            cmds.joint(rig_spine(1), e=True, oj="xyz", sao="zup", ch=True, zso=True)
        elif part == "Neck":
            cmds.duplicate("Neck1", n=rig_neck(1), po=True)
            cmds.duplicate("Head1", n=rig_neck(5), po=True)
            cmds.parent("RIG_Neck*", w=True)
            Setting_neck(rig_neck(5), rig_neck(1))
        else:
            tmp = []
            for i in range(3):
                tmp += cmds.duplicate(body[i]+str(num), n=joint_name(0,body[i],num), po=True)
            cmds.parent(tmp, w=True)
            cmds.parent(joint_name(0,body[2],num), joint_name(0,body[1],num))
            cmds.parent(joint_name(0,body[1],num), joint_name(0,body[0],num))
            
        duplicate_joints(0,body[0],1,num)
        duplicate_joints(0,body[0],2,num)
        if part in ["Arm", "Leg"]:
            mid_name = "R_Shoulder" if part == "Arm" else "R_Hip"
            for type in range(3):
                cmds.mirrorJoint(joint_name(type,body[0],num), mirrorBehavior=True, myz=True, sr=("L_", "R_"))
            spread(joint_name(0,mid_name,num), joint_name(1,mid_name,num), joint_name(2,mid_name,num))
        spread(joint_name(0,body[0],num), joint_name(1,body[0],num), joint_name(2,body[0],num))
    Setting_FKIK(part)


def Setting_spine(top, bottom, num):
    trans = []
    for i in range(1, 3):
        for axis in ["X", "Y"]:
            num_top = cmds.getAttr(top+TRANSLATE+axis)
            num_bottom = cmds.getAttr(bottom+TRANSLATE+axis)
            if num_top < num_bottom:
                trans.append(num_bottom - (num_bottom - num_top)/3*i)
            else:
                trans.append((num_top - num_bottom)/3*i + num_bottom)
        num_top = cmds.getAttr(top+TRANSLATE+"Z")
        num_bottom = cmds.getAttr(bottom+TRANSLATE+"Z")
        if num_top < num_bottom:
            tmp = 1 if i == 1 else 3
            trans.append(num_bottom - (num_bottom - num_top)/5*tmp)
        else:
            tmp = 2 if i == 1 else 4
            trans.append((num_top - num_bottom)/5*tmp + num_bottom)
    tmp = cmds.joint(bottom, n="RIG_Spine"+str(num), p=(trans[0], trans[1], trans[2]))
    cmds.joint(tmp, n="RIG_Spine"+str(num+1), p=(trans[3], trans[4], trans[5]))
    
    
def Setting_neck(top, bottom):
    trans = []
    for i in range(1, 4):
        for axis in AXISES:
            num_top = cmds.getAttr(top+TRANSLATE+axis)
            num_bottom = cmds.getAttr(bottom+TRANSLATE+axis)
            if num_top < num_bottom:
                trans.append(num_bottom - (num_bottom - num_top)/4*i)
            else:
                trans.append((num_top - num_bottom)/4*i + num_bottom)
    tmp = cmds.joint(bottom, n="RIG_Neck2", p=(trans[0], trans[1], trans[2]))
    mid = cmds.joint(tmp, n="RIG_Neck3", p=(trans[3], trans[4], trans[5]))
    cmds.joint(mid, n="RIG_Neck4", p=(trans[6], trans[7], trans[8]))
    cmds.parent("RIG_Neck5", "RIG_Neck4")
    
    
def Setting_head():
    cmds.duplicate("Head1_end", n="RIG_Head1_end", po=True)
    cmds.parent("RIG_Head1_end", "RIG_Neck5")

    for part in ["Jaw", "L_Eye", "R_Eye"]:
        cmds.duplicate(part+"1", n=joint_name(0,part,1), po=True)
        cmds.duplicate(part+"1_end", n=joint_name(0,part,1)+"_end", po=True)
    for part in ["Jaw", "L_Eye", "R_Eye"]:
        cmds.parent(joint_name(0,part,1)+"_end", joint_name(0,part,1))
    for part in ["Jaw", "L_Eye", "R_Eye"]:
        cmds.parent(joint_name(0,part,1), "RIG_Neck5")
    

def Setting_scapula():
    end_num = cmds.intField(arm, q=True, v=True)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            cmds.duplicate(lr+"_Scapula"+str(num), n="RIG_"+lr+"_Scapula"+str(num), po=True)
            cmds.parent("RIG_"+lr+"_Scapula"+str(num), "RIG_Spine7")

    
def Setting_FKIK(part):
    if part == "Spine":
        obj = "RIG_Spine1"
        ctrl_name = "FKIK_Spine"
        attrs = [TRANSLATE+"X"]
        attr_num = 2.5
        end_num = 7
    elif part == "Neck":
        obj = "RIG_Neck1"
        ctrl_name = "FKIK_Neck"
        attrs = [TRANSLATE+"X", TRANSLATE+"Y"]
        attr_num = 0.8
        end_num = 5
    elif part in ["Arm", "Leg"]:
        Setting_FKIK_armleg(part)
        return
    
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    CtrlCreate(obj, FKIK_CROSS, 9, ctrl_name, BLUE, 1)
    for attr in attrs:
        cmds.setAttr(ctrl_name+ctrlgrp()+attr, attr_num*world_scale)
    cmds.parentConstraint(obj, ctrl_name+ctrlgrp(1), mo=True)
    cmds.makeIdentity(ctrl_name+ctrlgrp(), apply=True, t=1, r=1, s=1, n=0, pn=1)
    add_attrs(ctrl_name+ctrlgrp())
    add_attrs(ctrl_name+ctrlgrp(), "FKIK", 2)
    for num in range(1, end_num+1):
        cmds.connectAttr(ctrl_name+ctrlgrp()+".FKIK", joint_name(0,part,num)+".spread")
     

def Setting_FKIK_armleg(part):
    if part == "Arm":
        end_num = cmds.intField(arm, q=True, v=True)
        attrs = [TRANSLATE+"X", TRANSLATE+"Y"]
        attr_num = [2, 1]
        mid_names = ["_Shoulder", "_Elbow", "_Wrist"]
    else:
        end_num = cmds.intField(leg, q=True, v=True)
        attrs = [TRANSLATE+"X", TRANSLATE+"Y"]
        attr_num = [1, -1]
        mid_names = ["_Hip", "_Knee", "_Ankle"]
        
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    for num in range(1, end_num+1):
        if part == "Arm":
            l_obj = "RIG_L_Scapula"+str(num)
            r_obj = "RIG_R_Scapula"+str(num)
            l_parent = l_obj
            r_parent = r_obj
        else:
            l_obj = "RIG_L_Hip"+str(num)
            r_obj = "RIG_R_Hip"+str(num)
            l_parent = "RIG_Pelvic1"
            r_parent = l_parent

        l_ctrl_name = "FKIK_L_"+part+str(num)
        r_ctrl_name = "FKIK_R_"+part+str(num)
        CtrlCreate(l_obj, FKIK_CROSS, 9, l_ctrl_name, BLUE, 1)
        
        for idx, attr in enumerate(attrs):
            cmds.setAttr(l_ctrl_name+ctrlgrp()+attr, attr_num[idx]*world_scale)
        if part == "Arm":
            cmds.setAttr(l_ctrl_name+ctrlgrp()+ROTATE+"X", 90)
            cmds.makeIdentity(l_ctrl_name+ctrlgrp(), apply=True, t=1, r=1, s=1, n=0, pn=1)
        else:
            cmds.parent(l_ctrl_name+ctrlgrp(), w=True)
            match_objs("RIG_Pelvic1", l_ctrl_name+ctrlgrp(1))
            cmds.parent(l_ctrl_name+ctrlgrp(), l_ctrl_name+ctrlgrp(1))
        cmds.parentConstraint(l_parent, l_ctrl_name+ctrlgrp(1), mo=True)
        
        add_attrs(l_ctrl_name+ctrlgrp())
        add_attrs(l_ctrl_name+ctrlgrp(), "FKIK", 2)
        cmds.duplicate(l_ctrl_name+ctrlgrp(), n=r_ctrl_name+ctrlgrp())
        cmds.duplicate(l_ctrl_name+ctrlgrp(1), n=r_ctrl_name+ctrlgrp(1), po=True)
        cmds.parent(r_ctrl_name+ctrlgrp(), r_ctrl_name+ctrlgrp(1))
        cmds.group(n="tmp", em=True)
        cmds.parent(r_ctrl_name+ctrlgrp(1), "tmp")
        cmds.setAttr("tmp"+SCALE+"X", -1)
        cmds.parent(r_ctrl_name+ctrlgrp(1), w=True)
        cmds.delete("tmp")
        cmds.parentConstraint(r_parent, r_ctrl_name+ctrlgrp(1), mo=True)
        
        for lr in LFRT:
            ctrl_name = "FKIK_"+lr+"_"+part+str(num)
            for name in mid_names:
                cmds.connectAttr(ctrl_name+ctrlgrp()+".FKIK", "RIG_"+lr+name+str(num)+".spread")
 
 
#----------------------------------------------------------------------------#


def Setting_vis(part):
    if part == "Spine":
        end_num = 7
    elif part == "Neck":
        end_num = 4

    fk_grp = "FK_"+part+ctrlgrp(2)
    ik_grp = "IK_"+part+ctrlgrp(2)
    fkik_ctrl = "FKIK_"+part+ctrlgrp()

    cmds.connectAttr(fkik_ctrl+".FKIK", ik_grp+".visibility")
    reverse_attr("FKIK_"+part+"_Reverse", fkik_ctrl+".FKIK", fk_grp+".visibility")
    for num in range(1, end_num+1):
        cmds.connectAttr(fkik_ctrl+".FKIK", "IK_volume_"+part+str(num)+"_BlendColors.blender")
    cmds.parent("FKIK_"+part+ctrlgrp(1), "FKIK_ctrl_grp")


def Setting_vis_armleg(part):
    if part == "Arm":
        end_num = cmds.intField(arm, q=True, v=True)
    else:
        end_num = cmds.intField(leg, q=True, v=True)
    
    final_ctrl = cmds.group(n="FKIK_"+part+ctrlgrp(2), em=True)
    for lr in LFRT:
        mid_name = lr+"_"+part
        for num in range(1, end_num+1):
            fk_grp = joint_name(1,mid_name,num)+ctrlgrp(2)
            ik_grp = joint_name(2,mid_name,num)+ctrlgrp(1)
            pv_grp = "IK_PV_"+mid_name+str(num)+ctrlgrp(1)
            fkik_ctrl = "FKIK_"+mid_name+str(num)+ctrlgrp()

            cmds.connectAttr(fkik_ctrl+".FKIK", ik_grp+".visibility")
            cmds.connectAttr(fkik_ctrl+".FKIK", pv_grp+".visibility")
            reverse_attr("FKIK_"+mid_name+str(num)+"_Reverse", fkik_ctrl+".FKIK", fk_grp+".visibility")
            cmds.parent("FKIK_"+mid_name+str(num)+ctrlgrp(1), final_ctrl)
    cmds.parent(final_ctrl, "FKIK_ctrl_grp")

#----------------------------------------------------------------------------#


def duplicate_joints(type, body, dup_type, nb=1):
    num_arm = cmds.intField(arm, q=True, v=True)
    num_leg = cmds.intField(leg, q=True, v=True)
    arm_joints = ["L_Shoulder", "L_Elbow", "L_Wrist"]
    leg_joints = ["L_Hip", "L_Knee", "L_Ankle"]
   
    if body == "Spine":
        end_num = 7
    elif body == "Neck":
        end_num = 5
    else:
        end_num = nb+1
    if body in ["Spine", "Neck"]:
        for jnt_num in range(1, end_num+1):
            cmds.duplicate(joint_name(type,body,jnt_num), n=joint_name(dup_type,body,jnt_num), po=True)
            if jnt_num > 1:
                cmds.parent(joint_name(dup_type,body,jnt_num), joint_name(dup_type,body,jnt_num-1))
    else:
        cmds.duplicate(joint_name(type,body,nb))
        cmds.select(joint_name(type,body,end_num), hi=True)
        objs = pm.ls(sl=True)
        for idx, obj in enumerate(objs):
            if body == "L_Shoulder":
                obj.rename(joint_name(dup_type, arm_joints[idx], nb))
            elif body == "L_Hip":
                obj.rename(joint_name(dup_type, leg_joints[idx], nb))
            else:
                obj.rename(joint_name(dup_type,body,idx+1))


def spread(rig, fk, ik, tmp=0):
    cmds.select(rig, hi=True)
    rig_joints = cmds.ls(sl=True)
    cmds.select(fk, hi=True)
    fk_joints = cmds.ls(sl=True)
    cmds.select(ik, hi=True)
    ik_joints = cmds.ls(sl=True)
    
    spread_prepare(rig_joints, fk_joints, ik_joints, tmp)
    constraints = cmds.listRelatives(rig_joints, ad=True, typ='constraint')[::-1]
    attrs = cmds.listAttr(constraints, ud=True)

    cons_idx = 0
    for rig_jnt in rig_joints:
        attrs = cmds.listAttr(constraints[cons_idx], ud=True)
        rev_name = constraints[cons_idx]+"_"+attrs[0][:-2]+"_Reverse"
        reverse_attr(rev_name, rig_jnt+".spread", constraints[cons_idx]+"."+attrs[0])
        cmds.connectAttr(rig_jnt+".spread", constraints[cons_idx]+"."+attrs[1])
        cons_idx += 1


def spread_prepare(rig, fk, ik, tmp):
    for idx, value in enumerate(rig):
        cmds.parentConstraint(fk[idx], ik[idx], value)
        if not tmp:
            add_attrs(value)
            add_attrs(value, "spread", 2)


#----------------------------------------------------------------------------#


def fk_divide_ctrl(div_names):
    for div_name in div_names:
        cmds.shadingNode(MULDIV, n=div_name+"_Divide", au=True)
        if div_name == "FK_Pelvic":
            joint_mid = "Spine"
            num_lists = [1, 2, 3]
        elif div_name == "FK_Spine":
            joint_mid = "Spine"
            num_lists = [4, 5, 6]
        elif div_name == "FK_Neck":
            joint_mid = "Neck"
            num_lists = [1, 2, 3, 4]
            
        for axis in AXISES:
            cmds.setAttr(div_name+"_Divide.input2"+axis, len(num_lists))
        cmds.setAttr(div_name+"_Divide.operation", 2)
        cmds.connectAttr(div_name+ctrlgrp()+ROTATE, div_name+"_Divide.input1")
        for num in num_lists:
            cmds.connectAttr(div_name+"_Divide.output", joint_name(1, joint_mid, num)+ROTATE)


def fk_grouping(func, part, num_lists):
    if part == "Spine":
        parent_joint = "RIG_Root1"
        fk_ctrl = ["FK_Spine", "FK_Chest"]
        parent_lists = ["FK_Pelvic", "FK_Spine", "FK_Chest"]
    elif part == "Neck":
        parent_joint = "RIG_Spine7"
        fk_ctrl = ["FK_Head"]
        parent_lists = ["FK_Neck", "FK_Head"]
    elif part == "Head":
        parent_joint = "RIG_Neck5"
        parent_lists = ["FK_Jaw", "FK_L_Eye", "FK_R_Eye"]
        
    if func is not None:
        for num, value in enumerate(num_lists):
            grp_name = func(value)+ctrlgrp(2)
            grp = cmds.group(n=grp_name, em=True)
            match_objs(func(value+1), grp_name)
            cmds.parent(grp_name, func(value))
            cmds.parentConstraint(grp_name, fk_ctrl[num]+ctrlgrp(1), mo=True)
    final_grp = "FK_"+part+ctrlgrp(2)
    cmds.group(n=final_grp, em=True)
    match_objs(parent_joint, final_grp)
    for name in parent_lists:
        cmds.parent(name+ctrlgrp(1), final_grp)
    cmds.parentConstraint(parent_joint, final_grp, mo=True)
    cmds.parent(final_grp, "FK_grp")


#----------------------------------------------------------------------------#


def ArmLegFKIK(part):
    if part == "Arm":
        end_num = cmds.intField(arm, q=True, v=True)
    else:
        end_num = cmds.intField(leg, q=True, v=True)
        
    fk_armleg_ctrl(part)
    fk_armleg_grouping(part)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            ik_handle(part, lr, num)
            ik_handle_follow(part, lr, num)
            ik_pole_vector(part, lr, num)
            ik_pole_vector_follow(part, lr, num)
            ik_stretchy_armleg(part, lr, num)
    ik_grouping_armleg(part, end_num)


def fk_armleg_ctrl(part):
    def fk_armleg(body):
        return(joint_name(1,lr+body,num))
        
    if part == "Arm":
        bodies = ["_Shoulder", "_Elbow", "_Wrist"]
        end_num = cmds.intField(arm, q=True, v=True)
    else:
        bodies = ["_Hip", "_Knee", "_Ankle"]
        end_num = cmds.intField(leg, q=True, v=True)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            fk_top = fk_armleg(bodies[0])
            fk_mid = fk_armleg(bodies[1])
            fk_bottom = fk_armleg(bodies[2])
            
            for part in [fk_top, fk_mid, fk_bottom]:
                CtrlCreate(part, CIRCLE, 0, part, SKYBLUE)
                cmds.connectAttr(part+ctrlgrp()+SCALE, part+SCALE)
                cmds.scale(0.6, 0.6, 0.6, part+"_ctrl.cv[0:7]", r=True, ocp=True)
            cmds.parentConstraint(fk_mid+ctrlgrp(), fk_bottom+ctrlgrp(1), mo=True)
            cmds.parentConstraint(fk_top+ctrlgrp(), fk_mid+ctrlgrp(1), mo=True)


def fk_armleg_grouping(part):
    if part == "Arm":
        end_num = cmds.intField(arm, q=True, v=True)
        parent_lists = ["_Shoulder", "_Elbow", "_Wrist"]
        upper = "RIG_Spine7"
    else:
        end_num = cmds.intField(leg, q=True, v=True)
        parent_lists = ["_Hip", "_Knee", "_Ankle"]
        upper = "RIG_Pelvic1"
    
    part_grp = "FK_"+part+ctrlgrp(2)
    cmds.group(n=part_grp, em=True)
    match_objs(upper, part_grp)
    cmds.parent(part_grp, "FK_grp")
    cmds.parentConstraint(upper, part_grp)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            if part == "Arm":
                parent_joint = "RIG_"+lr+"_Scapula"+str(num)
            else:
                parent_joint = "RIG_"+lr+"_Hip"+str(num)
                
            final_grp = "FK_"+lr+"_"+part+str(num)+ctrlgrp(2)
            cmds.group(n=final_grp, em=True)
            match_objs(parent_joint, final_grp)
            
            for name in parent_lists:
                cmds.parent("FK_"+lr+name+str(num)+ctrlgrp(1), final_grp)
            cmds.parent(final_grp, part_grp)
            
            if part == "Arm":
                fk_upper = "FK_"+lr+"_Scapula"+str(num)
                cmds.parent(fk_upper+ctrlgrp(1), part_grp)
                cmds.parentConstraint(fk_upper+ctrlgrp(), final_grp)


#----------------------------------------------------------------------------#


def ik_spline_handle(func, part, end_num):
    handle = cmds.ikHandle(sj=func(1), ee=func(end_num), sol="ikSplineSolver", scv=False, pcv=False, ns=4)
    pm.ls(handle[2])[0].rename("IK_"+part+"_ikHandle_crv")
    cmds.delete(handle[0])
    cmds.select(func(1), hi=True)
    objs = cmds.ls(sl=True)
    for obj in objs:
        for axis in AXISES:
            cmds.setAttr(obj+ROTATE+axis, 0)
    cmds.ikHandle(sj=func(1), ee=func(end_num), c="IK_"+part+"_ikHandle_crv", n="IK_"+part+"_ikHandle", sol="ikSplineSolver", ccv=False, scv=False, pcv=False)
    

def ik_spline_handle_cluster(func, part, mid_num, end_num):
    clus_grp = "_cluster_grp"
    for num in range(end_num):
        if num == 0:
            crv_num = "0:1"
        elif num == end_num-1:
            crv_num = str(end_num)+":"+str(end_num+1)
        else:
            crv_num = str(num+1)
        cmds.select("IK_"+part+"_ikHandle_crv.cv["+crv_num+"]", r=True)
        cluster = cmds.cluster(n=joint_name(2,part,num+1)+"_cluster")
        grp = cmds.group(n=joint_name(2,part,num+1)+clus_grp,em=True)
        match_objs(func(num+1), grp)
        cmds.parent(cluster[1], grp)
        
    CtrlCreate(joint_name(2,part,1)+clus_grp, BOX, 0, func(1), RED, 1)
    CtrlCreate(joint_name(2,part,mid_num)+clus_grp, CIRCLE, 0, func(2), RED, 1)
    CtrlCreate(joint_name(2,part,end_num)+clus_grp, BOX, 0, func(3), RED, 1)


def ik_twist(part):
    if part == "Spine":
        ik_end = 7
    elif part == "Neck":
        ik_end = 5
    handle = "IK_"+part+"_ikHandle"
    top = "IK_"+part+"_top"
    bottom = "IK_"+part+"_bottom"
        
    cmds.duplicate(joint_name(2,part,1), n=bottom, po=True)
    cmds.duplicate(joint_name(2,part,ik_end), n=top, po=True)
    cmds.parent(top, w=True)
    cmds.setAttr(handle+".dTwistControlEnable", 1)
    cmds.setAttr(handle+".dWorldUpType", 4)
    cmds.setAttr(handle+".dForwardAxis", 0)
    cmds.setAttr(handle+".dWorldUpAxis", 3)
    cmds.setAttr(handle+".dWorldUpVectorX", 1)
    cmds.setAttr(handle+".dWorldUpVectorEndX", 1)
    for axis in ["Y", "Z"]:
        cmds.setAttr(handle+".dWorldUpVector"+axis, 0)
        cmds.setAttr(handle+".dWorldUpVectorEnd"+axis, 0)

    cmds.connectAttr(bottom+".worldMatrix[0]", handle+".dWorldUpMatrix", f=True)
    cmds.connectAttr(top+".worldMatrix[0]", handle+".dWorldUpMatrixEnd", f=True)
    cmds.parentConstraint(joint_name(2,part,1)+ctrlgrp(), bottom)
    cmds.parentConstraint(joint_name(2,part,3)+ctrlgrp(), top)
    cmds.setAttr(top+".visibility", 0)
    cmds.setAttr(bottom+".visibility", 0)


def ik_hybrid(part):
    def hybrid(num):
        return("IK_"+part+"_Hybrid"+str(num))
        
    if part == "Spine":
        range_num = [1, 4, 7]
    elif part == "Neck":
        range_num = [1, 3, 5]
    clus_grp = "_cluster_grp"
        
    for num, value in enumerate(range_num):
        CtrlCreate(joint_name(2,part,value)+clus_grp, DIA, 9, hybrid(num+1), PINK)
        if part == "Neck" and value == 2:
            cmds.parentConstraint("IK_Neck2"+clus_grp, "IK_Neck3"+clus_grp, hybrid(num+1)+ctrlgrp(1), n="tmp")
            cmds.delete("tmp")
            
    cmds.parent(hybrid(3)+ctrlgrp(1), hybrid(2)+ctrlgrp())
    cmds.parent(hybrid(2)+ctrlgrp(1), hybrid(1)+ctrlgrp())
    cmds.parentConstraint(hybrid(3)+ctrlgrp(), joint_name(2,part,3)+ctrlgrp(1), mo=True)
    add_attrs(joint_name(2,part,2)+ctrlgrp())
    add_attrs(joint_name(2,part,2)+ctrlgrp(), "IK_Hybrid_Vis", 2)
    cmds.connectAttr(joint_name(2,part,2)+ctrlgrp()+".IK_Hybrid_Vis", hybrid(1)+"_ctrl_grp.visibility")
    cmds.setAttr(joint_name(2,part,2)+ctrlgrp()+".IK_Hybrid_Vis", 1)


def ik_middle_follow(part):
    ik_mid = joint_name(2,part,2)+ctrlgrp()
    ik_mid_grp = joint_name(2,part,2)+ctrlgrp(1)
    follow_top = "IK_"+part+"_follow_top"
    follow_bottom = "IK_"+part+"_follow_bottom"
    add_attrs(ik_mid)
    add_attrs(ik_mid, "follow", 2, 5, 0, 10)

    for num in [1, 3]:
        name = follow_bottom if num == 1 else follow_top
        ctrl = joint_name(2,part,str(num))+ctrlgrp()
        grp = cmds.group(n=name, em=True)
        match_objs(ik_mid, grp)
        cmds.parent(name, ctrl+ctrlgrp(2))
        cmds.parentConstraint(ctrl, name, mo=True)

    cmds.parentConstraint(follow_top, follow_bottom, ik_mid_grp)
    cons_top = ik_mid_grp+"_parentConstraint1."+follow_top+"W0"
    cons_bottom = ik_mid_grp+"_parentConstraint1."+follow_bottom+"W1"
    follow_attr(ik_mid, cons_top, cons_bottom, 5)


def ik_stiff(part):
    if part == "Spine":
        end_num = 7
        num_lists = [2, 3, 5, 6]
        weights = [1, 0.05, 1, 0.3, 0.3, 1, 0.05, 1]
    elif part == "Neck":
        end_num = 5
        num_lists = [2, 4]
        weights = [1, 0.4, 0.4, 1]
        
    add_attrs(joint_name(2,part,3)+ctrlgrp(), "stiff", 2, 5, 0, 10)
    stiff_attr = joint_name(2,part,3)+ctrlgrp()+".stiff"
    
    for set_num in [10, 0]:
        cmds.setAttr(stiff_attr, set_num)
        idx = 0
        for num in num_lists:
            parent_grp = joint_name(2,part,num)+"_cluster_grp_parentConstraint1."
            attrs = cmds.listAttr(parent_grp, ud=True)
            if set_num == 0:
                cmds.setAttr(parent_grp+attrs[0], weights[idx])
                cmds.setAttr(parent_grp+attrs[1], weights[idx+1])
            cmds.setDrivenKeyframe(parent_grp+attrs[0], cd=stiff_attr)
            cmds.setDrivenKeyframe(parent_grp+attrs[1], cd=stiff_attr)
            idx += 2
    cmds.setAttr(stiff_attr, 5)
            

def ik_grouping(part):
    if part == "Spine":
        end_num = 7
        parent_joint = "RIG_Root1"
    elif part == "Neck":
        end_num = 5
        parent_joint = "RIG_Spine7"
    
    cluster_grp = cmds.group(n="IK_"+part+"_cluster_grp", em=True)
    for num in range(1, end_num+1):
        cmds.parent(joint_name(2,part,num)+"_cluster_grp", cluster_grp)
    cmds.parent(cluster_grp, "IK_cluster_ctrl_grp")
    
    handle_grp = cmds.group(n="IK_"+part+"_ikHandle_grp", em=True)
    cmds.parent("IK_"+part+"_ikHandle", "IK_"+part+"_ikHandle_crv", handle_grp)
    cmds.parent(handle_grp, "extra_grp")
    
    grouping_obj = [joint_name(2,part,1)+ctrlgrp(1),
                    joint_name(2,part,2)+ctrlgrp(1),
                    joint_name(2,part,3)+ctrlgrp(1),
                    "IK_"+part+"_Hybrid1_ctrl_grp",
                    "IK_"+part+"_bottom", "IK_"+part+"_top"]
    final_grp = "IK_"+part+ctrlgrp(2)
    
    cmds.group(n=final_grp, em=True)
    match_objs(parent_joint, final_grp)
    cmds.parent(grouping_obj, final_grp)
    cmds.parentConstraint(parent_joint, final_grp, mo=True)
    cmds.parent(final_grp, "IK_ctrl_grp")
    

#----------------------------------------------------------------------------#


def ik_stretchy(part):
    if part == "Spine":
        end_num = 7
    elif part == "Neck":
        end_num = 5
    add_attrs(joint_name(2,part,3)+ctrlgrp())
    add_attrs(joint_name(2,part,3)+ctrlgrp(), "stretch", 2, 0, 0, 10)
    
    ik_stretch_refresh(part, end_num)
    ik_stretch_info(part)
    IK_stretch_switch(part, end_num)
    ik_stretch_each_joints(part, end_num)
    ik_stretch_top(part, end_num)
    ik_stretch_grouping(part, end_num)
    

def ik_stretch_refresh(part, end_num):
    prepare_div = "IK_stretch_"+part+"_10into1_Divide"
    
    for num in range(1, end_num+1):
        cmds.delete(joint_name(0,part,num)+"_parentConstraint1*")
        
    for num in range(1, end_num+1):
        cmds.select(joint_name(2,part,num))
        obj = pm.ls(sl=True)[0]
        obj.rename(joint_name(3,part,num))
    duplicate_joints(3,part,2,1)
    duplicate_joints(3,part,4,1)
    spread(joint_name(0,part,1), joint_name(1,part,1), joint_name(2,part,1), 1)
    spread(joint_name(2,part,1), joint_name(3,part,1), joint_name(4,part,1))
    
    cmds.shadingNode(MULDIV, n=prepare_div, au=True)
    cmds.setAttr(prepare_div+".operation", 2)
    cmds.connectAttr(joint_name(2,part,3)+ctrlgrp()+".stretch", prepare_div+".input1X")
    cmds.setAttr(prepare_div+".input2X", 10)
    for num in range(1, end_num+1):
        cmds.connectAttr(prepare_div+".outputX", joint_name(2,part,num)+".spread")


def ik_stretch_info(part):
    crv_div = "IK_crv_"+part+"_Divide"
    world_div = "IK_world_"+part+"_Divide"
    crvinfo_div = "IK_crvinfo_all_"+part+"_Divide"
    
    if part == "Spine":
        crv_info = "curveInfo1"
    elif part == "Neck":
        crv_info = "curveInfo2"
        
    for div_name in [crv_div, world_div, crvinfo_div]:
        cmds.shadingNode(MULDIV, n=div_name, au=True)
        cmds.setAttr(div_name+".operation", 2)
    cmds.arclen("IK_"+part+"_ikHandle_crv", ch=1)
    cmds.connectAttr(crv_info+".arcLength", crv_div+".input1X")
    crvlen = cmds.getAttr(crv_div+".input1X")
    cmds.setAttr(crv_div+".input2X", crvlen)
    cmds.connectAttr("World_ctrl.scale", world_div+".input1")
    cmds.connectAttr(crv_div+".outputX", crvinfo_div+".input1X")
    cmds.connectAttr(world_div+".outputX", crvinfo_div+".input2X")


def IK_stretch_switch(part, end_num):
    def stretch_div(part, num):
        return("IK_stretch_"+part+str(num)+"_Divide")
    def blend_two(part, num):
        return("IK_stretch_"+part+str(num)+"_BlendTwo")

    crvinfo_div = "IK_crvinfo_all_"+part+"_Divide"
    prepare_div = "IK_stretch_"+part+"_10into1_Divide"
        
    for num in range(1, end_num):
        transX = cmds.getAttr(joint_name(3,part,num)+TRANSLATE+"X")
        cmds.shadingNode(MULDIV, n=stretch_div(part,num), au=True)
        cmds.setAttr(stretch_div(part,num)+".input1X", transX)
        cmds.connectAttr(crvinfo_div+".outputX", stretch_div(part,num)+".input2X")
        
        cmds.shadingNode(BLENDTWO, n=blend_two(part,num), au=True)
        cmds.setAttr(blend_two(part,num)+".input[0]", transX)
        cmds.connectAttr(stretch_div(part,num)+".outputX", blend_two(part,num)+".input[1]")
        cmds.connectAttr(prepare_div+".outputX", blend_two(part,num)+".attributesBlender")
        cmds.connectAttr(blend_two(part,num)+".output", joint_name(3,part,num)+TRANSLATE+"X")
        
    
def ik_stretch_each_joints(part, end_num):
    for num in range(1, end_num+1):
        grp = cmds.group(n=joint_name(4,part,num)+"_aim_grp", em=True)
        match_objs(joint_name(2,part,num)+"_cluster_grp", grp)
        cmds.pointConstraint(joint_name(2,part,num)+"_cluster_grp", grp)
        cmds.pointConstraint(grp, joint_name(4,part,num))
    for num in range(2, end_num+1):
        cmds.parent(joint_name(4,part,num), w=True)
    for num in range(end_num-1, 0, -1):
        aim_cons = joint_name(4,part,num)+"_aimConstraint1"
        cmds.aimConstraint(joint_name(4,part,num+1), joint_name(4,part,num))
        cmds.connectAttr(joint_name(3,part,num)+ROTATE+"X", aim_cons+".offsetX")
        cmds.setAttr(aim_cons+".worldUpType", 2)
        for nb, value in enumerate(["Y", "Z"]):
            cmds.setAttr(aim_cons+".upVector"+value, nb)
            cmds.setAttr(aim_cons+".worldUpVector"+value, nb)
        if num > 1:
            cmds.connectAttr(joint_name(4,part,num-1)+".worldMatrix[0]", aim_cons+".worldUpMatrix")
            
    fake = "IK_fake_"+part+"1"
    cmds.duplicate(joint_name(3,part,1), n=fake, po=True)
    cmds.parentConstraint(joint_name(3,part,1), fake)
    cmds.connectAttr(fake+".worldMatrix[0]", aim_cons+".worldUpMatrix")
    

def ik_stretch_top(part, end_num):
    for num in range(1, 4):
        orient_grp = cmds.group(n=joint_name(2,part,num)+"_orient1", em=True)
        match_objs(joint_name(2,part,num)+"_ctrl", orient_grp)
        cmds.parent(orient_grp, joint_name(2,part,num)+"_ctrl")
        cmds.duplicate(orient_grp)
        cmds.parent(joint_name(2,part,num)+"_orient2", orient_grp)
    
    cmds.delete(joint_name(2,part,end_num)+"_parentConstraint1*")
    cmds.orientConstraint(joint_name(2,part,3)+"_orient2", joint_name(2,part,end_num), mo=True)
    cmds.pointConstraint(joint_name(3,part,end_num), joint_name(4,part,end_num), joint_name(2,part,end_num), mo=True)
    cmds.connectAttr(joint_name(2,part,end_num)+".spread", joint_name(2,part,end_num)+"_pointConstraint1."+joint_name(4,part,end_num)+"W1")
    reverse_attr("IK_stretch_"+part+"_reverse", joint_name(2,part,end_num)+".spread", joint_name(2,part,end_num)+"_pointConstraint1."+joint_name(3,part,end_num)+"W0")
    

def ik_stretch_grouping(part, end_num):
    stretch_grp = "IK_stretch_"+part+"_jnt_grp"
    aim_grp = "IK_stretch_"+part+"_aim_grp"
    
    cmds.group(n=stretch_grp, em=True)
    cmds.group(n=aim_grp, em=True)
    cmds.parent("IK_fake_"+part+"1", stretch_grp)
    cmds.parent(joint_name(3,part,1), stretch_grp)
    for num in range(1, end_num+1):
        cmds.parent(joint_name(4,part,num), stretch_grp)
        cmds.parent(joint_name(4,part,num)+"_aim_grp", aim_grp)
    cmds.parent(stretch_grp, "IK_jnt_grp")
    cmds.parent(aim_grp, "IK_spline_ctrl_grp")


#----------------------------------------------------------------------------#


def ik_volume(part):
    prepare_stretch_div = "IK_stretch_"+part+"_10into1_Divide"
    prepare_volume_div = "IK_volume_"+part+"_10into1_Divide"
    crvinfo_div = "IK_crvinfo_all_"+part+"_Divide"
    obj_ctrl = joint_name(2,part,3)+ctrlgrp()
    mul_stretch = "IK_volume_mul_stretch_"+part+"_Multiply"
    vol_div = "IK_volume_"+part+"_Divide"
    vol_pow = "IK_volume_"+part+"_POWER"
    vol_blend = "IK_volume_"+part+"_BlendTwo"
    
    if part == "Spine":
        end_num = 7
        weights = [[1,0,0],[0.75,0.25,0],[0.25,0.75,0],[0,1,0],
                    [0,0.75,0.25],[0,0.25,0.75],[0,0,1]]
        scaler_weight = [0.5, 0.75, 1, 0.75, 0.5]
    elif part == "Neck":
        end_num = 5
        weights = [[1,0,0],[0.5,0.5,0],[0,1,0],[0,0.5,0.5],[0,0,1]]
        scaler_weight = [0.5, 1, 0.5]

    add_attrs(obj_ctrl, "volume", 2, 0, 0, 10)
    
    for vol_name in [prepare_volume_div, mul_stretch, vol_div, vol_pow]:
        cmds.shadingNode(MULDIV, n=vol_name, au=True)
    cmds.shadingNode(BLENDTWO, n=vol_blend, au=True)
    
    cmds.setAttr(prepare_volume_div+".operation", 2)
    cmds.connectAttr(obj_ctrl+".volume", prepare_volume_div+".input1X")
    cmds.setAttr(prepare_volume_div+".input2X", 10)
    cmds.connectAttr(prepare_volume_div+".outputX", mul_stretch+".input1X")
    cmds.connectAttr(prepare_stretch_div+".outputX", mul_stretch+".input2X")
    cmds.connectAttr(mul_stretch+".outputX", vol_blend+".attributesBlender")
    
    cmds.setAttr(vol_div+".operation", 2)
    cmds.setAttr(vol_div+".input1X", 1)
    cmds.connectAttr(crvinfo_div+".outputX", vol_div+".input2X")
    cmds.connectAttr(vol_div+".outputX", vol_pow+".input1X")
    
    cmds.setAttr(vol_pow+".operation", 3)
    cmds.setAttr(vol_pow+".input2X", 0.5)
    cmds.connectAttr(vol_pow+".outputX", vol_blend+".input[1]")
    cmds.setAttr(vol_blend+".input[0]", 1)
    
    ik_volume_scaler(part, end_num, weights)
    ik_volume_each_joints(part, end_num, scaler_weight)
    ik_volume_grouping(part, end_num)
        

def ik_volume_scaler(part, end_num, weights):
    def vol_sum(jnt_num, num):
        return("IK_volume_"+part+str(jnt_num)+"_Sum"+str(num))
    def vol_mul(jnt_num, num):
        return("IK_volume_"+part+str(jnt_num)+"_Multiply"+str(num))
    def vol_bc(jnt_num):
        return("IK_volume_"+part+str(jnt_num)+"_BlendColors")
    
    for num in range(1,end_num+1):
        for idx in range(1, 3):
            cmds.shadingNode(PLUSMIN, n=vol_sum(num,idx), au=True)
            cmds.shadingNode(MULDIV, n=vol_mul(num,idx), au=True)
        cmds.shadingNode(BLENDCOLORS, n=vol_bc(num), au=True)
        scaler = "IK_scaler_"+part+str(num)+"_grp"
        cmds.group(n=scaler, em=True)
        cmds.scaleConstraint(joint_name(2,part,1)+"_orient2",
                            joint_name(2,part,2)+"_orient2",
                            joint_name(2,part,3)+"_orient2",
                            scaler)
        for idx in range(3):
            cmds.setAttr(scaler+"_scaleConstraint1."+joint_name(2,part,idx+1)+"_orient2W"+str(idx), weights[num-1][idx])
    
    
def ik_volume_each_joints(part, end_num, scaler_weight):
    def vol_sum(jnt_num, num):
        return("IK_volume_"+part+str(jnt_num)+"_Sum"+str(num))
    def vol_mul(jnt_num, num):
        return("IK_volume_"+part+str(jnt_num)+"_Multiply"+str(num))
    def vol_bc(jnt_num):
        return("IK_volume_"+part+str(jnt_num)+"_BlendColors")
        
    vol_blend = "IK_volume_"+part+"_BlendTwo"
        
    for num in range(2, end_num):
        cmds.connectAttr(vol_blend+".output", vol_sum(num,1)+".input1D[0]")
        cmds.setAttr(vol_sum(num,1)+".input1D[1]", -1)
        cmds.connectAttr(vol_sum(num, 1)+".output1D", vol_mul(num, 1)+".input1X")
        cmds.setAttr(vol_mul(num,1)+".input2X", scaler_weight[num-2])
        cmds.connectAttr(vol_mul(num, 1)+".outputX", vol_sum(num, 2)+".input1D[0]")
        cmds.setAttr(vol_sum(num,2)+".input1D[1]", 1)
        for axis in AXISES:
            cmds.connectAttr(vol_sum(num,2)+".output1D", vol_mul(num, 2)+".input2"+axis)
        cmds.connectAttr("IK_scaler_"+part+str(num)+"_grp"+SCALE, vol_mul(num,2)+".input1")
        cmds.connectAttr(vol_mul(num,2)+".output", vol_bc(num)+".color1")
        cmds.connectAttr(joint_name(1,part,num)+SCALE, vol_bc(num)+".color2")
        cmds.connectAttr(vol_bc(num)+".output", joint_name(0,part,num)+SCALE)
        
    for num in [1, end_num]:
        cmds.connectAttr("IK_scaler_"+part+str(num)+"_grp"+SCALE, vol_bc(num)+".color1")
        cmds.connectAttr(joint_name(1,part,num)+SCALE, vol_bc(num)+".color2")
        cmds.connectAttr(vol_bc(num)+".output", joint_name(0,part,num)+SCALE)
            

def ik_volume_grouping(part, end_num):
    scaler_grp = "IK_volume_"+part+ctrlgrp(2)
    cmds.group(n=scaler_grp, em=True)
    for num in range(1, end_num+1):
        cmds.parent("IK_scaler_"+part+str(num)+"_grp", scaler_grp)
    cmds.parent(scaler_grp, "IK_spline_ctrl_grp")
        

#----------------------------------------------------------------------------#


def ik_handle(part, lr, num):
    def ik_armleg(body):
        return(joint_name(2,lr+body,num))
        
    if part == "Arm":
        bodies = ["_Shoulder", "_Elbow", "_Wrist"]
    elif part == "Leg":
        bodies = ["_Hip", "_Knee", "_Ankle"]

    ik_top = ik_armleg(bodies[0])+ctrlgrp(2)
    ik_bottom = ik_armleg(bodies[2])+ctrlgrp(2)
    ik_ctrl = ik_armleg("_"+part)
    ik_handle_grp = "IK_"+part+"_ikHandle"
    
    for body in bodies:
        cmds.duplicate(ik_armleg(body), n=ik_armleg(body)+ctrlgrp(2), po=True)
        match_objs(ik_armleg(body), ik_armleg(body)+ctrlgrp(2))
        cmds.parent(ik_armleg(body), ik_armleg(body)+ctrlgrp(2))
        
    cmds.parent(ik_armleg(bodies[2])+ctrlgrp(2), ik_armleg(bodies[1])+ctrlgrp(2))
    cmds.parent(ik_armleg(bodies[1])+ctrlgrp(2), ik_armleg(bodies[0])+ctrlgrp(2))

    cmds.ikHandle(sj=ik_top, ee=ik_bottom, n=ik_ctrl+"_ikHandle")
    CtrlCreate(ik_ctrl+"_ikHandle", BOX, 9, ik_ctrl, RED, 1)
    cmds.setAttr(ik_ctrl+ctrlgrp()+SCALE+"Y", 0.3)
    cmds.setAttr(ik_ctrl+ctrlgrp()+SCALE+"Z", 0.3)
    cmds.select(ik_ctrl+ctrlgrp())
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.scale(2, 2, 2, ik_ctrl+ctrlgrp())
    cmds.makeIdentity(a=True, t=1, r=1, s=1, n=0, pn=1)

    cmds.parentConstraint(ik_ctrl+ctrlgrp(), ik_ctrl+"_ikHandle", mo=True)


def ik_handle_follow(part, lr, num):
    if part == "Arm":
        ik_joint = "RIG_"+lr+"_Scapula"+str(num)
    elif part == "Leg":
        ik_joint = "RIG_Pelvic1"
        
    ik_ctrl = "IK_"+lr+"_"+part+str(num)+ctrlgrp()
    follow_on = ik_ctrl+"_follow_on"
    follow_off = ik_ctrl+"_follow_off"
    
    add_attrs(ik_ctrl)
    add_attrs(ik_ctrl, "follow", 2, 0, 0, 10)
    
    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(ik_ctrl, grp_name)
    cmds.group(n=follow_on+ctrlgrp(2), em=True)
    match_objs(ik_joint, follow_on+ctrlgrp(2))
    cmds.parentConstraint(ik_joint, follow_on+ctrlgrp(2), mo=True)
    cmds.parent(follow_on, follow_on+ctrlgrp(2))

    cmds.parent(follow_on+ctrlgrp(2), "IK_follow_ctrl_grp")
    cmds.parent(follow_off, "IK_static_ctrl_grp")
    cmds.parentConstraint(follow_on, follow_off, ik_ctrl+ctrlgrp(2))

    attr_follow_on = ik_ctrl+ctrlgrp(2)+"_parentConstraint1."+follow_on+"W0"
    attr_follow_off = ik_ctrl+ctrlgrp(2)+"_parentConstraint1."+follow_off+"W1"
    follow_attr(ik_ctrl, attr_follow_on, attr_follow_off, 0)


def ik_pole_vector(part, lr, num):
    if part == "Arm":
        bodies = ["_Shoulder", "_Elbow", "_Wrist"]
    elif part == "Leg":
        bodies = ["_Hip", "_Knee", "_Ankle"]
    
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    ik_mid = "IK_"+lr+bodies[1]+str(num)
    pole_vector = "IK_PV_"+lr+"_"+part+str(num)
    ik_handle_name = "IK_"+lr+"_"+part+str(num)+"_ikHandle"
    
    CtrlCreate(ik_mid, DIAMOND, 9, pole_vector, RED)
    attr_num = cmds.getAttr(pole_vector+ctrlgrp(1)+TRANSLATE+"Z")
    if part == "Arm":
        attr_num -= 2*world_scale
    else:
        attr_num += 2*world_scale
    cmds.setAttr(pole_vector+ctrlgrp(1)+TRANSLATE+"Z", attr_num)
    cmds.makeIdentity(pole_vector+ctrlgrp(1), a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.poleVectorConstraint(pole_vector+ctrlgrp(), ik_handle_name)
    
    
def ik_pole_vector_follow(part, lr, num):
    if part == "Arm":
        ik_joint = lr+"_Wrist"
    elif part == "Leg":
        ik_joint = lr+"_Ankle"

    ik_ctrl = "IK_"+lr+"_"+part+str(num)+ctrlgrp()
    pole_vector = "IK_PV_"+lr+"_"+part+str(num)
    follow_on = pole_vector+"_follow_on"
    follow_off = pole_vector+"_follow_off"
    
    add_attrs(pole_vector+ctrlgrp())
    add_attrs(pole_vector+ctrlgrp(), "follow", 2, 0, 0, 10)
    
    orient_grp = cmds.group(n=ik_ctrl+"_orient1", em=True)
    match_objs(joint_name(2,ik_joint,num), orient_grp)
    cmds.parent(orient_grp, ik_ctrl)
    cmds.duplicate(orient_grp)
    cmds.parent(ik_ctrl+"_orient2", orient_grp)
    
    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(pole_vector+ctrlgrp(), grp_name)
    cmds.group(n=follow_on+ctrlgrp(2), em=True)
    match_objs(joint_name(2,ik_joint,num), follow_on+ctrlgrp(2))
    cmds.parent(follow_on, follow_on+ctrlgrp(2))
    
    cmds.parentConstraint(ik_ctrl+"_orient2", follow_on+ctrlgrp(2), mo=True)
    cmds.parent(follow_on+ctrlgrp(2), "IK_follow_ctrl_grp")
    cmds.parent(follow_off, "IK_static_ctrl_grp")
    cmds.parentConstraint(follow_on, follow_off, pole_vector+ctrlgrp(1))
    
    attr_follow_on = pole_vector+ctrlgrp(1)+"_parentConstraint1."+follow_on+"W0"
    attr_follow_off = pole_vector+ctrlgrp(1)+"_parentConstraint1."+follow_off+"W1"
    follow_attr(pole_vector+ctrlgrp(), attr_follow_on, attr_follow_off, 0)


#----------------------------------------------------------------------------#


def ik_stretchy_armleg(part, lr, num):
    def stretch_name(type):
        return(joint_name(type,lr+"_"+part,num))
        
    if part == "Arm":
        ik_joints = [lr+"_Shoulder", lr+"_Elbow", lr+"_Wrist"]
    elif part == "Leg":
        ik_joints = [lr+"_Hip", lr+"_Knee", lr+"_Ankle"]
        
    ik_ctrl = stretch_name(2)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    stretch_distance = [stretch_name(4)+"_distance",
                        stretch_name(5)+"_pv_top_distance",
                        stretch_name(5)+"_top_mid_distance",
                        stretch_name(5)+"_pv_bottom_distance",
                        stretch_name(5)+"_mid_bottom_distance"]
    
    prepare_div = stretch_name(4)+"_Divide"
    messure_div = stretch_name(4)+"_messure_Divide"
    stretch_blendtwo = stretch_name(4)+"_BlendTwo"
    
    add_attrs(ik_ctrl)
    add_attrs(ik_ctrl, "stretch", 2, 0, 0, 10)
    add_attrs(ik_ctrl, "length_top", 1, 1)
    add_attrs(ik_ctrl, "length_bottom", 1, 1)
    add_attrs(pole_vector_ctrl, "lock", 2)
    
    ik_stretchy_armleg_distance(part, lr, num, ik_joints, stretch_name)
    ik_stretchy_armleg_node(part, lr, num, ik_joints, stretch_name(4))
    
    tmp_num = 1 if lr == "L" else -1
    all_length = cmds.getAttr(stretch_distance[0]+"Shape.distance") * tmp_num
    top_length = cmds.getAttr(stretch_distance[2]+"Shape.distance") * tmp_num
    bottom_length = cmds.getAttr(stretch_distance[4]+"Shape.distance") * tmp_num

    cmds.connectAttr(ik_ctrl+".stretch", prepare_div+".input1X")
    cmds.setAttr(prepare_div+".input2X", 10)
    cmds.connectAttr(prepare_div+".outputX", stretch_blendtwo+".attributesBlender")
    cmds.setAttr(stretch_blendtwo+".input[0]", all_length)
    cmds.connectAttr(stretch_distance[0]+"Shape.distance", stretch_blendtwo+".input[1]")
    cmds.connectAttr(stretch_blendtwo+".output", messure_div+".input1X")
    cmds.setAttr(messure_div+".input2X", all_length)

    ik_stretchy_armleg_lock(part, lr, num,
                            "top", top_length, ik_joints, stretch_name)
    ik_stretchy_armleg_lock(part, lr, num,
                            "bottom", bottom_length, ik_joints, stretch_name)
    
    cmds.orientConstraint(ik_ctrl+"_orient2", joint_name(2,ik_joints[2],num)+ctrlgrp(2), mo=True)
    cmds.connectAttr(ik_ctrl+SCALE, joint_name(2,ik_joints[2],num)+ctrlgrp(2)+SCALE)
    

def ik_stretchy_armleg_distance(part, lr, num, ik_joints, stretch_name):
    ik_top = joint_name(2,ik_joints[0],num)+ctrlgrp(2)
    ik_mid = joint_name(2,ik_joints[1],num)+ctrlgrp(2)
    ik_ctrl = joint_name(2,lr+"_"+part,num)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    stretch_loc = [stretch_name(4)+"_top_loc", stretch_name(4)+"_bottom_loc",
                    stretch_name(5)+"_pv_loc", stretch_name(4)+"_mid_loc"]
    stretch_distance = [stretch_name(4)+"_distance",
                        stretch_name(5)+"_pv_top_distance",
                        stretch_name(5)+"_top_mid_distance",
                        stretch_name(5)+"_pv_bottom_distance",
                        stretch_name(5)+"_mid_bottom_distance"]
    
    tmp = cmds.group(em=True)
    match_objs(ik_top, tmp)
    top_trans = cmds.getAttr(tmp+TRANSLATE)[0]
    match_objs(ik_mid, tmp)
    mid_trans = cmds.getAttr(tmp+TRANSLATE)[0]
    match_objs(ik_ctrl, tmp)
    ik_ctrl_trans = cmds.getAttr(tmp+TRANSLATE)[0]
    match_objs(pole_vector_ctrl, tmp)
    pv_ctrl_trans = cmds.getAttr(tmp+TRANSLATE)[0]
    cmds.delete(tmp)
    
    cmds.distanceDimension(sp=top_trans, ep=ik_ctrl_trans)
    cmds.select("locator1", "locator2")
    objs = pm.ls(sl=True)
    for idx, obj in enumerate(objs):
        obj.rename(stretch_loc[idx])
    cmds.parentConstraint(ik_top, stretch_loc[0])
    cmds.parentConstraint(ik_ctrl, stretch_loc[1])
    cmds.select("distanceDimension1")
    pm.ls(sl=True)[0].rename(stretch_distance[0])

    cmds.distanceDimension(sp=top_trans, ep=pv_ctrl_trans)
    cmds.select("locator1")
    pm.ls(sl=True)[0].rename(stretch_loc[2])
    cmds.parentConstraint(pole_vector_ctrl, stretch_loc[2])
    cmds.select("distanceDimension1")
    pm.ls(sl=True)[0].rename(stretch_distance[1])

    cmds.distanceDimension(sp=top_trans, ep=mid_trans)
    cmds.select("locator1")
    pm.ls(sl=True)[0].rename(stretch_loc[3])
    cmds.parentConstraint(ik_mid, stretch_loc[3])
    cmds.select("distanceDimension1")
    pm.ls(sl=True)[0].rename(stretch_distance[2])
    
    cmds.distanceDimension(sp=pv_ctrl_trans, ep=ik_ctrl_trans)
    cmds.distanceDimension(sp=mid_trans, ep=ik_ctrl_trans)
    for idx in range(2):
        cmds.select("distanceDimension"+str(idx+1))
        pm.ls(sl=True)[0].rename(stretch_distance[idx+3])
        
    mid_name = lr+"_"+part+str(num)
    messure_grp = joint_name(4,lr+"_"+part,num)+"_messure_grp"
    cmds.group(n=messure_grp, em=True)
    for name in ["*loc", "*distance"]:
        cmds.select("*"+mid_name+name)
        select_objs = cmds.ls(sl=True)
        cmds.parent(select_objs, messure_grp)
    cmds.parent(messure_grp, "IK_messure_ctrl_grp")


def ik_stretchy_armleg_node(part, lr, num, ik_joints, stretch_name):
    prepare_div = stretch_name+"_Divide"
    messure_div = stretch_name+"_messure_Divide"
    stretch_blendtwo = stretch_name+"_BlendTwo"
    
    messure_top_mul = joint_name(4,ik_joints[1],num)+"_messure_top_Multiply"
    stretch_top_mul = joint_name(4,ik_joints[1],num)+"_top_Multiply"
    lock_top_div = joint_name(5,ik_joints[1],num)+"_messure_top_Divide"
    lock_top_blendtwo = joint_name(5,ik_joints[1],num)+"_top_BlendTwo"
    
    messure_bottom_mul = joint_name(4,ik_joints[2],num)+"_messure_bottom_Multiply"
    stretch_bottom_mul = joint_name(4,ik_joints[2],num)+"_bottom_Multiply"
    lock_bottom_div = joint_name(5,ik_joints[2],num)+"_messure_bottom_Divide"
    lock_bottom_blendtwo = joint_name(5,ik_joints[2],num)+"_bottom_BlendTwo"
    
    for div_name in [prepare_div, messure_div,
                    messure_top_mul, stretch_top_mul, lock_top_div,
                    messure_bottom_mul, stretch_bottom_mul, lock_bottom_div]:
        cmds.shadingNode(MULDIV, n=div_name, au=True)
    for div_name in [prepare_div, messure_div, lock_top_div, lock_bottom_div]:
        cmds.setAttr(div_name+".operation", 2)
        
    for div_name in [stretch_blendtwo, lock_top_blendtwo, lock_bottom_blendtwo]:
        cmds.shadingNode(BLENDTWO, n=div_name, au=True)


def ik_stretchy_armleg_lock(part, lr, num,
                            position, length, ik_joints, stretch_name):
    ik_ctrl = stretch_name(2)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    messure_div = stretch_name(4)+"_messure_Divide"
    length_attr = ".length_"+position
    
    if position == "top":
        messure_mul = joint_name(4,ik_joints[1],num)+"_messure_top_Multiply"
        stretch_mul = joint_name(4,ik_joints[1],num)+"_top_Multiply"
        lock_div = joint_name(5,ik_joints[1],num)+"_messure_top_Divide"
        lock_blendtwo = joint_name(5,ik_joints[1],num)+"_top_BlendTwo"
        stretch_distance = stretch_name(5)+"_pv_top_distance"
        ik_joint = ik_joints[1]
    else:
        messure_mul = joint_name(4,ik_joints[2],num)+"_messure_bottom_Multiply"
        stretch_mul = joint_name(4,ik_joints[2],num)+"_bottom_Multiply"
        lock_div = joint_name(5,ik_joints[2],num)+"_messure_bottom_Divide"
        lock_blendtwo = joint_name(5,ik_joints[2],num)+"_bottom_BlendTwo"
        stretch_distance = stretch_name(5)+"_pv_bottom_distance"
        ik_joint = ik_joints[2]
        
    cmds.connectAttr(messure_div+".outputX", stretch_mul+".input1X")
    cmds.connectAttr(ik_ctrl+length_attr, messure_mul+".input1X")
    cmds.setAttr(messure_mul+".input2X", length)
    cmds.connectAttr(messure_mul+".outputX", stretch_mul+".input2X")
    cmds.connectAttr(stretch_mul+".outputX", lock_blendtwo+".input[0]")
    
    cmds.connectAttr(pole_vector_ctrl+".lock", lock_blendtwo+".attributesBlender")
    cmds.connectAttr(stretch_distance+"Shape.distance", lock_div+".input1X")
    cmds.connectAttr("World_ctrl.scaleX", lock_div+".input2X")
    cmds.connectAttr(lock_div+".outputX", lock_blendtwo+".input[1]")
    cmds.connectAttr(lock_blendtwo+".output", joint_name(2,ik_joint,num)+ctrlgrp(2)+TRANSLATE+"X")


#----------------------------------------------------------------------------#


def ik_grouping_armleg(part, end_num):
    if part == "Arm":
        lower = "_Shoulder"
    else:
        lower = "_Hip"
        
    handle_grp = "IK_"+part+"_ikHandle"+ctrlgrp(2)
    ctrl_grp = "IK_"+part+ctrlgrp(2)
    pv_grp = "IK_PV_"+part+ctrlgrp(2)
    
    for grp_name in [handle_grp, ctrl_grp, pv_grp]:
        cmds.group(n=grp_name, em=True)
    for lr in LFRT:
        for num in range(1, end_num+1):
            if part == "Arm":
                upper = joint_name(0,lr+"_Scapula",num)
            else:
                upper = "RIG_Pelvic1"
            
            cmds.parent(joint_name(2,lr+"_"+part,num)+"_ikHandle", handle_grp)
            cmds.parent(joint_name(2,lr+"_"+part,num)+ctrlgrp(1), ctrl_grp)
            cmds.parent("IK_PV_"+lr+"_"+part+str(num)+ctrlgrp(1), pv_grp)
            cmds.parent(joint_name(0,lr+lower,num), upper)
            cmds.parent(joint_name(1,lr+lower,num), upper)
            cmds.parent(joint_name(2,lr+lower,num)+ctrlgrp(2), upper)
            
    cmds.parent(handle_grp, "extra_grp")
    cmds.parent(ctrl_grp, pv_grp, "IK_ctrl_grp")


#----------------------------------------------------------------------------#


def CtrlCreate(obj_name, shape, idx, ctrl_name, ctrl_color, ik_identity=0):
    obj = cmds.ls(obj_name)
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    if shape == CIRCLE:
        c = cmds.circle(nr=(1,0,0))[0]
    elif shape == SQUARE:
        c = cmds.curve(d=1, p=[(0,1,1),(0,1,-1),(0,-1,-1),(0,-1,1),(0,1,1)])
    elif shape == ARROW1:
        tmp1 = cmds.curve(d=1, p=[(-1,0,-7),(1,0,-7),(1,0,-8),(2,0,-8),(0,0,-10),(-2,0,-8),(-1,0,-8),(-1,0,-7)])
        tmp2 = cmds.curve(d=1, p=[(-7,0,-1),(-7,0,1),(-8,0,1),(-8,0,2),(-10,0,0),(-8,0,-2),(-8,0,-1),(-7,0,-1)])
        tmp3 = cmds.curve(d=1, p=[(-1,0,7),(1,0,7),(1,0,8),(2,0,8),(0,0,10),(-2,0,8),(-1,0,8),(-1,0,7)])
        tmp4 = cmds.curve(d=1, p=[(7,0,1),(8,0,1),(8,0,2),(10,0,0),(8,0,-2),(8,0,-1),(7,0,-1),(7,0,1)])
        for tmp_name in [tmp1, tmp2, tmp3, tmp4]:
            cmds.scale(0.2, 0.2, 0.2, tmp_name)
            cmds.makeIdentity(tmp_name, a=True, t=1, r=1, s=1, n=0, pn=1)
        sh2 = cmds.listRelatives(tmp2, ad=True)[0]
        sh3 = cmds.listRelatives(tmp3, ad=True)[0]
        sh4 = cmds.listRelatives(tmp4, ad=True)[0]
        for sh_name in [sh2, sh3, sh4]:
            cmds.parent(sh_name, tmp1, r=True, s=True)
        cmds.delete(cmds.ls(tmp2), cmds.ls(tmp3), cmds.ls(tmp4))
        c = tmp1
    elif shape == ARROW4:
        c = cmds.curve(d=1, p=[(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)])
        cmds.scale(0.08, 0.08, 0.08, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == DIA:
        c = cmds.curve(d=1, p=[(-1,0,-2),(0,0,-3),(1,0,-2),(2,0,-2),(2,0,-1),(3,0,0),(2,0,1),(2,0,2),(1,0,2),(0,0,3),(-1,0,2),(-2,0,2),(-2,0,1),(-3,0,0),(-2,0,-1),(-2,0,-2),(-1,0,-2)])
        cmds.setAttr(c+ROTATE+"Z", 90)
        cmds.scale(0.3, 0.3, 0.3, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == BOX:
        c = cmds.curve(d=1, p=[(1,1,1),(1,-1,1), (1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1)])
        cmds.setAttr(c+SCALE+"X", 0.3)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == BALL:
        tmp1 = cmds.circle(nr=(1,0,0))
        tmp2 = cmds.circle(nr=(0,1,0))
        tmp3 = cmds.circle(nr=(0,0,1))
        sh2 = cmds.listRelatives(tmp2[0], ad=True)[0]
        sh3 = cmds.listRelatives(tmp3[0], ad=True)[0]
        cmds.parent(sh2, tmp1[0], r=True, s=True)
        cmds.parent(sh3, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp2), cmds.ls(tmp3))
        c = cmds.ls(tmp1)[0]
        cmds.scale(0.5, 0.5, 0.5, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == DIAMOND:
        c = cmds.curve(d=1, p=[(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(0,1,0),(-1,0,0),(1,0,0),(0,-1,0),(-1,0,0),(0,0,-1),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(0,0,1),(-1,0,0)])
        cmds.scale(0.5, 0.5, 0.5, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == FKIK_CROSS:
        c = cmds.curve(d=1, p=[(-0.5,0,-1.5),(0.5,0,-1.5),(0.5,0,-0.5),(1.5,0,-0.5),(1.5,0,0.5),(0.5,0,0.5),(0.5,0,1.5),(-0.5,0,1.5),(-0.5,0,0.5),(-1.5,0,0.5),(-1.5,0,-0.5),(-0.5,0,-0.5),(-0.5,0,-1.5)])
        cmds.scale(0.15, 0.15, 0.15, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == CROSS:
        c = cmds.curve(d=1, p=[(0,0,-1),(0,0,1),(0,0,0),(-1,0,0),(1,0,0)])
        cmds.setAttr(c+ROTATE+"Y", 90)
        cmds.scale(0.3, 0.3, 0.3, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif shape == EYE:
        tmp1 = cmds.circle(nr=(0,1,0))
        tmp2 = cmds.curve(d=3, p=[(-2.05541,0,-0.0124173),(-1.365656,0,-0.507243),(0.0138526,0,-1.496896),(1.337951,0,-0.498965),(2,0,0)])
        tmp3 = cmds.curve(d=3, p=[(-2.05541,0,-0.0124173),(-1.365656,0,-0.507243),(0.0138526,0,-1.496896),(1.337951,0,-0.498965),(2,0,0)])
        cmds.setAttr(tmp3+SCALE+"Z", -1)
        pm.makeIdentity(tmp3, a=True, t=1, r=1, s=1, n=0, pn=1)
        sh2 = cmds.listRelatives(tmp2, ad=True)[0]
        sh3 = cmds.listRelatives(tmp3, ad=True)[0]
        cmds.parent(sh2, tmp1[0], r=True, s=True)
        cmds.parent(sh3, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp2), cmds.ls(tmp3))
        c = cmds.ls(tmp1)[0]
        cmds.setAttr(c+ROTATE+"Y", 90)
        cmds.setAttr(c+ROTATE+"Z", 90)
        
    grp = cmds.group(n=ctrl_name+ctrlgrp(1), em=True)
    cmds.parent(c, grp)
    cmds.scale(world_scale, world_scale, world_scale, c)
    cmds.select(c)
    cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    match_objs(obj, grp)
    if ik_identity:
        pm.makeIdentity(grp, a=True, t=1, r=1, s=1, n=0, pn=1)
    
    func_cons = {0: cmds.parentConstraint, 1: cmds.pointConstraint,
                2: cmds.orientConstraint, 3: cmds.scaleConstraint, 9: None}
    if func_cons[idx] is not None:
        func_cons[idx](c, obj, mo=True)
    cmds.DeleteHistory(c)
    CtrlColor(c, ctrl_color)
    pm.ls(c)[0].rename(ctrl_name+ctrlgrp())
    
    
def CtrlColor(ctrls, color):
    if color == RED:
        num = 13
    elif color == YELLOW:
        num = 17
    elif color == BLUE:
        num = 6
    elif color == SKYBLUE:
        num = 18
    elif color == PINK:
        num = 20
    cmds.select(ctrls)
    cons = cmds.ls(sl=True)
    for col in cons:
        b = cmds.listRelatives(col, c=True)
        cmds.setAttr(col+".overrideEnabled", 1)
        cmds.setAttr(col+".overrideColor", num)


#----------------------------------------------------------------------------#


def add_attrs(objs, name="", type=9, dv_num=0, min_num=0, max_num=1):
    pm.select(objs)
    objs = pm.ls(sl=True)
    for obj in objs:
        if type == 1:
                pm.addAttr(obj, ln=name, at="double", dv=dv_num)
                pm.setAttr(obj+"."+name, k=True)
        elif type == 2:
                pm.addAttr(obj, ln=name, at="double", dv=dv_num, min=min_num, max=max_num)
                pm.setAttr(obj+"."+name, k=True)
        elif type == 9:
            cnt = 0
            flag = True
            while flag:
                cnt_str = "separator"+str(cnt)
                if pm.attributeQuery(cnt_str, n=obj.name(), ex=True):
                    cnt += 1
                else:
                    pm.addAttr(obj, ln=cnt_str, nn="----------", at="enum", en="--------:")
                    pm.setAttr(obj+"."+cnt_str, cb=True)
                    flag = False


def add_bool_attr(objs, name, en="FK:IK"):
    pm.select(objs)
    objs = pm.ls(sl=True)
    for obj in objs:
        pm.addAttr(obj, ln=name, at="enum", en=en)
        pm.setAttr(obj+"."+name, k=True)


def follow_attr(follow, follow_on, follow_off, attr_num):
    for num in range(2):
        tmp = 1 if num == 0 else 0
        cmds.setAttr(follow+".follow", num*10)
        cmds.setAttr(follow_off, tmp)
        cmds.setAttr(follow_on, num)
        cmds.setDrivenKeyframe(follow_off, cd=follow+".follow")
        cmds.setDrivenKeyframe(follow_on, cd=follow+".follow")
    cmds.setAttr(follow+".follow", attr_num)


def match_objs(obj, grp):
    cmds.parentConstraint(obj, grp, mo=False, n="tmp")
    cmds.delete("tmp")


def reverse_attr(rev_name, input_attr, output_attr):
    cmds.shadingNode(REVERSE, n=rev_name, au=True)
    cmds.connectAttr(input_attr, rev_name+".inputX")
    cmds.connectAttr(rev_name+".outputX", output_attr)


#----------------------------------------------------------------------------#


# Select joints to bind skin
def SelectJnt():
    cmds.warning("SelectJnt")


#----------------------------------------------------------------------------#


# Go back to Default Pose
def DefaultPose():
    cmds.warning("Default Pose")

# Save keys
def SaveKey():
    cmds.warning("Save Key")

# Mirror keys
def MirrorKey():
    cmds.warning("Mirror Key")


#----------------------------------------------------------------------------#


def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)
    print "Change Jnts Size: "+str(j)


def lockUnlock(i, j, tmp=False):
    ranges = []
    objs = cmds.ls(sl=True)
    
    if tmp:
        sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
        for sl_attr in sl_attrs:
            ranges.append("."+sl_attr)
        for obj in objs:
            for attr1 in ranges:
                cmds.setAttr(obj+attr1, l=i, k=j)
    else:
        if cmds.checkBoxGrp(lock_check, q=True, v1=True):
            ranges.append(".t")
        if cmds.checkBoxGrp(lock_check, q=True, v2=True):
            ranges.append(".r")
        if cmds.checkBoxGrp(lock_check, q=True, v3=True):
            ranges.append(".s")
        for obj in objs:
            for attr1 in ranges:
                for attr2 in ["x", "y", "z"]:
                    cmds.setAttr(obj+attr1+attr2, l=i, k=j)
            if cmds.checkBoxGrp(lock_check, q=True, v4=True):
                cmds.setAttr(obj+".visibility", l=i, k=j)


def matchFreeze():
    if cmds.checkBoxGrp(match_check, q=True, v1=True):
        cmds.MatchTranslation()
    if cmds.checkBoxGrp(match_check, q=True, v2=True):
        cmds.MatchRotation()
    if cmds.checkBoxGrp(match_check, q=True, v3=True):
        cmds.MatchScaling()
    if cmds.checkBoxGrp(match_check, q=True, v4=True):
        cmds.MatchPivots()
