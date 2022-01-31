import maya.cmds as cmds
import pymel.core as pm
import copy, re

TOOLNAME = "MyUse"
TOOLTITLE = "My Use"

WI01 = (2,273)
WI02 = (1,136,136)

CREATE00 = [
    "  Blend Shape", "  Cluster", "  Lattice",
]

CREATE01 = [
    "  Bend", "  Squash", "  Twist", "  Wave", "  Sine", "  Flare",
]
CREATE02 = [
    "  Distance Tool", "  Face Normal", "  = Normal Size",
    "  Border Edges", "  = Edge Width", "="*14, "  File Path Editor",
]

def btnLayout(cnt):
    if cnt == 1:
        cmds.rowLayout(nc=2, cw2=WI01)
        cmds.text("")
    elif cnt == 2:
        cmds.rowLayout(nc=3, cw3=WI02)
        cmds.text("")

def frame(text, tmp=True):
    cmds.frameLayout(l=text, cll=True, w=285)
    if tmp:
        cmds.rowLayout(nc=1, h=1)
        cmds.setParent("..")

def endSpace():
    cmds.setParent("..")
    cmds.separator(h=1)
    cmds.setParent("..")

def createBtn(subject, things):
    wi = (50,111,111)
    cmds.rowLayout(nc=3, cw3=wi)
    cmds.text(subject, w=wi[0])
    cmds.button(l=things[0][0], c=things[0][1], w=wi[1], h=25)
    cmds.button(l=things[1][0], c=things[1][1], w=wi[2], h=25)
    cmds.setParent("..")

def applyMenuItem(item):
    # CREATE00
    if item == CREATE00[0]:
        cmds.CreateBlendShapeOptions()
    elif item == CREATE00[2]:
        cmds.CreateLatticeOptions()
    elif item == CREATE00[1]:
        cmds.CreateClusterOptions()
    # CREATE01
    elif item == CREATE01[0]:
        cmds.BendOptions()
    elif item == CREATE01[1]:
        cmds.SquashOptions()
    elif item == CREATE01[2]:
        cmds.TwistOptions()
    elif item == CREATE01[3]:
        cmds.WaveOptions()
    elif item == CREATE01[4]:
        cmds.SineOptions()
    elif item == CREATE01[5]:
        cmds.FlareOptions()
    # CREATE02
    elif item == CREATE02[0]:
        cmds.DistanceTool()
    elif item == CREATE02[1]:
        cmds.ToggleFaceNormalDisplay()
    elif item == CREATE02[2]:
        cmds.ChangeNormalSize()
    elif item == CREATE02[3]:
        cmds.ToggleBorderEdges()
    elif item == CREATE02[4]:
        cmds.ChangeEdgeWidth()
    elif item == CREATE02[6]:
        cmds.FilePathEditor()

if cmds.window(TOOLNAME, ex=True):
    cmds.deleteUI(TOOLNAME)

WINDOW = cmds.window(TOOLNAME, t=TOOLTITLE)
tabs = cmds.tabLayout(imh=5, imw=5)
# form = cmds.formLayout()
# cmds.formLayout(form, e=True, attachForm=((tabs,'top',0), (tabs,'left',0), (tabs,'right',0), (tabs,'bottom',0)))

#--------------------------------------------------------------------------------------------#

# 1: Create
ch1 = cmds.rowColumnLayout(w=285, nc=1)


# Joint Size
frame("Joint Size", 0)
jnt = cmds.floatSliderButtonGrp(l="Size   ", bl="Set", bc="jointSize()", cw4=(50,50,70,50), f=True, min=0.1, max=1, v=0.5, h=30)
cmds.setParent("..")


# Create
frame("Create")

btnLayout(2)
cmds.button(l="Loc", c="cmds.CreateLocator()", w=WI02[1], h=25)
cmds.button(l="Curve", c="cmds.EPCurveToolOptions()", w=WI02[2], h=25)
cmds.setParent("..")

createBtn(
    "    Joints : ",
    [["Jnt", "cmds.JointTool()"], ["Insert", "cmds.InsertJointTool()"]]
)
createBtn(
    "",
    [["Orient","cmds.OrientJointOptions()"], ["Mirror", "cmds.MirrorJointOptions()"]]
)
createBtn(
    "  Handle : ",
    [["IK", "cmds.IKHandleToolOptions()"], ["IK Spline", "cmds.IKSplineHandleToolOptions()"]]
)
createBtn(
    "      Skin : ",
    [["Bind", "cmds.SmoothBindSkinOptions()"], ["Detach", "cmds.DetachSkinOptions()"]]
)
createBtn(
    " Weights: ",
    [["Paint", "cmds.ArtPaintSkinWeightsToolOptions()"], ["Add Influence", "cmds.AddInfluenceOptions()"]]
)
createBtn(
    "",
    [["HSW", "cmds.WeightHammer()"], ["Mirror", "cmds.MirrorSkinWeightsOptions()"]]
)

wi = (50,111,111)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="CpEd", c="cmds.ComponentEditor()", w=wi[1], h=25)
create_options = cmds.optionMenu(w=wi[2], cc=applyMenuItem, h=25)
for obj in CREATE00:
    cmds.menuItem(l=obj)
cmds.setParent("..")
cmds.separator(h=1)

cmds.rowLayout(nc=2, cw2=WI01)
cmds.text("")
cmds.button(l="Node Editor", c="cmds.NodeEditorWindow()", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(2)
cmds.button(l="Set Driven Key", c="cmds.SetDrivenKeyOptions()()", w=WI02[1], h=30)
cmds.button(l="Connection Editor", c="cmds.ConnectionEditor()", w=WI02[2], h=30)
cmds.setParent("..")

btnLayout(2)
create_options = cmds.optionMenu(w=WI02[1], cc=applyMenuItem, h=25)
for obj in CREATE01:
    cmds.menuItem(l=obj)
create_options = cmds.optionMenu(w=WI02[2], cc=applyMenuItem, h=25)
for obj in CREATE02:
    cmds.menuItem(l=obj)
endSpace()


# TRS
frame("TRS")

cmds.rowLayout(nc=1)
match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,58,52,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Match", c="matchFreeze()", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Freeze", c="matchFreeze(False)", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

btnLayout(2)
cmds.button(l="Rest Tfm", c="cmds.ResetTransformations()", w=WI02[1], h=30)
cmds.button(l="Center Pivot", c="cmds.CenterPivot()", w=WI02[2], h=30)
cmds.setParent("..")

btnLayout(2)
cmds.button(l="Delete Hist", c="cmds.DeleteHistory()", w=WI02[1], h=30)
cmds.button(l="LBA", c="cmds.ToggleLocalRotationAxes()", w=WI02[2], h=30)
endSpace()

#--------------------------------------------------------------------------------------------#

# 2: Naming
cmds.setParent(WINDOW)
ch2 = cmds.rowColumnLayout(w=285, nc=1)


# Outline
frame("Outline")
btnLayout(1)
cmds.button(l="Set in order", c="setInOrder()", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Copy and New Group", c="newGroup()", w=WI01[1], h=30)
endSpace()


# Rename
frame("Rename")

cmds.rowLayout(nc=1)
pos_check = cmds.radioButtonGrp(l="Position : ", cw4=(60,65,65,10), la3=["rt","lf","None"], nrb=3, sl=3, h=25)
cmds.setParent("..")

btnLayout(2)
hf = cmds.textField(w=WI02[1], tx="Front", h=25)
hb = cmds.textField(w=WI02[2], tx="Back", h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Rename", c="hashRenamer()", w=WI01[1], h=30)
endSpace()


# Replace
frame("Replace")

cmds.rowLayout(nc=1)
replace_check = cmds.radioButtonGrp(l="Check : ", cw3=(80,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi=(80,195)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="    Search for :", w=wi[0])
search_w = cmds.textField(w=wi[1], tx="", h=25)
cmds.setParent("..")

cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="Replace with :", w=wi[0])
replace_w = cmds.textField(w=wi[1], tx="", h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Replace", c="SearchReplace()", w=WI01[1], h=30)
endSpace()


# Add
frame("Add")

cmds.rowLayout(nc=1)
add_check = cmds.radioButtonGrp(l="Check : ", cw3=(50,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi = (50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("Before", l="  Before : ", w=wi[0])
brn = cmds.textField(w=wi[1], h=25)
cmds.text("")
cmds.button(l="Add", c="renamer(1)", w=wi[3], h=25)
cmds.setParent("..")

cmds.rowLayout(nc=4, cw4=wi)
cmds.text("After", l="    After : ", w=wi[0])
arn = cmds.textField(w=wi[1], h=25)
cmds.text("")
cmds.button(l="Add", c="renamer(2)", w=wi[3], h=25)
cmds.setParent("..")
cmds.separator(h=1)

wi = (1,90,90,90)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("")
cmds.button(l="grp", w=wi[1], c="add(1)", h=25)
cmds.button(l="jnt", w=wi[2], c="add(2)", h=25)
cmds.button(l="ctrl", w=wi[3], c="add(3)", h=25)
cmds.setParent("..")

cmds.rowLayout(nc=4, cw4=wi)
cmds.text("")
cmds.button(l="extra", w=wi[1], c="add(4)", h=25)
cmds.button(l="loc", w=wi[2], c="add(5)", h=25)
cmds.button(l="drv", w=wi[3], c="add(6)", h=25)
endSpace()

#--------------------------------------------------------------------------------------------#

# 3: Attr
cmds.setParent(WINDOW)
ch3 = cmds.rowColumnLayout(w=285, nc=1)


# Lock
frame("Lock")

cmds.rowLayout(nc=1)
lock_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,60,60,60,10), la4=["Trans","Rot","Scale","Vis"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

btnLayout(2)
cmds.button(l="Lock + UnKeyable", c="lockUnlock(True, False)", w=WI02[1], h=30)
cmds.button(l="Lock + Keyable", c="lockUnlock(True, True)", w=WI02[2], h=30)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Unlock + Keyable", c="lockUnlock(False, True)", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

btnLayout(2)
cmds.button(l="Lock Selected", c="lockUnlock(True, True, True)", w=WI02[1], h=30)
cmds.button(l="Unlock Selected", c="lockUnlock(False, True, True)", w=WI02[2], h=30)
endSpace()


# Attribute
frame("Attribute")

wi=(45,230)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="  Name : ", w=wi[0])
attr_tx = cmds.textField(w=wi[1], tx="", h=25)
cmds.setParent("..")

wi = (45,20,65,69,69)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text(l="   Reset :  ", w=wi[0])
attr_check = cmds.checkBox(l="", w=wi[1], h=25)
cmds.text(l="  Min/Max :", w=wi[2])
min_attr = cmds.textField(w=wi[3], tx=0.0, h=25)
max_attr = cmds.textField(w=wi[4], tx=1.0, h=25)
cmds.setParent("..")

wi=(65,210)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="  Enum List : ", w=wi[0])
en01_tx = cmds.textField(w=wi[1], tx="OFF:ON", h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Change Attr Name", c="changeAttrName()", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Add Float Attr", c="addAttr(0)", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Add Bool Attr", c="addAttr(1)", w=WI01[1], h=30)
cmds.setParent("..")

btnLayout(2)
cmds.button(l="Separator Attr", c="addAttr(2)", w=WI02[1], h=30)
cmds.button(l="Delete Attr", c="deleteAttr()", w=WI02[2], h=30)
cmds.setParent("..")
cmds.separator(h=1)

wi=(1,67,67,67,67)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("")
cmds.button(l="UUP", c="deleteAttr(True, True)", w=wi[1], h=30)
cmds.button(l="UP", c="changeAttrOder(True)", w=wi[2], h=30)
cmds.button(l="DOWN", c="changeAttrOder(False)", w=wi[3], h=30)
cmds.button(l="DDOWN", c="deleteAttr(False, True)", w=wi[4], h=30)
endSpace()


# Spread Constraint
frame("Spread Constraint")

btnLayout(1)
spread_quick_check = cmds.checkBoxGrp(l="Quick: ", ncb=1, cw2=(55,10), h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
spread_axes_check = cmds.checkBoxGrp(l=" Axes: ", ncb=3, cw4=(60,60,60,10), la3=["X","Y","Z"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
spread_const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Add Attr", c="spread()", w=WI01[1], h=30)
endSpace()

#--------------------------------------------------------------------------------------------#

# 4: Ctrl
cmds.setParent(WINDOW)
ch4 = cmds.rowColumnLayout(w=285, nc=1)


# Controller
frame("Controller")

cmds.rowLayout(nc=1)
ctrl_make = cmds.radioButtonGrp(l=" Make : ", cw3=(60,100,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi = (60,100)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("      Shape :", w=wi[0])
shapes = cmds.optionMenu(w=wi[1], h=25)
cmds.menuItem(l="  Circle")
cmds.menuItem(l="  Box")
cmds.menuItem(l="  Ball")
cmds.menuItem(l="  Cross 1")
cmds.menuItem(l="  Cross 2")
cmds.menuItem(l="  Eyes")
cmds.menuItem(l="  Handle")
cmds.menuItem(l="  Arrow 1")
cmds.menuItem(l="  Arrow 2")
cmds.menuItem(l="  Arrow 4")
cmds.setParent("..")

cmds.rowLayout(nc=1)
axes = cmds.radioButtonGrp(l="Axes : ", la3=["X","Y","Z"], nrb=3, cw4=(60,70,70,20), sl=1, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Create Controller", c="createController()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

# Text
wi = (45,175,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="   Text :  ", w=wi[0])
tx = cmds.textField(w=wi[1], h=25)
cmds.text("")
cmds.button(l="Create", c="text()", w=wi[3], h=25)
endSpace()


# Constraint
frame("Constraint")

btnLayout(2)
mo_quick_check = cmds.checkBoxGrp(l="Quick: ", ncb=1, cw2=(55,10), h=25)
mo_check = cmds.checkBoxGrp(l="Maintain offset : ", ncb=1, v1=True, cw2=(90,10), h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
axes_check = cmds.checkBoxGrp(l=" Axes: ", ncb=3, cw4=(60,60,60,10), la3=["X","Y","Z"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
mo_const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Constraint", c="const()", w=WI01[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

btnLayout(2)
cmds.button(l="Aim Constraint", c="cmds.AimConstraintOptions()", w=WI02[1], h=30)
cmds.button(l="PoleVector Constraint", c="cmds.poleVectorConstraint(w=1)", w=WI02[1], h=30)
endSpace()


# Color Picker
frame("Color Picker", 0)

wi=(45,45,45,45,45,45)
cmds.rowLayout(nc=6, cw6=wi)
cmds.button(l="", w=wi[0], c="colorPicker(13)", bgc=(1,0,0), h=30)
cmds.button(l="", w=wi[1], c="colorPicker(17)",bgc=(1,1,0), h=30)
cmds.button(l="", w=wi[2], c="colorPicker(6)", bgc=(0,0,1), h=30)
cmds.button(l="", w=wi[3], c="colorPicker(18)", bgc=(0,1,1), h=30)
cmds.button(l="", w=wi[4], c="colorPicker(20)", bgc=(1,0.75,0.75), h=30)
cmds.button(l="More", w=wi[5], c="color()", h=30)
cmds.setParent("..")
cmds.setParent("..")

#--------------------------------------------------------------------------------------------#

# 4: Advance
cmds.setParent(WINDOW)
ch5 = cmds.rowColumnLayout(w=285, nc=1)


# ing
# Rivet
frame("Rivet")

cmds.rowLayout(nc=1)
rivet_check = cmds.radioButtonGrp(l="Check : ", cw3=(50,90,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
cmds.setParent("..")

btnLayout(1)
cmds.button(l="Rivet", c="rivet()", w=WI01[1], h=30)
endSpace()


# ing
# Motion path
frame("Motion path")

endSpace()

# ing
# Copy Weight



#--------------------------------------------------------------------------------------------#

cmds.tabLayout(tabs, edit=True, tabLabel=((ch1, "Create"), (ch2, "Naming"), (ch3, "Attr"), (ch4, "Ctrl"), (ch5, "Advance")))

cmds.showWindow(TOOLNAME)

#-------------------------------------- Active Code ------------------------------------#

def jointSize():
    j = cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)


def colorPicker(num):
    a = cmds.ls(sl=True)
    for col in a:
        b = cmds.listRelatives(col, c=True)
        #cmds.setAttr(b[0]+".overrideEnabled", 1)
        #cmds.setAttr(b[0]+".overrideColor", num)
        cmds.setAttr(col+".overrideEnabled", 1)
        cmds.setAttr(col+".overrideColor", num)


def matchFreeze(tmp=True):
    if tmp:
        if cmds.checkBoxGrp(match_check, q=True, v1=True):
            cmds.MatchTranslation()
        if cmds.checkBoxGrp(match_check, q=True, v2=True):
            cmds.MatchRotation()
        if cmds.checkBoxGrp(match_check, q=True, v3=True):
            cmds.MatchScaling()
        if cmds.checkBoxGrp(match_check, q=True, v4=True):
            cmds.MatchPivots()
    else:
        if cmds.checkBoxGrp(match_check, q=True, v1=True):
            cmds.makeIdentity(a=True, t=1, r=0, s=0, n=0, pn=1)
        if cmds.checkBoxGrp(match_check, q=True, v2=True):
            cmds.makeIdentity(a=True, t=0, r=1, s=0, n=0, pn=1)
        if cmds.checkBoxGrp(match_check, q=True, v3=True):
            cmds.makeIdentity(a=True, t=0, r=0, s=1, n=0, pn=1)


def lockUnlock(i, j, tmp=False):
    ranges = []
    objs = cmds.ls(sl=True)
    
    if tmp:
        sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
        for sl_attr in sl_attrs:
            ranges.append("."+sl_attr)
        for obj in objs:
            for attr1 in ranges:
                cmds.setAttr(obj+attr1, l=i, k=j)
    else:
        if cmds.checkBoxGrp(lock_check, q=True, v1=True):
            ranges.append(".t")
        if cmds.checkBoxGrp(lock_check, q=True, v2=True):
            ranges.append(".r")
        if cmds.checkBoxGrp(lock_check, q=True, v3=True):
            ranges.append(".s")
        for obj in objs:
            for attr1 in ranges:
                for attr2 in ["x", "y", "z"]:
                    cmds.setAttr(obj+attr1+attr2, l=i, k=j)
            if cmds.checkBoxGrp(lock_check, q=True, v4=True):
                cmds.setAttr(obj+".visibility", l=i, k=j)

#--------------------------------------------------------------------------------------------#

# ing
def newGroup():
    objs = pm.ls(sl=True)
    tmps = pm.duplicate(rr=True)
    print tmps.reverse()
    for x in range(len(tmps)):
        tmp = pm.ls(tmps[x])
        print tmp
#        pm.parent(tmp, w=True)
        grp = pm.group(em=True)
        pm.parentConstraint(tmp, grp, mo=False, n="ex")
        pm.delete("ex")
        pm.parent(tmp, grp)
        pm.parent(pm.ls(tmps[x+1]), pm.ls(tmps[x]))
        
#    for x in range(len(tmp), 0):
#        print tmp[x]
#        grp = cmds.group(em=True)
#        lst.append(grp)
#        cmds.parentConstraint(tmp[x], grp, mo=False, n="ex")
#        cmds.delete("ex")
#        cmds.parent(tmp[x].split("|")[-1], grp)
#        cmds.parent(grp, tmp[x-1])


def setInOrder():
    objs = pm.listRelatives(ad=True, typ='joint')
    objs += pm.listRelatives(ad=True, typ='transform')
    objs += pm.ls(sl=True)
    num_list = []
    for obj in objs:
        num_list.append(int(re.sub(r"[^0-9]", "", obj.name())))
    for x in range(min(num_list), max(num_list)+1):
        for y in range(len(num_list)):
            if x == num_list[y]:
                pm.reorder(objs[y], b=True)
                break

#--------------------------------------------------------------------------------------------#

def text():
    t = pm.textField(tx, q=True, tx=True)
    
    pm.textCurves(t=t, ch=True)
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
    pm.ls("Text_*")[0].rename(t+"_crv")


def hashRenamer():
    hf_text = cmds.textField(hf, q=True, tx=True)
    hb_text = cmds.textField(hb, q=True, tx=True)
    
    if cmds.radioButtonGrp(pos_check, q=True, sl=1) == 1:
        hf_text = "rt_"+hf_text
    elif cmds.radioButtonGrp(pos_check, q=True, sl=1) == 2:
        hf_text = "lf_"+hf_text
    if hb_text != "":
        hb_text = "_"+hb_text
    
    objs = pm.ls(sl=True)
    for x in range(len(objs)):
        if len(objs) == 1:
            name = hf_text+hb_text
        elif x < 9:
            name = hf_text+"_0"+str(x+1)+hb_text
        else:
            name = hf_text+"_"+str(x+1)+hb_text
        objs[x].rename(name)


def SearchReplace():
    search_wd = cmds.textField(search_w, q=True, tx=True)
    replace_wd = cmds.textField(replace_w, q=True, tx=True)
    
    if cmds.radioButtonGrp(replace_check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True)
        objs += pm.ls(sl=True)
    else:
        objs = pm.ls(sl=True)
    for obj in objs:
        obj.rename(obj.name().replace(search_wd, replace_wd))


def namer(i, objs, tmp):
    if tmp:
        arn_text = tmp
    else:
        brn_text = cmds.textField(brn, q=True, tx=True)
        arn_text = cmds.textField(arn, q=True, tx=True)

    for obj in objs:
        if i == 1:
            blen = len(brn_text)
            bcheck=""
            for x in range(blen+1):
                bcheck += obj[x]
            if bcheck != brn_text+"_":
                name = brn_text+"_"+obj
                obj.rename(name)
        else:
            alen = len(arn_text)
            acheck=""
            for x in range(alen+1):
                tmp = len(obj.name())-len(arn_text)+x-1
                acheck += obj[tmp]
            if acheck != "_"+arn_text:
                name = obj+"_"+arn_text
                obj.rename(name)


def renamer(i):
    if cmds.radioButtonGrp(add_check, q=True, sl=1) == 2:
        objs = pm.listRelatives(ad=True, typ='joint')
        objs += pm.listRelatives(ad=True, typ='transform')
        objs += pm.ls(sl=True)
        print objs
    else:
        objs = pm.ls(sl=True)
    namer(i, objs, None)


def add(tail):
    tails = [
        "grp", "jnt", "ctrl",
        "extra", "loc", "drv",
    ]
    objs = pm.ls(sl=True)
    text = tails[tail-1]
    namer(0, objs, text)

#--------------------------------------------------------------------------------------------#

def addAttr(tmp):
    attr_text = cmds.textField(attr_tx, q=True, tx=True)
    
    objs = pm.ls(sl=True)
    for obj in objs:
        if tmp == 0:
            if cmds.checkBox(attr_check, q=True, v=True):
                pm.addAttr(obj, ln=attr_text, at="double", dv=0)
                pm.setAttr(obj+"."+attr_text, k=True)
            else:
                min_num = float(cmds.textField(min_attr, q=True, tx=True))
                max_num = float(cmds.textField(max_attr, q=True, tx=True))
                pm.addAttr(obj, ln=attr_text, at="double", dv=0, min=min_num, max=max_num)
                pm.setAttr(obj+"."+attr_text, k=True)
        elif tmp == 1:
                en = cmds.textField(en01_tx, q=True, tx=True)
                pm.addAttr(obj, ln=attr_text, at="enum", en=en)
                pm.setAttr(obj+"."+attr_text, k=True)
        else:
            cnt = 0
            flag = True
            while flag:
                cnt_str = "separator"+str(cnt)
                if pm.attributeQuery(cnt_str, n=obj.name(), ex=True):
                    cnt += 1
                else:
                    pm.addAttr(obj, ln=cnt_str, nn="----------", at="enum", en="--------:")
                    pm.setAttr(obj+"."+cnt_str, cb=True)
                    flag = False


# ing
def changeAttrName():
    attr_text = cmds.textField(attr_tx, q=True, tx=True)
    objs = pm.ls(sl=True)
    for obj in objs:
        sl_attr = pm.channelBox("mainChannelBox", q=True, sma=True)
        print sl_attr, attr_text
        
    

def deleteAttr(up=False, tmp=False):
    objs = pm.ls(sl=True)
    attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    sl_attrs = copy.deepcopy(attrs)
    
    for obj in objs:
        if up:
            attrs = pm.listAttr(obj, ud=True)
            for attr in sl_attrs:
                attrs.remove(attr)
        for attr in attrs:
            try:
                pm.deleteAttr (obj, at=attr)
                if tmp:
                    pm.undo()
            except:
                pass


def subDelAttr(obj, string):
    pm.deleteAttr(obj, at=string)
    pm.undo()


def changeAttrOder(updown):
    objs = pm.ls(sl=True)
    sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    
    if updown:
        for obj in objs:
            attrs = pm.listAttr(obj, ud=True)
            flag = False
            for x in range(len(attrs)):
                if attrs[x] == sl_attrs[0]:
                    subDelAttr(obj, attrs[x-1])
                    x += len(sl_attrs)
                    flag = True
                elif attrs[x] in sl_attrs:
                    if x+len(sl_attrs)-1 < len(attrs):
                        subDelAttr(obj, attrs[x+len(sl_attrs)-1])
                        x += 1
                elif flag == True:
                    subDelAttr(obj, attrs[x])
    else:
        for obj in objs:
            attrs = pm.listAttr(obj, ud=True)
            flag = False
            for x in range(len(attrs)):
                if attrs[x] == sl_attrs[0]:
                    if x+len(sl_attrs) < len(attrs):
                        tmp = attrs[x+len(sl_attrs)]
                        subDelAttr(obj, tmp)
                        subDelAttr(obj, attrs[x])
                        x += len(sl_attrs)
                        flag = True
                elif attrs[x] in sl_attrs:
                    subDelAttr(obj, attrs[x])
                    x += 1
                elif flag == True and attrs[x] != tmp:
                    subDelAttr(obj, attrs[x])
            
#--------------------------------------------------------------------------------------------#

def subSpread(obj, num):
    pm.addAttr(obj, ln="separator", nn="----------", at="enum", en="--------:")
    pm.setAttr(obj+"."+"separator", cb=True)
    pm.addAttr(obj, ln="spread", at="double", dv=0, min=0, max=num)
    pm.setAttr(obj+".spread", k=True)


def spread():
    tmp = const(True)
    if tmp:
        objs = pm.ls(sl=True)
        cons = []
        if cmds.checkBoxGrp(spread_quick_check, q=True, v1=True):
            for nb in range(2, len(objs), 3):
                subSpread(objs[nb], 1)
                cons += pm.listRelatives(pm.ls(objs[nb]), ad=True, typ='constraint')
        else:
            subSpread(objs[-1], len(objs)-2)
            cons += pm.listRelatives(pm.ls(objs[-1]), ad=True, typ='constraint')
        attrs = []
        sel = -1
        for con in cons:
            attrs.append(pm.listAttr(con, ud=True))
        for con_count in range(len(cons)):
            if tmp:
                if sel+3 < len(objs) and con_count < len(objs)-1:
                    if objs[sel] != cons[con_count].split("_")[0]:
                        sel += 3
            attr = attrs[con_count]
            for x in range(len(attr)):
                pm.setAttr(objs[sel]+".spread", x)
                pm.setAttr(cons[con_count]+"."+attr[x], 1)
                for y in range(len(attr)):
                    if x != y:
                        pm.setAttr(cons[con_count]+"."+attr[y], 0)
                for z in range(len(attr)):
                    pm.setDrivenKeyframe(cons[con_count]+"."+attr[z], cd=objs[sel]+".spread")
                    
#--------------------------------------------------------------------------------------------#

def subConst(objs, num):
    for x in range(len(objs)-1):
        constrains(objs[x], objs[-1], num)


def const(tmp=False):
    objs = cmds.ls(sl=True)
    if len(objs) == 1:
        cmds.warning("Select only one obj!")
    if tmp:
        num = 1
        if cmds.checkBoxGrp(spread_quick_check, q=True, v1=True):
            if len(objs) % 3 != 0:
                cmds.warning("Select an obj as a multiple of 3! Objs nums: {}".format(len(objs)))
                return False
            else:
                for x in range(0, len(objs), 3):
                    constrains(objs[x], objs[x+2], num)
                    constrains(objs[x+1], objs[x+2], num)
                return True
        else:
            subConst(objs, num)
            return True
    else:
        num = 2
        if cmds.checkBoxGrp(mo_quick_check, q=True, v1=True):
            if len(objs) % 2 != 0:
                cmds.warning("Select even numbers of objs! Objs nums: {}".format(len(objs)))
            else:
                for x in range(0, len(objs), 2):
                    constrains(objs[x], objs[x+1], num)
        else:
            subConst(objs, num)


def constrains(con, obj, i):
    skip = []
    if i == 0:
        a = const_check
    elif i == 1:
        a = spread_const_check
        if not cmds.checkBoxGrp(spread_axes_check, q=True, v1=True):
            skip.append("x")
        if not cmds.checkBoxGrp(spread_axes_check, q=True, v2=True):
            skip.append("y")
        if not cmds.checkBoxGrp(spread_axes_check, q=True, v3=True):
            skip.append("z")
    else:
        a = mo_const_check
        if not cmds.checkBoxGrp(axes_check, q=True, v1=True):
            skip.append("x")
        if not cmds.checkBoxGrp(axes_check, q=True, v2=True):
            skip.append("y")
        if not cmds.checkBoxGrp(axes_check, q=True, v3=True):
            skip.append("z")
    if cmds.checkBoxGrp(mo_check, q=True, v1=True):
        if cmds.checkBoxGrp(a, q=True, v1=True):
            cmds.parentConstraint(con, obj, mo=True, st=skip, sr=skip)
        if cmds.checkBoxGrp(a, q=True, v2=True):
            cmds.pointConstraint(con, obj, mo=True, sk=skip)
        if cmds.checkBoxGrp(a, q=True, v3=True):
            cmds.orientConstraint(con, obj, mo=True, sk=skip)
        if cmds.checkBoxGrp(a, q=True, v4=True):
            cmds.scaleConstraint(con, obj, mo=True, sk=skip)
    else:
        if cmds.checkBoxGrp(a, q=True, v1=True):
            cmds.parentConstraint(con, obj, st=skip, sr=skip)
        if cmds.checkBoxGrp(a, q=True, v2=True):
            cmds.pointConstraint(con, obj, sk=skip)
        if cmds.checkBoxGrp(a, q=True, v3=True):
            cmds.orientConstraint(con, obj, sk=skip)
        if cmds.checkBoxGrp(a, q=True, v4=True):
            cmds.scaleConstraint(con, obj, sk=skip)
    cmds.DeleteHistory(con)


def createController():
    objs = cmds.ls(sl=True)
    if cmds.radioButtonGrp(ctrl_make, q=True, sl=1) == 1:
        for x in range(len(objs)):
            obj = objs[x]
            selectShape(obj)
    else:
        selectShape(objs)


def selectShape(obj):
    # circle
    if cmds.optionMenu(shapes, q=True, sl=1) == 1:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            c = cmds.circle(nr=(1,0,0))[0]
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 2:
            c = cmds.circle(nr=(0,1,0))[0]
        else:
            c = cmds.circle(nr=(0,0,1))[0]
    # box
    elif cmds.optionMenu(shapes, q=True, sl=2) == 2:
        c = cmds.curve(d=1, p=[(1,1,1),(1,-1,1), (1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1)])
    # ball
    elif cmds.optionMenu(shapes, q=True, sl=3) == 3:
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
    # cross 1
    elif cmds.optionMenu(shapes, q=True, sl=4) == 4:
        c = cmds.curve(d=1, p=[(0,0,-2),(0,0,2),(0,0,0),(-2,0,0),(2,0,0)])
    # cross 2
    elif cmds.optionMenu(shapes, q=True, sl=5) == 5:
        c = cmds.curve(d=1, p=[(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),(1,0,1),(1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),(-1,0,-1),(-1,0,-3)])
    # eye
    elif cmds.optionMenu(shapes, q=True, sl=6) == 6:
        tmp1 = cmds.circle(nr=(0,1,0))
        tmp2 = cmds.curve(d=3, p=[(-2.05541,0,-0.0124173),(-1.365656,0,-0.507243),(0.0138526,0,-1.496896),(1.337951,0,-0.498965),(2,0,0)])
        tmp3 = cmds.curve(d=3, p=[(-2.05541,0,-0.0124173),(-1.365656,0,-0.507243),(0.0138526,0,-1.496896),(1.337951,0,-0.498965),(2,0,0)])
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
    elif cmds.optionMenu(shapes, q=True, sl=7) == 7:
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
    elif cmds.optionMenu(shapes, q=True, sl=8) == 8:
        c = cmds.curve(d=1, p=[(-2,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),(1,0,1),(-2,0,1),(-2,0,-1)])
    # arrow 2
    elif cmds.optionMenu(shapes, q=True, sl=9) == 9:
        c = cmds.curve(d=1, p=[(-1,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),(1,0,1),(-1,0,1),(-1,0,2),(-3,0,0),(-1,0,-2),(-1,0,-1)])
    # arrow 4
    elif cmds.optionMenu(shapes, q=True, sl=10) == 10:
        c = cmds.curve(d=1, p=[(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)])
        
    grp = cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.ResetTransformations(c)

    if cmds.optionMenu(shapes, q=True, sl=4) == 4 or cmds.optionMenu(shapes, q=True, sl=5) == 5:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
        pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif cmds.optionMenu(shapes, q=True, sl=7) == 7:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", -90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
    elif cmds.optionMenu(shapes, q=True, sl=8) == 8 or cmds.optionMenu(shapes, q=True, sl=9) == 9:
        if cmds.radioButtonGrp(axes, q=True, sl=2) == 2:
            cmds.setAttr(c+".rotateX", 90)
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateY", -90)
            
    pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    cmds.parentConstraint(obj, grp, mo=False, n="ex")
    cmds.delete("ex")
    if cmds.radioButtonGrp(ctrl_make, q=True, sl=1) == 1:
        constrains(c, obj, 0)

#--------------------------------------------------------------------------------------------#

def rivet():
    # Each
    if cmds.radioButtonGrp(rivet_check, q=True, sl=1) == 1:
        pass
    # Sum
    else:
        pass
    objs = pm.ls(sl=True)
    for obj in objs:
        print obj.name()

#--------------------------------------------------------------------------------------------#

def color():
    win = "ColorPicker"
    wintitle = "Color Picker"
    
    if cmds.window(win, ex=True):
        cmds.deleteUI(win)
    cmds.window(win, t=wintitle)
    cmds.rowColumnLayout(w=255)
    
    wi=(125,125)
    cmds.rowLayout(nc=2, cw2=wi)
    cmds.button(l="", w=wi[0], h=60, c="colorPicker(13)", bgc=(1,0,0))
    cmds.button(l="", w=wi[1], h=60, c="colorPicker(17)",bgc=(1,1,0))
    cmds.setParent("..")
    
    cmds.rowLayout(nc=2, cw2=wi)
    cmds.button(l="", w=wi[0], h=60, c="colorPicker(6)", bgc=(0,0,1))
    cmds.button(l="", w=wi[1], h=60, c="colorPicker(18)", bgc=(0,1,1))
    cmds.setParent("..")
    
    wi2=(41,41,41,41,41,41)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="colorPicker(20)", bgc=(1,0.75,0.75))
    cmds.button(l="", w=wi2[1], h=40, c="colorPicker(21)", bgc=(1,0.7,0.5))
    cmds.button(l="", w=wi2[2], h=40, c="colorPicker(9)", bgc=(0.9,0,0.9))
    cmds.button(l="", w=wi2[3], h=40, c="colorPicker(31)", bgc=(0.6,0.2,0.4))
    cmds.button(l="", w=wi2[4], h=40, c="colorPicker(12)", bgc=(0.7,0.2,0))
    cmds.button(l="", w=wi2[5], h=40, c="colorPicker(4)", bgc=(0.7,0,0.2))
    cmds.setParent("..")
    
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="colorPicker(16)", bgc=(1,1,1))
    cmds.button(l="", w=wi2[1], h=40, c="colorPicker(30)", bgc=(0.4,0.2,0.6))
    cmds.button(l="", w=wi2[2], h=40, c="colorPicker(22)", bgc=(1,1,0.4))
    cmds.button(l="", w=wi2[3], h=40, c="colorPicker(19)", bgc=(0.2,1,0.6))
    cmds.button(l="", w=wi2[4], h=40, c="colorPicker(14)", bgc=(0,1,0))
    cmds.button(l="", w=wi2[5], h=40, c="colorPicker(27)", bgc=(0.3,0.6,0.3))
    cmds.setParent("..")
    
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="colorPicker(25)", bgc=(0.6,0.6,0.2))
    cmds.button(l="", w=wi2[1], h=40, c="colorPicker(26)", bgc=(0.4,0.6,0.2))
    cmds.button(l="", w=wi2[2], h=40, c="colorPicker(23)", bgc=(0,0.6,0.3))
    cmds.button(l="", w=wi2[3], h=40, c="colorPicker(29)", bgc=(0.2,0.4,0.75))
    cmds.button(l="", w=wi2[4], h=40, c="colorPicker(15)", bgc=(0,0.3,0.7))
    cmds.button(l="", w=wi2[5], h=40, c="colorPicker(5)", bgc=(0,0.1,0.5))
    cmds.setParent("..")
    
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="colorPicker(28)", bgc=(0.2,0.6,0.6))
    cmds.button(l="", w=wi2[1], h=40, c="colorPicker(7)", bgc=(0,0.3,0.1))
    cmds.button(l="", w=wi2[2], h=40, c="colorPicker(8)", bgc=(0,0.1,0.2))
    cmds.button(l="", w=wi2[3], h=40, c="colorPicker(24)", bgc=(0.6,0.4,0.2))
    cmds.button(l="", w=wi2[4], h=40, c="colorPicker(10)", bgc=(0.5,0.3,0.2))
    cmds.button(l="", w=wi2[5], h=40, c="colorPicker(11)", bgc=(0.2,0.1,0.1))
    cmds.setParent("..")
    
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="colorPicker(3)", bgc=(0.7,0.7,0.7))
    cmds.button(l="", w=wi2[1], h=40, c="colorPicker(2)", bgc=(0.3,0.3,0.3))
    cmds.button(l="", w=wi2[2], h=40, c="colorPicker(1)", bgc=(0,0,0))
 
    cmds.showWindow(win)

#--------------------------------------------------------------------------------------------#
