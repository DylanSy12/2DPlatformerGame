from cmu_graphics import *
from ClassFunctions import *
from Character import *
class Coin:
    coinList = []
    score = Label("Score: " + str(app.score), 175, 410, size = 12,fill = 'limegreen', border = 'black', borderWidth = 0.1)
    def __init__(self, cX, cY, amount, level, room, group):
        if level <= 6:
            self.shape = Circle(cX, cY, 6, fill = gradient('red', 'orange', 'yellow'))
        else:
            if amount == 1:
                self.shape=Circle(cX, cY, 2.5, fill = gradient('red', 'orange', 'yellow'))
            elif amount == 50:
                self.shape = Circle(cX, cY, 25, fill = gradient('red', 'orange', 'yellow'))
            elif amount == 5:
                self.shape = Circle(cX, cY, 5, fill = gradient('red', 'orange', 'yellow'))
            elif amount == 10:
                self.shape = Circle(cX, cY, 10, fill = gradient('red', 'orange', 'yellow'))
            elif amount == 25:
                self.shape = Circle(cX, cY, 15, fill = gradient('red', 'orange', 'yellow'))
        self.amount = amount
        objctSet(self, level, room, group)
        Coin.coinList[level - 1][room].append(self)
    def getCoin(self):
        if self.shape.hitsShape(character.shape) and self.shape.visible:
            self.shape.visible = False
            app.score += self.amount