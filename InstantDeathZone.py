from cmu_graphics import *
from ClassFunctions import *
from Character import *
class InstantDeathZone:
    zoneList = []
    def __init__(self, x1, y1, x2, y2, lW, level, room, group, *, Fill = 'black'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        objctSet(self, level, room, group)
        InstantDeathZone.zoneList[level - 1].append(self)
    def deathCheck(self):
        if self.shape.hitsShape(character.shape):
            character.hp = 0