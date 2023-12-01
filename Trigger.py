from cmu_graphics import *
from ClassFunctions import *
from LevelLists import *
from Character import *
class Trigger:
    triggerList = []
    def __init__(self, x1, y1, x2, y2, lW, triggersTrue, triggersFalse, level, room):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, visible = False)
        self.level = level
        self.room = room
        self.triggersTrue = triggersTrue
        for i in self.triggersTrue:
            if i in obstacleGroupList[self.level - 1][self.room]:
                i.obstacle = True
                i.ground = False
            elif i in groundGroupList[self.level - 1][self.room]:
                i.ground = True
                i.obstacle = False
        self.triggersFalse = triggersFalse
        self.triggered = False
        Trigger.triggerList[level - 1][room].append(self)
    def trigger(self):
        if not self.triggered:
            for i in self.triggersTrue:
                if i.ground:
                    currentGroup(groundGroupList).add(i)
                elif i.obstacle:
                    currentGroup(obstacleGroupList).add(i)
            for i in self.triggersFalse:
                if i.ground:
                    if i in currentGroup(groundGroupList):
                        currentGroup(groundGroupList).remove(i)
                elif i.obstacle:
                    if i in currentGroup(obstacleGroupList):
                        currentGroup(obstacleGroupList).remove(i)
            if self.shape.hitsShape(character.shape):
                self.triggered = True
        else:
            for i in self.triggersTrue:
                if i.ground:
                    if i in currentGroup(groundGroupList):
                        currentGroup(groundGroupList).remove(i)
                elif i.obstacle:
                    if i in currentGroup(obstacleGroupList):
                        currentGroup(obstacleGroupList).remove(i)
            for i in self.triggersFalse:
                if i.ground:
                    currentGroup(groundGroupList).add(i)
                elif i.obstacle:
                    currentGroup(obstacleGroupList).add(i)
    def reset(self):
        if self.level == app.level and self.room == app.room:
            self.triggered = False
            self.trigger()