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

DIST = "distanceBetween"
PLUSMIN = "plusMinusAverage"
MULDIV = "multiplyDivide"
REVERSE = "reverse"
BLENDTWO = "blendTwoAttr"
BLENDCOLORS = "blendColors"

CIRCLE = "circle"
SUB = "half_circle"
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
PINK_RED = "pink_red"

def joint_name(type, body, num):
    types = {0: "RIG_", 1: "FK_", 2: "IK_", 3: "IK_non_", 4: "IK_stretch_",
            5: "IK_snap_", 6: "IK_ribbon_"}
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

btn_layout(2)
cmds.button(l="Select Skin Joints", c="SelectJnt()", w=WI02[1], h=30)
cmds.button(l="Bind Skin Options", c="cmds.SmoothBindSkinOptions()", w=WI02[2], h=30)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Component Editor", c="cmds.ComponentEditor()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

wi=(70,250)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="  Direction : ", w=wi[0])
skin_check = cmds.checkBox(l="Positive to negative (+X to -X)", w=wi[1], v=True, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Mirror Skin Weights", c="MirrorSkinWeights()", w=WI01[1], h=30)
endspace()


# UI2: Tool
frame("Tool")

btn_layout(2)
cmds.button(l="LBA", c="cmds.ToggleLocalRotationAxes()", w=WI02[1], h=30)
cmds.button(l="Loc", c="cmds.CreateLocator()", w=WI02[2], h=30)
cmds.setParent("..")

cmds.rowLayout(nc=1)
match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,58,52,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Match", c="matchFreeze()", w=WI01[1], h=30)
cmds.setParent("..")

btn_layout(1)
cmds.button(l="Copy and New Group", c="newGroup()", w=WI01[1], h=30)
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
    cmds.select(cl=True)
    cmds.joint(n="Head1", p=(0,15.7,-0.1))
    cmds.parent("Head1", "Neck1")
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
    
    cmds.joint("L_Ankle"+str(num), n="L_Heel_end"+str(num), r=True, p=(0.84,1,0))
    cmds.joint("L_Toes_end"+str(num), n="L_FootSideInner_end"+str(num), r=True, p=(0,1,-0.5))
    cmds.joint("L_Toes_end"+str(num), n="L_FootSideOuter_end"+str(num), r=True, p=(0,1,0.5))
    cmds.parent("L_FootSide*"+str(num), w=True)
    cmds.parent("L_FootSide*"+str(num), "L_Toes"+str(num))


def JntArm_sub(x,z,num):
    cmds.joint("Chest1", n="L_Clavicle"+str(num), p=(0.4-x,14,-0.1-z))
    cmds.joint(n="L_Shoulder"+str(num), p=(1.3-x,14,-0.1-z))
    cmds.joint(n="L_Elbow"+str(num), p=(4-x,14,-0.2-z))
    cmds.joint(n="L_Wrist"+str(num), p=(6.4-x,14,-z))
    cmds.joint(n="tmp", p=(7.4-x,14,-z))
    
    cmds.joint("L_Clavicle"+str(num), e=True, oj="xyz", sao="ydown", ch=True, zso=True)
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
    
    for base in range(1, num_basefinger+1):
        cmds.select(wrist)
        if base == 1:
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(6.5+0.2*sub,14-0.08*sub,0.18*sub-y))
        elif base == 2:
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(7+0.2*sub,14-0.01*sub,0.1+0.05*sub-y))
        elif base == 3:
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(7.1+0.25*sub,14,-y))
        elif base == 4:
            cmds.joint(n=finger+"Cup", p=(6.7,14,-0.15-y))
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(7+0.25*sub,14,-0.2-0.03*sub-y))
        elif base == 5:
            cmds.select(finger+"Cup")
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(7+0.2*sub ,14-0.03*sub,-0.3-0.07*sub-y))
        elif base >= 6:
            cmds.select(finger+"Cup")
            for sub in range(1, num_subfinger+1):
                cmds.joint(n=finger+str(base)+"_"+str(sub), p=(7+(0.2-0.03*(base-5))*sub-0.1*(base-5),14-0.02*(base-5),-0.3-(0.1+0.01*(base-5))*sub-0.1*(base-5)-y))
    JntFingerOrient(num)


def JntFingerOrient(num):
    bf_int = cmds.intField(basefinger, q=True, v=True)
    for x in range(1, bf_int+1):
        cmds.select("L_Finger"+str(num)+"_"+str(x)+"_1")
        cmds.FreezeTransformations()
        cmds.joint(e=True, oj="xyz", sao="ydown", ch=True, zso=True)
    cmds.makeIdentity("L_Wrist"+str(num), a=True, r=True)
    cmds.DeleteHistory("L_Wrist"+str(num))


#----------------------------------------------------------------------------#


# Mirror Hip(leg), Clavicle(Arm), Eye
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
        JntMirror_check(num_arm, "Clavicle", "Arm")
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
    
#    if cmds.checkBox(leg_check, q=True, v=True):
#        for num in range(1, num_leg+1):
#            cmds.parent(["L_Toes"+str(num), "L_Heel_end"+str(num)], w=True)
#            cmds.joint("L_Ankle"+str(num), n="leg_tmp"+str(num), r=True, p=(2, 0, 0))
#
#    if cmds.checkBox(arm_check, q=True, v=True):
#        idx_finger = num_finger if num_finger < 3 else 3
#        for num in range(1, num_arm+1):
#            for i in range(1, idx_finger+1):
#                cmds.parent("L_Finger"+str(num)+"_"+str(i)+"_1", w=True)
#            if num_finger > 3:
#                cmds.parent("L_Finger"+str(num)+"_Cup", w=True)
#            cmds.joint("L_Wrist"+str(num), n="wrist_tmp"+str(num), r=True, p=(2, 0, 0))
#
#    cmds.joint("Spine0", e=True, oj="xyz", sao="zup", ch=True, zso=True)
#    cmds.joint("Jaw1", e=True, oj="xyz", sao="ydown", ch=True, zso=True)
#    cmds.joint("L_Eye1", e=True, oj="xyz", sao="zup", ch=True, zso=True)
#    print "Orient Head Jnts"
#
#    if cmds.checkBox(leg_check, q=True, v=True):
#        for num in range(1, num_leg+1):
#            cmds.joint("L_Hip"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
#            cmds.joint("L_Toes"+str(num), e=True, oj="xyz", sao="zdown", ch=True, zso=True)
#            cmds.delete("leg_tmp"+str(num))
#            cmds.parent(["L_Toes"+str(num), "L_Heel_end"+str(num)], "L_Ankle"+str(num))
#        print "Orient Hip Jnts"
#
#    if cmds.checkBox(arm_check, q=True, v=True):
#        for num in range(1, num_arm+1):
#            cmds.joint("L_Clavicle" + str(num), e=True, oj="xzy", sao="zdown", ch=True, zso=True)
#            cmds.delete("wrist_tmp"+str(num))
#            for i in range(1, idx_finger+1):
#                cmds.parent("L_Finger"+str(num)+"_"+str(i)+"_1", "L_Wrist"+str(num))
#            if num_finger > 3:
#                cmds.parent("L_Finger"+str(num)+"_Cup", "L_Wrist"+str(num))
#        print "Orient Arm Jnts"

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
    ribbon_grp = "Ribbon_grp"
    fkik_grp = "FKIK"+ctrlgrp(1)
    jnt_grp = "jnt_grp"
    extra_grp = "extra_grp"
    ctrl_grp = "ctrl_grp"
    
    ikjnt_grp = "IK_jnt_grp"
    ikctrl_grp = "IK"+ctrlgrp(1)
    ikcluster_grp = "IK_cluster"+ctrlgrp(1)
    ikspline_grp = "IK_spline"+ctrlgrp(1)
    ikfollow_grp = "IK_follow"+ctrlgrp(1)
    ikmessure_grp = "IK_messure"+ctrlgrp(1)
    
    grp_names = [rig_grp, world_grp, ik_grp, fk_grp, ribbon_grp, fkik_grp,
                jnt_grp, extra_grp, ctrl_grp, ikjnt_grp, ikctrl_grp,
                ikcluster_grp, ikspline_grp, ikfollow_grp, ikmessure_grp]
        
    for grp_name in grp_names:
        cmds.group(n=grp_name, em=True)
    cmds.parent(ikjnt_grp, ikctrl_grp, ikcluster_grp, ikspline_grp,
                ikfollow_grp, ikmessure_grp, ik_grp)

    SettingRoot()
    SettingSpine()
    SettingHead()
    if cmds.checkBox(arm_check, q=True, v=True):
       SettingArm()
       SettingFinger()
    if cmds.checkBox(leg_check, q=True, v=True):
       SettingLeg()
       SettingFoot()
    SettingVisibility()

    cmds.delete("scale_grp")
    cmds.parent("World_ctrl", world_grp)
    cmds.parent("Root", rig_grp)
    for grp_name in [fk_grp, ik_grp, fkik_grp, jnt_grp]:
        cmds.connectAttr("World_ctrl"+SCALE, grp_name+SCALE)
    cmds.parent(world_grp, "Root_ctrl_grp", fk_grp, ik_grp, ribbon_grp,
                fkik_grp, extra_grp, ctrl_grp)
    cmds.parent(jnt_grp, ctrl_grp, rig_grp)
    for grp_name in ["Root", ikjnt_grp, ikcluster_grp,
                    ikmessure_grp, extra_grp]:
        cmds.hide(grp_name)
    print "Finish!!!"
    cmds.warning("Finish!!!")


#----------------------------------------------------------------------------#

def SettingRoot():
    cmds.duplicate("Root", n="RIG_Root1", po=True)
    cmds.parent("RIG_Root1", "jnt_grp")
    
    CtrlCreate("RIG_Root1", ARROW1, 0, "Root", YELLOW)
    cmds.parent("Root"+ctrlgrp(1), "rig_grp")
    
    cmds.parentConstraint("World_ctrl", "Root"+ctrlgrp(1), mo=True)
    cmds.connectAttr("World_ctrl"+SCALE, "Root_ctrl"+SCALE)

    for axis in ["sx", "sy", "sz"]:
        cmds.setAttr("Root_ctrl."+axis, l=True, k=False, cb=False)

#----------------------------------------------------------------------------#


def SettingSpine():
    Setting_prepare("Spine")
    SpineFK()
    SpineIK()
    Setting_vis("Spine")
    cmds.parent("RIG_Spine1", "FK_Spine1_grp", "IK_Spine1", "RIG_Root1")
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
    
    cmds.group(n="FK_Spine1_grp", em=True)
    match_objs("FK_Spine1", "FK_Spine1_grp")
    cmds.parent("FK_Spine1", "FK_Spine1_grp")
    cmds.parentConstraint("Root_ctrl", "FK_Spine1_grp", mo=True)


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
    ik_hybrid_follow("Spine")
    ik_middle_follow("Spine")
    ik_stretch("Spine")
    ik_stiff("Spine")
    ik_volume("Spine")
    ik_grouping("Spine")


#----------------------------------------------------------------------------#


def SettingHead():
    Setting_prepare("Neck")
    NeckFK()
    NeckIK()
    Setting_vis("Neck")
    cmds.parent("RIG_Neck1", "FK_Neck1", "IK_Neck1", "RIG_Spine7")
    
    Setting_head()
    HeadFK()
    EyeAim()
    print "Create Head"
    
    
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
    ik_hybrid_follow("Neck")
    ik_middle_follow("Neck")
    ik_stretch("Neck")
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
    for mid in ["Jaw", "L_Eye", "R_Eye"]:
        mid_scale = "FK_"+mid+"_scale_Multiply"
        cmds.shadingNode(MULDIV, n=mid_scale, au=True)
        cmds.connectAttr("RIG_Neck5"+SCALE, mid_scale+".input1")
        cmds.connectAttr("FK_"+mid+ctrlgrp()+SCALE, mid_scale+".input2")
        cmds.connectAttr(mid_scale+".output", joint_name(0,mid,1)+SCALE)

    
    fk_grouping(None, "Head", None)
    cmds.connectAttr("RIG_Neck5"+SCALE, "FK_Head"+ctrlgrp(2)+SCALE)
    fk_head_follow()


def fk_head_follow():
    fk_head = "FK_Head"
    follow_on = fk_head+"_follow_on"
    follow_off = fk_head+"_follow_off"
    
    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(fk_head+ctrlgrp(), grp_name)
    cmds.delete("FK_Neck4_grp", "FK_Head_ctrl_grp_parentConstraint1")
    cmds.parent(follow_on, "FK_Neck4")
    cmds.parent(follow_off, "FK_Neck_ctrl_grp")
    cmds.orientConstraint(follow_on, follow_off, fk_head+ctrlgrp(1))
    cmds.pointConstraint(follow_on, fk_head+ctrlgrp(1))
    
    follow_attr(fk_head+ctrlgrp(), fk_head+ctrlgrp(1), follow_on, follow_off, 10, "orient")


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

    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(aim_all+ctrlgrp(1), grp_name)
    cmds.group(n=follow_on+ctrlgrp(2), em=True)
    match_objs("RIG_Neck5", follow_on+ctrlgrp(2))
    cmds.parentConstraint("RIG_Neck5", follow_on+ctrlgrp(2), mo=True)
    cmds.parent(follow_on, follow_on+ctrlgrp(2))
    cmds.parentConstraint(follow_on, follow_off, aim_all+ctrlgrp(1))

    follow_attr(aim_all+ctrlgrp(), aim_all+ctrlgrp(1), follow_on, follow_off, 10)
    
    cmds.group(n=aim_all+ctrlgrp(2), em=True)
    match_objs("RIG_Neck5", aim_all+ctrlgrp(2))
    cmds.parent(aim_all+ctrlgrp(1), follow_on+ctrlgrp(2), follow_off, aim_all+ctrlgrp(2))
    cmds.parent(aim_all+ctrlgrp(2), "FK_grp")
    cmds.connectAttr("RIG_Neck5"+SCALE, aim_all+ctrlgrp(2)+SCALE)
    
    
#----------------------------------------------------------------------------#


def SettingArm():
    Setting_clavicle()
    Setting_prepare("Arm")
    ClavicleFK()
    ArmLegFKIK("Arm")
    Setting_vis_armleg("Arm")
    print "Create Arm"


def ClavicleFK():
    end_num = cmds.intField(arm, q=True, v=True)
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            rig_clavicle = joint_name(0,lr+"_Clavicle",num)
            rig_shoulder = joint_name(0,lr+"_Shoulder",num)
            fk_clavicle = joint_name(1,lr+"_Clavicle",num)
            attr_num = -1 if lr == "L" else 1
            
            CtrlCreate(rig_clavicle, ARROW4, 9, fk_clavicle, YELLOW)
            cmds.pointConstraint(rig_shoulder, fk_clavicle+ctrlgrp(), n="tmp")
            cmds.delete("tmp")
            cmds.setAttr(fk_clavicle+ctrlgrp()+TRANSLATE+"Y", attr_num*world_scale)
            cmds.select(fk_clavicle+ctrlgrp())
            cmds.makeIdentity(a=True, t=1, r=1, n=0)
            cmds.ResetTransformations()
            cmds.parentConstraint(fk_clavicle+ctrlgrp(), rig_clavicle, mo=True)
            cmds.connectAttr(fk_clavicle+ctrlgrp()+SCALE, rig_clavicle+SCALE)
            for trs in [TRANSLATE, SCALE]:
                for axis in AXISES:
                    cmds.setAttr(fk_clavicle+ctrlgrp()+trs+axis, l=True, k=False)
            


#----------------------------------------------------------------------------#


def SettingFinger():
    Setting_finger()
    for lr in LFRT:
        FingerFK(lr)
        FingerIK(lr)
        FingerScale(lr)
    FingerSub()
    Finger_grouping()
    Setting_vis_armleg("Finger")
    print "Create Finger"


def FingerFK(lr):
    end_num = cmds.intField(arm, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)

    for num in range(1, end_num+1):
        name = joint_name(1,lr+"_Finger",num)
        for base in range(1, base_num+1):
            finger = name+"_"+str(base)+"_"
            for sub in range(1, sub_num+1):
                CtrlCreate(finger+str(sub), CIRCLE, 0, finger+str(sub), SKYBLUE)
                cmds.scale(0.15, 0.15, 0.15, finger+str(sub)+"_ctrl.cv[0:7]", r=True, ocp=True)
                finger_scale = finger+str(sub)+"_scale_Multiply"
                cmds.shadingNode(MULDIV, n=finger_scale, au=True)
                cmds.connectAttr(joint_name(0,lr+"_Wrist",num)+SCALE, finger_scale+".input1")
                cmds.connectAttr(finger+str(sub)+ctrlgrp()+SCALE, finger_scale+".input2")
                cmds.connectAttr(finger_scale+".output", finger+str(sub)+SCALE)
            for sub in range(sub_num, 1, -1):
                cmds.parent(finger+str(sub)+ctrlgrp(1), finger+str(sub-1)+ctrlgrp())
                
        if base_num > 3:
            cup = name+"_Cup"
            CtrlCreate(cup, CIRCLE, 0, cup, SKYBLUE)
            cmds.scale(0.3, 0.3, 0.3, cup+"_ctrl.cv[0:7]", r=True, ocp=True)
            cup_scale = cup+"_scale_Multiply"
            cmds.shadingNode(MULDIV, n=cup_scale, au=True)
            cmds.connectAttr(joint_name(0,lr+"_Wrist",num)+SCALE, cup_scale+".input1")
            cmds.connectAttr(cup+ctrlgrp()+SCALE, cup_scale+".input2")
            cmds.connectAttr(cup_scale+".output", cup+SCALE)
            for base in range(4, base_num+1):
                finger = name+"_"+str(base)+"_1"
                cmds.parent(finger+ctrlgrp(1), cup+ctrlgrp())
        
        finger_grp = name+ctrlgrp(2)
        cmds.group(n=finger_grp, em=True)
        cmds.parentConstraint(joint_name(0,lr+"_Wrist",num), finger_grp)
        end_num = 4 if base_num > 3 else base_num+1
        for base in range(1, end_num):
            finger = name+"_"+str(base)+"_1"+ctrlgrp(1)
            cmds.parent(finger, finger_grp)
        if base_num > 3:
            cmds.parent(name+"_Cup"+ctrlgrp(1), finger_grp)


def FingerIK(lr):
    end_num = cmds.intField(arm, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    
    for num in range(1, end_num+1):
        for base in range(1, base_num+1):
            ik_finger_handle(lr, num, base)
            ik_finger_pole_vector(lr, num, base)
            ik_finger_pole_vector_follow(lr, num, base)
        ik_finger_grouping(lr, num)
        
        ik_arm = joint_name(2, lr+"_Arm", num)
        cmds.connectAttr(ik_arm+ctrlgrp()+SCALE, ik_arm+"_ikHandle"+ctrlgrp(2)+SCALE)
        cmds.connectAttr(ik_arm+ctrlgrp()+SCALE, joint_name(2,lr+"_Wrist",num)+SCALE)
        
        for base in range(1, base_num+1):
            ik_finger = joint_name(2, lr+"_Finger", num)+"_"+str(base)
            cmds.connectAttr(ik_finger+"_master"+ctrlgrp()+SCALE, ik_finger+"_ikHandle"+ctrlgrp(2)+SCALE)
            for sub in range(1, sub_num+1):
                cmds.connectAttr(joint_name(0,lr+"_Wrist",num)+SCALE, ik_finger+"_"+str(sub)+SCALE)
        if base_num > 3:
            cmds.connectAttr(joint_name(0,lr+"_Wrist",num)+SCALE, joint_name(2, lr+"_Finger", num)+"_Cup"+SCALE)
        if base_num > 3:
            cup = joint_name(2,lr+"_Finger",num)+"_Cup"
            CtrlCreate(cup, CIRCLE, 0, cup, SKYBLUE)
            cmds.scale(0.3, 0.3, 0.3, cup+"_ctrl.cv[0:7]", r=True, ocp=True)
            for base in range(4, base_num+1):
                finger = joint_name(2,lr+"_Finger",num)+"_"+str(base)+"_master"+ctrlgrp(1)
                cmds.parent(finger, cup+ctrlgrp())
            cmds.parent(cup+ctrlgrp(1), joint_name(2,lr+"_Finger",num)+ctrlgrp(1))
    
    
def FingerScale(lr):
    end_num = cmds.intField(arm, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    
    for num in range(1, end_num+1):
        rig_wrist = joint_name(0,lr+"_Wrist",num)+SCALE
        cmds.connectAttr(rig_wrist, joint_name(1,lr+"_Finger",num)+ctrlgrp(2)+SCALE)
        cmds.connectAttr(rig_wrist, joint_name(2,lr+"_Finger",num)+ctrlgrp(1)+SCALE)
        cmds.connectAttr(rig_wrist, "IK_PV_"+lr+"_Finger"+str(num)+ctrlgrp(1)+SCALE)
        cmds.connectAttr(rig_wrist, joint_name(2,lr+"_Finger",num)+"_ikHandle"+ctrlgrp(2)+SCALE)


def FingerSub():
    end_num = cmds.intField(arm, q=True, v=True)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            sub_fkik(lr, num)
            sub_ctrls(lr, num)
            sub_add_attrs(lr, num)
            sub_spread(lr, num)
            sub_relax_slide_scrunch(lr, num)
    print "Create Finger Sub"


def Finger_grouping():
    end_num = cmds.intField(arm, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    
    fk_grp = "FK_Finger_grp"
    handle_grp = "IK_Finger_ikHandle"+ctrlgrp(2)
    ik_grp = "IK_Finger"+ctrlgrp(2)
    pv_grp = "IK_PV_Finger"+ctrlgrp(2)
            
    for grp_name in [fk_grp, handle_grp, ik_grp, pv_grp]:
        cmds.group(n=grp_name, em=True)
        
    for lr in LFRT:
        for num in range(1, end_num+1):
            cmds.parent(joint_name(1,lr+"_Finger",num)+ctrlgrp(2), fk_grp)
            lr_handle_grp = joint_name(2,lr+"_Finger",num)+"_ikHandle"+ctrlgrp(2)
            lr_ik_grp = joint_name(2,lr+"_Finger",num)+ctrlgrp(1)
            lr_pv_grp = "IK_PV_"+lr+"_Finger"+str(num)+ctrlgrp(1)
            cmds.parent(lr_handle_grp, handle_grp)
            cmds.parent(lr_ik_grp, ik_grp)
            cmds.parent(lr_pv_grp, pv_grp)
            
    cmds.connectAttr("World_ctrl"+SCALE, handle_grp+SCALE)
    cmds.parent(fk_grp, "FK_grp")
    cmds.parent(handle_grp, "extra_grp")
    cmds.parent(ik_grp, pv_grp, "IK_ctrl_grp")
    

#----------------------------------------------------------------------------#


def SettingLeg():
    Setting_prepare("Leg")
    ArmLegFKIK("Leg")
    Setting_vis_armleg("Leg")
    print "Create Leg"

        
#----------------------------------------------------------------------------#


def SettingFoot():
    end_num = cmds.intField(leg, q=True, v=True)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            Setting_foot(lr, num)
            FootFK(lr, num)
            FootIK(lr, num)
            FootScale(lr, num)
    print "Create Foot"
    

def FootFK(lr, num):
    CtrlCreate(joint_name(1,lr+"_Toes",num), CIRCLE, 0, joint_name(1,lr+"_Toes",num), SKYBLUE)
    cmds.scale(0.5, 0.5, 0.5, joint_name(1,lr+"_Toes",num)+"_ctrl.cv[0:7]", r=True, ocp=True)
    cmds.parent(joint_name(1,lr+"_Toes",num)+ctrlgrp(1), joint_name(1,lr+"_Ankle",num)+ctrlgrp())
    
    toe_scale = joint_name(1,lr+"_Toes",num)+"_scale_Multiply"
    cmds.shadingNode(MULDIV, n=toe_scale, au=True)
    cmds.connectAttr(joint_name(1,lr+"_Ankle",num)+ctrlgrp()+SCALE, toe_scale+".input1")
    cmds.connectAttr(joint_name(1,lr+"_Toes",num)+ctrlgrp()+SCALE, toe_scale+".input2")
    cmds.connectAttr(toe_scale+".output", joint_name(1,lr+"_Toes",num)+SCALE)


def FootIK(lr, num):
    ik_foot_prepare(lr, num)
    ik_foot_rock(lr, num)
    ik_foot_roll(lr, num)
    ik_foot_swivel(lr, num)
    ik_foot_sub_ctrl(lr, num)
    
    name = joint_name(2, lr+"_Leg", num)
    cmds.connectAttr(name+ctrlgrp()+SCALE, name+ctrlgrp(2)+SCALE)
    for mid_name in [lr+"_Ankle", lr+"_Toes"]:
        cmds.connectAttr(name+ctrlgrp()+SCALE, joint_name(2,mid_name,num)+SCALE)


def FootScale(lr, num):
    name = joint_name(2, lr+"_Leg", num)
    ankle_bc = name+"_ankle_BlendColors"
    toe_bc = name+"_toe_BlendColors"
    fkik_ctrl = "FKIK_"+lr+"_Leg"+str(num)+ctrlgrp()

    mid = [lr+"_Ankle", lr+"_Toes"]
    for idx, grp_name in enumerate([ankle_bc, toe_bc]):
        cmds.shadingNode(BLENDCOLORS, n=grp_name, au=True)
        cmds.connectAttr(joint_name(2,mid[idx],num)+SCALE, grp_name+".color1")
        cmds.connectAttr(joint_name(1,mid[idx],num)+SCALE, grp_name+".color2")
        cmds.connectAttr(fkik_ctrl+".FKIK", grp_name+".blender")
        cmds.connectAttr(grp_name+".output", joint_name(0,mid[idx],num)+SCALE)


#----------------------------------------------------------------------------#

########
def SettingVisibility():
    num_arm = cmds.intField(arm, q=True, v=True)
    num_leg = cmds.intField(leg, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    
    cmds.hide("jnt_grp")
    for lr in LFRT:
        if cmds.checkBox(arm_check, q=True, v=True):
            for num in range(1, num_arm+1):
                cmds.hide(joint_name(6,lr+"_Arm",num)+"_skin*_jnt*")
                cmds.hide(joint_name(6,lr+"_Arm",num)+"_geo")
        if cmds.checkBox(leg_check, q=True, v=True):
            for num in range(1, num_leg+1):
                cmds.hide(joint_name(6,lr+"_Leg",num)+"_skin*_jnt*")
                cmds.hide(joint_name(6,lr+"_Leg",num)+"_geo")
                
    grp_names = [joint_name(1,"Spine",1)+ctrlgrp(2), joint_name(2,"Spine",1),
                joint_name(1,"Neck",1), joint_name(2,"Neck",1)]
    for grp_name in grp_names:
        cmds.hide(grp_name)
    for lr in LFRT:
        if cmds.checkBox(arm_check, q=True, v=True):
            for num in range(1, num_arm+1):
                cmds.hide(joint_name(1,lr+"_Shoulder",num))
                cmds.hide(joint_name(2,lr+"_Shoulder",num)+ctrlgrp(2))
                for idx in range(1, 3):
                    if base_num > 3:
                        cmds.hide(joint_name(idx,lr+"_Finger",num)+"_Cup")
                    end_num = 4 if base_num > 3 else base_num+1
                    for base in range(1, end_num):
                        cmds.hide(joint_name(idx,lr+"_Finger",num)+"_"+str(base)+"_1")
        if cmds.checkBox(leg_check, q=True, v=True):
            for num in range(1, num_leg+1):
                cmds.hide(joint_name(1,lr+"_Hip",num))
                cmds.hide(joint_name(2,lr+"_Hip",num)+ctrlgrp(2))


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
    for idx in range(1, 3):
        for axis in ["X", "Y"]:
            num_top = cmds.getAttr(top+TRANSLATE+axis)
            num_bottom = cmds.getAttr(bottom+TRANSLATE+axis)
            if num_top < num_bottom:
                trans.append(num_bottom - (num_bottom - num_top)/3*idx)
            else:
                trans.append((num_top - num_bottom)/3*idx + num_bottom)
        num_top = cmds.getAttr(top+TRANSLATE+"Z")
        num_bottom = cmds.getAttr(bottom+TRANSLATE+"Z")
        if num_top < num_bottom:
            tmp = 1 if idx == 1 else 3
            trans.append(num_bottom - (num_bottom - num_top)/5*tmp)
        else:
            tmp = 2 if idx == 1 else 4
            trans.append((num_top - num_bottom)/5*tmp + num_bottom)
    tmp = cmds.joint(bottom, n="RIG_Spine"+str(num), p=(trans[0], trans[1], trans[2]))
    cmds.joint(tmp, n="RIG_Spine"+str(num+1), p=(trans[3], trans[4], trans[5]))
    
    
def Setting_neck(top, bottom):
    trans = []
    for idx in range(1, 4):
        for axis in AXISES:
            num_top = cmds.getAttr(top+TRANSLATE+axis)
            num_bottom = cmds.getAttr(bottom+TRANSLATE+axis)
            if num_top < num_bottom:
                trans.append(num_bottom - (num_bottom - num_top)/4*idx)
            else:
                trans.append((num_top - num_bottom)/4*idx + num_bottom)
    tmp = cmds.joint(bottom, n="RIG_Neck2", p=(trans[0], trans[1], trans[2]))
    mid = cmds.joint(tmp, n="RIG_Neck3", p=(trans[3], trans[4], trans[5]))
    cmds.joint(mid, n="RIG_Neck4", p=(trans[6], trans[7], trans[8]))
    cmds.parent("RIG_Neck5", "RIG_Neck4")

    
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
    for trs in [TRANSLATE, ROTATE, SCALE]:
        for axis in AXISES:
            cmds.setAttr(ctrl_name+ctrlgrp()+trs+axis, l=True, k=False)
     

def Setting_FKIK_armleg(part):
    if part == "Arm":
        end_num = cmds.intField(arm, q=True, v=True)
        attrs = [TRANSLATE+"X", TRANSLATE+"Y"]
        attr_num = [2, 1]
        mid_names = ["_Shoulder", "_Elbow", "_Wrist"]
    elif part == "Leg":
        end_num = cmds.intField(leg, q=True, v=True)
        attrs = [TRANSLATE+"X", TRANSLATE+"Y"]
        attr_num = [1, -1]
        mid_names = ["_Hip", "_Knee", "_Ankle"]
        
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    for num in range(1, end_num+1):
        if part == "Arm":
            l_obj = "RIG_L_Clavicle"+str(num)
            l_parent = l_obj
            r_parent = "RIG_R_Clavicle"+str(num)
        elif part == "Leg":
            l_obj = "RIG_L_Hip"+str(num)
            l_parent = "RIG_Spine1"
            r_parent = l_parent

        l_ctrl_name = "FKIK_L_"+part+str(num)
        r_ctrl_name = "FKIK_R_"+part+str(num)
        CtrlCreate(l_obj, FKIK_CROSS, 9, l_ctrl_name, BLUE, 1)
        
        for idx, attr in enumerate(attrs):
            cmds.setAttr(l_ctrl_name+ctrlgrp()+attr, attr_num[idx]*world_scale)
        if part == "Leg":
            cmds.parent(l_ctrl_name+ctrlgrp(), w=True)
            match_objs("RIG_Spine1", l_ctrl_name+ctrlgrp(1))
            cmds.parent(l_ctrl_name+ctrlgrp(), l_ctrl_name+ctrlgrp(1))
        else:
            cmds.setAttr(l_ctrl_name+ctrlgrp()+ROTATE+"X", 90)
        if part == "Finger":
            cmds.scale(0.7, 0.7, 0.7, l_ctrl_name+ctrlgrp())
        cmds.makeIdentity(l_ctrl_name+ctrlgrp(), a=True, t=1, r=1, s=1, n=0, pn=1)
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
            ctrl_name = "FKIK_"+lr+"_"+part+str(num)+ctrlgrp()
            for name in mid_names:
                cmds.connectAttr(ctrl_name+".FKIK", "RIG_"+lr+name+str(num)+".spread")
            for trs in [TRANSLATE, ROTATE, SCALE]:
                for axis in AXISES:
                    cmds.setAttr(ctrl_name+trs+axis, l=True, k=False)

 
#----------------------------------------------------------------------------#


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


def Setting_clavicle():
    end_num = cmds.intField(arm, q=True, v=True)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            cmds.duplicate(lr+"_Clavicle"+str(num), n=joint_name(0,lr+"_Clavicle",num), po=True)
            cmds.parent(joint_name(0,lr+"_Clavicle",num), "RIG_Spine7")


def Setting_foot(lr, num):
    foot_lists = [lr+"_Heel_end", lr+"_FootSideOuter_end", lr+"_FootSideInner_end"]
    for idx in range(3):
        cmds.duplicate(lr+"_Toes"+str(num), n=joint_name(idx,lr+"_Toes",num), po=True)
        cmds.duplicate(lr+"_Toes_end"+str(num), n=joint_name(idx,lr+"_Toes_end",num), po=True)
        cmds.parent(joint_name(idx,lr+"_Toes_end",num), joint_name(idx,lr+"_Toes",num))
        cmds.parent(joint_name(idx,lr+"_Toes",num), joint_name(idx,lr+"_Ankle",num))
        
        for name in foot_lists:
            cmds.duplicate(name+str(num), n=joint_name(idx,name,num), po=True)
        cmds.parent(joint_name(idx,foot_lists[1],num), joint_name(idx,lr+"_Toes",num))
        cmds.parent(joint_name(idx,foot_lists[2],num), joint_name(idx,lr+"_Toes",num))
        cmds.parent(joint_name(idx,foot_lists[0],num), joint_name(idx,lr+"_Ankle",num))
        
    spread(joint_name(0,lr+"_Toes",num), joint_name(1,lr+"_Toes",num), joint_name(2,lr+"_Toes",num))
    spread(joint_name(0,foot_lists[0],num), joint_name(1,foot_lists[0],num), joint_name(2,foot_lists[0],num))
    for name in [lr+"_Toes", lr+"_Toes_end", lr+"_Heel_end",
                lr+"_FootSideOuter_end", lr+"_FootSideInner_end"]:
        cmds.connectAttr("FKIK_"+lr+"_Leg"+str(num)+"_ctrl.FKIK", joint_name(0,name,num)+".spread")


def Setting_finger():
    num_arm = cmds.intField(arm, q=True, v=True)
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    
    for lr in LFRT:
        for num in range(1, num_arm+1):
            for base in range(1, base_num+1):
                joint_end = lr+"_Finger"+str(num)+"_"+str(base)+"_"+str(sub_num)
                for axis in AXISES:
                    cmds.setAttr(joint_end+".jointOrient"+axis, 0)
                        
            end_num = 4 if base_num > 3 else base_num+1
            for base in range(1, end_num):
                finger = lr+"_Finger"+str(num)+"_"+str(base)+"_"
                for sub in range(1, sub_num+1):
                    for type in ["RIG_", "FK_", "IK_"]:
                        cmds.duplicate(finger+str(sub), n=type+finger+str(sub), po=True)
            for base in range(4, base_num+1):
                finger = lr+"_Finger"+str(num)+"_"+str(base)+"_"
                for sub in range(1, sub_num+1):
                    for type in ["RIG_", "FK_", "IK_"]:
                        cmds.duplicate(finger+str(sub), n=type+finger+str(sub), po=True)
                        
            for base in range(1, base_num+1):
                for sub in range(sub_num, 1, -1):
                    finger = lr+"_Finger"+str(num)+"_"+str(base)+"_"
                    for type in ["RIG_", "FK_", "IK_"]:
                        cmds.parent(type+finger+str(sub), type+finger+str(sub-1))
                finger = lr+"_Finger"+str(num)+"_"+str(base)+"_1"
                for idx, value in enumerate(["RIG_", "FK_", "IK_"]):
                    cmds.parent(value+finger, "RIG_"+lr+"_Wrist"+str(num))

            if base_num > 3:
                cup = lr+"_Finger"+str(num)+"_Cup"
                for idx, value in enumerate(["RIG_", "FK_", "IK_"]):
                    cmds.duplicate(cup, n=value+cup, po=True)
                    cmds.parent(value+cup, "RIG_"+lr+"_Wrist"+str(num))
                    for base in range(4, base_num+1):
                        finger = lr+"_Finger"+str(num)+"_"+str(base)+"_1"
                        cmds.parent(value+finger, value+cup)
                spread("RIG_"+cup, "FK_"+cup, "IK_"+cup)
            for base in range(1, end_num):
                finger = lr+"_Finger"+str(num)+"_"+str(base)+"_1"
                spread("RIG_"+finger, "FK_"+finger, "IK_"+finger)


#----------------------------------------------------------------------------#


def Setting_vis(part):
    if part == "Spine":
        end_num = 7
    elif part == "Neck":
        end_num = 5

    fk_grp = "FK_"+part+ctrlgrp(2)
    ik_grp = "IK_"+part+ctrlgrp(2)
    fkik_ctrl = "FKIK_"+part+ctrlgrp()

    cmds.connectAttr(fkik_ctrl+".FKIK", ik_grp+".visibility")
    reverse_attr("FKIK_"+part+"_Reverse", fkik_ctrl+".FKIK", fk_grp+".visibility")
    for num in range(1, end_num+1):
        cmds.connectAttr(fkik_ctrl+".FKIK", "IK_volume_"+part+str(num)+"_BlendColors.blender")
    cmds.parent("FKIK_"+part+ctrlgrp(1), "FKIK_ctrl_grp")


def Setting_vis_armleg(part):
    if part == "Leg":
        end_num = cmds.intField(leg, q=True, v=True)
    else:
        end_num = cmds.intField(arm, q=True, v=True)
    
    fkik_ctrl_grp = cmds.group(n="FKIK_"+part+ctrlgrp(2), em=True)
    for lr in LFRT:
        for num in range(1, end_num+1):
            mid = lr+"_"+part
            fk_grp = joint_name(1,mid,num)+ctrlgrp(2)
            ik_grp = joint_name(2,mid,num)+ctrlgrp(1)
            pv_grp = "IK_PV_"+mid+str(num)+ctrlgrp(1)
            fkik_ctrl = "FKIK_"+mid+str(num)
            if part == "Finger":
                fkik_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"

            cmds.connectAttr(fkik_ctrl+ctrlgrp()+".FKIK", ik_grp+".visibility")
            cmds.connectAttr(fkik_ctrl+ctrlgrp()+".FKIK", pv_grp+".visibility")
            reverse_attr("FKIK_"+mid+str(num)+"_Reverse", fkik_ctrl+ctrlgrp()+".FKIK", fk_grp+".visibility")
            cmds.parent(fkik_ctrl+ctrlgrp(1), fkik_ctrl_grp)
    cmds.parent(fkik_ctrl_grp, "FKIK_ctrl_grp")


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
        for num in range(1, end_num+1):
            cmds.duplicate(joint_name(type,body,num), n=joint_name(dup_type,body,num), po=True)
            if num > 1:
                cmds.parent(joint_name(dup_type,body,num), joint_name(dup_type,body,num-1))
    else:
        cmds.duplicate(joint_name(type,body,nb))
        cmds.select(joint_name(type,body,end_num), hi=True)
        objs = pm.ls(sl=True)
        for idx, obj in enumerate(objs):
            if body == "L_Shoulder":
                obj.rename(joint_name(dup_type,arm_joints[idx],nb))
            elif body == "L_Hip":
                obj.rename(joint_name(dup_type,leg_joints[idx],nb))
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
    constraints = cmds.listRelatives(rig_joints, ad=True, typ="constraint")[::-1]
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
            cmds.connectAttr(div_name+"_Divide.output", joint_name(1,joint_mid,num)+ROTATE)


def fk_grouping(func, part, num_lists):
    if part == "Spine":
        parent_joint = "Root_ctrl"
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
            ik_pole_vector_swivel(part, lr, num)
            ik_armleg_stretch(part, lr, num)
    ik_armleg_grouping(part, end_num)

    for lr in LFRT:
        for num in range(1, end_num+1):
            ik_ribbon(part, lr, num)


#----------------------------------------------------------------------------#


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
        upper = "RIG_Spine1"
    
    part_grp = "FK_"+part+ctrlgrp(2)
    cmds.group(n=part_grp, em=True)
    match_objs(upper, part_grp)
    cmds.parent(part_grp, "FK_grp")
    cmds.parentConstraint(upper, part_grp)
    
    for lr in LFRT:
        for num in range(1, end_num+1):
            if part == "Arm":
                parent_joint = joint_name(0,lr+"_Clavicle",num)
            else:
                parent_joint = joint_name(0,lr+"_Hip",num)
                
            final_grp = "FK_"+lr+"_"+part+str(num)+ctrlgrp(2)
            cmds.group(n=final_grp, em=True)
            match_objs(parent_joint, final_grp)
            
            for name in parent_lists:
                cmds.parent("FK_"+lr+name+str(num)+ctrlgrp(1), final_grp)
            cmds.parent(final_grp, part_grp)
            
            if part == "Arm":
                fk_upper = "FK_"+lr+"_Clavicle"+str(num)
                cmds.parent(fk_upper+ctrlgrp(1), part_grp)
                cmds.parentConstraint(fk_upper+ctrlgrp(), final_grp)


#----------------------------------------------------------------------------#


def ik_spline_handle(func, part, end_num):
    handle = cmds.ikHandle(sj=func(1), ee=func(end_num), sol="ikSplineSolver", scv=False, pcv=False, ns=4)
    cmds.rename(handle[2], "IK_"+part+"_ikHandle_crv")
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
    CtrlCreate(joint_name(2,part,mid_num)+clus_grp, CIRCLE, 9, func(2), RED, 1)
    CtrlCreate(joint_name(2,part,end_num)+clus_grp, BOX, 0, func(3), RED, 1)
    
    cmds.parentConstraint(func(1)+ctrlgrp(), func(2)+ctrlgrp(), func(3)+ctrlgrp(), joint_name(2,part,mid_num)+clus_grp, mo=True)
    cmds.setAttr(joint_name(2,part,mid_num)+clus_grp+"_parentConstraint1."+func(1)+ctrlgrp()+"W0", 0.1)
    cmds.setAttr(joint_name(2,part,mid_num)+clus_grp+"_parentConstraint1."+func(3)+ctrlgrp()+"W2", 0.1)


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
    cmds.hide(top)
    cmds.hide(bottom)


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


def ik_hybrid_follow(part):
    ik_top = joint_name(2,part,3)+ctrlgrp()
    ik_bottom = joint_name(2,part,1)+ctrlgrp()
    hybrid = "IK_"+part+"_Hybrid1"
    follow_on = hybrid+"_follow_on"
    follow_off = hybrid+"_follow_off"
    
    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(hybrid+ctrlgrp(), grp_name)
    cmds.parent(follow_on, ik_bottom)
    cmds.parent(follow_off, "World_ctrl")
    cmds.parentConstraint(follow_on, follow_off, hybrid+ctrlgrp(1))
    
    follow_attr(ik_top, hybrid+ctrlgrp(1), follow_on, follow_off, 10)


def ik_middle_follow(part):
    ik_mid = joint_name(2,part,2)+ctrlgrp()
    ik_mid_grp = joint_name(2,part,2)+ctrlgrp(1)
    follow_top = "IK_"+part+"_follow_top"
    follow_bottom = "IK_"+part+"_follow_bottom"

    for num in [1, 3]:
        name = follow_bottom if num == 1 else follow_top
        ctrl = joint_name(2,part,str(num))+ctrlgrp()
        grp = cmds.group(n=name, em=True)
        match_objs(ik_mid, grp)
        cmds.parent(name, ctrl)
    cmds.parentConstraint(follow_top, follow_bottom, ik_mid_grp)
    
    follow_attr(ik_mid, ik_mid_grp, follow_top, follow_bottom, 5)


def ik_stiff(part):
    if part == "Spine":
        top_num_lists = [2, 3]
        bottom_num_lists = [5, 6]
        weights = [1, 0.1, 1, 0.75]
    elif part == "Neck":
        top_num_lists = [2]
        bottom_num_lists = [4]
        weights = [1, 0.6]
        
    add_attrs(joint_name(2,part,1)+ctrlgrp())
    ik_stiff_loop(part, 1, top_num_lists, weights)
    ik_stiff_loop(part, 3, bottom_num_lists, weights[::-1])


def ik_stiff_loop(part, num, num_lists, weights):
    add_attrs(joint_name(2,part,num)+ctrlgrp(), "stiff", 2, 5, 0, 10)
    stiff_attr = joint_name(2,part,num)+ctrlgrp()+".stiff"
    
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
        parent_joint = "Root_ctrl"
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


def ik_stretch(part):
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
    ik_stretch_top_bottom(part, end_num)
    ik_stretch_grouping(part, end_num)
    

def ik_stretch_refresh(part, end_num):
    prepare_div = "IK_stretch_"+part+"_10into1_Divide"
    
    for num in range(1, end_num+1):
        cmds.delete(joint_name(0,part,num)+"_parentConstraint1*")
    for num in range(1, end_num+1):
        cmds.rename(joint_name(2,part,num), joint_name(3,part,num))

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
    

def ik_stretch_top_bottom(part, end_num):
    for num in range(1, 4):
        orient_grp = cmds.group(n=joint_name(2,part,num)+"_orient1", em=True)
        match_objs(joint_name(2,part,num)+"_ctrl", orient_grp)
        cmds.parent(orient_grp, joint_name(2,part,num)+"_ctrl")
        cmds.duplicate(orient_grp)
        cmds.parent(joint_name(2,part,num)+"_orient2", orient_grp)
    
    for num in [1, end_num]:
        idx = 1 if num == 1 else 3
        cmds.delete(joint_name(2,part,num)+"_parentConstraint1*")
        cmds.orientConstraint(joint_name(2,part,idx)+"_orient2", joint_name(2,part,num), mo=True)
        cmds.pointConstraint(joint_name(3,part,num), joint_name(4,part,num), joint_name(2,part,num), mo=True)
        cmds.connectAttr(joint_name(2,part,num)+".spread", joint_name(2,part,num)+"_pointConstraint1."+joint_name(4,part,num)+"W1")
        reverse_attr("IK_stretch_"+part+str(num)+"_reverse", joint_name(2,part,num)+".spread", joint_name(2,part,num)+"_pointConstraint1."+joint_name(3,part,num)+"W0")
    

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
    vol_pow = "IK_volume_"+part+"_Power"
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
    for num in range(1,end_num+1):
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
        
    for num in range(1,end_num+1):
        for idx in range(1, 3):
            cmds.shadingNode(PLUSMIN, n=vol_sum(num,idx), au=True)
            cmds.shadingNode(MULDIV, n=vol_mul(num,idx), au=True)
        cmds.shadingNode(BLENDCOLORS, n=vol_bc(num), au=True)
    
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
    name = ik_armleg("_"+part)
    ik_handle_grp = name+"_ikHandle"+ctrlgrp(2)
    
    for body in bodies:
        cmds.duplicate(ik_armleg(body), n=ik_armleg(body)+ctrlgrp(2), po=True)
        match_objs(ik_armleg(body), ik_armleg(body)+ctrlgrp(2))
        cmds.parent(ik_armleg(body), ik_armleg(body)+ctrlgrp(2))
        
    cmds.parent(ik_armleg(bodies[2])+ctrlgrp(2), ik_armleg(bodies[1])+ctrlgrp(2))
    cmds.parent(ik_armleg(bodies[1])+ctrlgrp(2), ik_armleg(bodies[0])+ctrlgrp(2))

    cmds.ikHandle(sj=ik_top, ee=ik_bottom, n=name+"_ikHandle")
    CtrlCreate(name+"_ikHandle", BOX, 9, name, RED, 1)
    cmds.setAttr(name+ctrlgrp()+SCALE+"Y", 0.3)
    cmds.setAttr(name+ctrlgrp()+SCALE+"Z", 0.3)
    cmds.makeIdentity(name+ctrlgrp(), a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.scale(2, 2, 2, name+ctrlgrp())
    cmds.makeIdentity(name+ctrlgrp(), a=True, t=1, r=1, s=1, n=0, pn=1)

    cmds.group(n=ik_handle_grp, em=True)
    match_objs(name+"_ikHandle", ik_handle_grp)
    cmds.parent(name+"_ikHandle", ik_handle_grp)

    cmds.parentConstraint(name+ctrlgrp(), ik_handle_grp, mo=True)


def ik_handle_follow(part, lr, num):
    if part == "Arm":
        ik_joint = "RIG_"+lr+"_Clavicle"+str(num)
    elif part == "Leg":
        ik_joint = "RIG_Spine1"
        
    ik_ctrl = "IK_"+lr+"_"+part+str(num)+ctrlgrp()
    follow_on = ik_ctrl+"_follow_on"
    follow_off = ik_ctrl+"_follow_off"
    
    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(ik_ctrl, grp_name)
    cmds.parent(follow_on, ik_joint)
    cmds.parent(follow_off, "World_ctrl")
    cmds.duplicate(follow_on, n=follow_on+ctrlgrp(2))
    cmds.parent(follow_on, follow_on+ctrlgrp(2))
    cmds.parentConstraint(follow_on, follow_off, ik_ctrl+ctrlgrp(2))

    follow_attr(ik_ctrl, ik_ctrl+ctrlgrp(2), follow_on, follow_off, 0)


def ik_pole_vector(part, lr, num):
    if part == "Arm":
        body = "_Elbow"
    elif part == "Leg":
        body = "_Knee"
    
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    ik_mid = joint_name(2,lr+body,num)
    pole_vector = "IK_PV_"+lr+"_"+part+str(num)
    ik_handle_name = "IK_"+lr+"_"+part+str(num)+"_ikHandle"
    
    CtrlCreate(ik_mid, DIAMOND, 9, pole_vector, RED)
    if part == "Arm":
        tmp = 2 if lr == "L" else -2
        cmds.move(0, 0, tmp*world_scale, pole_vector+ctrlgrp(1), r=True, os=True, wd=True)
    else:
        tmp = -2 if lr == "L" else 2
        cmds.move(0, tmp*world_scale, 0, pole_vector+ctrlgrp(1), r=True, os=True, wd=True)
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

    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(pole_vector+ctrlgrp(1), grp_name)
        cmds.makeIdentity(grp_name, a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parent(follow_on, ik_ctrl)
    cmds.parent(follow_off, "World_ctrl")
    cmds.duplicate(follow_on, n=follow_on+ctrlgrp(2))
    cmds.parent(follow_on, follow_on+ctrlgrp(2))
    cmds.parentConstraint(follow_on, follow_off, pole_vector+ctrlgrp(1))

    follow_attr(pole_vector+ctrlgrp(), pole_vector+ctrlgrp(1), follow_on, follow_off, 0)
        
        
def ik_pole_vector_swivel(part, lr, num):
    if part == "Arm":
        point_obj = joint_name(0,lr+"_Clavicle",num)
        ik_joint = joint_name(2,lr+"_Wrist",num)
    else:
        point_obj = "RIG_Root1"
        ik_joint = joint_name(2,lr+"_Ankle",num)
        
    ik_ctrl = joint_name(2,lr+"_"+part,num)+ctrlgrp()
    pole_vector = "IK_PV_"+lr+"_"+part+str(num)
    follow_on = pole_vector+"_follow_on"
    sub = pole_vector+"_follow_sub"
    aim = pole_vector+"_follow_aim"
    
    add_attrs(ik_ctrl, "swivel", 1)
    
    orient_grp = cmds.group(n=ik_ctrl+"_orient1", em=True)
    match_objs(ik_joint, orient_grp)
    cmds.parent(orient_grp, ik_ctrl)
    cmds.duplicate(orient_grp)
    cmds.parent(ik_ctrl+"_orient2", orient_grp)
    
    for grp_name in [aim, sub, sub+ctrlgrp(2)]:
        cmds.group(n=grp_name, em=True)
    cmds.pointConstraint(point_obj, aim)
    cmds.aimConstraint(ik_ctrl, aim, upVector=[0, 0, 1], wut="objectrotation", wu=[0, 0, 1])
    cmds.connectAttr(ik_ctrl+"_orient2.worldMatrix[0]", aim+"_aimConstraint1.worldUpMatrix")
    
    aim_div = pole_vector+"follow_aim_Divide"
    cmds.shadingNode(MULDIV, n=aim_div, au=True)
    cmds.connectAttr(ik_ctrl+".swivel", aim_div+".input1X")
    idx = 1 if part == "Arm" and lr == "L" else -1
    cmds.setAttr(aim_div+".input2X", idx)
    cmds.connectAttr(aim_div+".outputX", aim+"_aimConstraint1.offsetX")
    
    cmds.parent(sub, sub+ctrlgrp(2))
    cmds.parentConstraint(aim, sub+ctrlgrp(2))
    cmds.parentConstraint(sub, follow_on, mo=True)
    
    for grp_name in [aim, sub+ctrlgrp(2)]:
        cmds.parent(grp_name, "IK_follow_ctrl_grp")


#----------------------------------------------------------------------------#


def ik_armleg_stretch(part, lr, num):
    def stretch_name(type):
        return(joint_name(type,lr+"_"+part,num))

    if part == "Arm":
        mid_names = [lr+"_Shoulder", lr+"_Elbow", lr+"_Wrist"]
    elif part == "Leg":
        mid_names = [lr+"_Hip", lr+"_Knee", lr+"_Ankle"]

    ik_ctrl = stretch_name(2)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    stretch_distance = [stretch_name(4)+"_distance",
                        stretch_name(5)+"_pv_top_distance",
                        stretch_name(5)+"_top_mid_distance",
                        stretch_name(5)+"_pv_bottom_distance",
                        stretch_name(5)+"_mid_bottom_distance"]

    ik_armleg_stretch_distance(part, lr, num, mid_names, stretch_name)
    ik_armleg_stretch_node(part, num, mid_names, stretch_name)

    all_length = cmds.getAttr(stretch_distance[0]+".distance")
    top_length = cmds.getAttr(stretch_distance[2]+".distance")
    bottom_length = cmds.getAttr(stretch_distance[4]+".distance")

    add_attrs(ik_ctrl)
    add_attrs(ik_ctrl, "stretch", 2, 0, 0, 10)
    add_attrs(ik_ctrl, "length_top", 1, 1)
    add_attrs(ik_ctrl, "length_bottom", 1, 1)
    add_attrs(pole_vector_ctrl)
    add_attrs(pole_vector_ctrl, "snap", 2)

    ik_armleg_stretch_prepare(stretch_name, ik_ctrl, all_length)
    ik_armleg_stretch_snap(part, lr, num, stretch_name, mid_names,
                            "top", top_length)
    ik_armleg_stretch_snap(part, lr, num, stretch_name, mid_names,
                            "bottom", bottom_length)

    cmds.orientConstraint(ik_ctrl+"_orient2", joint_name(2,mid_names[2],num)+ctrlgrp(2))
    cmds.connectAttr(ik_ctrl+SCALE, joint_name(2,mid_names[2],num)+ctrlgrp(2)+SCALE)
    

def ik_armleg_stretch_distance(part, lr, num, mid_names, stretch_name):
    ik_top = joint_name(2,mid_names[0],num)+ctrlgrp(2)
    ik_mid = joint_name(2,mid_names[1],num)+ctrlgrp(2)
    ik_ctrl = joint_name(2,lr+"_"+part,num)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    
    stretch_loc = [stretch_name(4)+"_top_loc", stretch_name(4)+"_bottom_loc",
                    stretch_name(5)+"_pv_loc", stretch_name(4)+"_mid_loc"]
    stretch_distance = [stretch_name(4)+"_distance",
                        stretch_name(5)+"_pv_top_distance",
                        stretch_name(5)+"_top_mid_distance",
                        stretch_name(5)+"_pv_bottom_distance",
                        stretch_name(5)+"_mid_bottom_distance"]
    trans = []
    for name in [ik_top, ik_ctrl, pole_vector_ctrl, ik_mid]:
        trans.append(cmds.xform(name, q=True, piv=True, ws=True)[0:3])
    for idx, loc_name in enumerate(stretch_loc):
        cmds.spaceLocator(n=loc_name)
    idx = 0
    for ctrl_name in [ik_top, ik_ctrl, pole_vector_ctrl, ik_mid]:
        cmds.parentConstraint(ctrl_name, stretch_loc[idx])
        idx += 1
    
    for dist_name in stretch_distance:
        cmds.shadingNode(DIST, n=dist_name, au=True)
    for idx in range(3):
        cmds.connectAttr(stretch_loc[0]+TRANSLATE, stretch_distance[idx]+".point1")
        cmds.connectAttr(stretch_loc[idx+1]+TRANSLATE, stretch_distance[idx]+".point2")
        if idx != 0:
            cmds.connectAttr(stretch_loc[1]+TRANSLATE, stretch_distance[idx+2]+".point1")
            cmds.connectAttr(stretch_loc[idx+1]+TRANSLATE, stretch_distance[idx+2]+".point2")
    for idx, value in enumerate([1, 3]):
        cmds.disconnectAttr(stretch_loc[idx]+TRANSLATE, stretch_distance[value]+".point1")
        cmds.disconnectAttr(stretch_loc[2]+TRANSLATE, stretch_distance[value]+".point2")
        cmds.connectAttr(stretch_loc[idx]+"Shape.worldPosition[0]", stretch_distance[value]+".point1")
        cmds.connectAttr(stretch_loc[2]+"Shape.worldPosition[0]", stretch_distance[value]+".point2")
            
    mid_name = lr+"_"+part+str(num)
    messure_grp = joint_name(4,lr+"_"+part,num)+"_messure_grp"
    cmds.group(n=messure_grp, em=True)
    cmds.parent(stretch_loc, messure_grp)
    cmds.parent(messure_grp, "IK_messure_ctrl_grp")


def ik_armleg_stretch_node(part, num, mid_names, stretch_name):
    prepare_div = stretch_name(4)+"_10into1_Divide"
    messure_div = stretch_name(4)+"_messure_Divide"
    stretch_blendtwo = stretch_name(4)+"_BlendTwo"
    snap_rev = stretch_name(5)+"_rev_Multiply"

    for grp_name in [prepare_div, messure_div, snap_rev]:
        cmds.shadingNode(MULDIV, n=grp_name, au=True)
    for grp_name in [prepare_div, messure_div]:
        cmds.setAttr(grp_name+".operation", 2)
    cmds.shadingNode(BLENDTWO, n=stretch_blendtwo, au=True)
    cmds.connectAttr("World_ctrl.scaleY", snap_rev+".input1X")
    cmds.setAttr(snap_rev+".input2X", -1)

    ik_armleg_stretch_node_pos(part, num, mid_names, "top")
    ik_armleg_stretch_node_pos(part, num, mid_names, "bottom")


def ik_armleg_stretch_node_pos(part, num, mid_names, pos):
    idx = 1 if pos == "top" else 2
    
    messure_mul = joint_name(4,mid_names[idx],num)+"_messure_"+pos+"_Multiply"
    stretch_mul = joint_name(4,mid_names[idx],num)+"_"+pos+"_Multiply"
    snap_div = joint_name(5,mid_names[idx],num)+"_messure_"+pos+"_Divide"
    snap_blendtwo = joint_name(5,mid_names[idx],num)+"_"+pos+"_BlendTwo"

    for div_name in [messure_mul, stretch_mul, snap_div]:
        cmds.shadingNode(MULDIV, n=div_name, au=True)
    cmds.setAttr(snap_div+".operation", 2)
    cmds.shadingNode(BLENDTWO, n=snap_blendtwo, au=True)


def ik_armleg_stretch_prepare(stretch_name, ik_ctrl, all_length):
    prepare_div = stretch_name(4)+"_10into1_Divide"
    messure_div = stretch_name(4)+"_messure_Divide"
    stretch_blendtwo = stretch_name(4)+"_BlendTwo"

    cmds.connectAttr(ik_ctrl+".stretch", prepare_div+".input1X")
    cmds.setAttr(prepare_div+".input2X", 10)
    cmds.connectAttr(prepare_div+".outputX", stretch_blendtwo+".attributesBlender")
    cmds.setAttr(stretch_blendtwo+".input[0]", all_length)
    
    cmds.connectAttr(stretch_name(4)+"_distance.distance", stretch_blendtwo+".input[1]")
    cmds.connectAttr(stretch_blendtwo+".output", messure_div+".input1X")
    cmds.setAttr(messure_div+".input2X", all_length)
    

def ik_armleg_stretch_snap(part, lr, num, stretch_name, mid_names,
                            position, length):
    ik_ctrl = stretch_name(2)+ctrlgrp()
    pole_vector_ctrl = "IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()
    messure_div = stretch_name(4)+"_messure_Divide"
    length_attr = ".length_"+position
    snap_rev = stretch_name(5)+"_rev_Multiply"

    if position == "top":
        messure_mul = joint_name(4,mid_names[1],num)+"_messure_top_Multiply"
        stretch_mul = joint_name(4,mid_names[1],num)+"_top_Multiply"
        snap_div = joint_name(5,mid_names[1],num)+"_messure_top_Divide"
        snap_blendtwo = joint_name(5,mid_names[1],num)+"_top_BlendTwo"
        stretch_distance = stretch_name(5)+"_pv_top_distance"
        mid = mid_names[1]
    else:
        messure_mul = joint_name(4,mid_names[2],num)+"_messure_bottom_Multiply"
        stretch_mul = joint_name(4,mid_names[2],num)+"_bottom_Multiply"
        snap_div = joint_name(5,mid_names[2],num)+"_messure_bottom_Divide"
        snap_blendtwo = joint_name(5,mid_names[2],num)+"_bottom_BlendTwo"
        stretch_distance = stretch_name(5)+"_pv_bottom_distance"
        mid = mid_names[2]

    cmds.connectAttr(messure_div+".outputX", stretch_mul+".input1X")
    cmds.connectAttr(ik_ctrl+length_attr, messure_mul+".input1X")
    length = length if lr == "L" else -length
    cmds.setAttr(messure_mul+".input2X", length)
    cmds.connectAttr(messure_mul+".outputX", stretch_mul+".input2X")
    cmds.connectAttr(stretch_mul+".outputX", snap_blendtwo+".input[0]")

    cmds.connectAttr(pole_vector_ctrl+".snap", snap_blendtwo+".attributesBlender")
    cmds.connectAttr(stretch_distance+".distance", snap_div+".input1X")
    if lr == "L":
        cmds.connectAttr("World_ctrl.scaleY", snap_div+".input2X")
    else:
        cmds.connectAttr(snap_rev+".outputX", snap_div+".input2X")
    cmds.connectAttr(snap_div+".outputX", snap_blendtwo+".input[1]")
    cmds.connectAttr(snap_blendtwo+".output", joint_name(2,mid,num)+ctrlgrp(2)+TRANSLATE+"X")


#----------------------------------------------------------------------------#


def ik_armleg_grouping(part, end_num):
    if part == "Arm":
        bodies = ["_Shoulder", "_Elbow"]
    else:
        bodies = ["_Hip", "_Knee"]
        
    handle_grp = "IK_"+part+"_ikHandle"+ctrlgrp(2)
    ctrl_grp = "IK_"+part+ctrlgrp(2)
    pv_grp = "IK_PV_"+part+ctrlgrp(2)
    
    for grp_name in [handle_grp, ctrl_grp, pv_grp]:
        cmds.group(n=grp_name, em=True)
    for lr in LFRT:
        for num in range(1, end_num+1):
            if part == "Arm":
                upper = joint_name(0,lr+"_Clavicle",num)
            else:
                upper = "RIG_Spine1"
            cmds.parent(joint_name(2,lr+"_"+part,num)+"_ikHandle"+ctrlgrp(2), handle_grp)
            cmds.parent(joint_name(2,lr+"_"+part,num)+ctrlgrp(1), ctrl_grp)
            cmds.parent("IK_PV_"+lr+"_"+part+str(num)+ctrlgrp(1), pv_grp)
            cmds.parent(joint_name(0,lr+bodies[0],num), upper)
            cmds.parent(joint_name(1,lr+bodies[0],num), upper)
            cmds.parent(joint_name(2,lr+bodies[0],num)+ctrlgrp(2), upper)
            for body in bodies:
                each_bc = joint_name(0,lr+body,num)+"_BlendColors"
                cmds.shadingNode(BLENDCOLORS, n=each_bc, au=True)
                cmds.connectAttr(joint_name(2,lr+body,num)+SCALE, each_bc+".color1")
                cmds.connectAttr(joint_name(1,lr+body,num)+SCALE, each_bc+".color2")
                cmds.connectAttr(each_bc+".output", joint_name(0,lr+body,num)+SCALE)
                cmds.connectAttr("FKIK_"+lr+"_"+part+str(num)+ctrlgrp()+".FKIK", each_bc+".blender")
    cmds.connectAttr("World_ctrl"+SCALE, handle_grp+SCALE)
    cmds.parent(handle_grp, "extra_grp")
    cmds.parent(ctrl_grp, pv_grp, "IK_ctrl_grp")


def ik_finger_grouping(lr, num):
    base_num = cmds.intField(basefinger, q=True, v=True)
    lr_handle_grp = joint_name(2,lr+"_Finger",num)+"_ikHandle"+ctrlgrp(2)
    lr_ik_grp = joint_name(2,lr+"_Finger",num)+ctrlgrp(1)
    lr_pv_grp = "IK_PV_"+lr+"_Finger"+str(num)+ctrlgrp(1)
    
    for grp_name in [lr_handle_grp, lr_ik_grp, lr_pv_grp]:
        cmds.group(n=grp_name, em=True)
        cmds.parentConstraint(joint_name(0,lr+"_Wrist",num), grp_name)
    for base in range(1, base_num+1):
        name = joint_name(2,lr+"_Finger",num)+"_"+str(base)
        pv = "IK_PV_"+lr+"_Finger"+str(num)+"_"+str(base)
        cmds.parent(name+"_ikHandle"+ctrlgrp(2), lr_handle_grp)
        cmds.parent(name+"_master"+ctrlgrp(1), lr_ik_grp)
        cmds.parent(pv+ctrlgrp(1)+ctrlgrp(2), lr_pv_grp)
        

#----------------------------------------------------------------------------#


def ik_ribbon(part, lr, num):
    if part == "Arm":
        bodies = [lr+"_Shoulder", lr+"_Elbow", lr+"_Wrist"]
    else:
        bodies = [lr+"_Hip", lr+"_Knee", lr+"_Ankle"]
    
    top_trans = cmds.xform(joint_name(0,bodies[0],num), q=True, piv=True, ws=True)[0:3]
    mid_trans = cmds.xform(joint_name(0,bodies[1],num), q=True, piv=True, ws=True)[0:3]
    bottom_trans = cmds.xform(joint_name(0,bodies[2],num), q=True, piv=True, ws=True)[0:3]
    name = joint_name(6,lr+"_"+part,num)
    
    ik_ribbon_group(name, bodies)
    ik_ribbon_skin(part, lr, num, bodies)
    ik_ribbon_ctrl(part, lr, num)
    ik_ribbon_twist(part, lr, num)
    ik_ribbon_volume(part, lr, num, bodies)
    ik_ribbon_sine(name)
    ik_ribbon_fix_mid(name)
    ik_ribbon_position(part, lr, num, bodies)
    
    print "Create "+lr+" "+part+str(num)+" Ribbbon"
    
    
#----------------------------------------------------------------------------#


def ik_ribbon_group(name, bodies):
    skin_grp = name+"_skin"+ctrlgrp(2)
    volume_grp = name+"_volume"+ctrlgrp(2)
    surface_grp = name+"_surface"+ctrlgrp(2)
    deformer_grp = name+"_deformer"+ctrlgrp(2)
    ctrl_grp = name+ctrlgrp(1)
    ribbon_grp = name+ctrlgrp(2)

    for grp_name in [skin_grp, volume_grp, surface_grp, deformer_grp,
                    ctrl_grp, ribbon_grp]:
        cmds.group(n=grp_name, em=True)
    for grp_name in [ctrl_grp, skin_grp, volume_grp,
                    surface_grp, deformer_grp]:
        cmds.parent(grp_name, ribbon_grp)

        
def ik_ribbon_skin(part, lr, num, bodies):
    name = joint_name(6,lr+"_"+part,num)
    geo = name+"_geo"
    ribbon_grp = name+ctrlgrp(2)
    skin_grp = name+"_skin"+ctrlgrp(2)
    
    width = cmds.getAttr(joint_name(0,bodies[1],num)+TRANSLATE+"X") + cmds.getAttr(joint_name(0,bodies[2],num)+TRANSLATE+"X")
    cmds.nurbsPlane(n=geo, ax=[0, 1, 0], w=width, lr=0.1, d=3, u=8, v=1, ch=1)
    for idx in [".u[0.505]", ".u[0.495]"]:
        cmds.select(geo+idx, r=True)
        cmds.insertKnotSurface(geo+idx, ch=1, nk=1, add=1, ib=0, rpo=1)
    cmds.delete(geo, ch=True)
    cmds.parent(geo, ribbon_grp)
    ik_ribbon_follicle(part, lr, geo, skin_grp, name, "_skin")


def ik_ribbon_follicle(part, lr, geo, grp, name, type):
    for idx in range(1, 10):
        follicle_name = name+type+str(idx)
        follicle_shape = follicle_name+"_shape"
        follicle_joint = follicle_name+"_jnt"
        par_num = float(1.0/8)*(idx-1)
        
        cmds.createNode("follicle", n=follicle_shape)
        cmds.rename("follicle1", follicle_name)
        cmds.parent(follicle_name, grp)
        
        cmds.connectAttr(follicle_shape+".outRotate", follicle_name+".rotate")
        cmds.connectAttr(follicle_shape+".outTranslate", follicle_name+".translate")
        cmds.connectAttr(geo+"Shape.local", follicle_shape+".inputSurface")
        cmds.connectAttr(geo+"Shape.worldMatrix[0]", follicle_shape+".inputWorldMatrix")
        cmds.setAttr(follicle_shape+".simulationMethod", 0)
        cmds.setAttr(follicle_shape+".parameterU", par_num)
        if type == "_skin":
            cmds.setAttr(follicle_shape+".parameterV", 0.5)
        cmds.hide(follicle_shape)
        
        if type == "_skin":
            CtrlCreate(follicle_name, SQUARE, 9, name+"_"+str(idx), PINK)
            cmds.scale(0.3, 0.3, 0.3, name+"_"+str(idx)+ctrlgrp()+".cv[0:4]", r=True, ocp=True)
            cmds.parent(name+"_"+str(idx)+ctrlgrp(1), follicle_name)
            cmds.joint(name+"_"+str(idx)+ctrlgrp(), n=follicle_joint)
            cmds.connectAttr("World_ctrl"+SCALE, follicle_name+SCALE)
            cmds.setAttr(name+"_"+str(idx)+ctrlgrp(1)+ROTATE+"X", 180)
            if part == "Leg":
                cmds.setAttr(name+"_"+str(idx)+ctrlgrp(1)+ROTATE+"X", -90)
            if lr == "R":
                cmds.setAttr(name+"_"+str(idx)+ctrlgrp(1)+ROTATE+"Z", 180)


#----------------------------------------------------------------------------#


def ik_ribbon_ctrl(part, lr, num):
    name = joint_name(6,lr+"_"+part,num)
    geo = name+"_geo"
    twist_geo = name+"_twist_geo"
    sine_geo = name+"_sine_geo"
    squash_geo = name+"_squash_geo"
    surface_grp = name+"_surface"+ctrlgrp(2)
    deformer_grp = name+"_deformer"+ctrlgrp(2)
    
    nb = 1
    for idx in range(1, 10, 2):
        follicle_name = name+"_skin"+str(idx)
        follicle_joint = follicle_name+"_jnt"
        follicle_bind = name+"_"+str(nb)+"_jnt"
        cmds.duplicate(follicle_joint, n=follicle_bind, po=True)
        nb += 1
    
    objs = []
    tmp = ["_start", "_upper", "_mid", "_lower", "_end"]
    for idx in range(1, 6):
        follicle_bind = name+"_"+str(idx)+"_jnt"
        CtrlCreate(follicle_bind, DIA, 9, name+tmp[idx-1], PINK_RED)
        cmds.scale(0.6, 0.6, 0.6, name+tmp[idx-1]+"_ctrl.cv[0:16]", r=True, ocp=True)
        cmds.parent(follicle_bind, name+tmp[idx-1]+ctrlgrp())
        cmds.parent(name+tmp[idx-1]+ctrlgrp(1), name+ctrlgrp(1))
        objs.append(follicle_bind)
        
    for grp_name in [twist_geo, sine_geo, squash_geo]:
        cmds.duplicate(geo, n=grp_name)
        cmds.parent(grp_name, surface_grp)
    cmds.blendShape(twist_geo, sine_geo, geo, n=name+"_blendshape", ex="characterPartition")
    for grp_name in [twist_geo, sine_geo]:
        cmds.setAttr(name+"_blendshape."+grp_name, 1)
    cmds.skinCluster(objs, geo, n=name+"_bind", mi=2)
    
    nb = ik_ribbon_deformer_num(part, lr, num)
    for grp_name in ["twist", "sine", "squash"]:
        cmds.nonLinear(name+"_"+grp_name+"_geo", type=grp_name, n="test")
        cmds.rename(grp_name+str(nb), name+"_"+grp_name)
        cmds.rename(grp_name+str(nb)+"Handle", name+"_"+grp_name+"_handle")
        
        cmds.setAttr(name+"_"+grp_name+"_handle"+ROTATE+"Z", -90)
        cmds.parent(name+"_"+grp_name+"_handle", deformer_grp)


def ik_ribbon_deformer_num(part, lr, num):
    num_arm = cmds.intField(arm, q=True, v=True)
    num_leg = cmds.intField(leg, q=True, v=True)
    
    idx = num
    if cmds.checkBox(arm_check, q=True, v=True):
        if part == "Leg":
            idx += num_arm*2
    if lr == "R":
        mul = num_arm if part == "Arm" else num_leg
        idx += mul
    return(idx)
    
    
#----------------------------------------------------------------------------#


def ik_ribbon_twist(part, lr, num):
    name = joint_name(6,lr+"_"+part,num)
    tmp = ["_start", "_mid", "_end"]
    bottom_ctrl = name+tmp[1]+ctrlgrp()
    top_mdl = name+tmp[0]+"_MultDoubleLinear"
    bottom_mdl = name+tmp[2]+"_MultDoubleLinear"
    
    for idx, grp_name in enumerate([tmp[0], tmp[2]]):
        add_attrs(name+grp_name+ctrlgrp())
        add_attrs(name+grp_name+ctrlgrp(), "twist", 1)
        add_attrs(name+grp_name+ctrlgrp(), "twist_offset", 1)
        add_attrs(name+grp_name+ctrlgrp(), "twist_affect_to_mid", 2, 10, 0, 10)
    add_attrs(bottom_ctrl)
    add_attrs(bottom_ctrl, "twist_roll", 1)
    add_attrs(bottom_ctrl, "twist_roll_offset", 1)
    
    for idx, grp_name in enumerate([tmp[0], tmp[2]]):
        twist_sum = name+grp_name+"_Sum"
        top_ctrl = name+tmp[idx*2]+ctrlgrp()
        
        cmds.shadingNode(PLUSMIN, n=twist_sum, au=True)
        cmds.connectAttr(top_ctrl+".twist", twist_sum+".input1D[0]")
        cmds.connectAttr(top_ctrl+".twist_offset", twist_sum+".input1D[1]")
        cmds.connectAttr(bottom_ctrl+".twist_roll", twist_sum+".input1D[2]")
        cmds.connectAttr(bottom_ctrl+".twist_roll_offset", twist_sum+".input1D[3]")

    if lr == "R":
        tmp = tmp[::-1]
    cmds.connectAttr(name+tmp[0]+"_Sum.output1D", name+"_twist.startAngle")
    cmds.connectAttr(name+tmp[2]+"_Sum.output1D", name+"_twist.endAngle")
    cmds.shadingNode("multDoubleLinear", n=top_mdl, au=True)
    cmds.setAttr(top_mdl+".input1", -0.1)
    cmds.connectAttr(name+tmp[0]+ctrlgrp()+".twist_affect_to_mid", top_mdl+".input2")
    cmds.connectAttr(top_mdl+".output", name+"_twist.lowBound")
    cmds.shadingNode("multDoubleLinear", n=bottom_mdl, au=True)
    cmds.setAttr(bottom_mdl+".input1", 0.1)
    cmds.connectAttr(name+tmp[2]+ctrlgrp()+".twist_affect_to_mid", bottom_mdl+".input2")
    cmds.connectAttr(bottom_mdl+".output", name+"_twist.highBound")


def ik_ribbon_volume(part, lr, num, bodies):
    name = joint_name(6,lr+"_"+part,num)
    mid_ctrl = name+"_mid"+ctrlgrp()
    squash_geo = name+"_squash_geo"
    volume_grp = name+"_volume"+ctrlgrp(2)
    vol_rev = name+"_rev_Multiply"
    vol_mul = name+"_Multiply"
    vol_scale_sum = name+"_scale_Sum"
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    add_attrs(mid_ctrl)
    add_attrs(mid_ctrl, "volume", 2, 0, -1, 1)
    add_attrs(mid_ctrl, "volume_multiplier", 2, 1, 0.1, 10)
    add_attrs(mid_ctrl, "volume_start_dropoff", 2, 1, 0, 1)
    add_attrs(mid_ctrl, "volume_end_dropoff", 2, 1, 0, 1)
    add_attrs(mid_ctrl, "volume_scale", 1)
    add_attrs(mid_ctrl, "volume_position", 2, 0, -10, 10)

    ik_ribbon_follicle(part, lr, squash_geo, volume_grp, name, "_volume")
    attr_num = cmds.getAttr(name+"_volume1"+TRANSLATE+"Z")
    cmds.setAttr(squash_geo+TRANSLATE+"Z", -attr_num)
    cmds.setAttr(name+"_squash_handle"+TRANSLATE+"Z", -attr_num)
    
    cmds.shadingNode(MULDIV, name=vol_rev, au=True)
    cmds.shadingNode(MULDIV, name=vol_mul, au=True)
    cmds.shadingNode(PLUSMIN, n=vol_scale_sum, au=True)
    
    cmds.connectAttr(mid_ctrl+".volume", vol_rev+".input1X")
    cmds.setAttr(vol_rev+".input2X", -1)
    cmds.connectAttr(vol_rev+".outputX", name+"_squash.factor")
    
    attr = ["startSmoothness", "endSmoothness"] if lr == "L" else ["endSmoothness", "startSmoothness"]
    cmds.connectAttr(mid_ctrl+".volume_start_dropoff", name+"_squash."+attr[0])
    cmds.connectAttr(mid_ctrl+".volume_end_dropoff", name+"_squash."+attr[1])
    
    cmds.connectAttr(mid_ctrl+".volume_scale", vol_mul+".input1X")
    cmds.setAttr(vol_mul+".input2X", world_scale)
    cmds.connectAttr(vol_mul+".outputX", vol_scale_sum+".input1D[0]")
    cmds.setAttr(vol_scale_sum+".input1D[1]", cmds.getAttr(name+"_squash_handle"+SCALE+"X"))
    cmds.connectAttr(vol_scale_sum+".output1D", name+"_squash_handle"+SCALE+"Y")
    
    width = cmds.getAttr(joint_name(0,bodies[1],num)+TRANSLATE+"X") + cmds.getAttr(joint_name(0,bodies[2],num)+TRANSLATE+"X")
    for idx in [-1, 1]:
        cmds.setAttr(mid_ctrl+".volume_position", 10*idx)
        cmds.setAttr(name+"_squash_handle"+TRANSLATE+"X", width*idx)
        cmds.setDrivenKeyframe(name+"_squash_handle"+TRANSLATE+"X", cd=mid_ctrl+".volume_position")
    cmds.setAttr(mid_ctrl+".volume_position", 0)
    
    for idx in range(1, 10):
        follicle_name = name+"_volume"+str(idx)
        fol_mul = follicle_name+"_Multiply"
        fol_sum = follicle_name+"_Sum"
        fol_rev = follicle_name+"_rev_Multiply"
        
        cmds.shadingNode(MULDIV, name=fol_mul, au=True)
        cmds.shadingNode(PLUSMIN, name=fol_sum, au=True)
        
        cmds.connectAttr(mid_ctrl+".volume_multiplier", fol_mul+".input1Z")
        cmds.connectAttr(follicle_name+TRANSLATE, fol_mul+".input2")
        cmds.setAttr(fol_sum+".input1D[0]", 1)
        if lr == "L":
            cmds.connectAttr(fol_mul+".outputZ", fol_sum+".input1D[1]")
        else:
            cmds.shadingNode(MULDIV, name=fol_rev, au=True)
            cmds.connectAttr(fol_mul+".outputZ", fol_rev+".input1X")
            cmds.setAttr(fol_rev+".input2X", -1)
            cmds.connectAttr(fol_rev+".outputX", fol_sum+".input1D[1]")
        cmds.connectAttr(fol_sum+".output1D", name+"_"+str(idx)+ctrlgrp(1)+SCALE+"Y")
        cmds.connectAttr(fol_sum+".output1D", name+"_"+str(idx)+ctrlgrp(1)+SCALE+"Z")


def ik_ribbon_sine(name):
    mid_ctrl = name+"_mid"+ctrlgrp()
    
    add_attrs(mid_ctrl)
    add_attrs(mid_ctrl, "sine_amplitude", 1)
    add_attrs(mid_ctrl, "sine_wavelength", 1, 2)
    add_attrs(mid_ctrl, "sine_offset", 1)
    add_attrs(mid_ctrl, "sine_twist", 1)
    
    cmds.connectAttr(mid_ctrl+".sine_amplitude", name+"_sine.amplitude")
    cmds.connectAttr(mid_ctrl+".sine_wavelength", name+"_sine.wavelength")
    cmds.connectAttr(mid_ctrl+".sine_offset", name+"_sine.offset")
    cmds.connectAttr(mid_ctrl+".sine_twist", name+"_sine_handle"+ROTATE+"Y")
    
    cmds.setAttr(name+"_sine.dropoff", 1)


#----------------------------------------------------------------------------#
        

def ik_ribbon_fix_mid(name):
    for idx in range(5, 0, -2):
        follicle_name = name+"_skin"+str(idx)
        follicle_bind = name+"_"+str(idx)+"_jnt"
        follicle_fix = name+"_"+str(idx)+"_fix"
        cmds.duplicate(follicle_bind, n=follicle_fix, po=True)
    cmds.duplicate(name+"_3_fix", n=name+"_5_fix_end")
    cmds.rename(name+"_1_fix", name+"_3_fix_end")
    cmds.parent(name+"_3_fix_end", name+"_3_fix")
    cmds.parent(name+"_5_fix_end", name+"_5_fix")
    cmds.parent(name+"_3_fix", w=True)
    cmds.parent(name+"_5_fix", w=True)
    
    for idx in [3, 5]:
        cmds.ikHandle(sj=name+"_"+str(idx)+"_fix", ee=name+"_"+str(idx)+"_fix_end", n=name+"_"+str(idx)+"_fix_ikhandle")
        cmds.skinCluster(name+"_geo", e=True, lw=True, wt=0, ai=name+"_"+str(idx)+"_fix")
    for idx in range(4):
        cmds.skinPercent(name+"_bind", name+"_geo.cv[4]["+str(idx)+"]", tv=[(name+"_3_fix", 0.5)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[4]["+str(idx)+"]", tv=[(name+"_3_jnt", 0)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[5]["+str(idx)+"]", tv=[(name+"_3_fix", 1)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[10]["+str(idx)+"]", tv=[(name+"_5_fix", 0.5)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[10]["+str(idx)+"]", tv=[(name+"_5_jnt", 0)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[11]["+str(idx)+"]", tv=[(name+"_5_fix", 1)])
        cmds.skinPercent(name+"_bind", name+"_geo.cv[12]["+str(idx)+"]", tv=[(name+"_5_fix", 1)])

    cmds.parent(name+"_3_fix_ikhandle", name+"_1_jnt")
    cmds.parent(name+"_5_fix_ikhandle", name+"_3_jnt")
    cmds.parent(name+"_3_fix", name+"_mid_ctrl")
    cmds.parent(name+"_5_fix", name+"_end_ctrl")
    
    
def ik_ribbon_position(part, lr, num, bodies):
    name = joint_name(6,lr+"_"+part,num)
    grp_names = [name+"_upper", name+"_lower"]
    grp_bc = name+"_BlendColors"
    grp_div = name+"_10into1_Divide"
        
    tmp = ["_start", "_mid", "_end"]
    for idx, body in enumerate(bodies):
        cmds.parentConstraint(joint_name(0,body,num), name+tmp[idx]+ctrlgrp(1))
        cmds.connectAttr(joint_name(0,body,num)+SCALE, name+tmp[idx]+ctrlgrp(1)+SCALE)
    
    cmds.pointConstraint(name+"_1_jnt", name+"_3_jnt", grp_names[0]+ctrlgrp(1))
    cmds.pointConstraint(name+"_3_jnt", name+"_5_jnt", grp_names[1]+ctrlgrp(1))
    cmds.scaleConstraint(name+"_1_jnt", name+"_3_jnt", grp_names[0]+ctrlgrp(1))
    cmds.scaleConstraint(name+"_3_jnt", name+"_5_jnt", grp_names[1]+ctrlgrp(1))
    
    cmds.shadingNode(BLENDCOLORS, n=grp_bc, au=True)
    cmds.shadingNode(MULDIV, n=grp_div, au=True)
    cmds.setAttr(grp_div+".operation", 2)
    cmds.connectAttr("IK_PV_"+lr+"_"+part+str(num)+ctrlgrp()+".follow", grp_div+".input1X")
    cmds.setAttr(grp_div+".input2X", 10)
    cmds.connectAttr(grp_div+".outputX", grp_bc+".blender")
    cmds.connectAttr(joint_name(2,lr+"_"+part,num)+ctrlgrp()+".swivel", grp_bc+".color1R")
    
    for idx, grp_name in enumerate(grp_names):
        cmds.group(n=grp_name+"_aim", em=True)
        cmds.group(n=grp_name+"_aimpoint", em=True)
        match_objs(grp_name+ctrlgrp(1), grp_name+"_aim")
        match_objs(name+"_"+str(3+idx*2)+"_jnt", grp_name+"_aimpoint")
        cmds.parent(grp_name+"_aim", grp_name+ctrlgrp(1))
        cmds.parent(grp_name+ctrlgrp(), grp_name+"_aim")
        cmds.parent(grp_name+"_aimpoint", name+"_"+str(3+idx*2)+"_jnt")
        cmds.duplicate(grp_name+"_aimpoint", n=grp_name+"_aimpoint"+ctrlgrp(2))
        cmds.parent(grp_name+"_aimpoint", grp_name+"_aimpoint"+ctrlgrp(2))
        cmds.connectAttr(grp_bc+".outputR", grp_name+"_aimpoint"+ROTATE+"X")
        
    aimVector = [1, 0, 0] if lr == "L" else [-1, 0, 0]
    upVector = [0, 1, 0] if part == "Arm" else [0, 0, 1]
    worldUp = [0, 1, 0] if part == "Arm" else [0, 0, 1]
    for idx in range(2):
        cmds.aimConstraint(name+"_"+str(3+idx*2)+"_jnt", grp_names[idx]+"_aim", wut="objectrotation", aim=aimVector, u=upVector, wu=worldUp)
        cmds.connectAttr(grp_names[idx]+"_aimpoint.worldMatrix[0]", grp_names[idx]+"_aim_aimConstraint1.worldUpMatrix")
    cmds.duplicate(name+"_skin4_jnt", n=name+"_skin4_jnt_sub")
    cmds.pointConstraint(name+"_skin5_jnt", name+"_skin4_jnt_sub")
    
    for idx in range(1, 10):
        cmds.duplicate(name+"_"+str(idx)+ctrlgrp(1), n=name+"_"+str(idx)+ctrlgrp(2), po=True)
        cmds.parent(name+"_"+str(idx)+ctrlgrp(1), name+"_"+str(idx)+ctrlgrp(2))
    for idx in range(1, 10, 4):
        cmds.connectAttr(joint_name(0,bodies[(idx-1)/3],num)+SCALE, name+"_"+str(idx)+ctrlgrp(2)+SCALE)
    for idx in range(2, 5):
        cmds.scaleConstraint(name+"_1"+ctrlgrp(2), name+"_5"+ctrlgrp(2), name+"_"+str(idx)+ctrlgrp(2))
    for idx in range(6, 9):
        cmds.scaleConstraint(name+"_5"+ctrlgrp(2), name+"_9"+ctrlgrp(2), name+"_"+str(idx)+ctrlgrp(2))
        
    cmds.setAttr(name+"_2"+ctrlgrp(2)+"_scaleConstraint1."+name+"_1"+ctrlgrp(2)+"W0", 2)
    cmds.setAttr(name+"_4"+ctrlgrp(2)+"_scaleConstraint1."+name+"_5"+ctrlgrp(2)+"W1", 2)
    cmds.setAttr(name+"_6"+ctrlgrp(2)+"_scaleConstraint1."+name+"_5"+ctrlgrp(2)+"W0", 2)
    cmds.setAttr(name+"_8"+ctrlgrp(2)+"_scaleConstraint1."+name+"_9"+ctrlgrp(2)+"W1", 2)
    cmds.parent(name+ctrlgrp(2), "Ribbon_grp")
    cmds.connectAttr("World_ctrl"+SCALE, name+ctrlgrp(1)+SCALE)

    cmds.duplicate(name+"_lower_aim", n=name+"_lower_x_grp", po=True)
    cmds.duplicate(name+"_lower_aim", n=name+"_lower_z_grp", po=True)
    cmds.parent(name+"_lower_ctrl", name+"_lower_x_grp")
    cmds.parent(name+"_lower_x_grp", name+"_lower_z_grp")
    cmds.parent(name+"_lower_z_grp", name+"_lower_aim")
    
    cmds.shadingNode(MULDIV, n=name+"_rot_Divide", au=True)
    cmds.setAttr(name+"_rot_Divide.operation", 2)
    cmds.connectAttr(name+"_9"+ctrlgrp(1)+ROTATE+"X", name+"_rot_Divide.input1X")
    cmds.connectAttr(name+"_9"+ctrlgrp(1)+ROTATE+"X", name+"_rot_Divide.input1Y")
    cmds.setAttr(name+"_rot_Divide.input2X", 2)
    cmds.setAttr(name+"_rot_Divide.input2Y", -2)
    cmds.connectAttr(name+"_rot_Divide.outputX", name+"_8"+ctrlgrp(1)+ROTATE+"X")
    cmds.connectAttr(name+"_rot_Divide.outputY", name+"_lower_x_grp"+ROTATE+"X")

    cmds.shadingNode(MULDIV, n=name+"_rot_Multiply", au=True)
    cmds.connectAttr(name+"_9"+ctrlgrp(1)+ROTATE+"Z", name+"_rot_Multiply.input1X")
    cmds.setAttr(name+"_rot_Multiply.input2X", -1)
    cmds.connectAttr(name+"_rot_Multiply.outputX", name+"_lower_aimpoint"+ROTATE+"Z")

    end_name = "_Wrist" if part == "Arm" else "_Ankle"
    cmds.pointConstraint(joint_name(0,lr+end_name,num), name+"_9"+ctrlgrp(1))
    cmds.connectAttr(joint_name(0,lr+end_name,num)+ROTATE, name+"_9"+ctrlgrp(1)+ROTATE)

    for idx in range(1, 6):
        cmds.hide(name+"_"+str(idx)+"_jnt")
        if idx in [3, 5]:
            cmds.hide(name+"_"+str(idx)+"_fix")
    cmds.hide(name+"_volume_grp", name+"_surface_grp", name+"_deformer_grp")


#----------------------------------------------------------------------------#
    
    
def ik_finger_handle(lr, num, base):
    sub_num = cmds.intField(subfinger, q=True, v=True)
    
    name = joint_name(2,lr+"_Finger",num)+"_"+str(base)
    ik_handle_grp = name+"_ikHandle"+ctrlgrp(2)
    ik_start = name+"_1"
    ik_end = name+"_"+str(sub_num+1)
    cmds.ikHandle(sj=ik_start, ee=ik_end, n=name+"_ikHandle")
    CtrlCreate(name+"_ikHandle", CIRCLE, 9, name, RED, 1)
    cmds.scale(0.1, 0.1, 0.1, name+ctrlgrp())
    match_objs(ik_end, name+ctrlgrp(1))
    cmds.makeIdentity(name+ctrlgrp(), a=True, t=1, r=1, s=1, n=0, pn=1)
    
    cmds.group(n=ik_handle_grp, em=True)
    match_objs(name+"_ikHandle", ik_handle_grp)
    cmds.parent(name+"_ikHandle", ik_handle_grp)
    cmds.parentConstraint(name+ctrlgrp(), ik_handle_grp, mo=True)
    
    cmds.duplicate(name+ctrlgrp(), n=name+"_master"+ctrlgrp())
    cmds.duplicate(name+ctrlgrp(1), n=name+"_master"+ctrlgrp(1), po=True)
    cmds.parent(name+"_master"+ctrlgrp(), name+"_master"+ctrlgrp(1))
    cmds.scale(1.5, 1.5, 1.5, name+"_master"+ctrlgrp(1))
    cmds.makeIdentity(name+"_master"+ctrlgrp(1), a=True, s=1, n=0, pn=1)
    cmds.parent(name+ctrlgrp(1), name+"_master"+ctrlgrp())
    CtrlColor(name+ctrlgrp(), PINK)
    

def ik_finger_pole_vector(lr, num, base):
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    pv_joint = joint_name(2,lr+"_Finger",num)+"_"+str(base)+"_"+str(sub_num/2)
    pole_vector = "IK_PV_"+lr+"_Finger"+str(num)+"_"+str(base)
    ik_handle_name = joint_name(2,lr+"_Finger",num)+"_"+str(base)+"_ikHandle"
    
    CtrlCreate(pv_joint, DIAMOND, 9, pole_vector, RED)
    cmds.scale(0.15, 0.15, 0.15, pole_vector+ctrlgrp())
    tmp = -0.3 if lr == "L" else 0.3
    cmds.move(0, tmp*world_scale, 0, pole_vector+ctrlgrp(1), r=True, os=True, wd=True)
    cmds.makeIdentity(pole_vector+ctrlgrp(), a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.poleVectorConstraint(pole_vector+ctrlgrp(), ik_handle_name)
    cmds.duplicate(pole_vector+ctrlgrp(1), n=pole_vector+ctrlgrp(1)+ctrlgrp(2), po=True)
    cmds.parent(pole_vector+ctrlgrp(1), pole_vector+ctrlgrp(1)+ctrlgrp(2))
    

def ik_finger_pole_vector_follow(lr, num, base):
    ik_ctrl = "IK_"+lr+"_Finger"+str(num)+"_"+str(base)+ctrlgrp()
    pole_vector = "IK_PV_"+lr+"_Finger"+str(num)+"_"+str(base)
    follow_on = pole_vector+"_follow_on"
    follow_off = pole_vector+"_follow_off"

    for grp_name in [follow_on, follow_off]:
        cmds.group(n=grp_name, em=True)
        match_objs(pole_vector+ctrlgrp(1), grp_name)
        cmds.duplicate(grp_name, n=grp_name+ctrlgrp(2))
        cmds.parent(grp_name, grp_name+ctrlgrp(2))
    cmds.parent(follow_on+ctrlgrp(2), ik_ctrl)
    cmds.parent(follow_off+ctrlgrp(2), "World_ctrl")
    cmds.parentConstraint(follow_on, follow_off, pole_vector+ctrlgrp(1))

    follow_attr(pole_vector+ctrlgrp(), pole_vector+ctrlgrp(1), follow_on, follow_off, 10)


#----------------------------------------------------------------------------#


def ik_foot_prepare(lr, num):
    ankle = joint_name(2, lr+"_Ankle", num)
    toe = joint_name(2, lr+"_Toes", num)
    toe_end = joint_name(2, lr+"_Toes_end", num)
    rock_in = joint_name(2, lr+"_FootSideInner_end", num)
    rock_out = joint_name(2, lr+"_FootSideOuter_end", num)
    heel = joint_name(2,lr+"_Heel_end", num)
    
    name = joint_name(2,lr+"_Leg",num)
    out_grp = name+"_rock_out"
    in_grp = name+"_rock_in"
    heel_grp = name+"_heel"
    toe_grp = name+"_toe"
    ball_grp = name+"_ball"
    wiggle_grp = name+"_toe_wiggle"
    ik_ctrl = name+ctrlgrp()
    
    cmds.ikHandle(sj=ankle, ee=toe, n="IK_"+lr+"_ball"+str(num)+"_ikHandle")
    cmds.ikHandle(sj=toe, ee=toe_end, n=toe+"_ikHandle")
    
    for grp_name in [out_grp, in_grp, out_grp+ctrlgrp(2), in_grp+ctrlgrp(2),
                    heel_grp, ball_grp, toe_grp, wiggle_grp]:
        cmds.group(n=grp_name, em=True)
    tmp = [out_grp, in_grp, heel_grp, toe_grp, ball_grp, wiggle_grp]
    for idx, obj in enumerate([rock_out, rock_in, heel, toe_end, toe, toe]):
        match_objs(obj, tmp[idx])
    tmp = [out_grp+ctrlgrp(2), in_grp+ctrlgrp(2)]
    for idx, obj in enumerate([rock_out, rock_in]):
        cmds.pointConstraint(obj, tmp[idx], n="tmp")
        cmds.delete("tmp")
    
    cmds.parent(toe+"_ikHandle", wiggle_grp)
    cmds.parent(name+"_ikHandle", "IK_"+lr+"_ball"+str(num)+"_ikHandle", ball_grp)
    cmds.parent(ball_grp, wiggle_grp, toe_grp)
    
    tmp = [toe_grp, heel_grp, in_grp, out_grp]
    for idx in range(len(tmp)-1):
        cmds.parent(tmp[idx], tmp[idx+1])
    cmds.rename(name+"_ikHandle"+ctrlgrp(2), name+ctrlgrp(2))
    cmds.parent(out_grp, name+ctrlgrp(2))
    
    for grp_name in [heel_grp, toe_grp]:
        CtrlCreate(grp_name, CIRCLE, 0, grp_name, RED, 1)
        cmds.rotate(0, 0, 90, grp_name+"_ctrl.cv[0:7]", r=True, os=True, fo=True)
    CtrlCreate(ball_grp, CIRCLE, 9, ball_grp, RED)
    cmds.rotate(0, 90, 0, ball_grp+"_ctrl.cv[0:7]", r=True, os=True, fo=True)
    cmds.makeIdentity(ball_grp+ctrlgrp(1), a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parentConstraint(ball_grp+ctrlgrp(), ball_grp, mo=True)
    CtrlCreate(wiggle_grp, CIRCLE, 0, wiggle_grp, RED)
    for grp_name in [heel_grp, toe_grp, wiggle_grp, ball_grp]:
        cmds.scale(0.5, 0.5, 0.5, grp_name+"_ctrl.cv[0:7]", r=True, ocp=True)
    
    cmds.parent(ball_grp+ctrlgrp(1), wiggle_grp+ctrlgrp(1), toe_grp+ctrlgrp())
    cmds.parent(toe_grp+ctrlgrp(1), heel_grp+ctrlgrp())
    tmp = [heel_grp+ctrlgrp(1), in_grp+ctrlgrp(2), out_grp+ctrlgrp(2), ik_ctrl]
    for idx in range(len(tmp)-1):
        cmds.parent(tmp[idx], tmp[idx+1])


#----------------------------------------------------------------------------#


def ik_foot_rock(lr, num):
    name = joint_name(2,lr+"_Leg",num)
    out_grp = name+"_rock_out"+ctrlgrp(2)
    in_grp = name+"_rock_in"+ctrlgrp(2)
    ik_ctrl = name+ctrlgrp()
    
    rock_mul = name+"_rock_Multiply"
    rev_mul = name+"_rock_rev_Multiply"
    rock_con = name+"_rock_Condition"
    
    add_attrs(ik_ctrl)
    add_attrs(ik_ctrl, "rock", 1)
        
    cmds.shadingNode(MULDIV, n=rock_mul, au=True)
    cmds.shadingNode(MULDIV, n=rev_mul, au=True)
    cmds.shadingNode("condition", n=rock_con, au=True)
    
    cmds.connectAttr(ik_ctrl+".rock", rock_mul+".input1X")
    cmds.setAttr(rock_mul+".input2X", -1)
    cmds.connectAttr(ik_ctrl+".rock", rock_con+".firstTerm")
    cmds.connectAttr(ik_ctrl+".rock", rock_con+".colorIfTrueR")
    cmds.connectAttr(rock_mul+".outputX", rock_con+".colorIfFalseG")
    cmds.setAttr(rock_con+".operation", 2)
    cmds.setAttr(rock_con+".colorIfFalseR", 0)
    cmds.connectAttr(rock_con+".outColorR", rev_mul+".input1X")
    cmds.connectAttr(rock_con+".outColorG", rev_mul+".input1Y")
    cmds.setAttr(rev_mul+".input2X", -1)
    cmds.setAttr(rev_mul+".input2Y", -1)
    if lr == "L":
        cmds.connectAttr(rev_mul+".outputX", out_grp+ROTATE+"Z")
        cmds.connectAttr(rock_con+".outColorG", in_grp+ROTATE+"Z")
    else:
        cmds.connectAttr(rock_con+".outColorR", out_grp+ROTATE+"Z")
        cmds.connectAttr(rev_mul+".outputY", in_grp+ROTATE+"Z")


def ik_foot_roll(lr, num):
    name = joint_name(2,lr+"_Leg",num)
    heel_grp = name+"_heel"+ctrlgrp(1)
    toe_grp = name+"_toe"+ctrlgrp(1)
    ball_grp = name+"_ball"+ctrlgrp(1)
    wiggle_grp = name+"_toe_wiggle"+ctrlgrp(1)
    ik_ctrl = name+ctrlgrp()
    roll_mul = name+"_roll_Multiply"

    add_attrs(ik_ctrl)
    for attr_name in ["heel", "ball", "toe"]:
        add_attrs(ik_ctrl, attr_name+"_roll", 1)
    add_attrs(ik_ctrl, "toe_wiggle", 1)
    
    cmds.shadingNode(MULDIV, n=roll_mul, au=True)
    cmds.connectAttr(ik_ctrl+".heel_roll", roll_mul+".input1X")
    cmds.setAttr(roll_mul+".input2X", -1)
    cmds.connectAttr(roll_mul+".outputX", heel_grp+ROTATE+"X")
    
    cmds.connectAttr(ik_ctrl+".ball_roll", ball_grp+ROTATE+"X")
    cmds.connectAttr(ik_ctrl+".toe_roll", toe_grp+ROTATE+"X")
    
    cmds.duplicate(wiggle_grp, n=wiggle_grp+ctrlgrp(2), po=True)
    cmds.parent(wiggle_grp, wiggle_grp+ctrlgrp(2))
    cmds.connectAttr(ik_ctrl+".toe_wiggle", roll_mul+".input1Y")
    cmds.setAttr(roll_mul+".input2Y", -1)
    cmds.connectAttr(roll_mul+".outputY", wiggle_grp+ROTATE+"Z")


def ik_foot_swivel(lr, num):
    name = joint_name(2,lr+"_Leg",num)
    ik_ctrl = name+ctrlgrp()
    
    add_attrs(ik_ctrl)
    for attr_name in ["heel", "ball", "toe"]:
        add_attrs(ik_ctrl, attr_name+"_swivel", 1)
        
    for attr_name in ["heel", "ball", "toe"]:
        cmds.connectAttr(ik_ctrl+"."+attr_name+"_swivel", name+"_"+attr_name+ctrlgrp(1)+ROTATE+"Y")


#----------------------------------------------------------------------------#


def ik_foot_sub_ctrl(lr, num):
    name = joint_name(2,lr+"_Leg",num)
    roll_name = "IK_roll_"+lr+"_Leg"+str(num)
    sub_ctrl = name+"_sub"+ctrlgrp()
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    ik_foot_sub_prepare(name, world_scale)
    
    add_attrs(sub_ctrl)
    add_attrs(sub_ctrl, "rock_angle", 1, 40)
    add_attrs(sub_ctrl, "roll_angle", 1, 40)
    add_attrs(sub_ctrl, "roll_start_trans", 1, 1)
    add_attrs(sub_ctrl, "roll_end_trans", 1, 2)
    
    ik_foot_sub_rock(lr, name, sub_ctrl, world_scale)
    ik_foot_sub_roll(name, roll_name, sub_ctrl, world_scale)
    ik_foot_sub_roll_heel(name, sub_ctrl, world_scale)
    
    for trs in [ROTATE, SCALE]:
        for axis in AXISES:
            cmds.setAttr(sub_ctrl+trs+axis, l=True, k=False)
    cmds.setAttr(sub_ctrl+TRANSLATE+"Y", l=True, k=False)
    

def ik_foot_sub_prepare(name, world_scale):
    for pos in ["_heel", "_toe", "_ball"]:
        cmds.duplicate(name+pos+ctrlgrp(1), n=name+pos+"_roll", po=True)
        cmds.duplicate(name+pos+ctrlgrp(1), n=name+pos+"_roll"+ctrlgrp(2), po=True)
        cmds.parent(name+pos+ctrlgrp(1), name+pos+"_roll")
        cmds.parent(name+pos+"_roll", name+pos+"_roll"+ctrlgrp(2))

    cmds.duplicate(name+"_rock_out"+ctrlgrp(2), n=name+"_rock_out_sub", po=True)
    cmds.duplicate(name+"_rock_in"+ctrlgrp(2), n=name+"_rock_in_sub", po=True)
    cmds.parent(name+"_rock_in"+ctrlgrp(2), name+"_rock_in"+"_sub")
    cmds.parent(name+"_rock_out"+ctrlgrp(2), name+"_rock_out_sub")
    cmds.rename(name+"_heel_roll_grp", name+"_heel_sub")

    CtrlCreate(name+"_toe"+ctrlgrp(), ARROW4, 9, name+"_sub", YELLOW, 1)
    cmds.setAttr(name+"_sub"+ctrlgrp()+TRANSLATE+"Z", 2*world_scale)
    cmds.parent(name+"_sub"+ctrlgrp(), w=True)
    match_objs(name+ctrlgrp(), name+"_sub"+ctrlgrp(1))
    cmds.parent(name+"_sub"+ctrlgrp(), name+"_sub"+ctrlgrp(1))
    cmds.makeIdentity(name+"_sub"+ctrlgrp(), apply=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parent(name+"_sub"+ctrlgrp(1), name+ctrlgrp())


def ik_foot_sub_rock(lr, name, sub_ctrl, world_scale):
    rock_con = name+"_sub_rock_Condition"
    rock_mul = name+"_sub_rock_Multiply"
    rev_mul = name+"_sub_rev_Multiply"
    input_mul = name+"_sub_input_Multiply"
    output_mul = name+"_sub_output_Multiply"
    rock_world_div = name+"_sub_rock_world_Divide"
    
    for grp_name in [rock_mul, rev_mul, input_mul, output_mul, rock_world_div]:
        cmds.shadingNode(MULDIV, n=grp_name, au=True)
    cmds.shadingNode("condition", n=rock_con, au=True)
    cmds.setAttr(rock_world_div+".operation", 2)
    
    cmds.connectAttr(sub_ctrl+TRANSLATE+"X", input_mul+".input1Y")
    cmds.setAttr(input_mul+".input2Y", -1)
    cmds.connectAttr(sub_ctrl+TRANSLATE+"X", rock_con+".firstTerm")
    cmds.connectAttr(sub_ctrl+TRANSLATE+"X", rock_con+".colorIfTrueR")
    cmds.connectAttr(input_mul+".outputY", rock_con+".colorIfFalseG")
    cmds.setAttr(rock_con+".operation", 2)
    cmds.setAttr(rock_con+".colorIfFalseR", 0)
    
    cmds.connectAttr(rock_con+".outColorR", output_mul+".input1Y")
    cmds.setAttr(output_mul+".input2Y", -1)
    cmds.connectAttr(output_mul+".outputY", rev_mul+".input1X")
    cmds.connectAttr(sub_ctrl+".rock_angle", rev_mul+".input2X")
    cmds.connectAttr(rev_mul+".outputX", rock_world_div+".input1X")
    cmds.setAttr(rock_world_div+".input2X", world_scale)

    cmds.connectAttr(rock_con+".outColorG", rock_mul+".input1X")
    cmds.connectAttr(sub_ctrl+".rock_angle", rock_mul+".input2X")
    cmds.connectAttr(rock_mul+".outputX", rock_world_div+".input1Y")
    cmds.setAttr(rock_world_div+".input2Y", world_scale)
    
    tmp_grp = [name+"_rock_out", name+"_rock_in"]
    if lr == "R":
        tmp_grp = tmp_grp[::-1]
    cmds.connectAttr(rock_world_div+".outputX", tmp_grp[0]+"_sub"+ROTATE+"Z")
    cmds.connectAttr(rock_world_div+".outputY", tmp_grp[1]+"_sub"+ROTATE+"Z")


def ik_foot_sub_roll(name, roll_name, sub_ctrl, world_scale):
    roll_input_mul = name+"_sub_roll_input_Multiply"
    roll_world_div = name+"_sub_roll_world_Divide"
    ball_set = roll_name+"_toe_SetRange"
    ball_set_sub = roll_name+"_toe_0_start_SetRange"
    ball_minus = name+"_toe_Minus"
    ball_mul = roll_name+"_toe_Multiply"
    ball_mul_sub = roll_name+"_toe_sub_Multiply"
    toe_set = roll_name+"_toe_end_SetRange"
    toe_mul = roll_name+"_toe_end_Multiply"
        
    for grp_name in [ball_set, ball_set_sub, toe_set]:
        cmds.shadingNode("setRange", n=grp_name, au=True)
    for grp_name in [ball_mul, ball_mul_sub, toe_mul, roll_input_mul, roll_world_div]:
        cmds.shadingNode(MULDIV, n=grp_name, au=True)
    cmds.shadingNode(PLUSMIN, n=ball_minus, au=True)
    cmds.setAttr(ball_minus+".operation", 2)
    cmds.setAttr(roll_world_div+".operation", 2)
    
    cmds.connectAttr(sub_ctrl+TRANSLATE+"Z", roll_world_div+".input1X")
    cmds.connectAttr(sub_ctrl+".roll_start_trans", roll_world_div+".input1Y")
    cmds.connectAttr(sub_ctrl+".roll_end_trans", roll_world_div+".input1Z")
    
    for axis in AXISES:
        cmds.setAttr(roll_world_div+".input2"+axis, world_scale)
        cmds.connectAttr(roll_world_div+".output"+axis, roll_input_mul+".input1"+axis)
        cmds.connectAttr(sub_ctrl+".roll_angle", roll_input_mul+".input2"+axis)
    
    cmds.connectAttr(roll_input_mul+".outputX", ball_set+".valueX")
    cmds.connectAttr(roll_input_mul+".outputY", ball_set+".oldMinX")
    cmds.connectAttr(roll_input_mul+".outputZ", ball_set+".oldMaxX")
    
    cmds.setAttr(ball_set+".maxX", 1)
    cmds.connectAttr(ball_set+".outValueX", ball_minus+".input1D[1]")
    cmds.setAttr(ball_minus+".input1D[0]", 1)
    cmds.connectAttr(ball_minus+".output1D", ball_mul+".input1X")
    
    cmds.connectAttr(roll_input_mul+".outputX", ball_set_sub+".valueX")
    cmds.setAttr(ball_set_sub+".maxX", 1)
    cmds.connectAttr(roll_input_mul+".outputY", ball_set_sub+".oldMaxX")
    cmds.connectAttr(ball_set_sub+".outValueX", ball_mul+".input2X")
    cmds.connectAttr(ball_mul+".outputX", ball_mul_sub+".input1X")
    cmds.connectAttr(roll_input_mul+".outputX", ball_mul_sub+".input2X")
    cmds.connectAttr(ball_mul_sub+".outputX", name+"_ball_roll"+ROTATE+"X")

    cmds.connectAttr(roll_input_mul+".outputX", toe_set+".valueX")
    cmds.setAttr(toe_set+".maxX", 1)
    cmds.connectAttr(roll_input_mul+".outputY", toe_set+".oldMinX")
    cmds.connectAttr(roll_input_mul+".outputZ", toe_set+".oldMaxX")
    cmds.connectAttr(toe_set+".outValueX", toe_mul+".input1X")
    cmds.connectAttr(roll_input_mul+".outputX", toe_mul+".input2X")
    cmds.connectAttr(toe_mul+".outputX", name+"_toe_roll"+ROTATE+"X")
    
    cmds.setAttr(sub_ctrl+".roll_start_trans", int(world_scale))
    cmds.setAttr(sub_ctrl+".roll_end_trans", int(world_scale*2))


def ik_foot_sub_roll_heel(name, sub_ctrl, world_scale):
    heel_clp = name+"_sub_heel_Clamp"
    heel_mul = name+"_sub_heel_Multiply"
    heel_world_div = name+"_sub_heel_world_Divide"
    
    for grp_name in [heel_mul, heel_world_div]:
        cmds.shadingNode(MULDIV, n=grp_name, au=True)
    cmds.setAttr(heel_world_div+".operation", 2)
    cmds.shadingNode("clamp", n=heel_clp, au=True)
    
    cmds.connectAttr(sub_ctrl+TRANSLATE+"Z", heel_clp+".inputR")
    cmds.connectAttr(sub_ctrl+TRANSLATE+"Z", heel_clp+".minR")
    cmds.connectAttr(heel_clp+".outputR", heel_mul+".input1X")
    cmds.connectAttr(sub_ctrl+".roll_angle", heel_mul+".input2X")
    cmds.connectAttr(heel_mul+".outputX", heel_world_div+".input1X")
    cmds.setAttr(heel_world_div+".input2X", world_scale)
    cmds.connectAttr(heel_world_div+".outputX", name+"_heel_sub"+ROTATE+"X")


#----------------------------------------------------------------------------#


def sub_fkik(lr, num):
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    sub_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"
    
    CtrlCreate(joint_name(0,lr+"_Wrist",num), SUB, 9, sub_ctrl, YELLOW)
    if lr == "R":
        cmds.setAttr(sub_ctrl+ctrlgrp()+ROTATE+"Y", 180)
        cmds.makeIdentity(sub_ctrl+ctrlgrp(), a=True, r=1, n=0, pn=1)
    cmds.parentConstraint(joint_name(0,lr+"_Wrist",num), sub_ctrl+ctrlgrp(1), mo=True)
    cmds.connectAttr(joint_name(0,lr+"_Wrist",num)+SCALE, sub_ctrl+ctrlgrp(1)+SCALE)
    for trs in [TRANSLATE, ROTATE, SCALE]:
        for axis in AXISES:
            cmds.setAttr(sub_ctrl+ctrlgrp()+trs+axis, l=True, k=False)
            
    add_attrs(sub_ctrl+ctrlgrp())
    add_attrs(sub_ctrl+ctrlgrp(), "FKIK", 2)
    tmp = [lr+"_Wrist"+str(num)]
    name = lr+"_Finger"+str(num)
    for base in range(1, base_num+1):
        for sub in range(1, sub_num+1):
            finger = lr+"_Finger"+str(num)+"_"+str(base)+"_"+str(sub)
            cmds.connectAttr(sub_ctrl+ctrlgrp()+".FKIK", "RIG_"+finger+".spread")
            tmp.append(name+"_"+str(base)+"_"+str(sub))
    if base_num > 3:
        cup = lr+"_Finger"+str(num)+"_Cup"
        cmds.connectAttr(sub_ctrl+ctrlgrp()+".FKIK", "RIG_"+cup+".spread")
        tmp.append(name+"_Cup")
    for grp_name in tmp:
        cmds.shadingNode(BLENDCOLORS, n=grp_name+"_BlendColors", au=True)
        cmds.connectAttr("IK_"+grp_name+SCALE, grp_name+"_BlendColors.color1")
        cmds.connectAttr("FK_"+grp_name+SCALE, grp_name+"_BlendColors.color2")
        if grp_name == lr+"_Wrist"+str(num):
            cmds.connectAttr("FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()+".FKIK", grp_name+"_BlendColors.blender")
        else:
            cmds.connectAttr("FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()+".FKIK", grp_name+"_BlendColors.blender")
        cmds.connectAttr(grp_name+"_BlendColors.output", "RIG_"+grp_name+SCALE)


def sub_ctrls(lr, num):
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)
    sub_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()
    names = ["thumb", "index", "middle", "ring", "pinky", "extra"]
    
    add_attrs(sub_ctrl)
    finger_duplicate(lr, num, "_sub", ctrlgrp(), 1)
    
    for base in range(1, base_num+1):
        name_ctrl = names[base-1] if base < 6 else names[5]+str(base-5)
        add_attrs(sub_ctrl, "FK_"+name_ctrl, 2, 0, -5, 10)
        fk_grp = joint_name(1,lr+"_Finger",num)+"_"+str(base)
        for sub in range(1, sub_num+1):
            finger_attr = fk_grp+"_"+str(sub)+"_sub"+ctrlgrp(2)+ROTATE+"Z"
            finger_set_driven_key([10, -5, 0], [90, -20, 0], sub_ctrl+".FK_"+name_ctrl, finger_attr)

    if base_num > 3:
        add_attrs(sub_ctrl, "FK_cup", 2, 0, 0, 10)
        cup = joint_name(1,lr+"_Finger",num)+"_Cup"
        cmds.duplicate(cup+ctrlgrp(1), n=cup+"_sub"+ctrlgrp(2), po=True)
        cmds.parent(cup+"_sub"+ctrlgrp(2), cup+ctrlgrp(1))
        cmds.parent(cup+ctrlgrp(), cup+"_sub"+ctrlgrp(2))
        finger_attr = joint_name(1,lr+"_Finger",num)+"_Cup_sub"+ctrlgrp(2)+ROTATE+"X"
        finger_set_driven_key([10, 0], [-70, 0], sub_ctrl+".FK_cup", finger_attr)


def sub_add_attrs(lr, num):
    sub_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()

    add_attrs(sub_ctrl)
    add_attrs(sub_ctrl, "FK_spread", 2, 0, -5, 10)
    add_attrs(sub_ctrl, "FK_relax", 2, 0, 0, 10)
    add_attrs(sub_ctrl, "FK_slide", 2, 0, 0, 10)
    add_attrs(sub_ctrl, "FK_scrunch", 2, 0, -5, 10)
    finger_duplicate(lr, num, "_relax",  "_sub"+ctrlgrp(2))
    finger_duplicate(lr, num, "_slide", "_relax"+ctrlgrp(2))
    finger_duplicate(lr, num, "_scrunch", "_slide"+ctrlgrp(2))

    
def sub_spread(lr, num):
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()
    
    for base in range(2, base_num+1):
        fk_grp = joint_name(1,lr+"_Finger",num)+"_"+str(base)+"_1"
        cmds.duplicate(fk_grp+ctrlgrp(1), n=fk_grp+"_spread"+ctrlgrp(2), po=True)
        cmds.parent(fk_grp+"_spread"+ctrlgrp(2), fk_grp+ctrlgrp(1))
        cmds.parent(fk_grp+"_scrunch"+ctrlgrp(2), fk_grp+"_spread"+ctrlgrp(2))
    
        if base != 3:
            finger_attr = joint_name(1,lr+"_Finger",num)+"_"+str(base)+"_1"+"_spread"+ctrlgrp(2)+ROTATE+"Y"
            if base == 2:
                finger_value = [25, -10, 0]
            else:
                finger_value = [-25-10*(base-4), 10+5*(base-4), 0]
            finger_set_driven_key([10, -5, 0], finger_value, sub_ctrl+".FK_spread", finger_attr)
    
    
def sub_relax_slide_scrunch(lr, num):
    def finger_attr(base, sub, attr):
        return(joint_name(1,lr+"_Finger",num)+"_"+str(base)+"_"+str(sub)+"_"+attr+ctrlgrp(2)+ROTATE+"Z")
        
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)
    sub_ctrl = "FKIK_"+lr+"_Finger"+str(num)+"_sub"+ctrlgrp()
    
    for base in range(2, base_num+1):
        for sub in range(1, sub_num+1):
            slide_value = [int(120/(sub_num-2)), 0]
            scrunch_value = [90, -20, 0]
            if sub == 1:
                slide_value = [-60, 0]
                scrunch_value = [-60, 0, 0]
            elif sub == sub_num:
                slide_value = [-60, 0]
            finger_set_driven_key([10, 0], [(2+base)*base, 0], sub_ctrl+".FK_relax", finger_attr(base, sub, "relax"))
            finger_set_driven_key([10, 0], slide_value, sub_ctrl+".FK_slide", finger_attr(base, sub, "slide"))
            finger_set_driven_key([10, -5, 0], scrunch_value, sub_ctrl+".FK_scrunch", finger_attr(base, sub, "scrunch"))


def finger_duplicate(lr, num, attr, below, start_num=2):
    base_num = cmds.intField(basefinger, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)

    for base in range(start_num, base_num+1):
        for sub in range(1, sub_num+1):
            fk_grp = joint_name(1,lr+"_Finger",num)+"_"+str(base)+"_"+str(sub)
            cmds.duplicate(fk_grp+ctrlgrp(1), n=fk_grp+attr+ctrlgrp(2), po=True)
            cmds.parent(fk_grp+attr+ctrlgrp(2), fk_grp+ctrlgrp(1))
            cmds.parent(fk_grp+below, fk_grp+attr+ctrlgrp(2))


def finger_set_driven_key(sub_value, finger_value, sub_attr, finger_attr):
    for idx in range(len(finger_value)):
        cmds.setAttr(sub_attr, sub_value[idx])
        cmds.setAttr(finger_attr, finger_value[idx])
        cmds.setDrivenKeyframe(finger_attr, cd=sub_attr)


#----------------------------------------------------------------------------#


def CtrlCreate(obj_name, shape, idx, ctrl_name, ctrl_color, ik_identity=0):
    obj = cmds.ls(obj_name)
    sub_num = cmds.intField(subfinger, q=True, v=True)-2
    world_scale = cmds.getAttr("scale_grp"+SCALE+"X")
    
    if shape == CIRCLE:
        c = cmds.circle(nr=(1,0,0))[0]
    elif shape == SUB:
        c = cmds.circle(r=1.5,nr=(0,1,0), sw=-180, cx=0.6+0.2*sub_num)[0]
        cmds.scale(0.9, 1, 0.6, c)
        cmds.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
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
    cmds.rename(c, ctrl_name+ctrlgrp())
    
    
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
    elif color == PINK_RED:
        num = 9
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


def follow_attr(follow, grp_name, follow_on, follow_off, attr_num, cons="parent"):
    add_attrs(follow)
    add_attrs(follow, "follow", 2, 0, 0, 10)

    attr_on = grp_name+"_"+cons+"Constraint1."+follow_on+"W0"
    attr_off = grp_name+"_"+cons+"Constraint1."+follow_off+"W1"

    for num in range(2):
        tmp = 1 if num == 0 else 0
        cmds.setAttr(follow+".follow", num*10)
        cmds.setAttr(attr_off, tmp)
        cmds.setAttr(attr_on, num)
        cmds.setDrivenKeyframe(attr_off, cd=follow+".follow")
        cmds.setDrivenKeyframe(attr_on, cd=follow+".follow")
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
    num_arm = cmds.intField(arm, q=True, v=True)
    num_leg = cmds.intField(leg, q=True, v=True)
    sub_num = cmds.intField(subfinger, q=True, v=True)+1
    
    objs = cmds.ls("RIG_*", typ="joint")
    tmp_lists = cmds.ls("RIG_*end*", typ="joint")
    tmp_lists += cmds.ls("RIG_*Finger*_"+str(sub_num))
    for body in ["Shoulder", "Elbow", "Wrist", "Hip", "Knee", "Ankle"]:
        tmp_lists += cmds.ls("*"+body+"*")
    for tmp in tmp_lists:
        if tmp in objs:
            objs.remove(tmp)
    objs.remove("RIG_Root1")
    
    for lr in LFRT:
        for num in range(1, num_arm+1):
            objs += cmds.ls(joint_name(6,lr+"_Arm",num)+"_skin*", typ="joint")
        for num in range(1, num_leg+1):
            objs += cmds.ls(joint_name(6,lr+"_Leg",num)+"_skin*", typ="joint")
    cmds.select(objs)
    print "Select : "+str(objs)


# Mirror Skin Weights
def MirrorSkinWeights():
    objs = cmds.ls(sl=True)[0]
    cluster = cmds.ls(cmds.listHistory(objs, pdo=True), type="skinCluster")
    if cluster == "":
        cmds.warning("NO Skin Cluster!!!")
    elif len(cluster) != 1:
        cmds.warning("Too Many SKin Cluster!!!")
    else:
        if cmds.checkBox(skin_check, q=True, v=True):
            cmds.copySkinWeights(ss=cluster[0], ds=cluster[0], mm="YZ", sa="closestPoint", ia=["oneToOne", "closestJoint"])
        else:
            cmds.copySkinWeights(ss=cluster[0], ds=cluster[0], mm="YZ",  sa="closestPoint", ia=["oneToOne", "closestJoint"], mi=True)


#----------------------------------------------------------------------------#


def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)
    print "Change Jnts Size: "+str(j)


def matchFreeze():
    if cmds.checkBoxGrp(match_check, q=True, v1=True):
        cmds.MatchTranslation()
    if cmds.checkBoxGrp(match_check, q=True, v2=True):
        cmds.MatchRotation()
    if cmds.checkBoxGrp(match_check, q=True, v3=True):
        cmds.MatchScaling()
    if cmds.checkBoxGrp(match_check, q=True, v4=True):
        cmds.MatchPivots()


def newGroup():
    objs = pm.ls(sl=True)
    tmps = pm.duplicate(rr=True)
    lst = []
    for x in range(len(tmps)):
        tmps[x].rename(objs[x])
        tmp = pm.ls(tmps[x])
        grp = pm.group(em=True)
        grp.rename(objs[x]+"_grp")
        pm.parentConstraint(tmp, grp, mo=False, n="ex")
        pm.delete("ex")
        pm.parent(tmp, grp)
        lst.append(grp)
        if x == 0:
            tmps[x].rename(objs[x])
            grp.rename(objs[x]+"_grp")
            lst = []
            lst.append(grp)
    tmps = tmps[:-1]
    lst = lst[1:]
    for x in range(len(lst)):
        pm.parent(lst[x], tmps[x])
