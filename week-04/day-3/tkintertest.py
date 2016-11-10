from Tkinter import *
root = Tk()

canvas = Canvas(root, width = 200, height = 200)
canvas.pack()
redline = canvas.create_line(0, 100, 200, 0, fill = "red")
purpleoval = canvas.create_oval(10, 20, 190, 100, fill = 'purple')




root.mainloop()
