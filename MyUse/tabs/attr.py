import maya.cmds as cmds
from imp import reload
import tabs.util

reload(tabs.util)

from tabs.util import Utils

WI01 = (2,273)
WI02 = (1,136,136)


class TabAttr():
    def __init__(self):
        self.frame_lock()
        self.frame_attr()
        self.frame_spread()


    # Lock
    def frame_lock(self):
        Utils().frame("Lock")

        cmds.rowLayout(nc=1)
        lock_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,60,60,60,10), la4=["Trans","Rot","Scale","Vis"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(2)
        cmds.button(l="Lock + UnKeyable", c="lockUnlock(True, False)", w=WI02[1], h=30)
        cmds.button(l="Lock + Keyable", c="lockUnlock(True, True)", w=WI02[2], h=30)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Unlock + Keyable", c="lockUnlock(False, True)", w=WI01[1], h=30)
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils().btn_layout(2)
        cmds.button(l="Lock Selected", c="lockUnlock(True, True, True)", w=WI02[1], h=30)
        cmds.button(l="Unlock Selected", c="lockUnlock(False, True, True)", w=WI02[2], h=30)
        Utils().end_space()


    # Attribute
    def frame_attr(self):
        Utils().frame("Attribute")

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

        Utils().btn_layout(1)
        cmds.button(l="Change Attr Name", c="changeAttrName()", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Add Float Attr", c="addAttr(0)", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Add Bool Attr", c="addAttr(1)", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils().btn_layout(2)
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
        Utils().end_space()


    # Spread Constraint
    def frame_spread(self):
        Utils().frame("Spread Constraint")

        cmds.rowLayout(nc=1)
        spread_axes_check = cmds.checkBoxGrp(l=" Axes: ", ncb=3, cw4=(60,60,60,10), la3=["X","Y","Z"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        spread_const_check = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent","Point","Orient","Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        cmds.button(l="Add Attr", c="spread()", w=WI01[1], h=30)
        Utils().end_space()