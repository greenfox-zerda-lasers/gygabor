# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def draw_line(x,y):
    line = canvas.create_line(x, y, 150, 150, fill = 'red')

draw_line(23, 45)
draw_line(200, 100)
draw_line(51, 179)

root.mainloop()
