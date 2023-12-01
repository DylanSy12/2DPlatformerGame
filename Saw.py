from cmu_graphics import *
from ClassFunctions import *
from Character import *
class Saw:
    sawList = []
    def __init__(self, cX, cY, size, damage, level, room, group):
        self.shape = Star(cX, cY, size, 20, roundness = 70, fill = 'yellow')
        self.damage = damage
        objctSet(self, level, room, group)
        Saw.sawList[level - 1][room].append(self)
    def rotate(self):
        if character.invTime <= 0:
            if self.shape.hitsShape(character.shape):
                character.invTime = character.maxInv
                character.hp -= self.damage
        self.shape.rotateAngle += 9