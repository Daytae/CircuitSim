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

        self.mode = ViewingMode
        #self.mode.setup()


    def exitProgram(self, e):
        root.destroy()

    def toggleMode(self, mode):
        # allows toggling
        self.mode = ViewingMode if self.mode == mode else mode
        self.mode.setup(self)

    def setGlobalControls(self):
        self.bind_all('<Escape>', self.exitProgram)
        self.bind_all('r', func = lambda e: self.toggleMode(ResistorMode))
        self.bind_all('c', func = lambda e: self.toggleMode(CapacitorMode))
        self.bind_all('l', func = lambda e: self.toggleMode(InductorMode))
        self.bind_all('v', func = lambda e: self.toggleMode(VoltageSourceMode))
        self.bind_all('i', func = lambda e: self.toggleMode(CurrentSourceMode))
        self.bind_all('<space>', func = lambda e: self.toggleMode(ViewingMode))
        self.bind_all('w', func = lambda e: self.toggleMode(WireMode))


    


# Main Loop, program start
root = Tk()
programGUI = GUI(root)
root.mainloop()



