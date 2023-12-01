from cmu_graphics import *
from ClassFunctions import *
class LinkedWall:
    wallList = []
    def __init__(
        self, x1, y1, x2, y2, lW, linked, level, room, group, *, 
        Fill = gradient('salmon', 'lightcoral', 'deeppink')
    ):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        self.linked = linked
        objctSet(self, level, room, group)
        LinkedWall.wallList[level - 1][room].append(self)
    def linkCheck(self):
        for i in self.linked:
            if i.health > 0:
                return
        self.shape.visible = False
    def reset(self):
        self.shape.visible = self.level == app.level and self.room == app.room