# Maya Scripts

Useful tools made with [**mel and pymel**](https://help.autodesk.com/cloudhelp/2020/ENU/Maya-Tech-Docs/PyMel/index.html) that helps you easily rigging something in **[Maya](https://www.autodesk.com/products/maya/overview?support=ADVANCED&plc=MAYA&term=3-YEAR&quantity=1)**.

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

## :mag: My use

![My_use](https://github.com/lisy0123/Maya_Scripts/blob/master/My_use.png)

- [x] joint, ik, weights options, set driven key, etc...
- [x] constrain: maintain offset toggle
- [x] namer(after): Exclude *shape => Delete once/hierarchy
- [x] rename: search and replace
- [x] quick add, lock, unlock attribute
- [ ] set in order: 방법 고민...
- [ ] joint copy for ik spline
- [ ] rivet (Each/Sum)
- [ ] motion path (Basic/Advance)
- [ ] text didn't work well (123..,[]!@#$%%^&*)

:label: Updating...

---

## :couple: Human auto rigging

![Human_auto_rigging](https://github.com/lisy0123/Maya_Scripts/blob/master/Human_auto_rigging.png)

- [ ] rename functions

:label: Updating...

----

## :bird: Wing auto rigging

YET



[↩️ Go Back](https://github.com/lisy0123/Study)
