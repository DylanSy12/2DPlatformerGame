from cmu_graphics import *
from Character import *
class Sword:
    def __init__(self):
        self.damage = 2
        self.shape = Line(0, 0, 7.5, 0, fill = gradient('lightGray', 'silver', start = 'right'), visible = False)
        self.width = 7.5
        self.direction = "r"
        self.time = 0
        self.goOut = True
        self.speed = 0.25
        self.powerDict = {
            "Width": self.width,
            "Damage": self.damage,
            "Speed": self.speed
        }
    def damageUp(self, amount):
        self.damage += amount
    def widthUp(self, amount):
        self.width += amount
        self.shape.x2 = self.shape.x1 + self.width
    def speedUp(self, amount):
        self.speed += amount
    def upgrade(self, amount, power):
        self.powerDict[power] += amount
        if power == "Width":
            self.shape.x2 = self.shape.x1 + self.width
    def swing(self):
        self.time = 1
        self.goOut = True
    def use(self):
        if character.weapon == "Sword":
            if self.time>0:
                self.shape.visible = True
                self.shape.centerY = character.shape.centerY
                if character.direction == "r":
                    self.shape.left = character.shape.centerX + (self.speed * self.time)
                    if self.shape.left >= character.shape.right:
                        self.goOut = False
                else:
                    self.shape.right = character.shape.centerX - (self.speed * self.time)
                    if self.shape.right <= character.shape.left:
                        self.gpOut = False
                if self.goOut:
                    self.time += 1
                else:
                    self.time -= 1
            else:
                self.shape.visible = False
sword = Sword()