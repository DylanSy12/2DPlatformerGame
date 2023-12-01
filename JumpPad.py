from cmu_graphics import *
from ClassFunctions import *
from Character import *
class JumpPad:
    jumpPadList = []
    def __init__(self, x1, y1, x2, y2, lW, strength, direction, level, room, group):
        self.shape = Line(x1, y1, x2, y2, lineWidth = lW, fill = 'green')
        self.strength = strength
        self.direction = direction
        objctSet(self, level, room, group)
        JumpPad.jumpPadList[level - 1][room].append(self)
    def bounce(self):
        if self.shape.hitsShape(character.shape):
            if self.direction == 'left':
                character.bounceLeft = self.strength
                character.bounceRight = 0
            elif self.direction == 'right':
                character.bounceRight = self.strength
                character.bounceLeft = 0
            elif self.direction == 'up':
                character.bounceUp = self.strength
            elif self.direction == 'down':
                character.bounceUp = 0
                character.jump = character.maxJump + 1