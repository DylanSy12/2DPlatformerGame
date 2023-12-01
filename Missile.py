from cmu_graphics import *
from ClassFunctions import *
from Character import *
from LevelLists import *
from Fireball import *
from Sword import *
from Shield import *
from BreakWall import *
from ClassFunctions import *
class Missile:
    missileList = []
    def __init__(self, x1, y1, x2, y2, life, damage, speed, angle, LineWidth, *, Fill = 'yellow'):
        self.shape = Line(x1, y1, x2, y2, lineWidth = LineWidth, fill = Fill, rotateAngle = angle)
        self.life = life
        self.damage = damage
        self.speed = speed
        Missile.missileList.append(self)
    def kill(self):
        self.shape.visible = False
        Missile.missileList.remove(self)
    def shoot(self):
        if self.life > 0:
            self.shape.centerX, self.shape.centerY = getPointInDir(self.shape.centerX, self.shape.centerY, self.shape.rotateAngle, self.speed)
            if hitCheck(breakWallGroupList, self.shape):
                for i in currentGroup(BreakWall.breakWallList):
                    if i.shape.hitsShape(self.shape):
                        i.health -= self.damage
                        self.kill()
            elif self.shape.hitsShape(character.shape):
                if character.invTime <= 0:
                    character.invTime = character.maxInv
                    character.hp -= self.damage
                self.kill()
            elif self.shape.hitsShape(sword.shape):
                if sword.shape.visible:
                    self.kill()
            elif self.shape.hitsShape(shield.shape):
                if shield.shape.visible:
                    shield.health -= self.damage
                    self.kill()
            else:
                for i in Fireball.fireballList:
                    if self.shape.hitsShape(i.shape):
                        self.kill()
            self.life -= 1
        else:
            self.kill()