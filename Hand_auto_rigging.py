import maya.cmds as cmds

width = 280
height_s = 3
height_m = 5
wi = (150,120)

toolName = "HandHandAutoRigging"
toolTitle = "Hand Auto Rigging"

text1 = "Base Finger"
text2 = "Sub Finger"

button1 = "Create Joints"
button2 = "Mirror Joints"
button3 = "Orient Joints"
button4 = "Create Controller"

warning_L = "L_Hand is already exists"
warning_R = "R_Hand is already exists"
warning_Ctrl = "Ctrls are already exists"

LR = ["L_", "R_"]
HW = "Hand_World"
LHD = "L_Hand"
RHD = "R_Hand"


if cmds.window(toolName, ex=True):
    cmds.deleteUI(toolName)
    
cmds.window(toolName, t=toolTitle)
cmds.rowColumnLayout(w=width)

cmds.separator(h=height_m)
cmds.rowLayout(nc=2,cw2=wi)
cmds.text(text1, l=text1, h=20, w=wi[0])
basefinger = cmds.intField(min=1, max=10, v=5, w=wi[1])
cmds.setParent("..")

cmds.separator(h=height_m)
cmds.rowLayout(nc=2,cw2=wi)
cmds.text(text2, l=text2, h=20, w=wi[0])
subfinger = cmds.intField(min=1, max=10, v=5, w=wi[1])
cmds.setParent("..")

cmds.separator(h=height_s)
cmds.separator(h=height_s)
cmds.button(l=button1, h=40, c="CreateHands()")
cmds.button(l=button2, h=40, c="MirrorJoints()")
cmds.button(l=button3, h=40, c="OrientJoints()")
cmds. button(l=button4, h=40, c="CreateController()")

cmds.separator(h=height_m)
jnt=cmds.floatSliderButtonGrp(l="Joint Size  ", bl="Set", bc="JointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)

cmds.separator(h=height_m)
cmds.showWindow(toolName)

#-------------------------------------- Active Code ------------------------------------#

def CreateHands():
    if cmds.objExists(LHD):
        cmds.warning(warning_L)
    else:
        hand=cmds.joint(n=LHD)
        cmds.setAttr("L_Hand.jointOrientX", -90)
            
        for i in range(1, cmds.intField(basefinger, q=True, v=True)+1):
            if i==1:
                createThumb(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
            elif i==2:
                createFingers(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
            else:
                createFin(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
                
        cmds.circle(nr=(0,1,0), n=HW)
        cmds.parent(LHD, HW)

def createThumb(count, sub, base):
    for x in range(1,sub):
        if x==1:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,0.5*(base-3)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*x,0,0.5*(base-3)))
    cmds.select(LHD)
    cmds.setAttr("L_finger_1_1.jointOrientZ", -45)

def createFingers(count, sub, base):
    for x in range(1,sub+1):
        if x>=2:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*(x+1),0,-count+0.5+0.5*(base-1)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,-count+0.5+0.5*(base-1)))
    cmds.select(LHD)

def createFin(count, sub, base):
    for x in range(1,sub+1):
        if x>=2:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*(x+1),0,0.5*(-count+base-2)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,0.5*(-count+base-2)))
    cmds.select(LHD)

def MirrorJoints():
    if cmds.objExists(RHD):
        cmds.warning(warning_R)
    else:
        cmds.mirrorJoint(LHD, mirrorBehavior=True, myz=True, sr=("L_", "R_"))

def OrientJoints():
    for x in range(1,cmds.intField(subfinger, q=True, v=True)+1):
        for i, j in [["L_", "zdown"], ["R_", "zup"]]:
            cmds.select(i+"finger_"+str(x)+"_1")
            cmds.joint(e=True, oj="xyz", sao=j, ch=True, zso=True)
            cmds.makeIdentity(i+"Hand", a=True, r=True)
            cmds.DeleteHistory(i+"Hand")

def CreateController():
    if cmds.objExists("L_Hand_ctrl_grp"):
            cmds.warning(warning_Ctrl)
    else:
        for f in LR:
            handgrp=cmds.group(em=True, n=f+"Hand_ctrl_grp")
            othergrp=cmds.group(em=True, n=f+"Hand_ctrl_g_grp")
            hand=cmds.circle(nr=(1, 0, 0), n=f+"Hand_ctrl")
            grouping(hand, othergrp, handgrp)
            z=cmds.getAttr("Hand_World.scaleX")
            cmds.scale(1*z,1.2*z,0.8*z, handgrp)
    
            cmds.parentConstraint(f+"Hand", handgrp, mo=False, n="L")
            cmds.delete("L")
            cmds.parentConstraint(hand, f+"Hand")
            cmds.DeleteHistory(f+"Hand_ctrl")
            coloring(f+"Hand_ctrl", 18)
    
            for i in range(1, cmds.intField(basefinger, q=True, v=True)+1):
                if i==1:
                    createCon(i, cmds.intField(subfinger, q=True, v=True)-1,f)
                else:
                    createCon(i, cmds.intField(subfinger, q=True, v=True),f)
    
            SubCon(cmds.intField(basefinger, q=True, v=True), f)
            SubConPlus(cmds.intField(basefinger, q=True, v=True), cmds.intField(subfinger, q=True, v=True), f)
    
            subgrp=cmds.group(em=True, n=f+"Hand_sub_ctrl_g_grp")
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
    for x in range(1, sub):
        finjoint=f+"finger_"+str(count)+"_"+str(x)
        
        handgrp=cmds.group(em=True, r=True, n=f+"finger_"+str(count)+"_"+str(x)+"_grp")
        othergrp=cmds.group(em=True, r=True, n=f+"finger_"+str(count)+"_"+str(x)+"_g_grp")
        hand=cmds.circle(nr=(1,0,0), n=f+"finger_"+str(count)+"_"+str(x)+"_ctrl")
        grouping(hand, othergrp, handgrp)
        z=cmds.getAttr("Hand_World.scaleX")
        cmds.scale(0.3*z,0.3*z,0.3*z, handgrp)
        
        cmds.parentConstraint(finjoint, handgrp, mo=False, n=f+str(count)+"_"+str(x))
        cmds.delete(f+str(count)+"_"+str(x))
        cmds.parentConstraint(hand, finjoint)
        cmds.DeleteHistory(hand)
        
        if x==1:
            cmds.parent(handgrp, f+"Hand_ctrl")
        else:
            cmds.parent(handgrp, f+"finger_"+str(count)+"_"+str(x-1)+"_ctrl")
        coloring(f+"finger_"+str(count)+"_"+str(x)+"_ctrl", 18)

def SubCon(base, f):
    if f=="L_":
        cir=cmds.circle(r=1.5, nr=(0,0,1), sw=-180, cx=0.2, n=f+"Hand_sub_ctrl")
    else:
        cir=cmds.circle(r=1.5,nr=(0,0,1), sw=180, cx=-0.2, n=f+"Hand_sub_ctrl")
    
    grp=cmds.group(em=True, n=f+"Hand_sub_ctrl_grp")
    cmds.parent(cir,grp)
    z=cmds.getAttr("Hand_World.scaleX")
    cmds.scale(2.5*z,1*z,1*z, grp)
    cmds.DeleteHistory(cir)
    c=f+"Hand_sub_ctrl_grp"
    
    for x in range(2,base+1):
        cmds.orientConstraint(f+"finger_"+str(x)+"_1", c, mo=False, n="sub"+str(x))
    cmds.parentConstraint(f+"Hand", c, n="sub")
    cmds.delete("sub*")
    coloring(c,17)
    
    for n in range(1, base+1):
        cmds.addAttr(f+"Hand_sub_ctrl", ln="finger_"+str(n), at="float", dv=0, max=10, min=-5, k=True)

def SubConPlus(base, sub, f):
    for x in range(1,base+1):
        if x==1:
            s=sub-1
        else:
            s=sub
        for y in range(2, s):
            grp=cmds.select(f+"finger_"+str(x)+"_"+str(y)+"_g_grp")
            con=f+"Hand_sub_ctrl.finger_"+str(x)
            for i, j in [[0, 0], [10, 90], [-5, -10]]:
                cmds.setDrivenKeyframe(cd=con, dv=i, at="rotateY", v=j)

def grouping(a,b,c):
    cmds.parent(a,b)
    cmds.parent(b,c)

def coloring(h, colors):
    a=cmds.listRelatives(h, c=True)
    cmds.setAttr(a[0]+".overrideEnabled", 1 )
    cmds.setAttr(a[0]+".overrideColor", colors)

def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)

