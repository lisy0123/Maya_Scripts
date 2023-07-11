import maya.cmds as cmds
import pymel.core as pm
from imp import reload
import tabs.util
import functions.outline
import functions.rename

reload(tabs.util)
reload(functions.outline)
reload(functions.rename)

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
        Utils().create_btn("Set in order", functions.outline.set_in_order, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Grouping", functions.outline.grouping, WI01[1])
        Utils().end_space()


    # Rename
    def frame_rename(self):
        Utils().frame("Rename")

        cmds.rowLayout(nc=1)
        self.pos_check = cmds.radioButtonGrp(l="Position : ", cw4=(60,65,65,10), la3=["R","L","None"], nrb=3, sl=3, h=25)
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
        self.replace_check = cmds.radioButtonGrp(l="Check : ", cw3=(80,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
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

        cmds.rowLayout(nc=1)
        self.add_check = cmds.radioButtonGrp(l="Check : ", cw3=(50,80,10), la2=["Once","Hierarchy"], nrb=2, sl=1, h=25)
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
        cmds.separator(h=1)

        wi = (1,90,90,90)
        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("")
        Utils().create_btn("grp", self.func_add_grp, wi[1], 25)
        Utils().create_btn("jnt", "add(2)", wi[2], 25)
        Utils().create_btn("ctrl", "add(3)", wi[3], 25)
        cmds.setParent("..")

        cmds.rowLayout(nc=4, cw4=wi)
        cmds.text("")
        Utils().create_btn("extra", "add(4)", wi[1], 25)
        Utils().create_btn("loc", "add(5)", wi[2], 25)
        Utils().create_btn("rig", "add(6)", wi[3], 25)
        Utils().end_space()


    def func_rename(self, _):
        hf = cmds.textField(self.hf, q=True, tx=True)
        hb = cmds.textField(self.hb, q=True, tx=True)
        functions.rename.hash_renamer(hf, hb, self.pos_check)

    
    def func_replace(self, _):
        search = cmds.textField(self.search, q=True, tx=True)
        replace = cmds.textField(self.replace, q=True, tx=True)
        functions.rename.replace(search, replace, self.replace_check)


    def func_add_before(self, _):
        before = cmds.textField(self.add_before, q=True, tx=True)
        after = cmds.textField(self.add_after, q=True, tx=True)
        functions.rename.add(1, before, after, self.add_check)


    def func_add_after(self, _):
        before = cmds.textField(self.add_before, q=True, tx=True)
        after = cmds.textField(self.add_after, q=True, tx=True)
        functions.rename.add(2, before, after, self.add_check)

    
    def func_add_grp(self, _):
        functions.rename.add_tail("grp")

    # def func_add_grp(self, _):
    #     functions.rename.add_tail("jnt")

    # def func_add_grp(self, _):
    #     functions.rename.add_tail("ctrl")

    # def func_add_grp(self, _):
    #     functions.rename.add_tail("extra")

    # def func_add_grp(self, _):
    #     functions.rename.add_tail("loc")
    
    # def func_add_grp(self, _):
    #     functions.rename.add_tail("rig")