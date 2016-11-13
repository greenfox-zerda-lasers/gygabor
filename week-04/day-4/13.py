from tkinter import *
root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()

def draw_triangle(x, y, size):

    z = size * 3**0.5/2
    triangle = canvas.create_polygon(x, y, x + size, y, x + size / 2, y - z, fill = 'white', outline ='black')
    size = size / 20
    z = size * 3**0.5/2
    for i in range(0, 18):
        triangle = canvas.create_polygon(x + size * i, y, (x + size * i)+(x + size), y, (x + size * i)+(x + size / 2), y - z, fill = 'white', outline ='black')
# def rec_draw(x, y, size, row):
#     p = (size * 3**0.5/2) / 2
#     if row <= 0:
#        return
#     else:
#       draw_triangle(x, y, size)
#       rec_draw(x + 28, y -= 19, size = 28, row -= 1)
#     #   rec_draw(x + size / 2, y, size / 2)
#     #   rec_draw(x + size / 4, y + p, size / 2)

draw_triangle(10, 560, 560)


root.mainloop()
