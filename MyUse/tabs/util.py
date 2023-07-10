import maya.cmds as cmds

WI01 = (2,273)
WI02 = (1,136,136)


class Utils():
    CREATE00 = [
        "  Blend Shape", "  Cluster", "  Lattice",
    ]
    CREATE01 = [
        "  Bend", "  Squash", "  Twist", "  Wave", "  Sine", "  Flare",
    ]
    CREATE02 = [
        "  Distance Tool", "  Face Normal", "  = Normal Size",
        "  Border Edges", "  = Edge Width", "="*14, "  File Path Editor",
    ]


    def btn_layout(self, cnt):
        if cnt == 1:
            cmds.rowLayout(nc=2, cw2=WI01)
            cmds.text("")
        elif cnt == 2:
            cmds.rowLayout(nc=3, cw3=WI02)
            cmds.text("")


    def frame(self, text, tmp=True):
        cmds.frameLayout(l=text, cll=True, w=285)
        if tmp:
            cmds.rowLayout(nc=1, h=1)
            cmds.setParent("..")


    def end_space(self):
        cmds.setParent("..")
        cmds.separator(h=1)
        cmds.setParent("..")


    def create_btn(self, subject, things):
        wi = (50,111,111)
        cmds.rowLayout(nc=3, cw3=wi)
        cmds.text(subject, w=wi[0])
        cmds.button(l=things[0][0], c=things[0][1], w=wi[1], h=25)
        cmds.button(l=things[1][0], c=things[1][1], w=wi[2], h=25)
        cmds.setParent("..")


    def apply_menu_item(self,item):
        # CREATE00
        if item == self.CREATE00[0]:
            cmds.CreateBlendShapeOptions()
        elif item == self.CREATE00[2]:
            cmds.CreateLatticeOptions()
        elif item == self.CREATE00[1]:
            cmds.CreateClusterOptions()

        # CREATE01
        elif item == self.CREATE01[0]:
            cmds.BendOptions()
        elif item == self.CREATE01[1]:
            cmds.SquashOptions()
        elif item == self.CREATE01[2]:
            cmds.TwistOptions()
        elif item == self.CREATE01[3]:
            cmds.WaveOptions()
        elif item == self.CREATE01[4]:
            cmds.SineOptions()
        elif item == self.CREATE01[5]:
            cmds.FlareOptions()

        # CREATE02
        elif item == self.CREATE02[0]:
            cmds.DistanceTool()
        elif item == self.CREATE02[1]:
            cmds.ToggleFaceNormalDisplay()
        elif item == self.CREATE02[2]:
            cmds.ChangeNormalSize()
        elif item == self.CREATE02[3]:
            cmds.ToggleBorderEdges()
        elif item == self.CREATE02[4]:
            cmds.ChangeEdgeWidth()
        elif item == self.CREATE02[6]:
            cmds.FilePathEditor()