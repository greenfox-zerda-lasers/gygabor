from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

def draw_hexa(x, y, size):
    z = size * 3**0.5/2
    hexagon = canvas.create_polygon(x + size/2, y, x+size*1.5, y, x+size*2, y + z, x+size*1.5, y+z*2, x + size/2, y+z*2, x, y+z, fill = 'white', outline ='black')

def rec_draw(x, y, size, row):
    z = size * 3**0.5/2

    if row == 0:
        return 0
    else:
        for i in range(0, row):

            draw_hexa(x + i*(size*1.5), y - z * i, size)
        time.sleep(0.1)
        rec_draw(x + i*(size*1.5), y + z *i, size, row - 1)
            # rec_draw(x + size, y, size)
            # rec_draw(x + size+size/3, y + p * 2, size)
            # rec_draw(x + size, y + p * 4, size)
            # rec_draw(x + size/3, y + p * 4, size)
            # rec_draw(x, y + p * 2, size)
            # z = size * 3**0.5/2
        return rec_draw(x, y, size, row-1)

    #   else:
    #       for i in range(0, piece):
    #           p = x
    #           p += i*size
    #           draw_triangle(p, y, p + size, y, p + size / 2, y - z)
      #
    #       return rec_draw(x+size/2, y-z, size, piece - 1)


rec_draw(50, 300, 20, 7)


root.mainloop()
