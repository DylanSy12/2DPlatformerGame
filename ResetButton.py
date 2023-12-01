from cmu_graphics import *
from ClassFunctions import *
from Character import *
class ResetButton:
    buttonList = []
    def __init__(self, x1, y1, x2, y2, lW, cooldown, resetList, level, room, group, *, Fill = 'black'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        self.resetList = resetList
        self.cooldown = 0
        self.maxCooldown = cooldown
        objctSet(self, level, room, group)
        ResetButton.buttonList[level-1][room].append(self)
    def push(self):
        if self.cooldown <= 0:
            self.shape.opacity = 100
            if self.shape.hitsShape(character.shape):
                for i in self.resetList:
                    i.reset()
                self.cooldown = self.maxCooldown
        else:
            self.cooldown -= 1
            self.shape.opacity = 25
    def reset(self):
        self.cooldown = 0