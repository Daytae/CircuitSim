from tkinter import *
from tkinter import ttk
from constants import *
from part import *

def snap(x):
    return x - (x % GRID_SIZE)
class Schematic(Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ghost = None
        self.thewindow = None
        self.configure(background=SCHEMATIC_BACKGROUND, width=SCHEMATIC_WIDTH, height=SCHEMATIC_HEIGHT)
        self.bind('<Motion>', self.drawGhost)
        self.drawGrid()

    def drawGrid(self):
        xmax = SCHEMATIC_WIDTH
        ymax = SCHEMATIC_HEIGHT
        for x in range(0, xmax, GRID_SIZE):
            self.create_line(x, 0, x, ymax)
        for y in range(0, ymax, GRID_SIZE):
            self.create_line(0, y, xmax, y)

    def drawGhost(self, e):
        e.x, e.y = snap(e.x), snap(e.y)

        if self.ghost == None:
            self.ghost = ResistorWidget(self)
            self.thewindow = self.create_window(e.x,e.y,window=self.ghost)
        self.moveto(self.thewindow, e.x, e.y)


#schematic.bind('<1>', schematic.draw)

        
    