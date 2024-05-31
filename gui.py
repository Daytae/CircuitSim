from schematic import *
from modes import *

class GUI(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.configure(borderwidth=5)
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.schematic = schematic = Schematic(self)
        schematic.grid()

        self.setGlobalControls()

    def exitProgram(self, e):
        root.destroy()

    def setGlobalControls(self):
        self.bind_all('<Escape>', self.exitProgram)
        self.bind_all('r', func = lambda e: self.schematic.toggleMode(ResistorMode, e))
        self.bind_all('c', func = lambda e: self.schematic.toggleMode(CapacitorMode, e))
        self.bind_all('l', func = lambda e: self.schematic.toggleMode(InductorMode, e))
        self.bind_all('v', func = lambda e: self.schematic.toggleMode(VoltageSourceMode, e))
        self.bind_all('i', func = lambda e: self.schematic.toggleMode(CurrentSourceMode, e))
        self.bind_all('<space>', func = lambda e: self.schematic.toggleMode(ViewingMode, e))
        self.bind_all('w', func = lambda e: self.schematic.toggleMode(WireMode, e))


    


# Main Loop, program start
root = Tk()
programGUI = GUI(root)
root.mainloop()



