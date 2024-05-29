from tkinter import *
from tkinter import ttk

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
mypad = Frame(frame)
mypad.configure(bg="Gray",width=500,height=500)
mypad.grid()

r = Frame(mypad, bg = 'Blue', highlightthickness=0)
myResGraphic = Canvas(r, bg = 'Green', width=20, height=20, highlightthickness=0)
myResGraphic.create_rectangle(10,10,20,20)
myResGraphic.place(x=0,y=0)
r.place(x=40,y=0)#places a thign






root.mainloop()



