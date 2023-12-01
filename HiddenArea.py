from cmu_graphics import *
from ClassFunctions import *
from Character import *
from Fireball import *
class HiddenArea:
    hiddenAreaList = []
    def __init__(self, x1, y1, x2, y2, lW, level, room, group, *, Fill = 'black'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        objctSet(self, level, room, group)
        HiddenArea.hiddenAreaList[level - 1][room].append(self)
    def reveal(self):
        if self.shape.visible != False and self.shape.opacity != 100:
            self.shape.opacity = 100
        elif not self.shape.visible:
            return
        if self.shape.hitsShape(character.shape):
            self.shape.visible = False
        else:
            for i in Fireball.fireballList:
                if self.shape.hitsShape(i.shape):
                    Fireball.fireballList.remove(i)
                    i.shape.visible = False
                    if app.level == 12:
                        i.light.visible = False
                    self.shape.opacity = 75
                    return