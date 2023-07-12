import maya.cmds as cmds


def color_picker(num):
    objs = cmds.ls(sl=True)
    for obj in objs:
        # tmp = cmds.listRelatives(obj, c=True)
        # cmds.setAttr(tmp[0]+".overrideEnabled", 1)
        # cmds.setAttr(tmp[0]+".overrideColor", num)
        cmds.setAttr(obj+".overrideEnabled", 1)
        cmds.setAttr(obj+".overrideColor", num)


class Color():
    def __init__(self, _):
        self.toolname = "ColorPicker"
        self.tooltitle = "Color Picker"
        self.built_ui()


    def built_ui(self):
        if cmds.window(self.toolname, ex=True):
            cmds.deleteUI(self.toolname)
        cmds.window(self.toolname, t=self.tooltitle)
        cmds.rowColumnLayout(w=255)
        
        wi=(125,125)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.button(l="", w=wi[0], h=60, c=lambda x: color_picker(13), bgc=(1,0,0))
        cmds.button(l="", w=wi[1], h=60, c=lambda x: color_picker(17),bgc=(1,1,0))
        cmds.setParent("..")
        
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.button(l="", w=wi[0], h=60, c=lambda x: color_picker(6), bgc=(0,0,1))
        cmds.button(l="", w=wi[1], h=60, c=lambda x: color_picker(18), bgc=(0,1,1))
        cmds.setParent("..")
        
        wi2=(41,41,41,41,41,41)
        cmds.rowLayout(nc=6, cw6=wi2)
        cmds.button(l="", w=wi2[0], h=40, c=lambda x: color_picker(20), bgc=(1,0.75,0.75))
        cmds.button(l="", w=wi2[1], h=40, c=lambda x: color_picker(21), bgc=(1,0.7,0.5))
        cmds.button(l="", w=wi2[2], h=40, c=lambda x: color_picker(9), bgc=(0.9,0,0.9))
        cmds.button(l="", w=wi2[3], h=40, c=lambda x: color_picker(31), bgc=(0.6,0.2,0.4))
        cmds.button(l="", w=wi2[4], h=40, c=lambda x: color_picker(12), bgc=(0.7,0.2,0))
        cmds.button(l="", w=wi2[5], h=40, c=lambda x: color_picker(4), bgc=(0.7,0,0.2))
        cmds.setParent("..")
        
        cmds.rowLayout(nc=6, cw6=wi2)
        cmds.button(l="", w=wi2[0], h=40, c=lambda x: color_picker(16), bgc=(1,1,1))
        cmds.button(l="", w=wi2[1], h=40, c=lambda x: color_picker(30), bgc=(0.4,0.2,0.6))
        cmds.button(l="", w=wi2[2], h=40, c=lambda x: color_picker(22), bgc=(1,1,0.4))
        cmds.button(l="", w=wi2[3], h=40, c=lambda x: color_picker(19), bgc=(0.2,1,0.6))
        cmds.button(l="", w=wi2[4], h=40, c=lambda x: color_picker(14), bgc=(0,1,0))
        cmds.button(l="", w=wi2[5], h=40, c=lambda x: color_picker(27), bgc=(0.3,0.6,0.3))
        cmds.setParent("..")
        
        cmds.rowLayout(nc=6, cw6=wi2)
        cmds.button(l="", w=wi2[0], h=40, c=lambda x: color_picker(25), bgc=(0.6,0.6,0.2))
        cmds.button(l="", w=wi2[1], h=40, c=lambda x: color_picker(26), bgc=(0.4,0.6,0.2))
        cmds.button(l="", w=wi2[2], h=40, c=lambda x: color_picker(23), bgc=(0,0.6,0.3))
        cmds.button(l="", w=wi2[3], h=40, c=lambda x: color_picker(29), bgc=(0.2,0.4,0.75))
        cmds.button(l="", w=wi2[4], h=40, c=lambda x: color_picker(15), bgc=(0,0.3,0.7))
        cmds.button(l="", w=wi2[5], h=40, c=lambda x: color_picker(5), bgc=(0,0.1,0.5))
        cmds.setParent("..")
        
        cmds.rowLayout(nc=6, cw6=wi2)
        cmds.button(l="", w=wi2[0], h=40, c=lambda x: color_picker(28), bgc=(0.2,0.6,0.6))
        cmds.button(l="", w=wi2[1], h=40, c=lambda x: color_picker(7), bgc=(0,0.3,0.1))
        cmds.button(l="", w=wi2[2], h=40, c=lambda x: color_picker(8), bgc=(0,0.1,0.2))
        cmds.button(l="", w=wi2[3], h=40, c=lambda x: color_picker(24), bgc=(0.6,0.4,0.2))
        cmds.button(l="", w=wi2[4], h=40, c=lambda x: color_picker(10), bgc=(0.5,0.3,0.2))
        cmds.button(l="", w=wi2[5], h=40, c=lambda x: color_picker(11), bgc=(0.2,0.1,0.1))
        cmds.setParent("..")
        
        cmds.rowLayout(nc=6, cw6=wi2)
        cmds.button(l="", w=wi2[0], h=40, c=lambda x: color_picker(3), bgc=(0.7,0.7,0.7))
        cmds.button(l="", w=wi2[1], h=40, c=lambda x: color_picker(2), bgc=(0.3,0.3,0.3))
        cmds.button(l="", w=wi2[2], h=40, c=lambda x: color_picker(1), bgc=(0,0,0))
    
        cmds.showWindow(self.toolname)