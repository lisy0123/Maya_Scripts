# Maya Scripts

Useful tools made with [**Maya commands**](https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/CommandsPython/index.html) and [**pymel**](https://help.autodesk.com/cloudhelp/2023/ENU/Maya-Tech-Docs/PyMel/index.html#) that helps you easily rigging something in **[Maya](https://www.autodesk.com/products/maya/overview?support=ADVANCED&plc=MAYA&term=3-YEAR&quantity=1)**.

## :couple: Human auto rigging

![Human_auto_rigging](https://github.com/lisy0123/Maya_Scripts/blob/master/Human_auto_rigging.png)

|    Part     | functions                                                    |
| :---------: | ------------------------------------------------------------ |
| Spine, Neck | fk/ik (spline), ik hybrid, stretch, follow, stiff, volume    |
|  Arm, Leg   | Multiple/None, fk/ik, stretch, follow, snap, ribbon(twist, volume, sine) |
|    Hand     | fk/ik, each attr, spread, relax, slide, scrunch              |
|    Foot     | fk/ik, rock, roll, swivel, sub ctrl                          |

:label: Updating...

---

## :mag: My use

![My_use](https://github.com/lisy0123/Maya_Scripts/blob/master/My_use.png)

- [x] joint, ik, weights options, set driven key, etc...
- [x] constraint: maintain offset toggle
- [x] quick constraint (1:1, M:1)
- [x] quick add, lock, unlock attribute
- [x] rename: search and replace
- [x] namer(after): Exclude *shape => Include joint, transform
- [x] set in order => Solved by ordering it from the bottom, not from the top.
- [x] text didn't work well (123..,[]!@#$%%^&*)
- [x] add/delete attribute
- [x] change attribute order
- [ ] change attribute name
- [ ] add attribute for target visibility
- [x] spread constraint
- [ ] spread constraint error: hi에서 꼬이는 경우 발생. 원인 찾기
- [ ] replace, resize, select, rotate, mirror ctrl
- [ ] add more ctrl shapes
- [ ] add picot ctrl
- [ ] cluster deformer(??)
- [x] copy and new group
- [ ] rivet (Each/Sum)
- [ ] freeze skinned joint
- [ ] motion path (Basic/Advance)
- [ ] ribbon
- [ ] joint copy (fk, ik, rig)
- [ ] joint copy for ik spline
- [ ] quick FK/IK rig
- [ ] quick mouth/eye rig
- [ ] copy/paste weight
- [ ] refactoring

:label: Updating...

---

## :hand: Hand auto rigging

![Hand_auto_rigging](https://github.com/lisy0123/Maya_Scripts/blob/master/Hand_auto_rigging.png)

- [x] one/both hand rigging

<details>
  <summary> Warning: Skipping L_finger_1_1: It has non-zero rotations. </summary>
  <div markdown="1">

```python
# If I freeze the joint's transforms, rotation values will be added to the joint orient and the rotation will become (0,0,0).
# So freeze transforms first and orient next.
```

  </div>
</details>

<details>
  <summary> Warning: Cannot parent components or objects in the underworld. </summary>
  <div markdown="1">

```python
import maya.cmds as cmds

cmds.circle(n="cir1")
cmds.circle(n="cir2")
cmds.parent("cir1", "cir2")
# No Warning, but uncomfortable

cir1 = cmds.circle()
cir2 = cmds.circle()
cmds.parent(cir1, cir2)
# Warning: Cannot parent components or objects in the underworld.
print cir1, cir2
# [u'nurbsCircle1', u'makeNurbCircle1'] [u'nurbsCircle2', u'makeNurbCircle2']

cir1 = cmds.circle()[0]
cir2 = cmds.circle()[0]
cmds.parent(cir1, cir2)
# No Warning
print cir1, cir2
# nurbsCircle1 nurbsCircle2
```

  </div>
</details>

---

## :bird: Wing auto rigging

YET



[↩️ Go Back](https://github.com/lisy0123/Study)

