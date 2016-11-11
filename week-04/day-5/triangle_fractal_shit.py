from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 800, height = 800)
canvas.pack()

def draw_triangle(x, y, size):
    z = size * 3**0.5/2
    triangle = canvas.create_polygon(x, y, x+size, y, x + size / 2, z, fill = 'white', outline ='black')



def rec_draw(x, y, size):
    z = size * 3**0.5/2
    print(z)
    if size < 10:
        return
    else:
        draw_triangle(x, y, size)
        rec_draw(x, y, size / 2)
        rec_draw(x + size / 2, y, size / 2)
        rec_draw(x + size / 4, y + z, size / 2)

rec_draw(0, 0, 600)


root.mainloop()
