

from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
for i in range(1, 19):
    i *= 10
    square = canvas.create_rectangle(i, i, i+10, i+10, fill = 'purple')

root.mainloop()
