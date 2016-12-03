from tkinter import *
root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

def draw_triangle(x, y, x2, y2, x3, y3):
    line = canvas.create_polygon(x, y, x2, y2, x3, y3, fill = 'white', outline ='black')


def rec_draw(x, y, size, piece):
    z = size * 3**0.5/2
    if piece == 0:
        return 0
    else:
        for i in range(0, piece):
            p = x
            p += i*size
            draw_triangle(p, y, p + size, y, p + size / 2, y - z)

        return rec_draw(x+size/2, y-z, size, piece - 1)



rec_draw(10, 560, 40, 10)


root.mainloop()
