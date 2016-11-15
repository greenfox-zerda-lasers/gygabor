from tkinter import *
import time
root = Tk()

canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

def draw_triangle(x, y, size):
    time.sleep(0.01)

    z = size * 3**0.5/2
    triangle = canvas.create_polygon(x, y, x+size, y, x + size / 2, y + z, fill = 'white', outline ='black')
    canvas.update()
    
def rec_draw(x, y, size):
    p = (size * 3**0.5/2) / 2
    if size < 3:
        return
    else:
        draw_triangle(x, y, size)
        rec_draw(x, y, size / 2)
        rec_draw(x + size / 2, y, size / 2)
        rec_draw(x + size / 4, y + p, size / 2)

rec_draw(10, 10, 750)


root.mainloop()
