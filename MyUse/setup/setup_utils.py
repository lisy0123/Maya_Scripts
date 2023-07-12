TOOLNAME = "HumanAutoRigging"
TOOLTITLE = "Human Auto Rigging"

TRANSLATE = ".translate"
ROTATE = ".rotate"
SCALE = ".scale"
AXISES = ["X", "Y", "Z"]
LFRT = ["L", "R"]

DIST = "distanceBetween"
PLUSMIN = "plusMinusAverage"
MULDIV = "multiplyDivide"
REVERSE = "reverse"
BLENDTWO = "blendTwoAttr"
BLENDCOLORS = "blendColors"

CIRCLE = "circle"
SUB = "half_circle"
SQUARE = "square"
ARROW1 = "arrow1"
ARROW4 = "arrow4"
DIA = "dia"
BOX = "box"
BALL = "ball"
DIAMOND = "diamond"
FKIK_CROSS = "cross1"
CROSS = "cross2"
EYE = "eye"

RED = "red"
YELLOW = "yellow"
BLUE = "blue"
SKYBLUE = "skyblue"
PINK = "pink"
PINK_RED = "pink_red"


def joint_name(type, body, num):
    types = {0: "RIG_", 1: "FK_", 2: "IK_", 
             3: "IK_non_", 4: "IK_stretch_",
             5: "IK_snap_", 6: "IK_ribbon_"}
    return(types[type]+body+str(num))


def ctrlgrp(num=0):
    res = "_ctrl"
    if num == 1:
        res += "_grp"
    elif num == 2:
        res = "_grp"
    elif num == 3:
        res = "_loc"
    return(res)