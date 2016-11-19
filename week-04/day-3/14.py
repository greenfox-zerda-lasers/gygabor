from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

x = 0
y = 0
for i in range (15):

    line = canvas.create_line(x, 0, 300, y, fill = 'purple')
    x += 20
    y += 20
x = 0
y = 0
for i in range (15):

    line = canvas.create_line(0, y, x, 300, fill = 'green')
    x += 20
    y += 20



root.mainloop()
