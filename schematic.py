from constants import *
from part import *
from modes import *

# Schematic is the main drawing window, a modified canvas where all parts will be drawn
    
class Schematic(Canvas):
    def __init__(self, root):
        super().__init__(root)

        # Canvas Configuration Settings
        self.configure(
                borderwidth = SCHEMATIC_BORDERWIDTH,
                background = SCHEMATIC_BACKGROUND,
                width = SCHEMATIC_WIDTH,
                height = SCHEMATIC_HEIGHT
        )

        # Local Schematic Variables
        self.ghost = None    # Current displayed ghost object
        self.mode = ViewingMode
        self.circuitElements = []
        self.drawGrid()
    
    def setGhost(self, shouldDrawGhost, e):
        # deletes old ghost
        if(self.ghost != None):
            self.delete(self.ghost.tag)
        
        if shouldDrawGhost:
            self.bind('<Motion>', self.drawGhost)
            self.ghost = self.mode.part(self, snap(e.x), snap(e.y))
            self.tag_bind(self.ghost.tag, sequence='<1>', func=self.placeImage)
            self.drawGhost(e)
        else:
             self.unbind('<Motion>') 

    def drawGrid(self):
        xmax = SCHEMATIC_WIDTH
        ymax = SCHEMATIC_HEIGHT
        for x in range(0, xmax, GRID_SIZE):
            self.create_line(x, 0, x, ymax, fill='Gray')
        for y in range(0, ymax, GRID_SIZE):
            self.create_line(0, y, xmax, y, fill='Gray')

    def placeImage(self, e):
        self.circuitElements.append(self.ghost)
        self.ghost = self.mode.part(self, snap(e.x), snap(e.y))
        self.tag_bind(self.ghost.tag, sequence='<1>', func=self.placeImage)

    def drawGhost(self, e):
        self.ghost.moveItem(e)
        
    def toggleMode(self, mode, e):
    # allows toggling
        self.mode = ViewingMode if self.mode == mode else mode
        print(str(self.mode.name))
        self.mode.setup(self, e)
        
