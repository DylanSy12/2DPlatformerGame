from cmu_graphics import *
from Character import *
from ClassFunctions import *
# slope1A001=Polygon(135, 390, 100, 390, 135, 355) #ground
# Slope(135, 390, 100.05, 390, 135, 355.05, 1, "A", obstacleGroup1A)
# slope1A002=Polygon(100, 360, 100, 325, 135, 325) #ground
# Slope(100, 359.95, 100, 325, 134.95, 325, 1, "A", obstacleGroup1A)
class Slope:
    slopeList = []
    def __init__(
        self, x1, y1, x2, y2, x3, y3, level, room, group, *, 
        Fill = 'black', Opacity = 100, ExtraPoints = []
    ):
        self.shape=Polygon(x1, y1, x2, y2, x3, y3, fill = Fill, opacity = Opacity)
        for coord in ExtraPoints:
            self.shape.addPoint(coord[0], coord[1])
        objctSet(self, level, room, group)
        Slope.slopeList[level - 1][room].append(self)
    def slope(self):
        if self.shape.hitsShape(character.shape):
            while self.shape.hitsShape(character.bottom):
                character.shape.centerY -= 0.05
