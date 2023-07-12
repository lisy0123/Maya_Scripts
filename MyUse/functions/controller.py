import maya.cmds as cmds
import pymel.core as pm
from imp import reload
import functions.constraint

reload(functions.constraint)


def create_ctrl(make, shapes, axes, const):
    objs = cmds.ls(sl=True)
    if cmds.radioButtonGrp(make, q=True, sl=1) == 1:
        for x in range(len(objs)):
            obj = objs[x]
            sel_shape(obj, make, shapes, axes, const)
    else:
        sel_shape(objs, make, shapes, axes, const)


def sel_shape(obj, make, shapes, axes, const):
    square_points = [(-1,0,-1),(1,0,-1),(1,0,1),(-1,0,1),(-1,0,-1)]
    box_points = [(1,1,1),(1,-1,1), (1,-1,-1),(1,1,-1),(-1,1,-1),
                  (-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),
                  (-1,-1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1)]
    
    diamond_points = [(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(0,1,0),(-1,0,0),
                      (1,0,0),(0,-1,0),(-1,0,0),(0,0,-1),(1,0,0),(0,1,0),
                      (0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(0,0,1),(-1,0,0)]
    polygon_points = [(0,0,-6),(2,0,-4),(4,0,-4),(4,0,-2),(6,0,0),(4,0,2),
                      (4,0,4),(2,0,4),(0,0,6),(-2,0,4),(-4,0,4),(-4,0,2),
                      (-6,0,0),(-4,0,-2),(-4,0,-4),(-2,0,-4),(0,0,-6)]
    
    cross2_points = [(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),(1,0,1),
                     (1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),(-1,0,-1),(-1,0,-3)]
    eyey_points = [(-2.05541,0,-0.0124173),(-1.365656,0,-0.507243),
                   (0.0138526,0,-1.496896),(1.337951,0,-0.498965),(2,0,0)]
    
    arrow1_points = [(-2,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),(1,0,1),(-2,0,1),(-2,0,-1)]
    arrow2_points = [(-1,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),
                     (1,0,1),(-1,0,1),(-1,0,2),(-3,0,0),(-1,0,-2),(-1,0,-1)]
    arrow4_points = [(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),
                     (1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1),
                     (1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),(-3,0,1),
                     (-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)]

    # circle
    if cmds.optionMenu(shapes, q=True, sl=1) == 1:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            c = cmds.circle(nr=(1,0,0))[0]
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 2:
            c = cmds.circle(nr=(0,1,0))[0]
        else:
            c = cmds.circle(nr=(0,0,1))[0]
    # square
    elif cmds.optionMenu(shapes, q=True, sl=2) == 2:
        c = cmds.curve(d=1, p=square_points)
    # box
    elif cmds.optionMenu(shapes, q=True, sl=3) == 3:
        c = cmds.curve(d=1, p=box_points)
    # ball
    elif cmds.optionMenu(shapes, q=True, sl=4) == 4:
        tmp1 = cmds.circle(nr=(1,0,0))
        tmp2 = cmds.circle(nr=(0,1,0))
        tmp3 = cmds.circle(nr=(0,0,1))
        sh2 = cmds.listRelatives(tmp2[0], ad=True)[0]
        sh3 = cmds.listRelatives(tmp3[0], ad=True)[0]
        cmds.parent(sh2, tmp1[0], r=True, s=True)
        cmds.parent(sh3, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp2))
        cmds.delete(cmds.ls(tmp3))
        c = cmds.ls(tmp1)[0]
    # diamond
    elif cmds.optionMenu(shapes, q=True, sl=5) == 5:
        c = cmds.curve(d=1, p=diamond_points)
    # polygon
    elif cmds.optionMenu(shapes, q=True, sl=6) == 6:
        c = cmds.curve(d=1, p=polygon_points)
    # cross 1
    elif cmds.optionMenu(shapes, q=True, sl=7) == 7:
        c = cmds.curve(d=1, p=[(0,0,-2),(0,0,2),(0,0,0),(-2,0,0),(2,0,0)])
    # cross 2
    elif cmds.optionMenu(shapes, q=True, sl=8) == 8:
        c = cmds.curve(d=1, p=cross2_points)
    # eye
    elif cmds.optionMenu(shapes, q=True, sl=9) == 9:
        tmp1 = cmds.circle(nr=(0,1,0))
        tmp2 = cmds.curve(d=3, p=eyey_points)
        tmp3 = cmds.curve(d=3, p=eyey_points)
        cmds.setAttr(tmp3+".scaleZ", -1)
        pm.makeIdentity(tmp3, a=True, t=1, r=1, s=1, n=0, pn=1)
        sh2 = cmds.listRelatives(tmp2, ad=True)[0]
        sh3 = cmds.listRelatives(tmp3, ad=True)[0]
        cmds.parent(sh2, tmp1[0], r=True, s=True)
        cmds.parent(sh3, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp2))
        cmds.delete(cmds.ls(tmp3))
        c = cmds.ls(tmp1)[0]
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateY", 90)
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
        pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    # handle
    elif cmds.optionMenu(shapes, q=True, sl=10) == 10:
        tmp1 = cmds.circle(nr=(1,0,0))
        tmp2 = cmds.circle(nr=(0,1,0))
        tmp3 = cmds.circle(nr=(0,0,1))
        sh2 = cmds.listRelatives(tmp2[0], ad=True)[0]
        sh3 = cmds.listRelatives(tmp3[0], ad=True)[0]
        cmds.parent(sh2, tmp1[0], r=True, s=True)
        cmds.parent(sh3, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp2))
        cmds.delete(cmds.ls(tmp3))
        cmds.setAttr(tmp1[0]+".translateY", 4)
        cmds.makeIdentity(tmp1[0], a=True, t=1, n=0, pn=1)
        tmp = cmds.curve(d=1, p=[(0,0,0),(0,3,0)])
        sh = cmds.listRelatives(tmp, ad=True)[0]
        cmds.parent(sh, tmp1[0], r=True, s=True)
        cmds.delete(cmds.ls(tmp))
        c = cmds.ls(tmp1)[0]
    # arrow 1
    elif cmds.optionMenu(shapes, q=True, sl=11) == 11:
        c = cmds.curve(d=1, p=arrow1_points)
    # arrow 2
    elif cmds.optionMenu(shapes, q=True, sl=12) == 12:
        c = cmds.curve(d=1, p=arrow2_points)
    # arrow 4
    elif cmds.optionMenu(shapes, q=True, sl=13) == 13:
        c = cmds.curve(d=1, p=arrow4_points)

    grp = cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.ResetTransformations(c)

    if cmds.optionMenu(shapes, q=True, sl=5) == 5 \
        or cmds.optionMenu(shapes, q=True, sl=7) == 7 \
        or cmds.optionMenu(shapes, q=True, sl=13) == 13:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
        pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif cmds.optionMenu(shapes, q=True, sl=2) == 2 \
        or cmds.optionMenu(shapes, q=True, sl=6) == 6 \
        or cmds.optionMenu(shapes, q=True, sl=8) == 8 \
        or cmds.optionMenu(shapes, q=True, sl=10) == 10:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", -90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
    elif cmds.optionMenu(shapes, q=True, sl=11) == 11 \
         or cmds.optionMenu(shapes, q=True, sl=12) == 12:
        if cmds.radioButtonGrp(axes, q=True, sl=2) == 2:
            cmds.setAttr(c+".rotateX", 90)
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateY", -90)

            
    pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parentConstraint(obj, grp, mo=False, n="ex")
    cmds.delete("ex")
    if cmds.radioButtonGrp(make, q=True, sl=1) == 1:
        functions.constraint.constrains(c, obj, 0, axes, const)