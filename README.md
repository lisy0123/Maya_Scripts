# Maya Scripts

Useful tools made with [**mel and pymel**](https://help.autodesk.com/cloudhelp/2020/ENU/Maya-Tech-Docs/PyMel/index.html) that helps you easily rigging something in **[Maya](https://www.autodesk.com/products/maya/overview?support=ADVANCED&plc=MAYA&term=3-YEAR&quantity=1)**.

## :hand: Hand auto rigging

![Hand_auto_rigging](https://github.com/lisy0123/Maya_Scripts/blob/master/Hand_auto_rigging.png)

- [x] orient joint error: didn't work
- [x] ctrl error: keep making ctrl

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

- [ ] constrain: maintain offset toggle
- [ ] rename: search and replace(hi, sel, all)
- [ ] text didn't work well (123..,[]!@#$%%^&*)
- [ ] controller hierarchy setting at beginning - on/off
- [ ] ctrl color: setting at beginning
- [ ] create joint
- [ ] mirror joint (search and replace)
- [ ] orient joint
- [ ] joint copy (ik spline)
- [ ] quick add, lock, unlock attribute
- [ ] set driven key
- [ ] weights options

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