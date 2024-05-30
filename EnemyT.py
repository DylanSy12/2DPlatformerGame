from tkinter import W
from cmu_graphics import *
from Enemy import *
from EnemyX import *
from LevelLists import *
from BreakWall import *
from Shield import *
class EnemyT(Enemy):
    enemyTList = []
    def __init__(self, cX, y1, y2, lW, health, speed, damage, grounded, level, room, group, *, maxInv = 45, knockbackResist = 0, boss = False):
        self.grounded = grounded
        self.boss = boss
        self.direction = 0
        self.enemyChecking = True
        super().__init__(cX, y1, y2, lW, health, speed, damage, level, room, group, maxInv, knockbackResist)
        EnemyT.enemyTList[level - 1][room].append(self)
    def enemyCollisionCheck(self, e):
        if e != self.shape and e != None:
            if e.opacity != 0:
                return True
        return False
    def enemyCheck(self, pushBack, pushDirection, pushingEnemy, startEnemy, *, times = 1, enemiesHit = set()):
        enemiesHit.add(self)
        #for e in enemiesHit:
        #    print(e)
        if startEnemy == self and times != 1:
            self.shape.centerX = rounded(self.shape.centerX/2.5)*2.5
            return
        a = 0
        while pushingEnemy.shape.right > self.shape.right > pushingEnemy.shape.left or pushingEnemy.shape.left < self.shape.left < pushingEnemy.shape.right:
            self.shape.centerX += pushBack * pushDirection
            self.shape.centerX = rounded(self.shape.centerX/2.5)*2.5
            a += 1
        if (
            (self.grounded and (not hitCheckAllOr(self.bottom)) and (not hitCheck(groundGroupList, self.bottom))) or
            (pushDirection == 1 and hitCheckAllOr(self.right)) or
            (pushDirection == -1 and hitCheckAllOr(self.left))
        ):
            self.shape.centerX -= pushBack * pushDirection
            self.shape.centerX = rounded(self.shape.centerX/2.5)*2.5
            if ((pushDirection == 1 and hitCheck(enemyGroupList, self.left)) or (pushDirection == -1 and hitCheck(enemyGroupList, self.right))):
                if pushDirection == -1:
                    e = hitFindNotObject(Enemy.enemyList, self, self.right)
                else:
                    e = hitFindNotObject(Enemy.enemyList, self, self.left)
                if e != None:
                    e.enemyCheck(pushBack, -pushDirection, self, self, times = times+1, enemiesHit = enemiesHit)
        elif ((pushDirection == 1 and hitCheck(enemyGroupList, self.right)) or (pushDirection == -1 and hitCheck(enemyGroupList, self.left))):
            if pushDirection == 1:
                e = hitFindNotObject(Enemy.enemyList, self, self.right)
            else:
                e = hitFindNotObject(Enemy.enemyList, self, self.left)
            if e != None:
                e.enemyCheck(pushBack, pushDirection, self, startEnemy, times = times+1, enemiesHit = enemiesHit)
    def move(self):
        if self.health > 0:
            if self.invTime <= 0:
                if self.shape.centerX < character.shape.centerX:
                    self.direction = 1
                elif self.shape.centerX > character.shape.centerX:
                    self.direction = -1
                else:
                    self.direction = 0
                self.shape.centerX += self.speed * self.direction
                if self.grounded:
                    if not hitCheckAllOr(self.bottom) and not hitCheck(groundGroupList, self.bottom):
                        self.shape.centerX -= self.speed * self.direction
                if (
                    (self.direction == 1 and hitCheckAllOr(self.right)) or 
                    (self.direction == -1 and hitCheckAllOr(self.left))
                ):
                    self.shape.centerX -= self.speed * self.direction
                if self.shape.hitsShape(shield.shape) and shield.shape.visible:
                    shield.health -= self.damage
                    self.invTime = self.maxInv
                    self.health -= shield.damage
                    self.shape.centerX -= (shield.pushMulti - self.knockbackResist) * self.speed * self.direction
                else:
                    self.damageCheck()
                    if self.shape.hitsShape(character.shape):
                        if ((self.direction == -1 and not hitCheckAllOr(character.left)) or (self.direction == 1 and not hitCheckAllOr(character.right))):
                            character.shape.centerX += self.speed * self.direction
                    e = hitFindNotObject(Enemy.enemyList, self, self.left)
                    if e != None:
                        e.enemyCheck(self.speed, -1, self, self)
                    e = hitFindNotObject(Enemy.enemyList, self, self.right)
                    if e != None:
                        e.enemyCheck(self.speed, 1, self, self)
            if app.level == 12:
                groupShapes(self.shape, self.light, 0, 0)
        else:
            self.shape.opacity = 0
            if self.level == 12:
                self.light.visible = False
        
                
                