from cmu_graphics import *
from ClassFunctions import *
from Character import *
class MovingPlatform:
    movePlatList=[]
    def __init__(self, x1, y1, x2, y2, lW, sX, sY, bXL, bXR, bYT, bYB, level, room, group, *, Fill = 'black'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill)
        self.startX = self.shape.centerX
        self.startY = self.shape.centerY
        self.sX = sX
        self.sY = sY
        self.bXL = bXL
        self.bXR = bXR
        self.bYT = bYT
        self.bYB = bYB
        self.yD = True
        self.xD = True
        objctSet(self, level, room, group)
        MovingPlatform.movePlatList[level - 1][room].append(self)
    def move(self):
        if self.xD:
            if self.shape.hitsShape(character.bottom):
                character.shape.centerX += self.sX
            self.shape.centerX += self.sX
            self.xD = self.shape.right < self.bXR
        else:
            if self.shape.hitsShape(character.bottom):
                character.shape.centerX -= self.sX
            self.shape.centerX -= self.sX
            self.xD = self.shape.left <= self.bXL
        if self.yD:
            if self.shape.left - 2.5 <= character.shape.centerX <= self.shape.right + 2.5:
                if self.shape.hitsShape(character.bottom):
                    character.shape.bottom = self.shape.top + self.sY
                if self.shape.hitsShape(character.top):
                    character.jump = character.maxJump + 1
                    character.bounceUp = 0
                    character.shape.centerY += 2 * self.sY
            self.shape.centerY += self.sY
            self.yD = self.shape.bottom < self.bYB
        else:
            if self.shape.left - 2.5 <= character.shape.centerX <= self.shape.right + 2.5:
                if self.shape.hitsShape(character.bottom):
                    character.shape.bottom = self.shape.top - self.sY
                if self.shape.hitsShape(character.top):
                    character.jump = character.maxJump + 1
                    character.bounceUp = 0
                    character.shape.centerY += 2 * self.sY
            self.shape.centerY -= self.sY
            self.yD = self.shape.top <= self.bYT
        if self.shape.hitsShape(character.bottom):
            character.groundJumped = True
            character.wallJumped = False
    def reset(self):
        if self.level == app.level and self.room == app.room:
            self.shape.centerX = self.startX
            self.shape.centerY = self.startY