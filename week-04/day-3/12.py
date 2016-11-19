# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

for i in range(8):
    for j in range(8):
        if (i+j)%2 != 0:

            canvas.create_rectangle(j*37, i*37, (j+1)*37, (i+1)*37, fill='black')


root.mainloop()
