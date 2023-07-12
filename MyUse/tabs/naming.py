import maya.cmds as cmds
import pymel.core as pm
from imp import reload
import tabs.util
import functions.outline as funcs_outline
import functions.rename as funcs_rename

reload(tabs.util)
funcs_outline = reload(funcs_outline)
funcs_rename = reload(funcs_rename)

from tabs.util import Utils


WI01 = (2,273)
WI02 = (1,136,136)


class TabNaming():
    def __init__(self):
        self.frame_outline()
        self.frame_rename()
        self.frame_replace()
        self.frame_add()


    # Outline
    def frame_outline(self):
        Utils().frame("Outline")
        Utils().btn_layout(1)
        Utils().create_btn("Set in order", funcs_outline.set_in_order, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Grouping", funcs_outline.grouping, WI01[1])
        Utils().end_space()


    # Rename
    def frame_rename(self):
        Utils().frame("Rename")

        cmds.rowLayout(nc=1)
        self.header = cmds.radioButtonGrp(l="Position : ", cw4=(60,65,65,10), la3=["R","L","None"], nrb=3, sl=3, h=25)
        cmds.setParent("..")

        Utils().btn_layout(2)
        self.hf = cmds.textField(w=WI02[1], tx="Front", h=25)
        self.hb = cmds.textField(w=WI02[2], tx="Back", h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Rename", self.func_rename, WI01[1])
        Utils().end_space()


    # Replace
    def frame_replace(self):
        Utils().frame("Replace")

        cmds.rowLayout(nc=1)
        self.check_replace = cmds.radioButtonGrp(l="Check : ", cw3=(80,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        wi=(80,195)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="    Search for :", w=wi[0])
        self.search = cmds.textField(w=wi[1], tx="", h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="Replace with :", w=wi[0])
        self.replace = cmds.textField(w=wi[1], tx="", h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Replace", self.func_replace, WI01[1])
        Utils().end_space()


    # Add
    def frame_add(self):
        Utils().frame("Add")

        wi = (50,200)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text("  Repeat : ", w=wi[0])
        self.repeat = cmds.checkBox(l="Keep adding words", h=25, w=wi[1])
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.check_hi = cmds.radioButtonGrp(l="Check : ", cw3=(50,90,10), la2=["Once", "Hierarchy"], nrb=2, sl=1, h=25)
        cmds.setParent("..")

        wi = (50,170,1,50)
        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("Before", l="  Before : ", w=wi[0])
        self.add_before = cmds.textField(w=wi[1], h=25)
        cmds.text("")
        Utils().create_btn("Add", self.func_add_before, wi[3], 25)
        cmds.setParent("..")

        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("After", l="    After : ", w=wi[0])
        self.add_after = cmds.textField(w=wi[1], h=25)
        cmds.text("")
        Utils().create_btn("Add", self.func_add_after, wi[3], 25)
        cmds.setParent("..")

        wi = (1,90,90,90)
        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("")
        Utils().create_btn("grp", lambda x: self.func_add("grp"), wi[1], 25)
        Utils().create_btn("jnt", lambda x: self.func_add("jnt"), wi[2], 25)
        Utils().create_btn("ctrl", lambda x: self.func_add("ctrl"), wi[3], 25)   
        cmds.setParent("..")

        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("")
        Utils().create_btn("extra", lambda x: self.func_add("extra"), wi[1], 25)
        Utils().create_btn("loc", lambda x: self.func_add("loc"), wi[2], 25)
        Utils().create_btn("rig", lambda x: self.func_add("rig"), wi[3], 25)
        Utils().end_space()


    def func_rename(self, _):
        hf = cmds.textField(self.hf, q=True, tx=True)
        hb = cmds.textField(self.hb, q=True, tx=True)
        funcs_rename.hash_renamer(hf, hb, self.header)

    def func_replace(self, _):
        search = cmds.textField(self.search, q=True, tx=True)
        replace = cmds.textField(self.replace, q=True, tx=True)
        funcs_rename.replace(search, replace, self.check_replace)

    def func_add_before(self, _):
        before = cmds.textField(self.add_before, q=True, tx=True)
        after = cmds.textField(self.add_after, q=True, tx=True)
        funcs_rename.add(1, before, after, self.check_hi, self.repeat)

    def func_add_after(self, _):
        before = cmds.textField(self.add_before, q=True, tx=True)
        after = cmds.textField(self.add_after, q=True, tx=True)
        funcs_rename.add(2, before, after, self.check_hi, self.repeat)
    
    def func_add(self, tail):
        funcs_rename.add(0, None, tail, self.check_hi, self.repeat) 