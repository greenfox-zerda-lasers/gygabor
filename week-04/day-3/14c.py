from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
x = 150
y = 0
for i in range(16):

    line = canvas.create_line(x, 150, 150, y, fill = 'green')
    line = canvas.create_line(x, 150, 150, 300 - y, fill = 'green')
    line = canvas.create_line(x - 150, 150, 150, 150 - y, fill = 'green')
    line = canvas.create_line(300 - x, 150, 150, 300 - y, fill = 'green')
    x += 10
    y += 10


root.mainloop()
