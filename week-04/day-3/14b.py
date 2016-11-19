from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def draw_line(x, y):
    h = x
    k = y

    for i in range(15):

        line = canvas.create_line(x, k, h+150, y, fill = 'purple')
        x += 10
        y += 10
    x = h
    y = k
    for i in range(15):

        line = canvas.create_line(h, y, x, k+150, fill = 'green')
        x += 10
        y += 10

draw_line(0, 0)
draw_line(150, 0)
draw_line(0, 150)
draw_line(150, 150)


root.mainloop()
