from tkinter import *
from tkinter import ttk
from constants import *

def snap(x):
    '''Snaps a position x to the grid'''
    return x - (x % GRID_SIZE)

class Schematic(Canvas):
    current_ghost = None
    wire_color = 'Black'
    wire_width = 5
    hasFixedFirstPosition = False
    init_x0 = 0
    init_y0 = 0

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
    
    def delete_ghost(self):
        if (self.current_ghost != None):
            self.delete(self.current_ghost)

    def draw_ghost(self, e):
        self.delete_ghost()
        if not self.hasFixedFirstPosition:
            self.init_x0 = e.x
            self.init_y0 = e.y

        self.current_ghost = self.draw_wire(self.init_x0, self.init_y0, e.x, e.y)
    
    def draw(self, e):
        if self.hasFixedFirstPosition:
            self.hasFixedFirstPosition = False
            self.draw_wire(self.init_x0, self.init_y0, e.x, e.y)
        else:
            self.init_x0 = e.x
            self.init_y0 = e.y
            self.hasFixedFirstPosition = True

    def draw_wire(self, x0, y0, x1, y1):
        x0, y0, x1, y1 = snap(x0), snap(y0), snap(x1), snap(y1) # snaps coords to top left grid
        
        # routes to shortest path to make it look nice
        pos1 = (x0, y0, x1, y0) if abs(x1 - x0) > abs(y1 - y0) else (x0, y0, x0, y1)
        pos2 = (pos1[2], pos1[3], x1, y1)
        return self.create_line(pos1, pos2, fill=self.wire_color, width=self.wire_width)

    def create_wire(self, x0, y0, x1, y1):
        pass
        