from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

j = 0
for i in range(1, 6):
    i *= 10
    j += 10
    square = canvas.create_rectangle(j, j, i+10, i+10, fill = 'purple')

root.mainloop()
