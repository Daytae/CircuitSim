from constants import *
from PIL import ImageTk, Image
from properties import *

class Part:
    partNumber = 0
    def __init__(self, schematic, properties):
        # Image File
        self.imageFileName = properties.get('image')
        self.imageFile = ImageTk.PhotoImage(Image.open(self.imageFileName))
        self.imageWidth = self.imageFile.width()
        self.imageHeight = self.imageFile.height()

        # Schematic
        self.schematic = schematic
        self.partIdentifier = properties.get('tag')
        self.nodeOffset = properties.get('nodeOffset')

        self.id = None
        self.tag = None
        Part.partNumber += 1
        #print(Part.partNumber)
    
    def createGraphic(self, x, y):
        self.id = self.schematic.create_image(x, y, image = self.imageFile)
        self.tag = self.partIdentifier + str(Part.partNumber)
        self.schematic.itemconfig(self.id, tag=(self.tag))
       
        x0, y0, x1, y1 = self.nodeOffset[0][0], self.nodeOffset[0][1],self.nodeOffset[0][2], self.nodeOffset[0][3]
        x0, y0, x1, y1 = x + x0, y + y0, x + x1, y + y1 
        self.nodeid = [self.schematic.create_rectangle(x0,y0,x1,y1, fill='Green', width=0)]
        self.schematic.tag_bind(self.nodeid, sequence='<1>', func=self.testFunc)

    def moveItem(self, e):
        x, y = snap(e.x - (self.imageWidth/2)), snap(e.y - (self.imageHeight/2))
        self.schematic.moveto(self.id, x, y)
        self.schematic.moveto(self.nodeid[0], x + self.nodeOffset[0][0], y + self.nodeOffset[0][1])
    
    def testFunc(self, e):
        print("HI")


class Resistor(Part):
    def __init__(self, schematic, x, y):
        super().__init__(schematic, Properties.ResistorProperties)
        self.createGraphic(x, y)

class Capacitor(Part):
    def __init__(self, schematic, x, y):
        super().__init__(schematic, Properties.CapacitorProperties)
        self.createGraphic(x, y)

class Inductor(Part):
    def __init__(self, schematic, x, y):
        super().__init__(schematic, Properties.InductorProperties)
        self.createGraphic(x, y)

class VoltageSource(Part):
    def __init__(self, schematic, x, y):
        super().__init__(schematic, Properties.VoltageSourceProperties)
        self.createGraphic(x, y)

class CurrentSource(Part):
    def __init__(self, schematic, x, y):
        super().__init__(schematic, Properties.CurrentSourceProperties)
        self.createGraphic(x, y)
