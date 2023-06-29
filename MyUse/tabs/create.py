import maya.cmds as cmds
from tabs.utils import Utils

Utils = reload(Utils)

WI01 = (2,273)
WI02 = (1,136,136)


class TabCreate():
    # Joint Size
    def frame_jnt_size(self):
        Utils.frame("Joint Size", 0)
        jnt = cmds.floatSliderButtonGrp(l="Size   ", bl="Set", bc="jointSize()", cw4=(50,50,70,50), f=True, min=0.1, max=1, v=0.5, h=30)
        cmds.setParent("..")


    # Create
    def frame_create(self):
        Utils.frame("Create")

        Utils.btn_layout(2)
        cmds.button(l="Loc", c="cmds.CreateLocator()", w=WI02[1], h=25)
        cmds.button(l="Curve", c="cmds.EPCurveToolOptions()", w=WI02[2], h=25)
        cmds.setParent("..")

        Utils.create_btn(
            "    Joints : ",
            [["Jnt", "cmds.JointTool()"], ["Insert", "cmds.InsertJointTool()"]]
        )
        Utils.create_btn(
            "",
            [["Orient","cmds.OrientJointOptions()"], ["Mirror", "cmds.MirrorJointOptions()"]]
        )
        Utils.create_btn(
            "  Handle : ",
            [["IK", "cmds.IKHandleToolOptions()"], ["IK Spline", "cmds.IKSplineHandleToolOptions()"]]
        )
        Utils.create_btn(
            "      Skin : ",
            [["Bind", "cmds.SmoothBindSkinOptions()"], ["Detach", "cmds.DetachSkinOptions()"]]
        )
        Utils.create_btn(
            " Weights: ",
            [["Paint", "cmds.ArtPaintSkinWeightsToolOptions()"], ["Add Influence", "cmds.AddInfluenceOptions()"]]
        )
        Utils.create_btn(
            "",
            [["HSW", "cmds.WeightHammer()"], ["Mirror", "cmds.MirrorSkinWeightsOptions()"]]
        )

        wi = (50,111,111)
        cmds.rowLayout(nc=3, cw3=wi)
        cmds.text("", w=wi[0])
        cmds.button(l="CpEd", c="cmds.ComponentEditor()", w=wi[1], h=25)
        create_options = cmds.optionMenu(w=wi[2], cc=Utils.apply_menu_item, h=25)
        for obj in Utils.CREATE00:
            cmds.menuItem(l=obj)
        cmds.setParent("..")
        cmds.separator(h=1)

        cmds.rowLayout(nc=2, cw2=WI01)
        cmds.text("")
        cmds.button(l="Node Editor", c="cmds.NodeEditorWindow()", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils.btn_layout(2)
        cmds.button(l="Set Driven Key", c="cmds.SetDrivenKeyOptions()()", w=WI02[1], h=30)
        cmds.button(l="Connection Editor", c="cmds.ConnectionEditor()", w=WI02[2], h=30)
        cmds.setParent("..")

        Utils.btn_layout(2)
        create_options = cmds.optionMenu(w=WI02[1], cc=Utils.apply_menu_item, h=25)
        for obj in Utils.CREATE01:
            cmds.menuItem(l=obj)
        create_options = cmds.optionMenu(w=WI02[2], cc=Utils.apply_menu_item, h=25)
        for obj in Utils.CREATE02:
            cmds.menuItem(l=obj)
        Utils.end_space()
        
        
    # TRS
    def frame_trs(self):
        Utils.frame("TRS")

        cmds.rowLayout(nc=1)
        match_check = cmds.checkBoxGrp(l="Attr : ", ncb=4, cw5=(40,58,52,55,10), la4=["Trans","Rot","Scale","Pivots"], v1=True, v2=True, v3=True, h=25)
        cmds.setParent("..")

        Utils.btn_layout(1)
        cmds.button(l="Match", c="matchFreeze()", w=WI01[1], h=30)
        cmds.setParent("..")

        Utils.btn_layout(1)
        cmds.button(l="Freeze", c="matchFreeze(False)", w=WI01[1], h=30)
        cmds.setParent("..")
        cmds.separator(h=1)

        Utils.btn_layout(2)
        cmds.button(l="LBA", c="cmds.ToggleLocalRotationAxes()", w=WI02[1], h=30)
        cmds.button(l="Center Pivot", c="cmds.CenterPivot()", w=WI02[2], h=30)
        cmds.setParent("..")

        Utils.btn_layout(2)
        cmds.button(l="Rest Tfm", c="cmds.ResetTransformations()", w=WI02[1], h=30)
        cmds.button(l="Delete Hist", c="cmds.DeleteHistory()", w=WI02[2], h=30)
        Utils.end_space()
