# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
square = canvas.create_rectangle(145, 145, 155, 155, fill = 'red')

root.mainloop()
