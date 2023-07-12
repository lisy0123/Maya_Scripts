import maya.cmds as cmds
import pymel.core as pm
import copy


def change_attr_name(name):
    objs = pm.ls(sl=True)
    for obj in objs:
        sl_attr = pm.channelBox("mainChannelBox", q=True, sma=True)
        cmds.addAttr(obj+'.'+sl_attr[0], e=True, nn=name)


def add_float(name, check, min, max):
    objs = pm.ls(sl=True)
    for obj in objs:
        if cmds.checkBox(check, q=True, v=True):
            pm.addAttr(obj, ln=name, at="double", dv=0)
            pm.setAttr(obj+"."+name, k=True)
        else:
            pm.addAttr(obj, ln=name, at="double", min=min, max=max)
            pm.setAttr(obj+"."+name, k=True)


def add_bool(name, enum_list):
    objs = pm.ls(sl=True)
    for obj in objs:            
        pm.addAttr(obj, ln=name, at="enum", en=enum_list)
        pm.setAttr(obj+"."+name, k=True)


def add_sep(_):
    objs = pm.ls(sl=True)
    for obj in objs:
        cnt = 0
        flag = True
        while flag:
            cnt_str = "separator"+str(cnt)
            if pm.attributeQuery(cnt_str, n=obj.name(), ex=True):
                cnt += 1
            else:
                pm.addAttr(obj, ln=cnt_str, nn="----------", at="enum", en="--------:")
                pm.setAttr(obj+"."+cnt_str, cb=True)
                flag = False


def del_attr(up=False, tmp=False):
    objs = pm.ls(sl=True)
    attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    sl_attrs = copy.deepcopy(attrs)

    for obj in objs:
        if up:
            attrs = pm.listAttr(obj, ud=True)
            for attr in sl_attrs:
                attrs.remove(attr)
        for attr in attrs:
            try:
                pm.deleteAttr (obj, at=attr)
                if tmp:
                    pm.undo()
            except:
                pass


def sub_del_attr(obj, string):
    pm.deleteAttr(obj, at=string)
    pm.undo()


def change_order_up(_):
    objs = pm.ls(sl=True)
    sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    
    for obj in objs:
        attrs = pm.listAttr(obj, ud=True)
        flag = False
        for idx in range(len(attrs)):
            if attrs[idx] == sl_attrs[0]:
                sub_del_attr(obj, attrs[idx-1])
                idx += len(sl_attrs)
                flag = True
            elif attrs[idx] in sl_attrs:
                if idx + len(sl_attrs)-1 < len(attrs):
                    sub_del_attr(obj, attrs[idx+len(sl_attrs)-1])
                    idx += 1
            elif flag == True:
                sub_del_attr(obj, attrs[idx])


def change_order_down(_):
    objs = pm.ls(sl=True)
    sl_attrs = pm.channelBox("mainChannelBox", q=True, sma=True)
    
    for obj in objs:
        attrs = pm.listAttr(obj, ud=True)
        flag = False
        for idx in range(len(attrs)):
            if attrs[idx] == sl_attrs[0]:
                if idx + len(sl_attrs) < len(attrs):
                    tmp = attrs[idx+len(sl_attrs)]
                    sub_del_attr(obj, tmp)
                    sub_del_attr(obj, attrs[idx])
                    idx += len(sl_attrs)
                    flag = True
            elif attrs[idx] in sl_attrs:
                sub_del_attr(obj, attrs[idx])
                idx += 1
            elif flag == True and attrs[idx] != tmp:
                sub_del_attr(obj, attrs[idx])