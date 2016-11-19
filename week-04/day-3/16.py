
# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
import random
from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300, background = 'black')
canvas.pack()
def random_square_draw(number):
    x = 0
    y = 0

    rgb = ''
    for i in range(number):
        color = '#'
        x = random.randint(0, 300)
        y = random.randint(0, 300)
        rgb = '%02x' % random.randint(0,255)
        color += rgb * 3
        print(color)
        line = canvas.create_rectangle(x, y, x+5, y+5, fill = color)




random_square_draw(10)

root.mainloop()
