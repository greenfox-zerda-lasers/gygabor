# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def square_draw(square_size):

    square = canvas.create_rectangle(150 - square_size / 2, 150 - square_size / 2, 150 + square_size / 2, 150 + square_size / 2)

for i in range(0, 100, 5):
    square_draw(i)

root.mainloop()
