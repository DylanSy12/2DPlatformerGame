from cmu_graphics import *
from ClassFunctions import *
from Character import *
from LevelLists import *
from Fireball import *
from Sword import *
from Shield import *
from BreakWall import *
from Missile import *
class LineCannon:
    lineCannonList = []
    def __init__(
        self, cX, cY, health, damage, speed, cooldown, missileLife, level, room, group, *, 
        maxInv = 45, size = 6, startingCooldown = 0, angle = 0, missileW = 10, missileL = 20
    ):
        self.shape = Circle(cX, cY, size, fill = 'yellow', rotateAngle = angle)
        self.cX = cX
        self.cY = cY
        self.health = health
        self.maxHealth = health
        self.speed = speed
        self.damage = damage
        self.invTime = 0
        self.missileW = missileW / 2
        self.missileL = missileL / 2
        self.cooldown = startingCooldown
        self.maxCooldown = cooldown
        self.missileLife = missileLife
        self.maxInv = maxInv
        LineCannon.lineCannonList[level - 1][room].append(self)
        objctSet(self, level, room, group)
    def shoot(self):
        self.damageCheck()
        if self.health > 0:
            if self.invTime <= 0:
                if self.cooldown <= 0:
                    halfLength = self.missileL / 2
                    Missile(
                        self.shape.centerX, self.shape.centerY - halfLength, 
                        self.shape.centerX, self.shape.centerY + halfLength,
                        self.missileLife, self.damage, self.speed, 
                        self.shape.rotateAngle, self.missileW
                    )
                    self.cooldown = self.maxCooldown
                else:
                    self.cooldown -= 1
        else:
            self.shape.visible = False
    def damageCheck(self):
        if self.shape.hitsShape(sword.shape) and sword.shape.visible:
            self.health -= sword.damage
            self.invTime = self.maxInv
        elif self.shape.hitsShape(shield.shape) and shield.shape.visible:
            self.health -= shield.damage
            self.invTime = self.maxInv
            shield.health -= self.damage
        else:
            for i in Fireball.fireballList:
                if i.shape.hitsShape(self.shape):
                    self.health -= i.damage
                    self.invTime = self.maxInv
                    i.life -= 2*i.damage
                    return
    def invFrames(self):
        self.invTime -= 1
        if self.invTime % 2 == 0 and self.invTime != 0:
            self.shape.opacity = 50
        else:
            self.shape.opacity = 100
    def reset(self):
        if self.room == app.room and self.level == app.level:
            self.health = self.maxHealth
            self.invTime = 0
            self.shape.visible = True
            self.shape.opacity = 100