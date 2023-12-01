from cmu_graphics import *
from ClassFunctions import *
from Character import *
class Spike:
    spikeList = []
    def __init__(self, cX, cY, damage, level, room, group):
        self.shape = Star(cX, cY, 5, 8, roundness = 25, rotateAngle = 45, fill = 'yellow')
        self.damage = damage
        objctSet(self, level, room, group)
        Spike.spikeList[level - 1][room].append(self)
    def damageCheck(self):
        if character.invTime <= 0:
            if self.shape.hitsShape(character.shape):
                character.invTime = character.maxInv
                character.hp -= self.damage