from cmu_graphics import *
from Character import *
from LevelLists import *
from ClassFunctions import *
class Fireball:
    fireballList = []
    cost = 4
    lightRange = 25
    brightness = 25
    speed = 2
    life = 45
    damage = 4
    size = 5
    powerDict = {
        "Cost": cost,
        "Light Range": lightRange,
        "Brightness": brightness,
        "Speed": speed,
        "Life": life,
        "Damage": damage,
        "Size": size
    }
    def __init__(self, cX, cY, direction):
        self.shape = Circle(cX, cY, Fireball.size, fill = gradient('orange', 'darkorange', 'orangered', 'red', 'crimson'))
        if app.level == 12:
            self.light = Circle(cX, cY, Fireball.lightRange, fill = gradient('white', 'ghostwhite', 'whitesmoke'), opacity = Fireball.brightness)
        self.damage = Fireball.damage
        self.life = Fireball.life
        self.speed = Fireball.speed
        self.direction = direction
    def cast(self):
        if character.mp - Fireball.cost >= 0:
            Fireball.fireballList.append(Fireball(character.shape.centerX, character.shape.centerY, character.direction))
            character.mp -= Fireball.cost
    def travel(self):
        if self.direction == "r":
            self.shape.centerX += self.speed
        elif self.direction == "l":
            self.shape.centerX -= self.speed
        if app.level == 12:
            groupShapes(self.shape, self.light, 0, 0)
        self.life -= 1
        if self.life <= 0:
            Fireball.fireballList.remove(self)
            self.shape.visible = False
            if app.level == 12:
                self.light.visible = False
        elif (
            currentGroup(groundGroupList).hitTest(self.shape.centerX, self.shape.centerY) or 
            currentGroup(obstacleGroupList).hitTest(self.shape.centerX, self.shape.centerY) or 
            currentGroup(keyDoorGroupList).hitTest(self.shape.centerX, self.shape.centerY)
        ):
            self.life = 0
    def lifeUp(self, amount):
        Fireball.life += amount
    def sizeUp(self, amount):
        Fireball.size += amount
    def damageUp(self, amount):
        Fireball.damage += amount
    def speedUp(self, amount):
        Fireball.speed += amount
    def costDown(self, amount):
        Fireball.cost -= amount
    def lightUp(self, amount):
        Fireball.lightRange += amount
    def upgrade(self, amount, power):
        Fireball.powerDict[power] += amount
fireball = Fireball(character.shape.centerX, character.shape.centerY, character.direction)
fireball.shape.visible = False