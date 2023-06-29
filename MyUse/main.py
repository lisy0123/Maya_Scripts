import maya.cmds as cmds
from tabs.create import TabCreate
from tabs.naming import TabNaming
from tabs.attr import TabAttr
from tabs.ctrl import TabCtrl
from tabs.advance import TabAdvance

TabCreate = reload(TabCreate)
TabNaming = reload(TabNaming)
TabAttr = reload(TabAttr)
TabCtrl = reload(TabCtrl)
TabAdvance = reload(TabAdvance)

TOOLNAME = "MyUse"
TOOLTITLE = "My Use"


class MyUse():
    def __init__(self):
        self.built_ui()
        
    
    def built_ui(self):
        if cmds.window(TOOLNAME, ex=True):
            cmds.deleteUI(TOOLNAME)

        WINDOW = cmds.window(TOOLNAME, t=TOOLTITLE)
        tabs = cmds.tabLayout(imh=5, imw=5)
        
        ch1 = self.tab_create()
        ch2 = self.tab_nameing(WINDOW)
        ch3 = self.tab_attr(WINDOW)
        ch4 = self.tab_ctrl(WINDOW)
        ch5 = self.tab_advance(WINDOW)
        
        cmds.tabLayout(tabs, edit=True, tabLabel=((ch1, "Create"), (ch2, "Naming"), (ch3, "Attr"), (ch4, "Ctrl"), (ch5, "Advance")))
        cmds.showWindow(TOOLNAME)


    # 1: Create
    def tab_create(self):
        col_layout = cmds.rowColumnLayout(w=285, nc=1)

        TabCreate().frame_jnt_size()
        TabCreate().frame_create()
        TabCreate().frame_trs()
        
        return(col_layout)


    # 2: Naming
    def tab_nameing(self, WINDOW):
        cmds.setParent(WINDOW)
        col_layout = cmds.rowColumnLayout(w=285, nc=1)
        
        TabNaming().frame_outline()
        TabNaming().frame_rename()
        TabNaming().frame_replace()
        TabNaming().frame_add()

        return(col_layout)
        

    # 3: Attr
    def tab_attr(self, WINDOW):
        cmds.setParent(WINDOW)
        col_layout = cmds.rowColumnLayout(w=285, nc=1)

        TabAttr().frame_lock()
        TabAttr().frame_attr()
        TabAttr().frame_spread()

        return(col_layout)


    # 4: Ctrl
    def tab_ctrl(self, WINDOW):
        cmds.setParent(WINDOW)
        col_layout = cmds.rowColumnLayout(w=285, nc=1)

        TabCtrl().frame_ctrl()
        TabCtrl().frame_text()
        TabCtrl().frame_const()
        TabCtrl().frame_color_picker()

        return(col_layout)
        

    # 5: Advance
    def tab_advance(self, WINDOW):
        cmds.setParent(WINDOW)
        col_layout = cmds.rowColumnLayout(w=285, nc=1)

        TabAdvance.frame_setup()
        TabAdvance.frame_motion_path()
        TabAdvance.frame_rivet()

        return(col_layout)


MyUse()
print "DONE!"
