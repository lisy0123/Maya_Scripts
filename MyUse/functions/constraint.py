import maya.cmds as cmds
import pymel.core as pm


def const(check_axes, check_const, quick, mo):
    objs = pm.ls(sl=True)
    if len(objs) == 1:
        pm.warning("Select only one obj!")
    if pm.checkBoxGrp(quick, q=True, v1=True):
        if len(objs) % 2 != 0:
            pm.warning("Select even numbers of objs! Objs nums: "+str(len(objs)))
        else:
            for x in range(0, len(objs), 2):
                constrains(objs[x], objs[x+1], 2, check_axes, check_const, mo)
    else:
        for idx in range(len(objs)-1):
            constrains(objs[idx], objs[-1], 2, check_axes, check_const, mo)


def constrains(con, obj, num, check_axes, check_const, mo=None):
    skip = []
    if num != 0:
        if not pm.checkBoxGrp(check_axes, q=True, v1=True):
            skip.append("x")
        if not pm.checkBoxGrp(check_axes, q=True, v2=True):
            skip.append("y")
        if not pm.checkBoxGrp(check_axes, q=True, v3=True):
            skip.append("z")

    tmp = False
    if mo is not None:
        tmp = True if pm.checkBoxGrp(mo, q=True, v1=True) else False
    tmp = True if num == 1 else tmp

    if pm.checkBoxGrp(check_const, q=True, v1=True):
        pm.parentConstraint(con, obj, mo=tmp, st=skip, sr=skip)
    if pm.checkBoxGrp(check_const, q=True, v2=True):
        pm.pointConstraint(con, obj, mo=tmp, sk=skip)
    if pm.checkBoxGrp(check_const, q=True, v3=True):
        pm.orientConstraint(con, obj, mo=tmp, sk=skip)
    if pm.checkBoxGrp(check_const, q=True, v4=True):
        pm.scaleConstraint(con, obj, mo=tmp, sk=skip)
    cmds.DeleteHistory(con)