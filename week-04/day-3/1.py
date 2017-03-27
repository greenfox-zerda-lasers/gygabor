# pylint: disable=missing-docstring
# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *
root = Tk()

canvas = Canvas(root, width=300, height=300)
h_line = canvas.create_line(0, 150, 300, 150, fill = 'red')
v_line = canvas.create_line(150, 0, 150, 300, fill= 'green')
canvas.pack()

root.mainloop()
