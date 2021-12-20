import maya.cmds as cmds

WIDTH = 280
WI = (150,120)

TOOLNAME = "HandHandAutoRigging"
TOOLTITLE = "Hand Auto Rigging"

TEXT01 = "Base Finger"
TEXT02 = "Sub Finger"

BUTTONS = [
    ["Create Joints", "createHands()"],
    ["Mirror Joints", "mirrorJoints()"],
    ["Orient Joints", "orientJoints()"],
    ["Create Controller", "createController()"]
]

LR = ["L_", "R_"]
HW = "Hand_World"
LHD = "L_Hand"
RHD = "R_Hand"

WARNING01 = "L_Hand is already exists"
WARNING02 = "R_Hand is already exists"
WARNING03 = "Ctrls are already exists"

def sep5():
    cmds.separator(h=5)

def sep3():
    cmds.separator(h=3)

def typing(text):
    sep5()
    cmds.rowLayout(nc=2,cw2=WI)
    cmds.text(text, l=text, h=20, w=WI[0])

#---------------------------------------------------------------------------------------#

if cmds.window(TOOLNAME, ex=True):
    cmds.deleteUI(TOOLNAME)
    
cmds.window(TOOLNAME, t=TOOLTITLE)
cmds.rowColumnLayout(w=WIDTH)

typing(TEXT01)
basefinger = cmds.intField(min=1, max=10, v=5, w=WI[1])
cmds.setParent("..")
typing(TEXT02)
subfinger = cmds.intField(min=1, max=10, v=5, w=WI[1])
cmds.setParent("..")

sep3()
sep3()
for btn_name, btn in BUTTONS:
    cmds.button(l=btn_name, h=40, c=btn)

sep5()
jnt = cmds.floatSliderButtonGrp(l="Joint Size ", bl="Set", bc="jointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)

sep5()
cmds.showWindow(TOOLNAME)

#-------------------------------------- Active Code ------------------------------------#

def createHands():
    if cmds.objExists(LHD):
        cmds.warning(WARNING01)
    else:
        bf_int = cmds.intField(basefinger, q=True, v=True)
        sf_int = cmds.intField(subfinger, q=True, v=True)
        
        hand = cmds.joint(n=LHD)
        cmds.setAttr("L_Hand.jointOrientX", -90)
        for i in range(1, bf_int+1):
            createFingers(i, sf_int, bf_int)
        cmds.circle(nr=(0,1,0), n=HW)[0]
        cmds.parent(LHD, HW)


def createFingers(count, sub, base):
    if count != 1:
        sub = sub+1
    for x in range(1, sub):
        if count == 1:
            if x == 1:
                position = (x-0.5,0,0.5*(base-3))
            else:
                position = (0.5*x,0,0.5*(base-3))
        else:
            if x >= 2:
                if count == 2:
                    position = (0.5*(x+1),0,0.5*base-count)
                else:
                    position = (0.5*(x+1),0,0.5*(base-count-2))
            else:
                if count == 2:
                    position = (x-0.5,0,0.5*base-count)
                else:
                    position = (x-0.5,0,0.5*(base-count-2))
        finger = cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=position)
    cmds.select(LHD)
    cmds.setAttr("L_finger_1_1.jointOrientZ", -45)


def mirrorJoints():
    if cmds.objExists(RHD):
        cmds.warning(WARNING02)
    else:
        cmds.mirrorJoint(LHD, mirrorBehavior=True, myz=True, sr=("L_", "R_"))
    orientJoints()


def orientJoints():
    bf_int = cmds.intField(basefinger, q=True, v=True)
    
    for x in range(1, bf_int+1):
        for i, j in [["L_", "zdown"], ["R_", "zup"]]:
            cmds.select(i+"finger_"+str(x)+"_1")
            cmds.joint(e=True, oj="xyz", sao=j, ch=True, zso=True)
            cmds.makeIdentity(i+"Hand", a=True, r=True)
            cmds.DeleteHistory(i+"Hand")


def createController():
    if cmds.objExists("L_Hand_ctrl_grp"):
            cmds.warning(WARNING03)
    else:
        bf_int = cmds.intField(basefinger, q=True, v=True)
        sf_int = cmds.intField(subfinger, q=True, v=True)
        
        for f in LR:
            handgrp = cmds.group(em=True, n=f+"Hand_ctrl_grp")
            othergrp = cmds.group(em=True, n=f+"Hand_ctrl_g_grp")
            hand = cmds.circle(nr=(1, 0, 0), n=f+"Hand_ctrl")[0]
            grouping(hand, othergrp, handgrp)
            z = cmds.getAttr("Hand_World.scaleX")
            cmds.scale(1*z,1.2*z,0.8*z, handgrp)
    
            cmds.parentConstraint(f+"Hand", handgrp, mo=False, n="L")
            cmds.delete("L")
            cmds.parentConstraint(hand, f+"Hand")
            cmds.DeleteHistory(f+"Hand_ctrl")
            coloring(f+"Hand_ctrl", 18)
    
            for i in range(1, bf_int+1):
                createCon(i, sf_int, f)
            subCon(bf_int, f)
            subConPlus(bf_int, sf_int, f)
    
            subgrp = cmds.group(em=True, n=f+"Hand_sub_ctrl_g_grp")
            cmds.parentConstraint(f+"Hand", subgrp, mo=False, n="L")
            cmds.delete("L")
            
            cmds.parent(f+"Hand_sub_ctrl_grp", subgrp)
            cmds.parentConstraint(f+"Hand", subgrp)
            cmds.rotate(0,0,0, f+"Hand_sub_ctrl_grp")
    
        cmds.makeIdentity(HW, a=True, s=True)
        cmds.DeleteHistory(HW)
        
        for num in LR:
            grouping(num+"Hand_sub_ctrl_g_grp", num+"Hand_ctrl_grp", HW)
            
        for num1 in [".t", ".r", ".s"]:
            for num2 in ["x", "y", "z"]:
                for num3 in LR:
                    cmds.setAttr(num3+"Hand_sub_ctrl"+num1+num2, l=True, k=False)
    
        for name in [LHD, RHD, "L_Hand_ctrl_grp", "R_Hand_ctrl_grp"]:
            cmds.parent(name, w=True)
        cmds.delete(HW)


def createCon(count, sub, f):
    if count == 1:
        sub = sub-1
        
    for x in range(1, sub):
        finjoint = f+"finger_"+str(count)+"_"+str(x)
        handgrp = cmds.group(em=True, r=True, n=f+"finger_"+str(count)+"_"+str(x)+"_grp")
        othergrp = cmds.group(em=True, r=True, n=f+"finger_"+str(count)+"_"+str(x)+"_g_grp")
        hand = cmds.circle(nr=(1,0,0), n=f+"finger_"+str(count)+"_"+str(x)+"_ctrl")[0]
        grouping(hand, othergrp, handgrp)
        z = cmds.getAttr("Hand_World.scaleX")
        cmds.scale(0.3*z,0.3*z,0.3*z, handgrp)
        
        cmds.parentConstraint(finjoint, handgrp, mo=False, n=f+str(count)+"_"+str(x))
        cmds.delete(f+str(count)+"_"+str(x))
        cmds.parentConstraint(hand, finjoint)
        cmds.DeleteHistory(hand)
        
        if x == 1:
            cmds.parent(handgrp, f+"Hand_ctrl")
        else:
            cmds.parent(handgrp, f+"finger_"+str(count)+"_"+str(x-1)+"_ctrl")
        coloring(f+"finger_"+str(count)+"_"+str(x)+"_ctrl", 18)


def subCon(base, f):
    if f == "L_":
        sweep = -180
        centerX = 0.2
    else:
        sweep = 180
        centerX = -0.2
    cir = cmds.circle(r=1.5,nr=(0,0,1), sw=sweep, cx=centerX, n=f+"Hand_sub_ctrl")[0]
    
    grp = cmds.group(em=True, n=f+"Hand_sub_ctrl_grp")
    cmds.parent(cir, grp)
    z = cmds.getAttr("Hand_World.scaleX")
    cmds.scale(2.5*z,1*z,1*z, grp)
    cmds.DeleteHistory(cir)
    c = f+"Hand_sub_ctrl_grp"
    
    base = base+1
    for x in range(2, base):
        cmds.orientConstraint(f+"finger_"+str(x)+"_1", c, mo=False, n="sub"+str(x))
    cmds.parentConstraint(f+"Hand", c, n="sub")
    cmds.delete("sub*")
    coloring(c,17)
    
    for n in range(1, base):
        cmds.addAttr(f+"Hand_sub_ctrl", ln="finger_"+str(n), at="float", dv=0, max=10, min=-5, k=True)


def subConPlus(base, sub, f):
    for x in range(1,base+1):
        if x == 1:
            sub = sub-1
        for y in range(2, sub):
            grp = cmds.select(f+"finger_"+str(x)+"_"+str(y)+"_g_grp")
            con = f+"Hand_sub_ctrl.finger_"+str(x)
            for i, j in [[0, 0], [10, 90], [-5, -10]]:
                cmds.setDrivenKeyframe(cd=con, dv=i, at="rotateY", v=j)


def grouping(a,b,c):
    cmds.parent(a,b)
    cmds.parent(b,c)

def coloring(h, colors):
    a = cmds.listRelatives(h, c=True)
    cmds.setAttr(a[0]+".overrideEnabled", 1 )
    cmds.setAttr(a[0]+".overrideColor", colors)

def jointSize():
    j = cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)
