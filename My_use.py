import maya.cmds as cmds

TOOLNAME = "MyUse"
TOOLTITLE = "My Use"

if cmds.window(TOOLNAME, ex=True):
    cmds.deleteUI(TOOLNAME)

cmds.window(TOOLNAME, t=TOOLTITLE)
form = cmds.formLayout()
tabs = cmds.tabLayout(imh =5, imw =5)
cmds.formLayout(form, e=True, attachForm=((tabs, 'top',0), (tabs,'left', 0), (tabs, 'right', 0), (tabs, 'bottom',0)))
cmds.rowColumnLayout(w=285)


# Joint Size
cmds.frameLayout(l="Joint Size", cll=True)
jnt = cmds.floatSliderButtonGrp(l="Joint    ", bl="Set", bc="jointSize()", cw4=(50,50,70,40), f=True, min=0.1, max=1, v=0.5)
cmds.setParent("..")
cmds.separator(h=1)


# Create
cmds.frameLayout(l="Create", cll=True)
wi = (1,137,137)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("", w=wi[0])
cmds.button(l="Loc", c="cmds.CreateLocator()", w=wi[1])
cmds.button(l="Curve", c="cmds.EPCurveTool()", w=wi[2])
cmds.setParent("..")

wi = (54,69,75,75)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("    Joints : ", w=wi[0])
cmds.button(l="Jnt", c="cmds.JointTool()", w=wi[1])
cmds.button(l="Orient", c="cmds.OrientJointOptions()", w=wi[2])
cmds.button(l="Mirror", c="cmds.MirrorJointOptions()", w=wi[3])
cmds.setParent("..")

wi = (54,110,110)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("        IK : ", w=wi[0])
cmds.button(l="IK", c="cmds.IKHandleTool()", w=wi[1])
cmds.button(l="IK Spline", c="cmds.ikHandle(sol='ikSplineSolver', ns=4)", w=wi[2])
cmds.setParent("..")

wi = (54,110,110)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("      Skin : ", w=wi[0])
cmds.button(l="Bind", c="cmds.SmoothBindSkinOptions()", w=wi[1])
cmds.button(l="Detach", c="cmds.DetachSkinOptions()", w=wi[2])
cmds.setParent("..")

cmds.rowLayout(nc=3, cw3=wi)
cmds.text(" Weights : ", w=wi[0])
cmds.button(l="Paint", c="cmds.ArtPaintSkinWeightsToolOptions()", w=wi[1])
cmds.button(l="Mirror", c="cmds.MirrorSkinWeightsOptions()", w=wi[2])
cmds.setParent("..")

wi = (54,79,70,70)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("    More : ", w=wi[0])
cmds.button(l="Blend Shape", c="cmds.CreateBlendShapeOptions()", w=wi[1])
cmds.button(l="Lattice", c="cmds.CreateLatticeOptions()", w=wi[2])
cmds.button(l="Cluster", c="cmds.CreateClusterOptions()", w=wi[3])
cmds.setParent("..")
cmds.separator(h=1)

wi = (1,67,68,67,68)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("")
cmds.button(l="FT", c="cmds.FreezeTransformations()", w=wi[1])
cmds.button(l="RT", c="cmds.ResetTransformations()", w=wi[2])
cmds.button(l="CP", c="cmds.CenterPivot()", w=wi[3])
cmds.button(l="MT", c="cmds.MatchTranslation()", w=wi[4])
cmds.setParent("..")

wi = (1,137,137)
cmds.rowLayout(nc=3, cw3=wi)
cmds.text("")
cmds.button(l="Delete History", c="cmds.DeleteHistory()", w=wi[1])
cmds.button(l="Set Driven Key", c="cmds.SetDrivenKeyOptions()", w=wi[2])
cmds.setParent("..")
cmds.setParent("..")
cmds.separator(h=1)


# Controller
cmds.frameLayout(l="Controller", cll=True)
cmds.rowLayout(nc=1)
make = cmds.radioButtonGrp(l=" Make : ", cw3=(60,110,10), la2=["Each","Sum"], nrb=2, sl=1)
cmds.setParent("..")

wi = (60,100)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("      Shape :", w=wi[0])
shapes = cmds.optionMenu(w=wi[1])
cmds.menuItem(l="Circle")
cmds.menuItem(l="Box")
cmds.menuItem(l="Ball")
#ing
cmds.menuItem(l="Cross")
cmds.menuItem(l="Eyes")
cmds.menuItem(l="Handle")
cmds.menuItem(l="Arrow1")
cmds.menuItem(l="Arrow2")
cmds.menuItem(l="Arrow4")

cmds.setParent("..")
cmds.rowLayout(nc=1)
axis=cmds.radioButtonGrp(l="Axis : ", la3=["X","Y","Z"], nrb=3, cw4=(60,70,70,20), sl=1)
cmds.setParent("..")

cmds.rowLayout(nc=1)
const = cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True)
cmds.setParent("..")

cmds.rowLayout(nc=1)
con_check = cmds.radioButtonGrp(l="Check : ", cw3=(60,110,10), la2=["Once","Hierarchy"], nrb=2, sl=1)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Create Controller", c="createController()", w=wi[1])
cmds.setParent("..")
cmds.separator(h=1)

wi = (40,180,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="  Text : ", w=wi[0])
tx = cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Create", w=wi[3], c="text()")
cmds.setParent("..")
cmds.setParent("..")
cmds.separator(h=1)


# Constrain
cmds.frameLayout(l="Constrain", cll=True)
cmds.rowLayout(nc=1)
mo_const = cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True)
cmds.setParent("..")

cmds.rowLayout(nc=1)
mo = cmds.radioButtonGrp(l="Maintain offset : ", cw3=(93,90,50), la2=["On","Off"], nrb=2, sl=1)
cmds.setParent("..")

wi = (2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Constrain", c="Const()", w=wi[1])
cmds.setParent("..")
cmds.setParent("..")
cmds.separator(h=1)


# Rename
cmds.frameLayout(l="Rename", cll=True)
wi=(50,84,84,1,50)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("Hash",l="Nums :", w=wi[0])
hf = cmds.textField(w=wi[1], tx="Front")
hb = cmds.textField(w=wi[2], tx="Back")
cmds.text("")
cmds.button(l="Add", c="hashRenamer()", w=wi[4])
cmds.setParent("..")
cmds.separator(h=1)

cmds.rowLayout(nc=1)
check = cmds.radioButtonGrp(l="Check : ", cw3=(50,120,10), la2=["Once","Hierarchy"], nrb=2, sl=2)
cmds.setParent("..")

wi = (50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("Before", l="(Before)", w=wi[0])
brn = cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Add", c="renamer(1)", w=wi[3])
cmds.setParent("..")

wi = (50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("After", l="(After)", w=wi[0])
arn = cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Add", c="renamer(2)", w=wi[3])
cmds.setParent("..")

wi = (45,45,45,45,45,45)
cmds.rowLayout(nc=6, cw6=wi)
cmds.button(l="grp", w=wi[0], c="add(1)")
cmds.button(l="jnt", w=wi[1], c="add(2)")
cmds.button(l="ctrl", w=wi[2], c="add(3)")
cmds.button(l="loc", w=wi[3], c="add(4)")
cmds.button(l="drv", w=wi[4], c="add(5)")
cmds.button(l="extra", w=wi[5], c="add(6)")
cmds.setParent("..")
cmds.setParent("..")
cmds.separator(h=1)


# Color Picker
cmds.frameLayout(l="Color Picker", cll=True)
wi=(45,45,45,45,45,45)
hi=30
cmds.rowLayout(nc=6, cw6=wi)
cmds.button(l="", w=wi[0], h=hi, c="colorPicker(13)", bgc=(1,0,0))
cmds.button(l="", w=wi[1], h=hi, c="colorPicker(17)",bgc=(1,1,0))
cmds.button(l="", w=wi[2], h=hi, c="colorPicker(6)", bgc=(0,0,1))
cmds.button(l="", w=wi[3], h=hi, c="colorPicker(18)", bgc=(0,1,1))
cmds.button(l="", w=wi[4], h=hi, c="colorPicker(20)", bgc=(1,0.75,0.75))
cmds.button(l="More", w=wi[5], c="color()", h=hi)
cmds.setParent("..")
cmds.setParent("..")

cmds.showWindow(TOOLNAME)

#-------------------------------------- Active Code ------------------------------------#

def jointSize():
    j = cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)

def colorPicker(num):
    a = cmds.ls(sl=True)
    for col in a:
        b=cmds.listRelatives(col, c=True)
        #cmds.setAttr(b[0]+".overrideEnabled", 1)
        #cmds.setAttr(b[0]+".overrideColor", num)
        cmds.setAttr(col+".overrideEnabled", 1)
        cmds.setAttr(col+".overrideColor", num)

# ing
def Const():
    a = cmds.ls(sl=True)
    for x in range(0, len(a)):
        if x == 0:
            constrains(a[0], a[1], 1)
        if x == 1:
            pass
        if x % 2 == 0:
            constrains(a[x], a[x+1], 1)
        if x % 2 == 1:
            pass

#--------------------------------------------------------------------------------------------#

def createController():
    objs = cmds.ls(sl=True)
    if cmds.radioButtonGrp(make, q=True, sl=1) == 1:
        for x in range(0,len(objs)):
            obj = objs[x]
            selectShape(obj)
    else:
        selectShape(objs)

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
    #ing
    grp = cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.parentConstraint(obj, grp, mo=False, n="ex")
    cmds.delete("ex")
    if cmds.radioButtonGrp(make, q=True, sl=1)==1:
        constrains(c, obj, 0)
    else:
        pass

def constrains(con, obj, i):
    if i == 0:
        a = const
    else:
        a = mo_const
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

# need to fix
def text():
    t = cmds.textField(tx, q=True, tx=True)
    cmds.textCurves(t=t)
    if t.isalpha():
        b = cmds.listRelatives(cmds.ls("Text_"+t+"_1"), c=True)
    else:
        tmp_t = "x"*len(t)
        b = cmds.listRelatives(cmds.ls("Text_"+tmp_t+"_1"), c=True)
    ci = cmds.listRelatives(b, c=True)
    c = cmds.ls(ci)
    for x in range(0, len(c)):
        s = c[x]
        cmds.select(s)
        a = cmds.rename(s, t+str(x+1))
    
    cmds.parent(t+"*", "Text_"+t+"_1")
    cmds.makeIdentity(t+"*", a=True, t=True)
    cmds.DeleteHistory(t+"*")
    cmds.parent(t+"*", "Text_"+t+"_1", r=True, s=True)
    cmds.delete("Char*")
    cmds.select(cl=True)
    sel = cmds.ls(t+"*", typ="transform")
    cmds.delete(sel)
    cmds.rename("Text_"+t+"_1", t+"_ctrl")

#--------------------------------------------------------------------------------------------#

def hashRenamer():
    hf_text = cmds.textField(hf, q=True, tx=True)
    hb_text = cmds.textField(hb, q=True, tx=True)
    
    objs = cmds.ls(sl=True)
    for x in range(0, len(objs)):
        obj = objs[x]
        if x<9:
            Name = hf_text+"_0"+str(x+1)+"_"+hb_text
        else:
            Name = hf_text+"_"+str(x+1)+"_"+hb_text
        cmds.rename(obj,Name)

def renamer(i):
    if cmds.radioButtonGrp(check, q=True, sl=1) == 2:
        ob = cmds.listRelatives(cmds.ls(sl=True), ad=True)
        objs = cmds.ls(ob)
        objs.append(cmds.ls(sl=True)[0])
        namer(i, objs)
    else:
        objs=cmds.ls(sl=True)
        namer(i, objs)

def namer(i, objs):
    brn_text = cmds.textField(brn, q=True, tx=True)
    arn_text = cmds.textField(arn, q=True, tx=True)
    
    for x in range(0, len(objs)):
        obj = objs[x]
        if i == 1:
            blen = len(brn_text)
            bcheck=""
            for x in range(0, blen+1):
                bcheck = bcheck+obj[x]
            if bcheck == brn_text+"_":
                pass
            else:
                Name = brn_text+"_"+obj
                cmds.rename(obj, Name)
        else:
            alen = len(arn_text)
            acheck=""
            for x in range(0, alen+1):
                w = len(obj)-len(arn_text)+x-1
                acheck = acheck+obj[w]
            if acheck == "_"+arn_text:
                pass
            else:
                Name = obj+"_"+arn_text
                cmds.rename(obj, Name)

def add(tail):
    tails = [
        "_grp", "_jnt", "_ctrl",
        "_loc", "_drv", "_extra"
    ]
    objs = cmds.ls(sl=True)
    for x in range(0, len(objs)):
        obj = objs[x]
        Name = obj+tails[tail-1]
        cmds.rename(obj, Name)

#--------------------------------------------------------------------------------------------#

def color():
    win = "ColorPicker"
    if cmds.window(win, ex=True):
        cmds.deleteUI(win)
    
    cmds.window(win, t="Color Picker")
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


