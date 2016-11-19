from tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
size = 0
distance = 10
for i in range(1, 6):
    size = i * 10
    distance += size - 10
    square = canvas.create_rectangle(distance, distance, distance + size, distance + size, fill = 'purple')


root.mainloop()
