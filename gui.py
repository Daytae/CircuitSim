from schematic import *


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = Frame(root)
frame.configure(borderwidth=5)
frame.grid(column=0, row=0, sticky=(N, W, E, S))


schematic = Schematic(frame)
schematic.grid()


root.mainloop()



