from cmu_graphics import *
from Character import *
class Portal:
    portalList = []
    def __init__(self, cX1, cY1, cX2, cY2, level, room, group):
        if level <= 6:
            self.portal1 = Line(cX1, cY1 - 10, cX1, cY1 + 10, lineWidth = 20, fill = gradient('blue', 'purple', 'purple'))
            self.portal2 = Line(cX2, cY2 - 10, cX2, cY2 + 10, lineWidth = 20, fill = gradient('blue', 'purple', 'purple'))
            self.portalClose1 = Circle(cX1, cY1, 10, fill = gradient('blue', 'purple', 'purple'))
            self.portalClose2 = Circle(cX2, cY2, 10, fill = gradient('blue', 'purple', 'purple'))
        else:
            self.portal1 = Line(cX1, cY1 - 5, cX1, cY1 + 5, lineWidth = 10, fill = gradient('blue', 'purple', 'purple'))
            self.portal2 = Line(cX2, cY2 - 5, cX2, cY2 + 5, lineWidth = 10, fill = gradient('blue', 'purple', 'purple'))
            self.portalClose1 = Circle(cX1, cY1, 5, fill = gradient('blue', 'purple', 'purple'))
            self.portalClose2 = Circle(cX2, cY2, 5, fill = gradient('blue', 'purple', 'purple'))
        group.add(self.portal1)
        group.add(self.portal2)
        group.add(self.portalClose1)
        group.add(self.portalClose2)
        self.usable = True
        self.level = level
        self.room = room
        Portal.portalList[level - 1][room].append(self)
    def teleport(self):
        if self.usable:
            if self.portal1.hitsShape(character.shape):
                character.shape.centerX = self.portal2.centerX
                character.shape.centerY = self.portal2.centerY
                self.usable = False
                self.portal1.fill = None
                self.portal2.fill = None
            elif self.portal2.hitsShape(character.shape):
                character.shape.centerX = self.portal1.centerX
                character.shape.centerY = self.portal1.centerY
                self.usable = False
                self.portal1.fill = None
                self.portal2.fill = None
        else:
            if not (self.portal1.hitsShape(character.shape) or self.portal2.hitsShape(character.shape)):
                self.usable = True
                self.portal1.fill = gradient('blue', 'purple', 'purple')
                self.portal2.fill = gradient('blue', 'purple', 'purple')