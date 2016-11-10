# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.
from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
line_top = canvas.create_line(5, 5, 295, 5, fill = 'red')
line_left = canvas.create_line(5, 5, 5, 295, fill= 'green')
line_bottom = canvas.create_line(5, 295, 295, 295, fill = 'blue')
line_right = canvas.create_line(295, 5, 295, 295, fill= 'black')
canvas.pack()



root.mainloop()
