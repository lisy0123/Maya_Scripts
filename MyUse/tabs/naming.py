import maya.cmds as cmds
from imp import reload
import tabs.util

reload(tabs.util)

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
        cmds.button(l="Set in order", c="setInOrder()", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Copy and New Group", c="newGroup()", w=WI01[1], h=30)
        Utils().end_space()


    # Rename
    def frame_rename(self):
        Utils().frame("Rename")

        cmds.rowLayout(nc=1)
        pos_check = cmds.radioButtonGrp(l="Position : ", cw4=(60,65,65,10), la3=["R","L","None"], nrb=3, sl=3, h=25)
        cmds.setParent("..")

        Utils().btn_layout(2)
        hf = cmds.textField(w=WI02[1], tx="Front", h=25)
        hb = cmds.textField(w=WI02[2], tx="Back", h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Rename", c="hashRenamer()", w=WI01[1], h=30)
        Utils().end_space()


    # Replace
    def frame_replace(self):
        Utils().frame("Replace")

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

        Utils().btn_layout(1)
        cmds.button(l="Replace", c="SearchReplace()", w=WI01[1], h=30)
        Utils().end_space()


    # Add
    def frame_add(self):
        Utils().frame("Add")

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
        cmds.button(l="rig", w=wi[3], c="add(6)", h=25)
        Utils().end_space()
