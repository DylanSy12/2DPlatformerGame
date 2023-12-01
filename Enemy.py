from cmu_graphics import *
from Fireball import *
from Sword import *
from Shield import *
from ClassFunctions import *
from Character import *
class Enemy:
    enemyList = []
    def __init__(self, cX, y1, y2, lW, health, speed, damage, level, room, group, maxInv, knockbackResist):
        self.box = Line(cX, y1, cX, y2, lineWidth = lW, fill = 'yellow')
        self.left = Line(cX + 1 - (lW / 2), y1 + 1, cX + 1 - (lW / 2), y2 - 1, lineWidth = 2, fill = 'yellow')
        self.right = Line(cX - 1 + (lW / 2), y1 + 1, cX - 1 + (lW / 2), y2 - 1, lineWidth = 2, fill = 'yellow')
        self.top = Line(cX + 1 - (lW / 2), y1 + 1, cX - 1 + (lW / 2), y1 + 1, lineWidth = 2, fill = 'yellow')
        self.bottom = Line(cX + 1 - (lW / 2), y2 - 1, cX - 1 + (lW / 2), y2 - 1, lineWidth = 2, fill = 'yellow')
        self.shape = Group(self.left, self.right, self.top, self.bottom, self.box)
        if level == 12:
            self.light = Oval(cX, self.shape.centerY, self.shape.width + 20, self.shape.height + 20, fill = gradient('white', 'ghostwhite', 'whitesmoke'), opacity = 25)
            group.add(self.light)
        self.knockbackResist = knockbackResist
        self.health = health
        self.maxHealth = health
        self.speed = speed
        self.invTime = 0
        self.maxInv = maxInv
        self.damage = damage
        self.sX = self.shape.centerX
        self.sY = self.shape.centerY
        objctSet(self, level, room, group)
        Enemy.enemyList[level - 1][room].append(self)
    def damageCheck(self):
        if self.shape.hitsShape(character.shape) and character.invTime <= 0:
            character.invTime = character.maxInv
            character.hp -= self.damage
        elif self.shape.hitsShape(sword.shape) and sword.shape.visible:
            self.health -= sword.damage
            self.invTime = self.maxInv
        else:
            for i in Fireball.fireballList:
                if self.shape.hitsShape(i.shape):
                    self.health -= i.damage
                    self.invTime = self.maxInv
                    i.life -= i.damage * 2
                    break
    def reset(self):
        if self.room == app.room and self.level == app.level:
            if self.level == 12:
                self.light.visible = True
            self.shape.centerX = self.sX
            self.shape.centerY = self.sY
            self.health = self.maxHealth
            self.invTime = 0
            self.shape.opacity = 100