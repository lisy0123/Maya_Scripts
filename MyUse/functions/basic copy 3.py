import maya.cmds as cmds

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

# ing check
def newGroup():
    objs = pm.ls(sl=True)
    tmps = pm.duplicate(rr=True)
    lst = []
    for x in range(len(tmps)):
        tmps[x].rename(objs[x])
        tmp = pm.ls(tmps[x])
        grp = pm.group(em=True)
        grp.rename(objs[x]+"_grp")
        pm.parentConstraint(tmp, grp, mo=False, n="ex")
        pm.delete("ex")
        pm.parent(tmp, grp)
        lst.append(grp)
        if x == 0:
            tmps[x].rename(objs[x])
            grp.rename(objs[x]+"_grp")
            lst = []
            lst.append(grp)
    tmps = tmps[:-1]
    lst = lst[1:]
    for x in range(len(lst)):
        pm.parent(lst[x], tmps[x])

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
        hf_text = "R_"+hf_text
    elif cmds.radioButtonGrp(pos_check, q=True, sl=1) == 2:
        hf_text = "L_"+hf_text
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
        "extra", "loc", "rig",
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


def changeAttrName():
    attr_text = cmds.textField(attr_tx, q=True, tx=True)
    objs = pm.ls(sl=True)
    for obj in objs:
        sl_attr = pm.channelBox("mainChannelBox", q=True, sma=True)
        cmds.addAttr(obj+'.'+sl_attr[0], e=True, nn=attr_text)
    

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
        subConst(objs, num)
        return True
    else:
        num = 2
        if cmds.checkBoxGrp(mo_quick_check, q=True, v1=True):
            if len(objs) % 2 != 0:
                cmds.warning("Select even numbers of objs! Objs nums: "+str(len(objs)))
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
    if cmds.checkBoxGrp(mo_check, q=True, v1=True) or a == spread_const_check:
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
    # diamond
    elif cmds.optionMenu(shapes, q=True, sl=4) == 4:
        c = cmds.curve(d=1, p=[(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(0,1,0),(-1,0,0),(1,0,0),(0,-1,0),(-1,0,0),(0,0,-1),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(0,0,1),(-1,0,0)])
    # cross 1
    elif cmds.optionMenu(shapes, q=True, sl=5) == 5:
        c = cmds.curve(d=1, p=[(0,0,-2),(0,0,2),(0,0,0),(-2,0,0),(2,0,0)])
    # cross 2
    elif cmds.optionMenu(shapes, q=True, sl=6) == 6:
        c = cmds.curve(d=1, p=[(-1,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,1),(1,0,1),(1,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,-1),(-1,0,-1),(-1,0,-3)])
    # eye
    elif cmds.optionMenu(shapes, q=True, sl=7) == 7:
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
    elif cmds.optionMenu(shapes, q=True, sl=8) == 8:
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
    elif cmds.optionMenu(shapes, q=True, sl=9) == 9:
        c = cmds.curve(d=1, p=[(-2,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),(1,0,1),(-2,0,1),(-2,0,-1)])
    # arrow 2
    elif cmds.optionMenu(shapes, q=True, sl=10) == 10:
        c = cmds.curve(d=1, p=[(-1,0,-1),(1,0,-1),(1,0,-2),(3,0,0),(1,0,2),(1,0,1),(-1,0,1),(-1,0,2),(-3,0,0),(-1,0,-2),(-1,0,-1)])
    # arrow 4
    elif cmds.optionMenu(shapes, q=True, sl=11) == 11:
        c = cmds.curve(d=1, p=[(-1,0,-1),(-1,0,-3),(-2,0,-3),(0,0,-5),(2,0,-3),(1,0,-3),(1,0,-1),(3,0,-1),(3,0,-2),(5,0,0),(3,0,2),(3,0,1),(1,0,1),(1,0,3),(2,0,3),(0,0,5),(-2,0,3),(-1,0,3),(-1,0,1),(-3,0,1),(-3,0,2),(-5,0,0),(-3,0,-2),(-3,0,-1),(-1,0,-1)])
    grp = cmds.group(em=True)
    cmds.parent(c,grp)
    cmds.ResetTransformations(c)

    if cmds.optionMenu(shapes, q=True, sl=4) == 4 or cmds.optionMenu(shapes, q=True, sl=5) == 5 or cmds.optionMenu(shapes, q=True, sl=11) == 11:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", 90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
        pm.makeIdentity(c, a=True, t=1, r=1, s=1, n=0, pn=1)
    elif cmds.optionMenu(shapes, q=True, sl=8) == 8:
        if cmds.radioButtonGrp(axes, q=True, sl=1) == 1:
            cmds.setAttr(c+".rotateZ", -90)
        elif cmds.radioButtonGrp(axes, q=True, sl=2) == 3:
            cmds.setAttr(c+".rotateX", 90)
    elif cmds.optionMenu(shapes, q=True, sl=9) == 9 or cmds.optionMenu(shapes, q=True, sl=10) == 10:
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


# ing
#setup_name = cmds.textField(w=wi[1], h=25)
#setup_check = cmds.checkBoxGrp(l="   Options :  ", ncb=3, cw4=(125,40,40,10), la3=["FK","IK","Ribbon"], v1=True, v2=True, h=25)
#ribbon_num = cmds.intField(w=wi[1], v=9, h=25)

def fkIkRibbon():
    cmds.warning("WIP!")

# ing
#mp_name = cmds.textField(w=wi[1], h=25)
#mp_loc_num = cmds.intField(w=wi[1], v=5, h=25)

def motionPath():
    cmds.warning("WIP!")
    
    
# ing
def rivet():
    cmds.warning("WIP!")
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