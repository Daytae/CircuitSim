class ViewingModeClass:
    def setup(self, gui):
        gui.schematic.toggleResistorMode(False)
        #print("ViewingModeClass")

class PartPlacementModeClass:  
    def setup(self, gui):
        gui.schematic.toggleResistorMode(True)
        #print("PartPlacementModeClass")

class WirePlacementModeClass:
    def setup(self, gui):
      #print("WireModeClass")
      pass


ViewingMode = ViewingModeClass()
ResistorMode = PartPlacementModeClass()
CapacitorMode = PartPlacementModeClass()
InductorMode = PartPlacementModeClass()
VoltageSourceMode = PartPlacementModeClass()
CurrentSourceMode = PartPlacementModeClass()
WireMode = WirePlacementModeClass()



