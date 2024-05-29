from constants import *
from part import *

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
        self.doesDrawGhost = False
        self.ghost = None    # Current displayed ghost object
        self.ghostid = None
        self.circuitElements = []
        self.mode = 'R'

        # Initialization of board visuals
        self.drawGrid()
    
    def toggleGhost(self):
        # toggles the ghost
        pass

    
    def toggleResistorMode(self, onOrOff):
        if onOrOff == True: #ie toggling it on
            print("ON")
            self.bind('<Motion>', self.drawGhost)
        else:
            print("OFF")
            if(self.ghost != None):
                self.delete(self.ghost.nodeid)
                self.delete(self.ghost.id)
            self.ghost = None
            self.ghostid = None
            self.unbind('<Motion>')     

    def drawGrid(self):
        xmax = SCHEMATIC_WIDTH
        ymax = SCHEMATIC_HEIGHT
        for x in range(0, xmax, GRID_SIZE):
            self.create_line(x, 0, x, ymax)
        for y in range(0, ymax, GRID_SIZE):
            self.create_line(0, y, xmax, y)

    def placeImage(self, e):
        self.circuitElements.append(self.ghost)
        self.ghost = None

    def drawGhost(self, e):
        if self.ghost == None:
            self.ghost = Resistor(self, snap(e.x), snap(e.y))
            self.tag_bind(self.ghost.tag, sequence='<1>', func=self.placeImage)
        
        # top left corner of ghost image
        self.ghost.moveItem(e)
        
        
