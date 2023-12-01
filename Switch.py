from cmu_graphics import *
from ClassFunctions import *
class Switch:
    switchList = []
    def __init__(self, x, y, state, connected, level, room, group):
        self.connected = connected
        if state: # On (Barrier on)
            self.base = Line(x - 2.5, y, x + 2.5, y, lineWidth = 3, fill = 'lime')
            self.off = Line(x, y, x - 2.5, y - 5, fill = None)
            self.on = Line(x, y, x + 2.5, y - 5, fill = 'deeppink')
            for i in self.connected:
                i.visible = not i in Switch.switchList[level - 1][room]
        else:
            self.base = Line(x - 2.5, y, x + 2.5, y, lineWidth = 3, fill = 'red')
            self.off = Line(x ,y, x - 2.5, y - 5, fill = 'deeppink')
            self.on = Line(x, y, x + 2.5, y - 5, fill = None)
            for i in self.connected:
                i.visible = i in Switch.switchList[level - 1][room]
        self.x = x
        self.y = y
        self.state = state
        self.initState = state
        self.shape = Group(self.on, self.off, self.base)
        objctSet(self, level, room, group)
        Switch.switchList[level - 1][room].append(self)
    def switch(self):
        if not self.switched:
            self.switched = True
            self.state = not self.state
            for i in self.connected:
                if i not in Switch.switchList[self.level - 1][self.room]:
                    i.visible = self.state
                else:
                    i.switch()
            self.colorSwitch()
    def reset(self):
        if self.level == app.level and self.room == app.room:
            self.state = self.initState
            x = self.x
            y = self.y
            if self.state:
                for i in self.connected:
                    i.visible = i not in Switch.switchList[self.level - 1][self.room]
            else:
                for i in self.connected:
                    i.visible = i in Switch.switchList[self.level - 1][self.room]
            self.colorSwitch()
    def colorSwitch(self):
        if self.state:
            self.base.fill = 'lime'
            self.off.fill = None
            self.on.fill = 'deeppink'
        else:
            self.base.fill = 'red'
            self.off.fill = 'deeppink'
            self.on.fill = None