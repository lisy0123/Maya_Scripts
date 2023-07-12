import maya.cmds as cmds
from imp import reload
import tabs.util
import functions.lock as funcs_lock
import functions.attribute as funcs_attr
import functions.spread as funcs_spread

reload(tabs.util)
funcs_lock = reload(funcs_lock)
funcs_spread = reload(funcs_spread)

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
        self.lock_attr = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,60,60,60,10), la4=["Trans", "Rot", "Scale","Vis"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(2)
        Utils().create_btn("Lock + UnKeyable", 
            lambda x: funcs_lock.lock(self.lock_attr, True, False), WI02[1])
        Utils().create_btn("Lock + Keyable", 
            lambda x: funcs_lock.lock(self.lock_attr, True, True), WI02[2])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Unlock + Keyable", 
            lambda x: funcs_lock.lock(self.lock_attr, False, True), WI01[1])
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils().btn_layout(2)
        Utils().create_btn("Lock Selected", 
            lambda x: funcs_lock.lock_sel(True, True), WI02[1])
        Utils().create_btn("Unlock Selected", 
            lambda x: funcs_lock.lock_sel(False, True), WI02[2])
        Utils().end_space()


    # Attribute
    def frame_attr(self):
        Utils().frame("Attribute")

        wi=(65,210)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="        Name : ", w=wi[0])
        self.attr_name = cmds.textField(w=wi[1], tx="", h=25)
        cmds.setParent("..")

        wi = (65,150)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="         Reset :  ", w=wi[0])
        self.reset = cmds.checkBox(l="No limit with min/max", w=wi[1], h=25)
        cmds.setParent("..")

        wi = (65,104,104)
        cmds.rowLayout(nc=3, cw3=wi)
        cmds.text(l="  Min/Max :", w=wi[0])
        self.min = cmds.textField(w=wi[1], tx=0.0, h=25)
        self.max = cmds.textField(w=wi[2], tx=1.0, h=25)
        cmds.setParent("..")

        wi=(65,210)
        cmds.rowLayout(nc=2, cw2=wi)
        cmds.text(l="  Enum List : ", w=wi[0])
        self.enum_list = cmds.textField(w=wi[1], tx="OFF:ON", h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Change Attr Name", self.func_change_attr_name, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Add Float Attr", self.func_add_float_attr, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Add Bool Attr", self.func_add_bool_attr, WI01[1])
        cmds.setParent("..")

        Utils().btn_layout(2)
        Utils().create_btn("Separator Attr", funcs_attr.add_sep, WI02[1])
        Utils().create_btn("Delete Attr", funcs_attr.del_attr, WI02[2])
        cmds.setParent("..")
        cmds.separator(h=1)

        wi=(1,67,67,67,67)
        cmds.rowLayout(nc=5, cw5=wi)
        cmds.text("")
        Utils().create_btn("UUP", lambda x: funcs_attr.del_attr(True, True), wi[1])
        Utils().create_btn("UP", funcs_attr.change_order_up, wi[2])
        Utils().create_btn("DOWN", funcs_attr.change_order_down, wi[3])
        Utils().create_btn("DDOWN", lambda x: funcs_attr.del_attr(False, True), wi[4])
        Utils().end_space()


    # Spread Constraint
    def frame_spread(self):
        Utils().frame("Spread Constraint")

        cmds.rowLayout(nc=1)
        self.axes = cmds.checkBoxGrp(l=" Axes: ", ncb=3, cw4=(60,60,60,10), la3=["X", "Y", "Z"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        cmds.rowLayout(nc=1)
        self.const = cmds.checkBoxGrp(l=" Constraint: ", ncb=4, cw5=(63,55,48,55,10), la4=["Parent", "Point", "Orient", "Scale"], v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils().btn_layout(1)
        Utils().create_btn("Add Attr", 
            lambda x: funcs_spread.spread(self.axes, self.const), WI01[1])
        Utils().end_space()


    def func_change_attr_name(self, _):
        name = cmds.textField(self.attr_name, q=True, tx=True)
        funcs_attr.change_attr_name(name)

    def func_add_float_attr(self, _):
        name = cmds.textField(self.attr_name, q=True, tx=True)
        min = float(cmds.textField(self.min, q=True, tx=True))
        max = float(cmds.textField(self.max, q=True, tx=True))
        funcs_attr.add_float(name, self.reset, min, max)

    def func_add_bool_attr(self, _):
        name = cmds.textField(self.attr_name, q=True, tx=True)
        enum_list = cmds.textField(self.enum_list, q=True, tx=True) 
        funcs_attr.add_bool(name, enum_list)