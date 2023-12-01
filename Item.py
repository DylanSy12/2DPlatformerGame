from cmu_graphics import *
from Character import *
from Sword import *
from Shield import *
from Fireball import *
from ClassFunctions import *
class Item:
    itemList = []
    def __init__(self, cX, cY, level, room, group):
        if level == 12:
            self.light = Circle(cX, cY, self.shape.width + 10, self.shape.height + 10, fill = gradient('white', 'ghostwhite', 'whitesmoke'), opacity = 20)
            group.add(self.light)
        objctSet(self, level, room, group)
        Item.itemList[level - 1][room].append(self)
    def reset(self):
        self.shape.visible = self.level == app.level and self.room == app.room
        if self.level == 12:
            self.light.visible = True
    def obtain(self):
        if self.shape.hitsShape(character.shape) and self.shape.visible:
            if self.level == 12:
                self.light.visible = False
            self.shape.visible = False
            self.effect()