from cmu_graphics import *
from Enemy import *
class EnemyC(Enemy):
    enemyCList = []
    def __init__(self, cX, y1, y2, lW, health, speed, damage, detectionRange, level, room, group, *, maxInv = 45, knockbackResist = 0, boss = False):
        self.moveX = 3
        self.moveY = 3
    def enemyCheck(self, times):
        if self.moveX == 0:
            if hitCheck(enemyGroupList, self.left):
                e = currentGroup(enemyGroupList).hitTest(self.shape.left + 1, self.shape.centerY)
                if e != self.shape and e != None:
                    if e.opacity != 0:
                        for i in currentGroup(EnemyC.enemyCList):
                            if i.shape == e:
                                self.shape.centerX += i.enemyCheck(times + 1) * self.speed
                                return times - 1
            if self.left.hitsShape(character.right):
                self.shape.centerX += self.speed
                if hitCheck(enemyGroupList, self.right):
                    e = currentGroup(enemyGroupList).hitTest(self.shape.right - 1, self.shape.centerY)
                    if e != self.shape and e != None:
                        if e.opacity != 0:
                            for i in currentGroup(EnemyC.enemyCList):
                                if i.shape == e:
                                    i.enemyCheck(2)
                                    return times - 1
        elif self.moveX == 1:
            if hitCheck(enemyGroupList, self.right):
                e = currentGroup(enemyGroupList).hitTest(self.shape.right - 1, self.shape.centerY)
                if e != self.shape and e != None:
                    if e.opacity != 0:
                        for i in currentGroup(EnemyC.enemyCList):
                            if i.shape == e:
                                self.shape.centerX -= i.enemyCheck(times + 1) * self.speed
                                return times - 1
            if self.right.hitsShape(character.left):
                self.shape.centerX -= self.speed
                if hitCheck(enemyGroupList, self.left):
                    e = currentGroup(enemyGroupList).hitTest(self.shape.left + 1, self.shape.centerY)
                    if e != self.shape and e != None:
                        if e.opacity != 0:
                            for i in currentGroup(EnemyC.enemyCList):
                                if i.shape == e:
                                    i.enemyCheck(2)
                                    return times - 1
        if self.moveY == 0:
            if hitCheck(enemyGroupList, self.bottom):
                e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.bottom - 1)
                if e != self.shape and e != None:
                    if e.opacity != 0:
                        for i in currentGroup(EnemyC.enemyCList):
                            if i.shape == e:
                                self.shape.centerY += i.enemyCheck(times + 1) * self.speed
                                return times - 1
            if self.bottom.hitsShape(character.top):
                self.shape.centerY += self.speed
                if hitCheck(enemyGroupList, self.top):
                    e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.top + 1)
                    if e != self.shape and e != None:
                        if e.opacity != 0:
                            for i in currentGroup(EnemyC.enemyCList):
                                if i.shape == e:
                                    i.enemyCheck(2)
                                    return times - 1
        elif self.moveY == 1:
            if hitCheck(enemyGroupList, self.top):
                e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.top + 1)
                if e != self.shape and e != None:
                    if e.opacity != 0:
                        for i in currentGroup(EnemyC.enemyCList):
                            if i.shape == e:
                                self.shape.centerY -= i.enemyCheck(times + 1) * self.speed
                                return times - 1
            if self.top.hitsShape(character.bottom):
                self.shape.centerY -= self.speed
                if hitCheck(enemyGroupList, self.bottom):
                    e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.bottom - 1)
                    if e != self.shape and e != None:
                        if e.opacity != 0:
                            for i in currentGroup(EnemyC.enemyCList):
                                if i.shape == e:
                                    i.enemyCheck(2)
                                    return times - 1
        return times
    def move(self):
        if self.health > 0:
            if self.invTime <= 0:
                if (
                    (self.shape.centerX + self.shape.width / 2) >= character.shape.centerX and 
                    character.shape.centerX >= (self.shape.centerX - self.shape.width / 2) and 
                    distance(character.shape.centerX, character.shape.centerY, self.shape.centerX, self.shape.centerY) <= self.range and
                    self.moveY == 3 and self.moveX == 3 
                ):
                    if character.shape.centerY > self.shape.centerY:
                        self.moveY = 0
                    elif character.shape.centerY < self.shape.centerY:
                        self.moveY = 1
                if (
                    (self.shape.centerY + self.shape.height / 2) >= character.shape.centerY and 
                    character.shape.centerY >= (self.shape.centerY - self.shape.height / 2) and 
                    distance(character.shape.centerX, character.shape.centerY, self.shape.centerX, self.shape.centerY) <= self.range and
                    self.moveX == 3 and self.moveY == 3
                ):
                    if character.shape.centerX > self.shape.centerX:
                        self.moveX = 0
                    elif character.shape.centerX < self.shape.centerX:
                        self.moveX = 1
                if self.moveY == 0:
                    if hitCheckAllOr(self.bottom) or hitCheck(groundGroupList, self.bottom):
                        self.moveY = 3
                    if self.moveY != 3:
                        self.shape.centerY += self.speed
                elif self.moveY == 1:
                    self.shape.centerY -= self.speed
                    if hitCheckAllOr(self.top) or hitCheck(groundGroupList, self.top):
                        self.shape.centerY += self.speed
                        self.moveY = 3
                if self.moveX == 0:
                    if hitCheckAllOr(self.right) or hitCheck(groundGroupList, self.right):
                        self.moveX = 3
                    if self.moveX != 3:
                        self.shape.centerX += self.speed
                elif self.moveX == 1:
                    self.shape.centerX -= self.speed
                    if hitCheckAllOr(self.left) or hitCheck(groundGroupList, self.left):
                        self.shape.centerX += self.speed
                        self.moveX = 3
                if self.shape.hitsShape(shield.shape):
                    if shield.visible:
                        shield.health -= self.damage
                        if shield.shape.centerY < i.centerY:
                            self.shape.centerY += self.speed
                        else:
                            self.shape.centerY -= self.speed
                        if shield.shape.centerX > self.shape.centerX:
                            self.shape.centerX -= self.speed
                        else:
                            self.shape.centerX += self.speed
                        self.health -= shield.damage
                        self.invTime = self.maxInv
                else:
                    self.damageCheck()
                    if self.shape.hitsShape(character.shape):
                        if character.invTime <= 0:
                            character.invTime = 45
                            character.hp -= self.damage
                        if self.moveY == 0:
                            character.shape.centerY += self.speed * 2
                        elif self.moveY == 1:
                            character.shape.centerY -= self.speed * 2
                        if self.moveX == 0:
                            character.shape.centerX += self.speed * 2
                        elif self.moveX == 1:
                            character.shape.centerX -= self.speed * 2
                        self.moveY = 3
                        self.moveX = 3
                        if character.shape.centerX > self.shape.centerX:
                            if not hitCheckAllOr(character.right):
                                character.shape.centerX += self.speed
                            else:
                                self.enemyCheck(1)
                        elif character.shape.centerX < self.shape.centerX:
                            if not hitCheckAllOr(character.left):
                                character.shape.centerX -= self.speed
                            else:
                                self.enemyCheck(1)
                    elif hitCheck(enemyGroupList, self.shape):
                        if hitCheck(enemyGroupList, self.left):
                            e = currentGroup(enemyGroupList).hitTest(self.shape.left + 1, self.shape.centerY)
                            if e != self.shape and e != None:
                                if e.opacity != 0:
                                    self.enemyCheck(1)
                        elif hitCheck(enemyGroupList, self.right):
                            e = currentGroup(enemyGroupList).hitTest(self.shape.right - 1, self.shape.centerY)
                            if e != self.shape and e != None:
                                if e.opacity != 0:
                                    self.enemyCheck(1)
                        elif hitCheck(enemyGroupList, self.top):
                            e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.top + 1)
                            if e != self.shape and e != None:
                                if e.opacity != 0:
                                    self.enemyCheck(1)
                        elif hitCheck(enemyGroupList, self.bottom):
                            e = currentGroup(enemyGroupList).hitTest(self.shape.centerX, self.shape.bottom - 1)
                            if e != self.shape and e != None:
                                if e.opacity != 0:
                                    self.enemyCheck(1)
                if app.level == 12:
                    groupShapes(self.shape, self.light, 0, 0)
        else:
            self.shape.opacity = 0
            if self.level == 12:
                self.light.visible = False