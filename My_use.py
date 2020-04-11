import maya.cmds as cmds

win="MyUse"
if cmds.window(win, ex=True):
    cmds.deleteUI(win)

cmds.window(win, t="My Use")
cmds.rowColumnLayout(w=285)

cmds.frameLayout(l="Joint Size", cll=True)
jnt=cmds.floatSliderButtonGrp(l="Joint    ", bl="Set", bc="JointSize()", cw4=(50,50,70,40), f=True, min=0.1, max=1, v=0.5)
cmds.setParent("..")

cmds.frameLayout(l="Color Picker", cll=True)
wi=(45,45,45,45,45,45)
hi=30
cmds.rowLayout(nc=6, cw6=wi)
cmds.button(l="", w=wi[0], h=hi, c="ColorPicker(13)", bgc=(1,0,0))
cmds.button(l="", w=wi[1], h=hi, c="ColorPicker(17)",bgc=(1,1,0))
cmds.button(l="", w=wi[2], h=hi, c="ColorPicker(6)", bgc=(0,0,1))
cmds.button(l="", w=wi[3], h=hi, c="ColorPicker(18)", bgc=(0,1,1))
cmds.button(l="", w=wi[4], h=hi, c="ColorPicker(20)", bgc=(1,0.75,0.75))
cmds.button(l="More", w=wi[5], c="Color()", h=hi)
cmds.setParent("..")
cmds.setParent("..")

cmds.frameLayout(l="Constrain", cll=True)
cmds.rowLayout(nc=1)
cons=cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True)
cmds.setParent("..")
wi=(2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Constrain", c="Cons()", w=wi[1])
cmds.setParent("..")
cmds.setParent("..")

#--------------------------------------------------------------------------------------------#

cmds.frameLayout(l="Controller", cll=True)
cmds.rowLayout(nc=1)
make=cmds.radioButtonGrp(l=" Make : ", cw3=(60,110,10), la2=["Each","Sum"], nrb=2, sl=1)
cmds.setParent("..")

wi=(60,100)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("      Shape :", w=wi[0])
shapes=cmds.optionMenu(w=wi[1])
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
const=cmds.checkBoxGrp(l="Constrain: ", ncb=4, cw5=(60,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v1=True)
cmds.setParent("..")

wi=(2,273)
cmds.rowLayout(nc=2, cw2=wi)
cmds.text("")
cmds.button(l="Create Controller", c="CreateController()", w=wi[1])
cmds.setParent("..")
cmds.separator(h=1)

#--------------------------------------------------------------------------------------------#

wi=(50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text(l="   Text :", w=wi[0])
tx=cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Create", w=wi[3], c="Text()")
cmds.setParent("..")
cmds.setParent("..")

cmds.frameLayout(l="Renamer", cll=True)
wi=(50,84,84,1,50)
cmds.rowLayout(nc=5, cw5=wi)
cmds.text("Hash",l="Nums", w=wi[0])
hf=cmds.textField(w=wi[1], tx="Front")
hb=cmds.textField(w=wi[2], tx="Back")
cmds.text("")
cmds.button(l="Add", c="Hash_Renamer()", w=wi[4])
cmds.setParent("..")
cmds.separator(h=1)

#ing
cmds.rowLayout(nc=1)
ch=cmds.checkBoxGrp(ncb=2, l="Check :  ", cw3=(50,100,50), la2=[" Hierarchy"," Once"])
cmds.setParent("..")

wi=(50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("Before",l="(Before)", w=wi[0])
brn=cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Add", c="Renamer(1)", w=wi[3])
cmds.setParent("..")

wi=(50,170,1,50)
cmds.rowLayout(nc=4, cw4=wi)
cmds.text("After",l="(After)", w=wi[0])
arn=cmds.textField(w=wi[1])
cmds.text("")
cmds.button(l="Add", c="Renamer(2)", w=wi[3])
cmds.setParent("..")
cmds.separator(h=1)

wi=(45,45,45,45,45,45)
cmds.rowLayout(nc=6, cw6=wi)
cmds.button(l="grp", w=wi[0], c="Add(1)")
cmds.button(l="jnt", w=wi[1], c="Add(2)")
cmds.button(l="ctrl", w=wi[2], c="Add(3)")
cmds.button(l="loc", w=wi[3], c="Add(4)")
cmds.button(l="drv", w=wi[4], c="Add(5)")
cmds.button(l="extra", w=wi[5], c="Add(6)")
cmds.setParent("..")
cmds.setParent("..")


cmds.showWindow(win)

#-------------------------------------- Active Code ------------------------------------#

def JointSize():
    j=cmds.floatSliderGrp(jnt, q=True, v=True)
    cmds.jointDisplayScale(j)

def ColorPicker(num):
    a=cmds.ls(sl=True)
    for col in a:
        b=cmds.listRelatives(col, c=True)
        #cmds.setAttr(b[0]+".overrideEnabled",1)
        #cmds.setAttr(b[0]+".overrideColor",num)
        cmds.setAttr(col+".overrideEnabled",1)
        cmds.setAttr(col+".overrideColor",num)

def Cons():
    a=cmds.ls(sl=True)
    for x in range(0, len(a)):
        if x==0:
            Constrains(a[0], a[1], 1)
        if x==1:
            pass
        if x%2==0:
            Constrains(a[x], a[x+1], 1)
        if x%2==1:
            pass

#--------------------------------------------------------------------------------------------#

def CreateController():
    objs=cmds.ls(sl=True)
    if cmds.radioButtonGrp(make, q=True, sl=1)==1:
        for x in range(0,len(objs)):
            obj=objs[x]
            SelectShape(obj)
    else:
        SelectShape(objs)

def SelectShape(obj):
    if cmds.optionMenu(shapes, q=True, sl=1)==1:
        if cmds.radioButtonGrp(axis, q=True, sl=1)==1:
            c=cmds.circle(nr=(1,0,0))
        elif cmds.radioButtonGrp(axis, q=True, sl=2)==2:
            c=cmds.circle(nr=(0,1,0))
        else:
            c=cmds.circle(nr=(0,0,1))
    elif cmds.optionMenu(shapes, q=True, sl=2)==2:
        c=cmds.curve(d=1, p=[(1,1,1),(1,-1,1), (1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1)])
    #need to fix
    elif cmds.optionMenu(shapes, q=True, sl=3)==3:
        a=cmds.circle(nr=(1,0,0), n="cir")
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
    grp=cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.parentConstraint(obj, grp, mo=False, n="ex")
    cmds.delete("ex")
    if cmds.radioButtonGrp(make, q=True, sl=1)==1:
        Constrains(c, obj, 0)
    else:
        pass

def Constrains(con, obj, i):
    if i==0:
        a=const
    else:
        a=cons
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

def Text():
    t=cmds.textField(tx, q=True, tx=True)
    cmds.textCurves(t=t)
    b=cmds.listRelatives(cmds.ls("Text_"+t+"_1"), c=True)
    ci=cmds.listRelatives(b, c=True)
    c=cmds.ls(ci)
    for x in range(0, len(c)):
        s=c[x]
        cmds.select(s)
        a=cmds.rename(s, t+str(x+1))
    
    cmds.parent(t+"*", "Text_"+t+"_1")
    cmds.makeIdentity(t+"*", a=True, t=True)
    cmds.DeleteHistory(t+"*")
    cmds.parent(t+"*", "Text_"+t+"_1", r=True, s=True)
    cmds.delete("Char*")
    cmds.select(cl=True)
    sel=cmds.ls(t+"*", typ="transform")
    cmds.delete(sel)
    cmds.rename("Text_"+t+"_1", t+"_ctrl")

#--------------------------------------------------------------------------------------------#

def Hash_Renamer():
    objs=cmds.ls(sl=True)
    for x in range(0,len(objs)):
        obj=objs[x]
        if x<9:
            Name=cmds.textField(hf, q=True, tx=True)+"_0"+str(x+1)+"_"+cmds.textField(hb, q=True, tx=True)
        else:
            Name=cmds.textField(hf, q=True, tx=True)+"_"+str(x+1)+"_"+cmds.textField(hb, q=True, tx=True)
        cmds.rename(obj,Name)

def Renamer(i):
    if cmds.checkBoxGrp(ch, q=True, v1=True):
        ob=cmds.listRelatives(cmds.ls(sl=True), ad=True)
        objs=cmds.ls(ob)
        objs.append(cmds.ls(sl=True)[0])
        #ing
        for x in range(0, len(objs)):
            if objs[x]=="*Shape":
                print "a"
        print objs
        Namer(i, objs)
    else:
        objs=cmds.ls(sl=True)
        Namer(i, objs)

def Namer(i, objs):
    for x in range(0,len(objs)):
        obj=objs[x]
        if cmds.checkBoxGrp(ch, q=True, v2=True):
            if i==1:
                blen=len(cmds.textField(brn, q=True, tx=True))
                bcheck=""
                for x in range(0,blen):
                    bcheck=bcheck+obj[x]
                print bcheck
                if bcheck==cmds.textField(brn, q=True, tx=True):
                    pass
                else:
                    Name=cmds.textField(brn, q=True, tx=True)+"_"+obj
                    cmds.rename(obj,Name)
            else:
                alen=len(cmds.textField(arn, q=True, tx=True))
                acheck=""
                for x in range(0,alen):
                    w=len(obj)-len(cmds.textField(arn, q=True, tx=True))+x
                    acheck=acheck+obj[w]
                print acheck
                if acheck==cmds.textField(arn, q=True, tx=True):
                    pass
                else:
                    Name=obj+"_"+cmds.textField(arn, q=True, tx=True)
                    cmds.rename(obj,Name)
        else:
            if i==1:
                Name=cmds.textField(brn, q=True, tx=True)+"_"+obj
            else:
                Name=obj+"_"+cmds.textField(arn, q=True, tx=True)
            cmds.rename(obj,Name)

def Add(i):
    objs=cmds.ls(sl=True)
    for x in range(0, len(objs)):
        obj=objs[x]
        if i==1:
            Name=obj+"_grp"
        elif i==2:
            Name=obj+"_jnt"
        elif i==3:
             Name=obj+"_ctrl"
        elif i==4:
             Name=obj+"_loc"
        elif i==5:
             Name=obj+"_drv"
        else:
             Name=obj+"_extra"
        cmds.rename(obj,Name)

#--------------------------------------------------------------------------------------------#

def Color():
    win="ColorPicker"
    if cmds.window(win, ex=True):
        cmds.deleteUI(win)
    
    cmds.window(win, t="Color Picker")
    cmds.rowColumnLayout(w=255)
    wi=(125,125)
    cmds.rowLayout(nc=2, cw2=wi)
    cmds.button(l="", w=wi[0], h=60, c="ColorPicker(13)", bgc=(1,0,0))
    cmds.button(l="", w=wi[1], h=60, c="ColorPicker(17)",bgc=(1,1,0))
    cmds.setParent("..")
    
    wi=(125,125)
    cmds.rowLayout(nc=2, cw2=wi)
    cmds.button(l="", w=wi[0], h=60, c="ColorPicker(6)", bgc=(0,0,1))
    cmds.button(l="", w=wi[1], h=60, c="ColorPicker(18)", bgc=(0,1,1))
    cmds.setParent("..")
    
    wi2=(41,40,40,41,40,40)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="ColorPicker(20)", bgc=(1,0.75,0.75))
    cmds.button(l="", w=wi2[1], h=40, c="ColorPicker(21)", bgc=(1,0.7,0.5))
    cmds.button(l="", w=wi2[2], h=40, c="ColorPicker(9)", bgc=(0.9,0,0.9))
    cmds.button(l="", w=wi2[3], h=40, c="ColorPicker(31)", bgc=(0.6,0.2,0.4))
    cmds.button(l="", w=wi2[4], h=40, c="ColorPicker(12)", bgc=(0.7,0.2,0))
    cmds.button(l="", w=wi2[5], h=40, c="ColorPicker(4)", bgc=(0.7,0,0.2))
    cmds.setParent("..")
    
    wi2=(41,40,40,41,40,40)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="ColorPicker(16)", bgc=(1,1,1))
    cmds.button(l="", w=wi2[1], h=40, c="ColorPicker(30)", bgc=(0.4,0.2,0.6))
    cmds.button(l="", w=wi2[2], h=40, c="ColorPicker(22)", bgc=(1,1,0.4))
    cmds.button(l="", w=wi2[3], h=40, c="ColorPicker(19)", bgc=(0.2,1,0.6))
    cmds.button(l="", w=wi2[4], h=40, c="ColorPicker(14)", bgc=(0,1,0))
    cmds.button(l="", w=wi2[5], h=40, c="ColorPicker(27)", bgc=(0.3,0.6,0.3))
    cmds.setParent("..")
    
    wi2=(41,40,40,41,40,40)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="ColorPicker(25)", bgc=(0.6,0.6,0.2))
    cmds.button(l="", w=wi2[1], h=40, c="ColorPicker(26)", bgc=(0.4,0.6,0.2))
    cmds.button(l="", w=wi2[2], h=40, c="ColorPicker(23)", bgc=(0,0.6,0.3))
    cmds.button(l="", w=wi2[3], h=40, c="ColorPicker(29)", bgc=(0.2,0.4,0.75))
    cmds.button(l="", w=wi2[4], h=40, c="ColorPicker(15)", bgc=(0,0.3,0.7))
    cmds.button(l="", w=wi2[5], h=40, c="ColorPicker(5)", bgc=(0,0.1,0.5))
    cmds.setParent("..")
    
    wi2=(41,40,40,41,40,40)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="ColorPicker(28)", bgc=(0.2,0.6,0.6))
    cmds.button(l="", w=wi2[1], h=40, c="ColorPicker(7)", bgc=(0,0.3,0.1))
    cmds.button(l="", w=wi2[2], h=40, c="ColorPicker(8)", bgc=(0,0.1,0.2))
    cmds.button(l="", w=wi2[3], h=40, c="ColorPicker(24)", bgc=(0.6,0.4,0.2))
    cmds.button(l="", w=wi2[4], h=40, c="ColorPicker(10)", bgc=(0.5,0.3,0.2))
    cmds.button(l="", w=wi2[5], h=40, c="ColorPicker(11)", bgc=(0.2,0.1,0.1))
    cmds.setParent("..")
    
    wi2=(41,40,40,41,40,40)
    cmds.rowLayout(nc=6, cw6=wi2)
    cmds.button(l="", w=wi2[0], h=40, c="ColorPicker(3)", bgc=(0.7,0.7,0.7))
    cmds.button(l="", w=wi2[1], h=40, c="ColorPicker(2)", bgc=(0.3,0.3,0.3))
    cmds.button(l="", w=wi2[2], h=40, c="ColorPicker(1)", bgc=(0,0,0))
 
    cmds.showWindow(win)

#--------------------------------------------------------------------------------------------#

