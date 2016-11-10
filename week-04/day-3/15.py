# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
def line_draw(list):
    j = list[1]
    k = list[0]
    for i in range(len(list)/2):

        print (j)
        line = canvas.create_line(k[0], k[1], j[0], j[1], fill = 'green')

        j[1] += 2
        k += 2


points = ([10, 10], [290,  10], [290, 290], [10, 290])
line_draw(points)

root.mainloop()
