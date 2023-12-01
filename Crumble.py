from cmu_graphics import *
from ClassFunctions import *
from Character import *
from Sword import *
class Crumble:
    crumbleList = []
    def __init__(self, x1, y1, x2, y2, lW, level, room, group, *, Opacity = 100, Fill = 'black', cooldown = 0, maxCooldown = 100):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = Fill, opacity = Opacity)
        self.maxOpacity = Opacity
        self.maxCooldown = maxCooldown
        self.cooldown = cooldown
        self.initCooldown = cooldown
        objctSet(self, level, room, group)
        Crumble.crumbleList[level - 1][room].append(self)
    def crumble(self):
        if self.shape.opacity > 0 and self.cooldown <= 0:
            self.shape.visible = True
            if self.shape.hitsShape(character.shape):
                a = 2
                if self.shape.opacity-a < 0:
                    a = 1
                self.shape.opacity -= a
            elif self.shape.hitsShape(sword.shape) and sword.shape.visible:
                a = sword.damage
                if self.shape.opacity - a < 0:
                    self.shape.opacity = 0
                else:
                    self.shape.opacity -= a
            elif not self.shape.hitsShape(character.shape):
                if self.shape.opacity < self.maxOpacity:
                    self.shape.opacity += 1
        elif self.shape.opacity <= 0:
            self.cooldown = self.maxCooldown
            self.shape.visible = False
        if self.cooldown > 0:
            self.cooldown -= 1
            self.shape.opacity += 1
    def reset(self):
        if self.level == app.level and self.room == app.room:
            self.shape.visible = True
            self.shape.opacity = self.maxOpacity
            self.cooldown = self.initCooldown