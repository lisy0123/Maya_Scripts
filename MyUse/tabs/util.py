import maya.cmds as cmds

WI01 = (2,273)
WI02 = (1,136,136)


class Utils():
    name_list = [
        [
            "  Blend Shape", "  Cluster", "  Lattice"
        ], [
            "  Bend", "  Squash", "  Twist",
            "  Wave", "  Sine", "  Flare"
        ], [
            "  Distance Tool",
            "  Face Normal",
            "  = Normal Size",
            "  Border Edges",
            "  = Edge Width",
            "==============",
            "  File Path Editor"
        ]
    ]


    def btn_layout(self, cnt):
        if cnt == 1:
            cmds.rowLayout(nc=2, cw2=WI01)
            cmds.text("")
        elif cnt == 2:
            cmds.rowLayout(nc=3, cw3=WI02)
            cmds.text("")


    def create_btn(self, title, command, width, height=30):
        cmds.button(l=title, c=command, w=width, h=height)


    def frame(self, text, tmp=True):
        cmds.frameLayout(l=text, cll=True, w=285)
        if tmp:
            cmds.rowLayout(nc=1, h=1)
            cmds.setParent("..")


    def end_space(self):
        cmds.setParent("..")
        cmds.separator(h=1)
        cmds.setParent("..")


    def multiple_btns(self):
        btn_list = (
            [
                "    Joints : ", 
                [["Jnt", "cmds.JointTool()"], ["Insert", "cmds.InsertJointTool()"]]
            ], [
                "",
                [["Orient","cmds.OrientJointOptions()"], ["Mirror", "cmds.MirrorJointOptions()"]]
            ], [
                "  Handle : ",
                [["IK", "cmds.IKHandleToolOptions()"], ["IK Spline", "cmds.IKSplineHandleToolOptions()"]]
            ], [
                "      Skin : ",
                [["Bind", "cmds.SmoothBindSkinOptions()"], ["Detach", "cmds.DetachSkinOptions()"]]
            ], [
                " Weights: ",
                [["Paint", "cmds.ArtPaintSkinWeightsToolOptions()"], ["Add Influence", "cmds.AddInfluenceOptions()"]]
            ], [
                "",
                [["HSW", "cmds.WeightHammer()"], ["Mirror", "cmds.MirrorSkinWeightsOptions()"]]
            ]
        )

        for btn in btn_list:
            wi = (50,111,111)
            cmds.rowLayout(nc=3, cw3=wi)
            cmds.text(btn[0], w=wi[0])
            for num in [0, 1]:
                self.create_btn(btn[1][num][0], btn[1][num][1], wi[num+1], 25)
            cmds.setParent("..")


    def apply_menu_item(self,item):
        command_list = (
            {
                self.name_list[0][0]: cmds.CreateBlendShapeOptions,
                self.name_list[0][1]: cmds.CreateClusterOptions,
                self.name_list[0][2]: cmds.CreateLatticeOptions
            }, {
                self.name_list[1][0]: cmds.BendOptions,
                self.name_list[1][1]: cmds.SquashOptions,
                self.name_list[1][2]: cmds.TwistOptions,
                self.name_list[1][3]: cmds.WaveOptions,
                self.name_list[1][4]: cmds.SineOptions,
                self.name_list[1][5]: cmds.FlareOptions
            }, {
                self.name_list[2][0]: cmds.DistanceTool,
                self.name_list[2][1]: cmds.ToggleFaceNormalDisplay,
                self.name_list[2][2]: cmds.ChangeNormalSize,
                self.name_list[2][3]: cmds.ToggleBorderEdges,
                self.name_list[2][4]: cmds.ChangeEdgeWidth,
                self.name_list[2][6]: cmds.FilePathEditor
            }
        )
        
        if item in command_list[0]:
            command_list[0][item]()
        elif item in command_list[1]:
            command_list[1][item]()
        elif item in command_list[2]:
            command_list[2][item]()