from cmu_graphics import *
from Character import *
from ClassFunctions import *
class HealZone:
    healZoneList = []
    def __init__(self, cX, cY, heal, cooldown, level, room, group):
        self.shape = Line(cX, cY - 13, cX, cY + 13, fill = gradient('azure', 'lightcyan', 'aqua'), lineWidth = 20)
        self.cooldown = cooldown
        self.maxCooldown = cooldown
        self.amount = heal
        objctSet(self, level, room, group)
        HealZone.healZoneList[level - 1][room].append(self)
    def heal(self):
        if self.cooldown <= 0:
            self.shape.fill = gradient('azure', 'lightcyan', 'aqua')
            if self.shape.hitsShape(character.shape):
                character.hpRestore(self.amount)
                character.invTime = character.maxInv
                self.cooldown = self.maxCooldown
        else:
            self.shape.fill = gradient('dodgerblue', 'royalblue', 'blue')
            self.cooldown -= 1