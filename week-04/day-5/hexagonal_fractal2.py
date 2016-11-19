import time, random
from tkinter import *
root = Tk()

root.wait_visibility(root)
root.wm_attributes('-alpha',0.7)

canvas = Canvas(root, width = 800, height = 800, background = 'black')
canvas.pack()

def draw_hexa(x, y, size, color):
    time.sleep(0.0001)
    z = size * 3**0.5/2
    triangle = canvas.create_polygon(x + size/2, y, x+size*1.5, y, x+size*2, y + z, x+size*1.5, y+z*2, x + size/2, y+z*2, x, y+z, fill = color, outline = color)
    canvas.update()

def randcolor():
    color = '#'+''.join(random.sample('0123456789ABCDEF',6))
    return color

def rec_draw(x, y, size):
    p = (size/3) * 3**0.5/2
    if size < 1:
        return
    else:
        color = randcolor()
        draw_hexa(x, y, size, color)
        rec_draw(x + size/3, y, size / 3)
        rec_draw(x + size, y, size / 3)
        rec_draw(x + size+size/3, y + p * 2, size / 3)
        rec_draw(x + size, y + p * 4, size / 3)
        rec_draw(x + size/3, y + p * 4, size / 3)
        rec_draw(x, y + p * 2, size / 3)



rec_draw(10, 10, 380)


root.mainloop()
