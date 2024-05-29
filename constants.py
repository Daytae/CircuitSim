from tkinter import *
from tkinter import ttk

SCHEMATIC_WIDTH = 1200
SCHEMATIC_HEIGHT = 800
SCHEMATIC_BACKGROUND = "#d3d3d3"
SCHEMATIC_BORDERWIDTH = 3
GRID_SIZE = 25

def snap(x):
    return GRID_SIZE * round(x / GRID_SIZE)