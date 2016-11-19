# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

import random
from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def square_draw(square_size, color):

    square = canvas.create_rectangle(150 - square_size / 2, 150 - square_size / 2, 150 + square_size / 2, 150 + square_size / 2, fill = color)

for i in range(300, 0, -10):
    col1 = ('%02x' %random.randint(0, 255))
    col2 = ('%02x' %random.randint(0, 255))
    col3 = ('%02x' %random.randint(0, 255))
    col = '#' + col1 + col2 + col3
    square_draw(i, col)


root.mainloop()
