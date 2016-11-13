from tkinter import *
root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

def draw_line(x, y, x2, y2):

    line = canvas.create_line(x, y, x2, y2)


def rec_draw(x, y, size, row):
    z = size * 3**0.5/2
    p = int(size / row)
    q = p * 3**0.5/2
    for i in range(0, size, p):
        draw_line(x + i*0.5, y - i * q , x + i*2, y - i * q)
        # draw_line(x + i*0.5, y, x + p / 2, y - q)
        # draw_line(x + p / 2, y - q, x + p, y)


rec_draw(10, 560, 560, 20)


root.mainloop()
