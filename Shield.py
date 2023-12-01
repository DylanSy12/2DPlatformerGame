from cmu_graphics import *
from Character import *
class Shield:
    def __init__(self):
        self.damage = 1
        self.health = 12
        self.maxHealth = 12
        self.cooldownTime = 0
        self.maxCooldown = 120
        self.time = 90
        self.maxTime = 90
        self.pushMulti = 4
        self.shape = RegularPolygon(0, 0, 12.5, 8, fill = gradient('lightcyan', 'paleturquoise', 'cyan', 'turquoise', 'darkturquoise'), opacity = 25, visible = False)
        self.powerDict = {
            "Damage": self.damage,
            "Health": self.maxHealth,
            "Time": self.maxTime,
            "Cooldown": self.maxCooldown,
            "Radius": self.shape.radius,
            "Push": self.pushMulti
        }
    def use(self):
        if self.cooldownTime <= 0:
            self.shape.centerX = character.shape.centerX
            self.shape.centerY = character.shape.centerY
            self.shape.visible = True
            self.time -= 1
            self.shape.opacity = (25 / self.maxTime) * self.time
            if self.health == self.maxHealth:
                self.shape.border = 'blue'
            elif self.health >= (self.maxHealth / 3) * 2:
                self.shape.border = 'mediumSlateBlue'
            elif self.health >= (self.maxHealth / 3):
                self.shape.border = 'lightSkyBlue'
            else:
                self.shape.border = 'aliceBlue'
            if self.time <= 0 or self.health <= 0:
                self.cooldownTime = 120
                self.shape.visible = False
    def cooldown(self):
        if app.reset == True:
            shield.cooldownTime = 0
            shield.health = shield.maxHealth
            shield.time = shield.maxTime
            app.reset = False
        elif self.cooldownTime > 0:
            self.cooldownTime -= 1
            if self.cooldownTime <= 0:
                self.health = self.maxHealth
                self.time = self.maxTime
    def damageUp(self, amount):
        self.damage += amount
    def healthUp(self, amount):
        self.maxHealth += amount
        self.health = self.maxHealth
    def timeUp(self, amount):
        self.maxTime += amount
        self.time = self.maxTime
    def cooldownDown(self, amount):
        self.maxCooldown -= amount
        self.cooldownTime = 0
    def sizeUp(self, amount):
        self.shape.radius += amount
    def pushUp(self, amount):
        self.pushMulti += amount
    def upgrade(self, amount, power):
        self.powerDict[power] += amount
        if power == "Health":
            self.health = self.maxHealth
        elif power == "Time":
            self.time = self.maxTime
        elif power == "Cooldown":
            self.cooldownTime = 0
shield = Shield()