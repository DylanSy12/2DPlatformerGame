from cmu_graphics import *
from ClassFunctions import *
from Character import *
from LevelLists import *
from Fireball import *
from Sword import *
from Shield import *
from BreakWall import *
class TrackMissile:
    trackMissileList = []
    def __init__(self, cX, cY, rng, health, damage, speed, level, room, group, *, maxInv = 45, size = 6):
        self.cannon = Circle(cX, cY, size, fill = 'yellow')
        self.range = Circle(cX, cY, rng, fill = 'yellow', opacity = 5)
        self.missileTop = Line(cX - 2, cY - 4, cX + 2, cY - 4, fill = None, lineWidth = 2)
        self.missileBox = Line(cX, cY - 5, cX, cY + 5, fill = None, lineWidth = 5)
        self.missile = Group(self.missileTop, self.missileBox)
        self.shape = Group(self.cannon, self.range)
        self.cX = cX
        self.cY = cY
        self.health = health
        self.maxHealth = health
        self.speed = speed
        self.damage = damage
        self.invTime = 0
        self.maxInv = maxInv
        TrackMissile.trackMissileList[level - 1][room].append(self)
        objctSet(self, level, room, group)
    def shoot(self):
        self.damageCheck()
        if self.health > 0:
            if self.shape.hitsShape(character.shape) and self.missile.fill == None and self.invTime <= 0:
                self.missile.fill = 'yellow'
                self.missile.centerX = self.cannon.centerX
                self.missile.centerY = self.cannon.centerY
                self.missile.rotateAngle = angleTo(self.missile.centerX, self.missile.centerY, character.shape.centerX, character.shape.centerY)
            elif self.missile.fill == 'yellow':
                self.missile.rotateAngle = angleTo(self.missile.centerX, self.missile.centerY, character.shape.centerX, character.shape.centerY)
                self.missile.centerX, self.missile.centerY = getPointInDir(self.missile.centerX, self.missile.centerY, self.missile.rotateAngle, self.speed)
                if hitCheck(breakWallGroupList, self.missileTop):
                    for i in currentGroup(BreakWall.breakWallList):
                        if i.shape.hitsShape(self.missile):
                            i.health -= self.damage
                            self.missile.fill = None
                elif hitCheck(obstacleGroupList, self.missileTop) or hitCheck(groundGroupList, self.missileTop) or hitCheck(keyDoorGroupList, self.missileTop):
                    self.missile.fill = None
                elif self.missile.hitsShape(sword.shape) and sword.shape.visible:
                    self.missile.fill = None
                elif self.missile.hitsShape(shield.shape) and shield.shape.visible:
                    shield.health -= self.damage
                    self.missile.fill = None
                else:
                    for i in Fireball.fireballList:
                        if i.shape.hitsShape(self.missile):
                            self.missile.fill = None
                            i.life -= i.damage
                            return
                    if self.missile.hitsShape(character.shape):
                        self.missile.fill = None
                        if character.invTime <= 0:
                            character.hp -= self.damage
                            character.invTime = character.maxInv
        else:
            self.missile.fill = None
            self.shape.visible = False
    def damageCheck(self):
        if self.cannon.hitsShape(sword.shape) and self.invTime <= 0:
            if sword.shape.visible:
                self.health -= sword.damage
                self.invTime = self.maxInv
        elif self.cannon.hitsShape(shield.shape) and self.invTime <= 0:
            if shield.shape.visible:
                self.health -= shield.damage
                self.invTime = self.maxInv
                shield.health -= self.damage
        else:
            for i in Fireball.fireballList:
                if i.shape.hitsShape(self.cannon) and self.invTime <= 0:
                    self.health -= i.damage
                    self.invTime = self.maxInv
                    i.life -= 2 * i.damage
    def invFrames(self):
        self.invTime -= 1
        if self.invTime % 2 == 0 and self.invTime != 0:
            self.cannon.opacity = 50
        else:
            self.cannon.opacity = 100
    def reset(self):
        if self.room == app.room and self.level == app.level:
            self.health = self.maxHealth
            self.invTime = 0
            self.shape.visible = True
            self.cannon.opacity = 100