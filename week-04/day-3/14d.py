import random
from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def color():
    col1 = ('%02x' %random.randint(0, 255))
    col2 = ('%02x' %random.randint(0, 255))
    col3 = ('%02x' %random.randint(0, 255))
    col = '#' + col1 + col2 + col3
    return col

x = 150
y = 0
for i in range(16):

    line = canvas.create_line(x, 150, 150, y, fill = color())
    line = canvas.create_line(x, 150, 150, 300 - y, fill = color())
    line = canvas.create_line(x - 150, 150, 150, 150 - y, fill = color())
    line = canvas.create_line(300 - x, 150, 150, 300 - y, fill = color())
    x += 10
    y += 10


root.mainloop()
