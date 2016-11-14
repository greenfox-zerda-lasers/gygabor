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
            if i > 0:
                draw_hexa(x+i*(size*1.5), y - (z * i)+z*2, size)
                draw_hexa(x+(i*(size*1.5))-(size*1.5), y - (z * i)-z, size)
            if i > 1:
                draw_hexa(x+(i*(size*1.5)), y - (z * i)+z*4, size)
                draw_hexa(x+(i*(size*1.5))-(size*1.5)*2, y - (z * i)-z*2, size)
            if i > 2:
                draw_hexa(x+(i*(size*1.5)), y - (z * i)+z*6, size)
                draw_hexa(x+(i*(size*1.5))-(size*1.5)*3, y - (z * i)-z*3, size)

        return rec_draw(x, y, size, row-1)

rec_draw(50, 300, 20, 7)


root.mainloop()
