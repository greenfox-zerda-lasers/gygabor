# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def square_draw(x,y):
    square = canvas.create_rectangle(x, y, x+50, y+50, fill = 'yellow')

square_draw(134, 91)
square_draw(10, 150)
square_draw(243, 78)

root.mainloop()
