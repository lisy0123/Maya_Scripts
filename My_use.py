import maya.cmds as cmds
import pymel.core as pm
import re

TOOLNAME = "MyUse"
TOOLTITLE = "My Use"

def startspace():
    cmds.rowLayout(nc=1, h=1)
    cmds.setParent("..")

def endspace():
    cmds.setParent("..")
    cmds.separator(h=1)
    cmds.setParent("..")

def applyMenuItem(item):
    if item == "  Blend Shape":
        cmds.CreateBlendShapeOptions()
    elif item == "  Lattice":
        cmds.CreateLatticeOptions(),
    elif item == "  Cluster":
        cmds.CreateClusterOptions()
    elif item == "  Distance Tool":
        cmds.DistanceTool()
    elif item == "  Face Normal":
        cmds.ToggleFaceNormalDisplay()
    elif item == "  = Normal Size":
        cmds.ChangeNormalSize()
    elif item == "  Border Edges":
        cmds.ToggleBorderEdges()
    elif item == "  = Edge Width":
        cmds.ChangeEdgeWidth()
    elif item == "  File Path Editor":
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
cmds.frameLayout(l="Joint Size", cll=True, w=285)
jnt = cmds.floatSliderButtonGrp(l="Size   ", bl="Set", bc="jointSize()", cw4=(50,50,70,50), f=True, min=0.1, max=1, v=0.5, h=30)
cmds.setParent("..")


# Create
cmds.frameLayout(l="Create", cll=True, w=285)
startspace()

wi = (1,137,137)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="Loc", c="cmds.CreateLocator()", w=wi[1], h=25)
cmds.button(l="Curve", c="cmds.EPCurveTool()", w=wi[2], h=25)
cmds.setParent("..")

wi = (50,112,112)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("    Joints : ", w=wi[0])
cmds.button(l="Jnt", c="cmds.JointTool()", w=wi[1], h=25)
cmds.button(l="Insert", c="cmds.InsertJointTool()", w=wi[2], h=25)
cmds.setParent("..")

wi = (50,112,112)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="Orient", c="cmds.OrientJointOptions()", w=wi[1], h=25)
cmds.button(l="Mirror", c="cmds.MirrorJointOptions()", w=wi[2], h=25)
cmds.setParent("..")

wi = (50,112,112)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("  Handle : ", w=wi[0])
cmds.button(l="IK", c="cmds.IKHandleTool()", w=wi[1], h=25)
cmds.button(l="IK Spline", c="cmds.ikHandle(sol='ikSplineSolver', ns=4)", w=wi[2], h=25)
cmds.setParent("..")

wi = (50,112,112)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("      Skin : ", w=wi[0])
cmds.button(l="Bind", c="cmds.SmoothBindSkinOptions()", w=wi[1], h=25)
cmds.button(l="Detach", c="cmds.DetachSkinOptions()", w=wi[2], h=25)
cmds.setParent("..")

cmds.rowLayout(nc=3, cw3=wi)
cmds.text(" Weights: ", w=wi[0])
cmds.button(l="Paint", c="cmds.ArtPaintSkinWeightsToolOptions()", w=wi[1], h=25)
cmds.button(l="Mirror", c="cmds.MirrorSkinWeightsOptions()", w=wi[2], h=25)
cmds.setParent("..")
cmds.separator(h=1)

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Node Editor", c="cmds.NodeEditorWindow()", w=wi[1], h=30)
cmds.setParent("..")

wi = (1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="Set Driven Key", c="cmds.SetDrivenKeyOptions()()", w=wi[1], h=30)
cmds.button(l="Connection Editor", c="cmds.ConnectionEditor()", w=wi[2], h=30)
cmds.setParent("..")

wi = (1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text(" ", w=wi[0])
create_options = cmds.optionMenu(w=wi[1], cc=applyMenuItem, h=25)
cmds.menuItem(l="  Blend Shape")
cmds.menuItem(l="  Lattice")
cmds.menuItem(l="  Cluster")
create_options = cmds.optionMenu(w=wi[1], cc=applyMenuItem, h=25)
cmds.menuItem(l="  Distance Tool")
cmds.menuItem(l="  Face Normal")
cmds.menuItem(l="  = Normal Size")
cmds.menuItem(l="  Border Edges")
cmds.menuItem(l="  = Edge Width")
cmds.menuItem(l="="*14)
cmds.menuItem(l="  File Path Editor")
endspace()


# TRS
cmds.frameLayout(l="TRS", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,55,55,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Match", c="match()", w=wi[1], h=30)
cmds.setParent("..")

wi = (1,90,90,90)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("")
cmds.button(l="Freeze Tfm", c="cmds.FreezeTransformations()", w=wi[1], h=30)
cmds.button(l="Rest Tfm", c="cmds.ResetTransformations()", w=wi[2], h=30)
cmds.button(l="Center Pivot", c="cmds.CenterPivot()", w=wi[3], h=30)
cmds.setParent("..")
cmds.separator(h=1)

wi = (1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="Delete Hist", c="cmds.DeleteHistory()", w=wi[1], h=30)
cmds.button(l="LBA", c="cmds.ToggleLocalRotationAxes()", w=wi[2], h=30)
endspace()

#--------------------------------------------------------------------------------------------#

# 2: Naming
cmds.setParent(WINDOW)
ch2 = cmds.rowColumnLayout(w=285, nc=1)


# Rename
cmds.frameLayout(l="Rename", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
pos_check = cmds.radioButtonGrp(l="Position : ", cw4=(60,65,65,10), la3=["rt","lf","None"], nrb=3, sl=3, h=25)
cmds.setParent("..")

wi=(1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
hf = cmds.textField(w=wi[1], tx="Front", h=25)
hb = cmds.textField(w=wi[2], tx="Back", h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Rename", c="hashRenamer()", w=wi[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Set in order", c="setInOrder()", w=wi[1], h=25)
endspace()


# Replace
cmds.frameLayout(l="Replace", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
replace_check = cmds.radioButtonGrp(l="Check : ", cw3=(80,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi=(80,195)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="    Search for :", w=wi[0])
search_w = cmds.textField(w=wi[1], tx="", h=25)
cmds.setParent("..")

wi=(80,195)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text(l="Replace with :", w=wi[0])
replace_w = cmds.textField(w=wi[1], tx="", h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Replace", c="SearchReplace()", w=wi[1], h=30)
endspace()


# Add
cmds.frameLayout(l="Add", cll=True, w=285)
startspace()

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

wi = (50,170,1,50)
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

wi = (1,90,90,90)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("")
cmds.button(l="extra", w=wi[1], c="add(4)", h=25)
cmds.button(l="loc", w=wi[2], c="add(5)", h=25)
cmds.button(l="drv", w=wi[3], c="add(6)", h=25)
endspace()

#--------------------------------------------------------------------------------------------#

# 3: Attribute
cmds.setParent(WINDOW)
ch3 = cmds.rowColumnLayout(w=285, nc=1)

# Lock
cmds.frameLayout(l="Lock", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
lock_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,60,60,60,10), la4=["Trans","Rot","Scale","Vis"], v1=True, v2=True, v3=True, h=25)
cmds.setParent("..")

wi = (1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("")
cmds.button(l="Lock + UnKeyable", c="lockUnlock(True, False)", w=wi[1], h=25)
cmds.button(l="Lock + Keyable", c="lockUnlock(True, True)", w=wi[2], h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Unlock + Keyable", c="lockUnlock(False, True)", w=wi[1], h=25)
endspace()

# ing, add delete
# Attribute
cmds.frameLayout(l="Attribute", cll=True, w=285)
startspace()

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
min_attr = cmds.textField(w=wi[3], tx="0.0", h=25)
max_attr = cmds.textField(w=wi[4], tx="1.0", h=25)
cmds.setParent("..")

wi = (1,136,136)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("")
cmds.button(l="Float Attr", c="addAttr(0)", w=wi[1], h=25)
cmds.button(l="Bool Attr", c="addAttr(1)", w=wi[2], h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Separator Attr", c="addAttr(2)", w=wi[1], h=25)
cmds.setParent("..")
cmds.separator(h=1)

wi=(1,67,67,67,67)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("")
cmds.button(l="TUP", c="lockUnlock(False, True)", w=wi[1], h=30)
cmds.button(l="UP", c="lockUnlock(False, True)", w=wi[2], h=30)
cmds.button(l="DOWN", c="lockUnlock(False, True)", w=wi[3], h=30)
cmds.button(l="TDOWN", c="lockUnlock(False, True)", w=wi[4], h=30)
endspace()

#--------------------------------------------------------------------------------------------#

# 4: Rigging
cmds.setParent(WINDOW)
ch4 = cmds.rowColumnLayout(w=285, nc=1)


# Controller
cmds.frameLayout(l="Controller", cll=True, w=285)
startspace()

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
# ing
cmds.menuItem(l="  Cross")
cmds.menuItem(l="  Eyes")
cmds.menuItem(l="  Handle")
cmds.menuItem(l="  Arrow1")
cmds.menuItem(l="  Arrow2")
cmds.menuItem(l="  Arrow4")
cmds.setParent("..")

cmds.rowLayout(nc=1)
axis = cmds.radioButtonGrp(l="Axis : ", la3=["X","Y","Z"], nrb=3, cw4=(60,70,70,20), sl=1, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
const_check = cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True, h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Create Controller", c="createController()", w=wi[1], h=30)
cmds.setParent("..")
cmds.separator(h=1)

# Text
wi = (45,175,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="   Text :  ", w=wi[0])
tx = cmds.textField(w=wi[1], h=25)
cmds.text("")
cmds.button(l="Create", c="text()", w=wi[3], h=25)
endspace()


# Constrain
cmds.frameLayout(l="Constrain", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
mo_const_check = cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True, h=25)
cmds.setParent("..")

cmds.rowLayout(nc=1)
mo = cmds.radioButtonGrp(l="Maintain offset : ", cw3=(93,80,50), la2=["On","Off"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Constrain", c="const()", w=wi[1], h=30)
endspace()


# Color Picker
cmds.frameLayout(l="Color Picker", cll=True, w=285)
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


# ing
# Rivet
cmds.frameLayout(l="Rivet", cll=True, w=285)
startspace()

cmds.rowLayout(nc=1)
rivet_check = cmds.radioButtonGrp(l="Check : ", cw3=(50,90,10), la2=["Each","Sum"], nrb=2, sl=1, h=25)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Rivet", c="rivet()", w=wi[1], h=30)
endspace()


# ing
# Motion path
cmds.frameLayout(l="Motion path", cll=True, w=285)
startspace()

endspace()

#--------------------------------------------------------------------------------------------#

cmds.tabLayout(tabs, edit=True, tabLabel=((ch1, "Create"), (ch2, "Naming"), (ch3, "Attribute"), (ch4, "Rigging")))

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


def match():
    if cmds.checkBoxGrp(match_check, q=True, v1=True):
        cmds.MatchTranslation();
    if cmds.checkBoxGrp(match_check, q=True, v2=True):
        cmds.MatchRotation();
    if cmds.checkBoxGrp(match_check, q=True, v3=True):
        cmds.MatchScaling();
    if cmds.checkBoxGrp(match_check, q=True, v4=True):
        cmds.MatchPivots();


def setInOrder():
    objs = pm.listRelatives(ad=True, typ='joint')
    objs += pm.listRelatives(ad=True, typ='transform')
    objs += pm.ls(sl=True)
    num_list = []
    for obj in objs:
        num_list.append(int(re.sub(r"[^0-9]", "", obj.name())))
    for x in range(min(num_list), max(num_list)+1):
        for y in range(0, len(num_list)):
            if x == num_list[y]:
                pm.reorder(objs[y], b=True)
                break


def lockUnlock(i, j):
    ranges = []
    objs = cmds.ls(sl=True)
    
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

# ing
#addAttr -ln "wetfgthjuki"  -at double  -min 0 -max 1 -dv 0 |locator1;
#setAttr -e-keyable true |locator1.wetfgthjuki;
#addAttr -ln "dfg" -nn "eerw" -at double  -dv 0 |locator1;
#setAttr -e-keyable true |locator1.dfg;

#addAttr -ln "sdf"  -at double  -dv 0 |locator1;
#setAttr -e-channelBox true |locator1.sdf;

#catch (`deleteAttr -attribute "sdf" "locator1"`);

#addAttr -ln "dngcdcv" -nn "------" -at "enum" -en "------:"  |locator1;

def addAttr(i):
    attr_text = cmds.textField(attr_tx, q=True, tx=True)
    min_num = cmds.textField(min_attr, q=True, tx=True)
    max_num = cmds.textField(max_attr, q=True, tx=True)
    
    objs = pm.ls(sl=True)
    for obj in objs:
        if i == 0:
            if cmds.checkBox(attr_check, q=True, v=True):
                pass
            else:
                pass
        elif i == 1:
            cnt = 0
            if pm.attributeQuery("separator"+str(cnt), n=obj, e=True):
                print "!!!!"
            pass
        else:
            cnt = 0
            flag = True
            while flag:
                cnt_str = "separator"+str(cnt)
                if pm.attributeQuery(cnt_str, n=obj, e=True):
                    cnt += 1
                else:
                    pm.addAttr(obj, ln=cnt_str, nn="------", at="enum", en="------:")
                    pm.setAttr(obj+"."+cnt_str, cb=True)
                    flag = False

#--------------------------------------------------------------------------------------------#

# ing
def const():
    a = cmds.ls(sl=True)
    for x in range(0, len(a)):
        if x == 0:
            constrains(a[0], a[1], 1)
        if x == 1:
            pass
        if x % 2 == 0:
            constrains(a[x], a[x+1], 1)
        else:
            pass


def createController():
    objs = cmds.ls(sl=True)
    if cmds.radioButtonGrp(ctrl_make, q=True, sl=1) == 1:
        for x in range(0,len(objs)):
            obj = objs[x]
            selectShape(obj)
    else:
        selectShape(objs)


# add check options
def selectShape(obj):
    if cmds.optionMenu(shapes, q=True, sl=1) == 1:
        if cmds.radioButtonGrp(axis, q=True, sl=1) == 1:
            c=cmds.circle(nr=(1,0,0))
        elif cmds.radioButtonGrp(axis, q=True, sl=2) == 2:
            c=cmds.circle(nr=(0,1,0))
        else:
            c=cmds.circle(nr=(0,0,1))
    elif cmds.optionMenu(shapes, q=True, sl=2) == 2:
        c=cmds.curve(d=1, p=[(1,1,1),(1,-1,1), (1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1)])
    #need to fix
    elif cmds.optionMenu(shapes, q=True, sl=3) == 3:
        a = cmds.circle(nr=(1,0,0), n="cir")
        cmds.circle(nr=(0,1,0), n="cir1")
        cmds.circle(nr=(0,0,1), n="cir2")
        cmds.DeleteHistory("cir")
        cmds.DeleteHistory("cir*")
        cmds.parent("cir1Shape","cir", r=True, s=True)
        cmds.parent("cir2Shape","cir", r=True, s=True)
        cmds.delete(cmds.ls("cir1"))
        cmds.delete(cmds.ls("cir2"))
        c=cmds.ls(a)
    grp = cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.parentConstraint(obj, grp, mo=False, n="ex")
    cmds.delete("ex")
    if cmds.radioButtonGrp(ctrl_make, q=True, sl=1) == 1:
        constrains(c, obj, 0)


def constrains(con, obj, i):
    if i == 0:
        a = const_check
    else:
        a = mo_const_check
        if cmds.radioButtonGrp(mo, q=True, sl=1) == 2:
            if cmds.checkBoxGrp(a, q=True, v1=True):
                cmds.parentConstraint(con, obj)
            if cmds.checkBoxGrp(a, q=True, v2=True):
                cmds.pointConstraint(con, obj)
            if cmds.checkBoxGrp(a, q=True, v3=True):
                cmds.orientConstraint(con, obj)
            if cmds.checkBoxGrp(a, q=True, v4=True):
                cmds.scaleConstraint(con, obj)
            return
    if cmds.checkBoxGrp(a, q=True, v1=True):
        cmds.parentConstraint(con, obj, mo=True)
    if cmds.checkBoxGrp(a, q=True, v2=True):
        cmds.pointConstraint(con, obj, mo=True)
    if cmds.checkBoxGrp(a, q=True, v3=True):
        cmds.orientConstraint(con, obj, mo=True)
    if cmds.checkBoxGrp(a, q=True, v4=True):
        cmds.scaleConstraint(con, obj, mo=True)
    cmds.DeleteHistory(con)

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
    for x in range(0, len(objs)):
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
    
    wi2=(41,40,40,41,40,40)
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
