from cmu_graphics import *
from ClassFunctions import *
from Sword import *
from Fireball import *
class BreakWall:
    breakWallList = []
    def __init__(self, x1, y1, x2, y2, lW, health, level, room, group, *, Fill = 'brown'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        self.health = health
        self.maxHealth = health
        self.inv = 0
        objctSet(self, level, room, group)
        BreakWall.breakWallList[level - 1][room].append(self)
    def wallBreak(self):
        if self.inv == 0:
            if self.shape.hitsShape(sword.shape) and sword.shape.visible:
                self.inv = 30
                self.health -= sword.damage
                return
            for i in Fireball.fireballList:
                if self.shape.hitsShape(i.shape):
                    self.inv = 30
                    self.health -= i.damage
                    i.life = 0
                    break
        else:
            self.inv -= 1
        self.shape.visible = self.health > 0
    def reset(self):
        if self.level == app.level and self.room == app.room:
            self.shape.visible = True
            self.health = self.maxHealth
            self.inv = 0