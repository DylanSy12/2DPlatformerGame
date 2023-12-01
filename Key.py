from cmu_graphics import *
from Item import Item
class Key(Item):
    keyList = []
    keyLabel = Label("Keys: " + str(app.keys), 230, 410, size = 12, fill = 'darkgoldenrod', border = 'black', borderWidth = 0.1)
    def __init__(self, cX, cY, level, room, group):
        self.shape = RegularPolygon(cX, cY, 3, 4, fill = gradient('gold', 'goldenrod'))
        super().__init__(cX, cY, level, room, group)
        Key.keyList[level - 1][room].append(self)
    def effect(self):
        app.keys += 1
        Key.keyLabel.value = "Keys: " + str(app.keys)