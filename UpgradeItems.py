from cmu_graphics import *
from Item import *
from Character import *
from Sword import *
from Shield import *
from Fireball import *
class MaxHPUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 2.5, 6, fill = gradient('azure', 'lightCyan', 'aqua'))
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        character.maxHPUp(self.amount)
class SwordDamageUpItem(Item):
    def __init__(self, cX, top, amount, level, room, group):
        self.shape = Line(cX, top, cX, top+7.5, fill = gradient('yellow', 'lightGray', 'lightGray', 'lightGray', 'silver', 'silver', start = 'top'))
        self.amount = amount
        super().__init__(cX, self.shape.centerY, level, room, group)
    def effect(self):
        sword.damageUp(self.amount)
class SwordRangeUpItem(Item):
    def __init__(self, cX, top, amount, level, room, group):
        self.shape = Line(cX, top, cX, top+8.5, fill = gradient('red', 'lightGray', 'lightGray', 'lightGray', 'silver', 'silver', start = 'top'))
        self.amount = amount
        super().__init__(cX, self.shape.centerY, level, room, group)
    def effect(self):
        sword.widthUp(self.amount)
class ShieldDamageUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 2.5, 8, fill = gradient('red', 'lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise'), opacity = 50)
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.damageUp(self.amount)
class ShieldSizeUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 3.5, 8, fill = gradient('lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise', 'yellow'), opacity = 50)
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.sizeUp(self.amount)
class ShieldCooldownDownItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 2.5, 8, fill = gradient('lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise'), opacity = 25)
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.cooldownDown(self.amount)
class ShieldTimeUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 2.5, 8, fill = gradient('lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise'), opacity = 75)
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.timeUp(self.amount)
class ShieldHPUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = RegularPolygon(cX, cY, 2.5, 12, fill = gradient('lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise'), opacity = 50, border = 'blue')
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.healthUp(self.amount)
class ShieldPushUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = Group(
            RegularPolygon(cX, cY, 2, 8, fill = gradient(
                    'lightCyan', 'paleTurquoise', 'cyan', 'turquoise', 'darkTurquoise'
                ), 
                opacity = 50
            ),
            Circle(cX, cY, 3.5, fill = 'paleTurqoise', opacity = 10)
        )
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        shield.pushUp(self.amount)
class FireballDamageUpItem(Item):
    def __init__(self, cX, cY, amount, level, room, group):
        self.shape = Circle(cX, cY, 2.5, fill = gradient('red', 'orange', 'darkOrange', 'orangeRed', 'red', 'crimson'), opacity = 50)
        self.amount = amount
        super().__init__(cX, cY, level, room, group)
    def effect(self):
        fireball.damageUp(self.amount)