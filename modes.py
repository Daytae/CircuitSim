class Mode:
    def __init__(self, modeName):
        self.modeName = modeName
        self.color

class WireMode(Mode):
    def __init__(self, modeName, wireColor ='Black', wireThickness=5):
        super().__init__(modeName)
        self.x0 = -1
        self.y0 = -1
        self.hasPlacedFirst = False
        self.wireColor = 


