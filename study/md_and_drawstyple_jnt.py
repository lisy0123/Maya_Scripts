#____md
######################################
#____select skinned mesh and mesh deform by jk____________________________________________________
import pymel.core as pm
skinClusters = pm.ls(typ='skinCluster')
skinnedMeshes = []
for node in skinClusters:
    skinnedMeshes.append( node.outputGeometry.connections() )
skinnedMeshes = [a for b in [node.outputGeometry.connections() for node in skinClusters] for a in b]
cmds.select(skinnedMeshes)
import maya.cmds as cmds
meshList = cmds.ls(selection=1)
for elem in meshList:
    attrCheck = cmds.attributeQuery( 'meshDeform', node=elem, ex=True )
    if attrCheck == False:
        cmds.addAttr (elem, ln='meshDeform', at="bool", dv = 1)
        print 'New attribute added on ' + elem

#--------------------------------------------------------------------------------------------#

#md
import maya.cmds as cmds
meshList = cmds.ls(selection=1)
for elem in meshList:
    attrCheck = cmds.attributeQuery( 'meshDeform', node=elem, ex=True )
    if attrCheck == False:
        cmds.addAttr (elem, ln='meshDeform', at="bool", dv = 1)
        print 'New attribute added on ' + elem

#--------------------------------------------------------------------------------------------#

#drawstyle_of_jnt
import pymel.core as pm
hd = pm.ls(selection=True)
for w in hd:
    print w
    pm.setAttr(w.drawStyle,2)


import pymel.core as pm
hd = pm.ls(sl=True)
print hd
print len(hd)
for x in range(0,len(hd)):
    h=hd[x]
    print h
    pm.setAttr(h.drawStyle,2)

