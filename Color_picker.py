import maya.cmds as cmds

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

#-------------------------------------- Active Code ------------------------------------#

def ColorPicker(num):
    a=cmds.ls(sl=True)
    for col in a:
        #b=cmds.listRelatives(col, c=True)
        #cmds.setAttr(b[0]+".overrideEnabled",1)
        #cmds.setAttr(b[0]+".overrideColor",num)
        cmds.setAttr(col+".overrideEnabled",1)
        cmds.setAttr(col+".overrideColor",num)

