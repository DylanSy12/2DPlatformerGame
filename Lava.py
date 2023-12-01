from cmu_graphics import *
from ClassFunctions import *
from Character import *
class Lava:
    lavaList = []
    def __init__(self, x1, y1, x2, y2, lW, dmg, level, room, group, *, rotate = 0):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = 'orange', rotateAngle = rotate)
        if app.level == 12:
            self.light = Oval(self.shape.centerX, self.shape.centerY, self.shape.width + 15, self.shape.height + 15, 
                fill = gradient('white', 'ghostwhite', 'whitesmoke'), opacity = 20, rotateAngle = rotate)
            group.add(self.light)
        self.dmg = dmg
        objctSet(self, level, room, group)
        Lava.lavaList[level - 1][room].append(self)
    def lavaCheck(self):
        if self.shape.hitsShape(character.shape) and character.invTime <= 0:
            character.hp -= self.dmg
            character.invTime = character.maxInv
            character.jump = character.maxJump + 1