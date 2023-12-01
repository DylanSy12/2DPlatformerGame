from cmu_graphics import *
from Fireball import *
from ClassFunctions import *
from Character import *
class WindZone:
    windZoneList = []
    def __init__(self, x1, y1, x2, y2, lW, amount, direction, level, room, group, *, Fill = 'paleGreen'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        self.direction = direction
        self.amount = amount
        objctSet(self, level, room, group)
        WindZone.windZoneList[level - 1][room].append(self)
    def push(self):
        if self.shape.hitsShape(character.shape):
            if self.direction == "x":
                character.shape.centerX += self.amount
            elif self.direction == "y":
                if self.amount > 0:
                    character.jump = character.maxJump + 1
                else:
                    character.jump = character.maxJump + 1
                character.shape.centerY += self.amount
        for i in Fireball.fireballList:
            if self.shape.hitsShape(i.shape):
                if self.direction == "x":
                    i.shape.centerX += self.amount
                elif self.direction == "y":
                    i.shape.centerY += self.amount