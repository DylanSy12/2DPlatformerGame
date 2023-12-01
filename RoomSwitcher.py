from cmu_graphics import *
from Character import *
from ClassFunctions import *
from Missile import *
from TrackMissile import *
def roomLevelChange():
    for i in range(0, len(levelGroupDictList)):
        for room in roomList:
            for group in levelGroupDictList[i][room]:
                checkIfVisible(group)
    for i in Missile.missileList:
        i.shape.visible = False
        i.shape.fill = None
    for d in TrackMissile.trackMissileList:
        for room in roomList:
            for c in d[room]:
                c.missile.fill = None
def checkIfVisible(group):
    group.visible = group in currentGroup(levelGroupDictList)
class RoomSwitcher:
    switcherList = []
    def __init__(self, x1, y1, x2, y2, lW, eX, eY, level, roomTo, roomFrom, group, *, Fill = gradient('mediumSpringGreen', 'lightGreen', 'paleGreen'), Opacity = 25):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill, opacity = Opacity)
        if level == 12:
            self.light = Oval(
                self.shape.centerX, self.shape.centerY, 
                (x2 + 10) - (x1 - 10), (y2 + 10) - (y2 - 10), 
                fill = gradient('white', 'ghostwhite', 'whitesmoke'), 
                opacity = 25
            )
            group.add(self.light)
        self.roomTo = roomTo
        self.eX = eX
        self.eY = eY
        objctSet(self, level, roomFrom, group)
        RoomSwitcher.switcherList[level - 1][roomFrom].append(self)
    def switch(self):
        if self.shape.hitsShape(character.shape):
            app.room = self.roomTo
            character.shape.centerX = self.eX
            character.shape.centerY = self.eY
            roomLevelChange()