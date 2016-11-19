# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def square_draw(square_size):

    square = canvas.create_rectangle(150 - square_size / 2, 150 - square_size / 2, 150 + square_size / 2, 150 + square_size / 2)

for i in range(0, 100, 5):
    square_draw(i)

root.mainloop()
