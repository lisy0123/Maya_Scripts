import maya.cmds as cmds


def match(match_check):
    if cmds.checkBoxGrp(match_check, q=True, v1=True):
        cmds.MatchTranslation()
    if cmds.checkBoxGrp(match_check, q=True, v2=True):
        cmds.MatchRotation()
    if cmds.checkBoxGrp(match_check, q=True, v3=True):
        cmds.MatchScaling()
    if cmds.checkBoxGrp(match_check, q=True, v4=True):
        cmds.MatchPivots()


def freeze(match_check):
    if cmds.checkBoxGrp(match_check, q=True, v1=True):
        cmds.makeIdentity(a=True, t=1, r=0, s=0, n=0, pn=1)
    if cmds.checkBoxGrp(match_check, q=True, v2=True):
        cmds.makeIdentity(a=True, t=0, r=1, s=0, n=0, pn=1)
    if cmds.checkBoxGrp(match_check, q=True, v3=True):
        cmds.makeIdentity(a=True, t=0, r=0, s=1, n=0, pn=1)