from tkinter import *
root = Tk()

canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

def draw_hexa(x, y, size):
    z = size * 3**0.5/2
    triangle = canvas.create_polygon(x + size/2, y, x+size*1.5, y, x+size*2, y + z, x+size*1.5, y+z*2, x + size/2, y+z*2, x, y+z, fill = 'white', outline ='black')

def rec_draw(x, y, size):
    p = (size/3) * 3**0.5/2
    if size < 1:
      return
    else:
      draw_hexa(x, y, size)
      rec_draw(x + size/3, y, size / 3)
      rec_draw(x + size, y, size / 3)
      rec_draw(x + size+size/3, y + p * 2, size / 3)
      rec_draw(x + size, y + p * 4, size / 3)
      rec_draw(x + size/3, y + p * 4, size / 3)
      rec_draw(x, y + p * 2, size / 3)

rec_draw(10, 10, 380)


root.mainloop()
