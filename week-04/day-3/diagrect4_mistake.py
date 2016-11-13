from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

for i in range(1, 6):
    i *= 10
    square = canvas.create_rectangle(i+i, i+i, i*2+10, i*2+10, fill = 'purple')

root.mainloop()
