from cmu_graphics import *
from Enemy import *
from LevelLists import *
class EnemyX(Enemy):
    enemyXList = []
    def __init__(self, cX, y1, y2, lW, health, speed, damage, direction, grounded, level, room, group,  *, maxInv = 45, knockbackResist = 0):
        self.direction = direction
        self.iDirection = direction
        self.grounded = grounded
        super().__init__(cX, y1, y2, lW, health, speed, damage, level, room, group, maxInv, knockbackResist)
        EnemyX.enemyXList[level - 1][room].append(self)
    def move(self):
        if self.health > 0:
            if self.invTime <= 0:
                if self.direction > 0:
                    if not hitCheckAllOr(self.right):
                        self.shape.centerX += self.speed * self.direction
                        if self.grounded:
                            if not hitCheckAllOr(self.bottom) and not hitCheck(groundGroupList, self.bottom):
                                self.shape.centerX -= self.speed * self.direction
                                self.direction *= -1
                    else:
                        self.direction *= -1
                elif self.direction < 0:
                    if not hitCheckAllOr(self.left):
                        self.shape.centerX += self.speed * self.direction
                        if self.grounded:
                            if not hitCheckAllOr(self.bottom) and not hitCheck(groundGroupList, self.bottom):
                                self.shape.centerX -= self.speed * self.direction
                                self.direction *= -1
                    else:
                        self.direction *= -1
                if self.shape.hitsShape(shield.shape) and shield.shape.visible:
                    shield.health -= self.damage
                    self.invTime = self.maxInv
                    self.health -= shield.damage
                    self.shape.centerX -= (shield.pushMulti - self.knockbackResist) * self.speed * self.direction
                    self.direction *= -1
                else:
                    self.damageCheck()
                    if self.shape.hitsShape(character.shape):
                        if character.shape.centerX > self.shape.centerX:
                            character.shape.centerX += self.speed
                        elif character.shape.centerX < self.shape.centerX:
                            character.shape.centerX -= self.speed
                if app.level == 12:
                    groupShapes(self.shape, self.light, 0, 0)
        else:
            self.shape.opacity = 0
            if self.level == 12:
                self.light.visible = False