import pymel.core as pm


def hash_renamer(hf, hb, check):
    if pm.radioButtonGrp(check, q=True, sl=1) == 1:
        hf = "R_" + hf if hf != "" else "R"
    elif pm.radioButtonGrp(check, q=True, sl=1) == 2:
        hf = "L_" + hf if hf != "" else "L"
    hf = hf + "_" if hf != "" else hf
    hb = "_" + hb if hb != "" else hb
    
    objs = pm.ls(sl=True)
    for idx in range(len(objs)):
        if len(objs) == 1:
            if hf != "":
                name = hf[:-1] if hb == "" else hf[:-1] + hb
            else:
                name = "XXX" if hb == "" else hb[1:]
        elif idx < 9:
            name = hf + "0" + str(idx+1) + hb if hf != "" else hb[1:] + "_0" + str(idx+1)
        else:
            name = hf + str(idx+1) + hb if hf != "" else hb[1:] + "_" + str(idx+1)
        objs[idx].rename(name)


def replace(search, replace, check):
    if pm.radioButtonGrp(check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True)
        objs += pm.ls(sl=True)
    else:
        objs = pm.ls(sl=True)
    for obj in objs:
        obj.rename(obj.name().replace(search, replace))


def add(num, before, after, check, repeat):
    if pm.radioButtonGrp(check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True, typ='joint')
        objs += pm.listRelatives(ad=True, typ='transform')
        objs += pm.ls(sl=True)
    else:
        objs = pm.ls(sl=True)
    namer(num, before, after, objs, repeat)


def namer(num, before, after, objs, repeat):
    for obj in objs:
        if num == 1:
            blen = len(before)
            bcheck = ""
            for idx in range(blen+1):
                bcheck += obj[idx]
            if bcheck != before + "_" or pm.checkBox(repeat, q=True, v=True):
                name = before + "_" + obj
                obj.rename(name)
        else:
            alen = len(after)
            acheck = ""
            for idx in range(alen+1):
                tmp = len(obj.name()) - len(after) + idx - 1
                acheck += obj[tmp]
            if acheck != "_" + after or pm.checkBox(repeat, q=True, v=True):
                name = obj + "_" + after
                obj.rename(name)