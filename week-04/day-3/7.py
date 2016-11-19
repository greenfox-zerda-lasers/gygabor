
# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
square = canvas.create_rectangle(0, 0, 125, 125, fill = 'yellow')
square = canvas.create_rectangle(125, 0, 300, 90, fill = 'blue')
square = canvas.create_rectangle(0, 125, 125, 300, fill = 'red')
square = canvas.create_rectangle(125, 90, 300, 300, fill = 'green')

root.mainloop()
