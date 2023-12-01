from cmu_graphics import *
from LevelLists import *
from ClassFunctions import *
class Character:
    def __init__(self, cX, cY, *, Fill = 'red'):
        self.box = Line(cX, cY - 10, cX, cY + 10, fill = Fill, lineWidth = 10)
        self.left = Line(cX - 4, cY - 9, cX - 4, cY + 9)
        self.right = Line(cX + 4, cY - 9, cX + 4, cY + 9)
        self.top = Line(cX - 4, cY - 9, cX + 4, cY - 9)
        self.bottom = Line(cX - 4, cY + 9, cX + 4, cY + 9)
        self.light = Oval(-100, -100, 50, 55, opacity = 20, fill = gradient('white', 'ghostwhite', 'whitesmoke'))
        self.shape = Group(self.left, self.right, self.top, self.bottom, self.box)
        self.shape.fill = Fill
        self.hp = 5
        self.maxHP = 5
        self.hpRegenTime = 195
        self.hpRegenSpeed = 195
        self.hpRegenAmount = 0
        self.mp = 5
        self.maxMP = 5
        self.mpRegenTime = 180
        self.mpRegenSpeed = 180
        self.mpRegenAmount = 1
        self.invTime = 0
        self.maxInv = 45
        self.spawnX = cX
        self.spawnY = cY
        self.deaths = 0
        self.jump = 21
        self.maxJump = 20
        self.wallJumped = False
        self.groundJumped = True
        self.bounceRight = 0
        self.bounceLeft = 0
        self.bounceUp = 0
        self.weapon = "Sword"
        self.direction = "r"
    def moveRight(self):
        self.direction = "r"
        if not hitCheck(waterGroupList, self.shape):
            if not hitCheckAllOr(self.right):
                if app.level <= 6:
                    self.shape.centerX += 5
                else:
                    self.shape.centerX = (rounded(self.shape.centerX / 2.5) * 2.5) + 2.5
        else:
            for i in range(3):
                if not hitCheckAllOr(self.right):
                    self.shape.centerX += 0.5
    def moveLeft(self):
        self.direction = "l"
        if not hitCheck(waterGroupList, self.shape):
            if not hitCheckAllOr(self.left):
                if app.level <= 6:
                    self.shape.centerX -= 5
                else:
                    self.shape.centerX = (rounded(self.shape.centerX / 2.5) * 2.5) - 2.5
        else:
            for i in range(3):
                if not hitCheckAllOr(self.left):
                    self.shape.centerX -= 0.5
    def jumpSet(self):
        if not hitCheck(waterGroupList, self.shape):
            if hitCheckAllOr(self.bottom) or hitCheck(groundGroupList, self.bottom) or self.bounceUp > 0: 
                if not hitCheckAllOr(self.top):
                    self.jump = 0
                    self.moveUp()
                else:
                    self.bounceUp = 0
            elif hitCheckAllOr(self.left) or hitCheckAllOr(self.right):
                if self.groundJumped:
                    self.jump = 0
                    self.moveUp()
                    self.groundJumped = False
                    self.wallJumped = True
        else:
            for i in range(7):
                if not hitCheckAllOr(self.top):
                    self.shape.centerY -= 0.5
                    if not hitCheck(waterGroupList, self.bottom):
                        self.jump = 0
    def moveUp(self):
        if not hitCheck(waterGroupList, self.shape):
            if not hitCheckAllOr(self.left) and not hitCheckAllOr(self.right):
                self.wallJumped = False
                self.groundJumped = True
            else:
                if not self.wallJumped:
                    self.jump += 1
            if self.jump <= self.maxJump:
                if app.level <= 6:
                    self.shape.centerY = (rounded(self.shape.centerY / 5) * 5) - 5
                else:
                    self.shape.centerY = (rounded(self.shape.centerY / 2.5) * 2.5) - 2.5
                self.jump += 1
                if hitCheckAllOr(self.top):
                    self.jump = self.maxJump + 1
    def gravity(self):
        if not hitCheckAllOr(self.left) and not hitCheckAllOr(self.right) and not hitCheckAllOr(self.bottom) and not hitCheck(groundGroupList, self.bottom):
            if hitCheck(waterGroupList, self.shape):
                self.shape.centerY += 0.25
            else:
                if app.level <= 6:
                    self.shape.centerY = (rounded(self.shape.centerY / 5) * 5) + 5
                else:
                    self.shape.centerY = (rounded(self.shape.centerY / 2.5) * 2.5) + 2.5
                    # self.shape.centerY = self.shape.centerY + 2.5
                self.jump = self.maxJump + 1
                self.wallJumped = False
                self.groundJumped = True
        elif hitCheckAllOr(self.bottom) or hitCheck(groundGroupList, self.bottom): 
            self.groundJumped = True
            self.wallJumped = False
        elif hitCheckAllOr(self.right) or hitCheckAllOr(self.left):
            if app.level <= 6:
                self.shape.centerY += 2
            else:
                if hitCheck(waterGroupList, self.shape):
                    self.shape.centerY = (rounded(self.shape.centerY / 0.25) * 0.25) + 0.25
                else:
                    self.shape.centerY += 1
    def spawnSet(self, x, y):
        app.level += 1
        app.keys = 0
        app.score += 10
        app.levelSpawnX = x
        app.levelSpawnY = y
        self.shape.centerX = x
        self.shape.centerY = y
        self.spawnX = x
        self.spawnY = y
    def respawn(self):
        self.deaths += 1
        app.score -= self.deaths
        self.hp = self.maxHP
        self.mp = self.maxMP
        self.invTime = 45
        self.jump = self.maxJump + 1
        self.wallJumped = False
        self.groundJumped = True
        self.shape.centerX = self.spawnX
        self.shape.centerY = self.spawnY
        self.bounceUp = 0
        self.bounceRight = 0
        self.bounceLeft = 0
        app.respawn = True
        self.mpRegenTime = self.mpRegenSpeed
        self.hpRegenTime = self.hpRegenSpeed
        for objct in app.resetableList:
            for dct in objct:
                for room in roomList:
                    for i in dct[room]:
                        i.reset()
    def levelReset(self):
        self.spawnX = app.levelSpawnX
        self.spawnY = app.levelSpawnY
        self.respawn()
    def bounce(self):
        if self.bounceRight > 0:
            self.bounceRight -= 1
            self.moveRight()
        elif self.bounceLeft > 0:
            self.bounceLeft -= 1
            self.moveLeft()
        if self.bounceUp > 0:
            self.bounceUp -= 1
            self.jumpSet()
    def mpRegen(self):
        if self.mp < self.maxMP:
            self.mpRegenTime -= 1
            if self.mpRegenTime <= 0:
                self.mpRegenTime = self.mpRegenSpeed
                self.mp += self.mpRegenAmount
                if self.mp > self.maxMP:
                    self.mp = self.maxMP
    def hpRegen(self):
        if self.hp < self.maxHP:
            if self.hpRegenAmount > 0:
                self.hpRegenTime -= 1
                if self.hpRegenTime <= 0:
                    self.hpRegenTime = self.hpRegenSpeed
                    self.hp += self.hpRegenAmount
                    if self.hp > self.maxHP:
                        self.hp = self.maxHP
                    self.invTime = 10
    def mpRegenTimeDown(self, amount):
        self.mpRegenSpeed -= amount
    def hpRegenTimeDown(self, amount):
        self.hpRegenSpeed -= amount
    def mpRegenAmountUp(self, amount):
        self.mpRegenAmount += amount
    def hpRegenAmountUp(self, amount):
        self.hpRegenAmount += amount
    def maxMPUp(self, amount):
        self.maxMP += amount
        self.mp = self.maxMP
    def maxHPUp(self, amount):
        self.maxHP += amount
        self.hp = self.maxHP
    def mpRestore(self, amount):
        self.mp += amount
        if self.mp > self.maxMP:
            self.mp = self.maxMP
    def hpRestore(self, amount):
        self.hp += amount
        if self.hp > self.maxHP:
            self.hp = self.maxHP
    def invTimeUp(self, amount):
        self.maxInv += amount
        self.invTime = self.maxInv
    def maxJumpUp(self, amount):
        self.maxJump += amount
character = Character(20, 370)