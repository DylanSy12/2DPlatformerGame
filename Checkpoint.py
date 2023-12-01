from cmu_graphics import *
from ClassFunctions import *
from Character import *
class Checkpoint:
    checkpointList = []
    def __init__(self, cX, cY, level, room, group):
        self.shape = Line(cX, cY - 5, cX, cY + 5, lineWidth = 10, fill = gradient('white', 'lightGray', 'silver'))
        if app.level == 12:
            self.light = Circle(cX, cY, 15, opacity = 25, fill = gradient('white', 'ghostwhite', 'whitesmoke'))
            group.add(self.light)
        objctSet(self, level, room, group)
        Checkpoint.checkpointList[level - 1][room].append(self)
    def setSpawn(self):
        if self.shape.hitsShape(character.shape):
            character.spawnX = self.shape.centerX
            character.spawnY = self.shape.centerY
            app.spawnRoom = app.room
            character.hp = character.maxHP
            character.mp = character.maxMP
        if (
            character.spawnX == self.shape.centerX and character.spawnY == self.shape.centerY and 
            app.spawnRoom == self.room and app.level == self.level
        ):
            self.shape.fill = gradient('yellow', 'orange', 'red')
            self.shape.opacity = 75
        else:
            self.shape.fill = gradient('white', 'lightGray', 'silver')
            self.shape.opacity = 100