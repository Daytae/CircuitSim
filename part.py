from constants import *
from PIL import ImageTk, Image



class Resistor:
    def __init__(self, schematic, x, y):
        self.img = img = ImageTk.PhotoImage(Image.open("ResistorTest.png"))
        self.id = schematic.create_image(x, y, image = self.img)
        self.imageWidth = img.width()
        self.imageHeight = img.height()
        self.tag = "R" + str(self.id)
        self.schematic = schematic
        self.schematic.itemconfig(self.id, tag=(self.tag))

        # nodes
        self.nodeOffset = [[0, 22, 5, 27], [95, 22, 100, 27]]
        x0, y0, x1, y1 = self.nodeOffset[0][0], self.nodeOffset[0][1],self.nodeOffset[0][2], self.nodeOffset[0][3]
        x0, y0, x1, y1 = x + x0, y + y0, x + x1, y + y1 
        self.nodeid = [schematic.create_rectangle(x0,y0,x1,y1, fill='Green', width=0)]
        self.schematic.tag_bind(self.nodeid, sequence='<1>', func=self.testFunc)

    def testFunc(self, e):
        print("HI")

    def moveItem(self, e):
        x, y = snap(e.x - (self.imageWidth/2)), snap(e.y - (self.imageHeight/2))
        self.schematic.moveto(self.id, x, y)
        self.schematic.moveto(self.nodeid[0], x + self.nodeOffset[0][0], y + self.nodeOffset[0][1])

    def id(self):
        return self.id
    
        

