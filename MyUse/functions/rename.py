import maya.cmds as cmds
import pymel.core as pm


def hash_renamer(hf, hb, check):
    if cmds.radioButtonGrp(check, q=True, sl=1) == 1:
        hf = "R_"+hf
    elif cmds.radioButtonGrp(check, q=True, sl=1) == 2:
        hf = "L_"+hf
    if hb != "":
        hb = "_"+hb
    
    objs = pm.ls(sl=True)
    for x in range(len(objs)):
        if len(objs) == 1:
            name = hf+hb
        elif x < 9:
            name = hf+"_0"+str(x+1)+hb
        else:
            name = hf+"_"+str(x+1)+hb
        objs[x].rename(name)


def replace(search, replace, check):
    if cmds.radioButtonGrp(check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True)
        objs += pm.ls(sl=True)
    else:
        objs = pm.ls(sl=True)
    for obj in objs:
        obj.rename(obj.name().replace(search, replace))


def namer(num, before, after, objs):
    for obj in objs:
        if num == 1:
            blen = len(before)
            bcheck=""
            for x in range(blen+1):
                bcheck += obj[x]
            if bcheck != before+"_":
                name = before+"_"+obj
                obj.rename(name)
        else:
            alen = len(after)
            acheck=""
            for x in range(alen+1):
                tmp = len(obj.name())-len(after)+x-1
                acheck += obj[tmp]
            if acheck != "_"+after:
                name = obj+"_"+after
                obj.rename(name)


def add(num, before, after, check):
    if cmds.radioButtonGrp(check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True, typ='joint')
        objs += pm.listRelatives(ad=True, typ='transform')
        objs += pm.ls(sl=True)
        print(objs)
    else:
        objs = pm.ls(sl=True)
    namer(num, before, after, objs)


def add_tail(tail):
    # tails = [
    #     "grp", "jnt", "ctrl",
    #     "extra", "loc", "rig",
    # ]
    objs = pm.ls(sl=True)
    namer(0, None, tail, objs)