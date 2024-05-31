from part import *
class ViewingModeClass:
    def __init__(self):
        self.name = "ViewingMode"
    def setup(self, schematic, e):
        schematic.setGhost(None, e)
        #print("ViewingModeClass")

class PartPlacementModeClass:  
    def __init__(self, part):
        self.part = part
        self.name = part.__name__
    def setup(self, schematic, e):
        schematic.setGhost(self.part, e)
        #print("PartPlacementModeClass")

class WirePlacementModeClass:
    def setup(self, schematic):
      #print("WireModeClass")
      pass

ViewingMode = ViewingModeClass()
ResistorMode = PartPlacementModeClass(Resistor)
CapacitorMode = PartPlacementModeClass(Capacitor)
InductorMode = PartPlacementModeClass(Inductor)
VoltageSourceMode = PartPlacementModeClass(VoltageSource)
CurrentSourceMode = PartPlacementModeClass(CurrentSource)
WireMode = WirePlacementModeClass()



