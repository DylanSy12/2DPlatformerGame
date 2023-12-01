from cmu_graphics import *
from ClassFunctions import *
import random
class Track:
    trackList = []
    def __init__(self, group, objctLst, level, room, addgroup):
        self.shape = group
        self.level = level
        self.room = room
        self.objctLst = objctLst
        for i in self.objctLst:
            i.direction = 1
            i.speed = 2
        Track.trackList[level - 1][room].append(self)
        objctSet(self, level, room, addgroup)
    def move(self):
        for objct in self.objctLst:
            if objct.shape.visible == True:
                directions = []
                if objct.direction == 1:
                    if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                        objct.shape.centerX += objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if len(directions) == 0:
                            objct.direction = 3
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 2:
                    if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                        objct.shape.centerY -= objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if len(directions) == 0:
                            objct.direction = 4
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 3:
                    if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                        objct.shape.centerX -= objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if len(directions) == 0:
                            objct.direction = 1
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 4:
                    if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                        objct.shape.centerY += objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if len(directions) == 0:
                            objct.direction = 2
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 5:
                    if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                        objct.shape.centerY += objct.speed
                        objct.shape.centerX += objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if len(directions) == 0:
                            objct.direction = 6
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 6:
                    if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                        objct.shape.centerY -= objct.speed
                        objct.shape.centerX -= objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(7)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(8)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if len(directions) == 0:
                            objct.direction = 5
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.direction == 7:
                    if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY - objct.speed):
                        objct.shape.centerY -= objct.speed
                        objct.shape.centerX += objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if len(directions) == 0:
                            objct.shape.direction = 8
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]
                elif objct.shape.direction == 8:
                    if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY + objct.speed):
                        objct.shape.centerY += objct.speed
                        objct.shape.centerX -= objct.speed
                    else:
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY + objct.speed):
                            directions.append(4)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY + objct.speed):
                            directions.append(5)
                        if self.shape.hitTest(objct.shape.centerX + objct.speed, objct.shape.centerY):
                            directions.append(1)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY - objct.speed):
                            directions.append(6)
                        if self.shape.hitTest(objct.shape.centerX, objct.shape.centerY - objct.speed):
                            directions.append(2)
                        if self.shape.hitTest(objct.shape.centerX - objct.speed, objct.shape.centerY):
                            directions.append(3)
                        if len(directions) == 0:
                            objct.direction = 7
                        else:
                            i = random.randint(0, len(directions) - 1)
                            objct.direction = directions[i]