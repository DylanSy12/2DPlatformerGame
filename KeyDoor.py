from cmu_graphics import *
from ClassFunctions import *
from Character import *
from Key import *
class KeyDoor:
    keyDoorList = []
    def __init__(self, x1, y1, x2, y2, lW, level, room, group, *, keysNeeded = 1):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = gradient('black', 'fireBrick', 'fireBrick', 'fireBrick'))
        objctSet(self, level, room, group)
        self.keysNeeded = keysNeeded
        KeyDoor.keyDoorList[level - 1][room].append(self)
    def openDoor(self):
        if self.shape.hitsShape(character.shape) and self.shape.visible:
            if app.keys >= self.keysNeeded:
                self.shape.visible = False
                app.keys -= self.keysNeeded
                Key.keyLabel.value = "Keys: " + str(app.keys)
    def reset(self):
        self.shape.visible = self.level == app.level and self.room == app.room