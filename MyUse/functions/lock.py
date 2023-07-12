import pymel.core as pm


def lock(check, lock, keyable):
    ranges = []
    objs = pm.ls(sl=True)

    if pm.checkBoxGrp(check, q=True, v1=True):
        ranges.append(".t")
    if pm.checkBoxGrp(check, q=True, v2=True):
        ranges.append(".r")
    if pm.checkBoxGrp(check, q=True, v3=True):
        ranges.append(".s")
    for obj in objs:
        for attr1 in ranges:
            for attr2 in ["x", "y", "z"]:
                pm.setAttr(obj+attr1+attr2, l=lock, k=keyable)
        if pm.checkBoxGrp(check, q=True, v4=True):
            pm.setAttr(obj+".visibility", l=lock, k=keyable)


def lock_sel(lock, keyable):
    ranges = []
    objs = pm.ls(sl=True)

    sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    for sl_attr in sl_attrs:
        ranges.append("."+sl_attr)
    for obj in objs:
        for attr1 in ranges:
            pm.setAttr(obj+attr1, l=lock, k=keyable)