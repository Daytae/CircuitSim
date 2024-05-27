from tkinter import *
from tkinter import ttk
from schematic import *
from constants import *

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = Frame(root)
frame.configure(borderwidth=5)
frame.grid(column=0, row=0, sticky=(N, W, E, S))


schematic = Schematic(frame)
schematic.configure(background="#d3d3d3", width=SCHEMATIC_WIDTH, height=SCHEMATIC_HEIGHT)
schematic.grid()

schematic.bind('<Motion>', schematic.draw_ghost)
schematic.bind('<1>', schematic.draw)




root.mainloop()



