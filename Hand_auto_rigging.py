import maya.cmds as cmds

win="HandAutoRigging"
if cmds.window(win, ex=True):
    cmds.deleteUI(win)
    
cmds.window(win, t="Hand Auto Rigging")
cmds.rowColumnLayout(w=280)

cmds.separator(h=5)
wi=(150,120)
cmds.rowLayout(nc=2,cw2=wi)
cmds.text("Base Finger", l="Base Finger", h=20, w=wi[0])
basefinger = cmds.intField(min=1, max=10, v=5, w=wi[1])
cmds.setParent("..")

cmds.separator(h=5)
wi=(150,120)
cmds.rowLayout(nc=2,cw2=wi)
cmds.text("Sub Finger", l="Sub Finger", h=20, w=wi[0])
subfinger = cmds.intField(min=1, max=10, v=5, w=wi[1])
cmds.setParent("..")

cmds.separator(h=3)
cmds.separator(h=3)
cmds.button(l="Create Joints", h=40, c="CreateHands()")
cmds.button(l="Mirror Joints", h=40, c="MirrorJoints()")
cmds.button(l="Orient Joints", h=40, c="OrientJoints()")
cmds. button(l="Create Controller", h=40, c="CreateController()")

cmds.separator(h=5)
jnt=cmds.floatSliderButtonGrp(l="Joint Size  ", bl="Set", bc="JointSize()", cw4=(60,50,130,30), f=True, min=0.1, max=1, v=1)

cmds.separator(h=5)
cmds.showWindow(win)

#-------------------------------------- Active Code ------------------------------------#

def CreateHands():
    if cmds.objExists("L_Hand"):
        cmds.warning("L_Hand is already exists")
    else:
        hand=cmds.joint(n="L_Hand")
        cmds.setAttr("L_Hand.jointOrientX", -90)
            
        for i in range(1, cmds.intField(basefinger, q=True, v=True)+1):
            if i==1:
                createThumb(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
            elif i==2:
                createFingers(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
            else:
                createFin(i, cmds.intField(subfinger, q=True, v=True), cmds.intField(basefinger, q=True, v=True))
                
        a=cmds.circle(nr=(0,1,0), n="Hand_World")
        cmds.parent("L_Hand",a)

#--------------------------------------------------------------------------------------------#

def createThumb(count, sub, base):
    for x in range(1,sub):
        if x==1:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,0.5*(base-3)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*x,0,0.5*(base-3)))
    cmds.select("L_Hand")
    cmds.setAttr("L_finger_1_1.jointOrientZ", -45)

def createFingers(count, sub, base):
    for x in range(1,sub+1):
        if x>=2:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*(x+1),0,-count+0.5+0.5*(base-1)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,-count+0.5+0.5*(base-1)))
    cmds.select("L_Hand")

def createFin(count, sub, base):
    for x in range(1,sub+1):
        if x>=2:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(0.5*(x+1),0,0.5*(-count+base-2)))
        else:
            finger=cmds.joint(n="L_finger_"+str(count)+"_"+str(x), p=(x-0.5,0,0.5*(-count+base-2)))
    cmds.select("L_Hand")

#--------------------------------------------------------------------------------------------#

def MirrorJoints():
    if cmds.objExists("R_Hand"):
        cmds.warning("R_Hand is already exists")
    else:
        cmds.mirrorJoint("L_Hand",mirrorBehavior=True, myz=True, sr=("L_","R_"))

def OrientJoints():
    cmds.makeIdentity("L_Hand", a=True, r=True)
    cmds.makeIdentity("R_Hand", a=True, r=True)

#--------------------------------------------------------------------------------------------#

def CreateController():
    for x in range(0,2): 
        if x==0: 
            f="L_"
        else: 
            f="R_"
            
        handgrp=cmds.group(em=True, n=f+"Hand_ctrl_grp")
        othergrp=cmds.group(em=True, n=f+"Hand_ctrl_g_grp")
        hand=cmds.circle(nr=(1, 0, 0), n=f+"Hand_ctrl")
        grouping(hand, othergrp, handgrp)
        z=cmds.getAttr("Hand_World.scaleX")
        cmds.scale(1*z,1.2*z,0.8*z, handgrp)
        
        cmds.parentConstraint(f+"Hand",handgrp, mo=False, n="L")
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
        cmds.parentConstraint(f+"Hand",subgrp, mo=False, n="L")
        cmds.delete("L")
        
        cmds.parent(f+"Hand_sub_ctrl_grp",subgrp)
        cmds.parentConstraint(f+"Hand", subgrp)
        
    cmds.makeIdentity("Hand_World",a=True, s=True)
    cmds.DeleteHistory("Hand_World")
    grouping("L_Hand_sub_ctrl_g_grp","L_Hand_ctrl_grp", "Hand_World")
    grouping("R_Hand_sub_ctrl_g_grp","R_Hand_ctrl_grp", "Hand_World")
    
    for num1 in [".t", ".r", ".s"]:
        for num2 in ["x", "y", "z"]:
            cmds.setAttr("L_Hand_sub_ctrl"+num1+num2, l=True, k=False)
            cmds.setAttr("R_Hand_sub_ctrl"+num1+num2, l=True, k=False)
    
    cmds.parent("L_Hand",w=True)
    cmds.parent("R_Hand",w=True)
    cmds.parent("L_Hand_ctrl_grp",w=True)
    cmds.parent("R_Hand_ctrl_grp",w=True)
    cmds.delete("Hand_World")

#--------------------------------------------------------------------------------------------#

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

#--------------------------------------------------------------------------------------------#

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
    cmds.parentConstraint(f+"Hand",c, mo=False, n="sub")
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
            cmds.setDrivenKeyframe(cd=con, dv=0, at="rotateY", v=0)
            cmds.setDrivenKeyframe(cd=con, dv=10, at="rotateY", v=90)
            cmds.setDrivenKeyframe(cd=con, dv=-5, at="rotateY", v=-10)

#--------------------------------------------------------------------------------------------#

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
