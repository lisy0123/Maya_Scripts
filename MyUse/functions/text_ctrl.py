import maya.cmds as cmds
import pymel.core as pm


def text(text):
    pm.textCurves(t=text, ch=True)
    objs = pm.listRelatives(ad=True, typ='transform')
    for obj in objs:
        if "Char_" in obj.name():
            objs.remove(obj)
    pm.parent(objs, "Text_*")
    pm.makeIdentity(objs, a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.ResetTransformations(pm.ls(objs))
    pm.delete(objs, ch=True)
    pm.parent(pm.listRelatives(objs, ad=True), "Text_*", r=True, s=True)
    pm.delete("Char_*", objs)
    pm.ls("Text_*")[0].rename(text+"_crv")