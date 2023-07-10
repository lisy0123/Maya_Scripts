import maya.cmds as cmds
from imp import reload

import tabs.create
import tabs.naming
import tabs.attr
import tabs.ctrl
import tabs.advance

reload(tabs.create)
reload(tabs.naming)
reload(tabs.attr)
reload(tabs.ctrl)
reload(tabs.advance)

from tabs.create import TabCreate
from tabs.naming import TabNaming
from tabs.attr import TabAttr
from tabs.ctrl import TabCtrl
from tabs.advance import TabAdvance


class MyUse():
    def __init__(self):
        self.built_ui()


    def built_ui(self):
        TOOLNAME = "MyUse"
        TOOLTITLE = "My Use"

        if cmds.window(TOOLNAME, ex=True):
            cmds.deleteUI(TOOLNAME)

        self.WINDOW = cmds.window(TOOLNAME, t=TOOLTITLE)
        tabs = cmds.tabLayout(imh=5, imw=5)
        
        ch1 = self.create_tab(1)
        ch2 = self.create_tab(2)
        ch3 = self.create_tab(3)
        ch4 = self.create_tab(4)
        ch5 = self.create_tab(5)
        
        cmds.tabLayout(tabs, edit=True, tabLabel=((ch1, "Create"), 
                    (ch2, "Naming"),
                    (ch3, "Attr"),
                    (ch4, "Ctrl"),
                    (ch5, "Advance")))
        cmds.showWindow(TOOLNAME)

    
    def tab_layout(self, tmp):
        if tmp:
            cmds.setParent(self.WINDOW)
        col_layout = cmds.rowColumnLayout(w=285, nc=1)

        return(col_layout)


    def create_tab(self, num):
        tmp = False if num == 1 else True
        col_layout = self.tab_layout(tmp)

        tab_list = {1: TabCreate,
                    2: TabNaming,
                    3: TabAttr, 
                    4: TabCtrl,
                    5: TabAdvance}
        tab_list[num]()

        return(col_layout)


MyUse()