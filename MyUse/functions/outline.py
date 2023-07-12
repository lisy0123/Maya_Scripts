import pymel.core as pm
import re

def set_in_order(_):
    objs = pm.listRelatives(ad=True, typ='joint')
    objs += pm.listRelatives(ad=True, typ='transform')
    objs += pm.ls(sl=True)
    num_list = []
    for obj in objs:
        num_list.append(int(re.sub(r"[^0-9]", "", obj.name())))
    for num in range(min(num_list), max(num_list)+1):
        for idx in range(len(num_list)):
            if num == num_list[idx]:    
                pm.reorder(objs[idx], b=True)
                break


def grouping(_):
    objs = pm.ls(sl=True)
    lst = []
    for idx in range(len(objs)):
        try:
            parent = pm.listRelatives(objs[idx], p=True)[0]
        except:
            parent = None
        grp = pm.group(em=True)
        grp.rename(objs[idx]+"_grp")
        pm.parentConstraint(objs[idx], grp, mo=False, n="ex")
        pm.delete("ex")
        pm.scaleConstraint(objs[idx], grp, mo=False, n="ex")
        pm.delete("ex")
        pm.parent(objs[idx], grp)
        lst.append(grp)
        if parent is not None:
            pm.parent(grp, parent)