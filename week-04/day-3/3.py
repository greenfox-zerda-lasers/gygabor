# create a 300x300 canvas.
# draw its diagonals in green.

from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
diagonal1 = canvas.create_line(0, 0, 300, 300, fill = 'green')
diagonal2 = canvas.create_line(300, 0, 0, 300, fill= 'green')
canvas.pack()

root.mainloop()
