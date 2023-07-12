import pymel.core as pm
from imp import reload
import functions.constraint

reload(functions.constraint)


def sub_spread(obj, num):
    pm.addAttr(obj, ln="separator", nn="----------", at="enum", en="--------:")
    pm.setAttr(obj+"."+"separator", cb=True)
    pm.addAttr(obj, ln="spread", at="double", dv=0, min=0, max=num)
    pm.setAttr(obj+".spread", k=True)


def spread(check_axes, check_const):
    objs = pm.ls(sl=True)
    if len(objs) < 3:
        pm.warning("Please select more than 3 obj!")
        return
    
    for idx in range(len(objs)-1):
        functions.constraint.constrains(objs[idx], objs[-1], 1, check_axes, check_const)

    cons = pm.listRelatives(pm.ls(objs[-1]), ad=True, typ='constraint')
    attrs = []

    sub_spread(objs[-1], len(objs)-2)
    for con in cons:
        attrs.append(pm.listAttr(con, ud=True))
    for con_count in range(len(cons)):
        attr = attrs[con_count]
        for idx in range(len(attr)):
            pm.setAttr(objs[-1] + ".spread", idx)
            pm.setAttr(cons[con_count] + "." + attr[idx], 1)
            for num in range(len(attr)):
                if idx != num:
                    pm.setAttr(cons[con_count] + "." + attr[num], 0)
            for num in range(len(attr)):
                pm.setDrivenKeyframe(cons[con_count] + "." + attr[num], cd=objs[-1] + ".spread")