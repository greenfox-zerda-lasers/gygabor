from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 600, height = 600, background = 'yellow')
canvas.pack()

def rect(x, y, size, number):
    canvas.create_rectangle(x,y,x+size,y+size)

    if number > 0:
        rect(x, y+size/3, size/3, number-1)
        rect(x+(size/3)*2 ,y+size/3, size/3, number-1)
        rect(x+size/3, y,size/3, number-1)
        rect(x+size/3, y+(size/3)*2, size/3, number-1)
rect(0, 0, 600, 4)

root.mainloop()
