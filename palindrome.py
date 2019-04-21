#code segment for vertical line
from tkinter import *
master = Tk()
w = Canvas(master, width=400, height=400)
w.pack()
canvas_height=200
canvas_width=200
#y = int(canvas_height / 2)
x = int(canvas_width / 2)
#w.create_line(0, y, canvas_width, y )
w.create_line(x, 0, x, canvas_height )
mainloop()