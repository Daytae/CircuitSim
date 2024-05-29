from tkinter import Frame, Canvas, Label
from PIL import ImageTk, Image
from constants import *

class ResistorWidget(Canvas):
    def __init__(self, parent, **kwargs):
        self.id = super().__init__(parent, **kwargs)
        print(self.id)
        self.img = img = ImageTk.PhotoImage(Image.open("Resistor.png"))
        self.configure(highlightthickness=0, width=img.width(), height=img.height(), bg=SCHEMATIC_BACKGROUND)
        self.create_image(0,0, anchor = 'nw', image = img)
    def id(self):
        return self.id
    
        

