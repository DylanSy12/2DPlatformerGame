from cmu_graphics import *
from Enemy import *
from LevelLists import *
#import time
class EnemyY(Enemy):
    enemyYList = []
    def __init__(self, cX, y1, y2, lW, health, speed, damage, direction, level, room, group, *, maxInv = 45, knockbackResist = 0):
        self.direction = direction
        self.iDirection = direction
        #self.time1 = time.time()
        #self.time2 = time.time()
        super().__init__(cX, y1, y2, lW, health, speed, damage, level, room, group, maxInv, knockbackResist)
        EnemyY.enemyYList[level - 1][room].append(self)
    def move(self):
        #self.time1 = time.time()
        if self.health > 0:
            if self.invTime <= 0:
                if self.direction > 0:
                    if not hitCheckAllOr(self.bottom) and not hitCheck(groundGroupList, self.bottom):
                        self.shape.centerY += self.speed * self.direction
                    else:
                        self.direction *= -1
                        #print(self.time1 - self.time2)
                        #self.time2 = time.time()
                else:
                    if not hitCheckAllOr(self.top):
                        self.shape.centerY += self.speed * self.direction
                    else:
                        self.direction *= -1
                        #print(self.time1 - self.time2)
                        #self.time2 = time.time()
                if self.shape.hitsShape(shield.shape) and shield.shape.visible:
                    shield.health -= self.damage
                    self.invTime = self.maxInv
                    self.health -= shield.damage
                    self.shape.centerY -= ((shield.pushMulti - self.knockbackResist) * self.speed) * self.direction
                    self.direction *= -1
                else:
                    self.damageCheck()
                    if self.shape.hitsShape(character.shape):
                        if character.shape.centerY > self.shape.centerY:
                            character.shape.centerY += self.speed
                        elif character.shape.centerY < self.shape.centerY:
                            character.shape.centerY -= self.speed
            if app.level == 12:
                groupShapes(self.shape, self.light, 0, 0)
        else:
            self.shape.opacity = 0
            if self.level == 12:
                self.light.visible = False