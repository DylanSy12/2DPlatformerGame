from cmu_graphics import *
from LevelLists import *
def objctSet(objct, level, room, group):
    objct.level = level
    objct.room = room
    group.add(objct.shape)
def groupShapes(shape1, shape2, elevation, distance):
    shape2.centerX = shape1.centerX + distance
    shape2.centerY = shape1.centerY + elevation
def currentGroup(groupList):
    return groupList[app.level - 1][app.room]
def hitCheck(groupList, shape):
    return currentGroup(groupList).hitsShape(shape)
def hitFindNotObject(groupList, objct, shape):
    for i in currentGroup(groupList):
        if i != objct:
            if i.shape.hitsShape(shape):
                return i
    return None
def hitCheckAllOr(shape):
    return hitCheck(obstacleGroupList, shape) or hitCheck(keyDoorGroupList, shape) or hitCheck(breakWallGroupList, shape)