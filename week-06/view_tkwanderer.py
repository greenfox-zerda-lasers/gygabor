from tkinter import *
from PIL import ImageTk, Image

class Display:

    def __init__(self):

        self.root = Tk()
        self.canvas = Canvas(self.root, width = 800, height = 800)
        self.canvas.pack()

        # read Area images
        self.floor = PhotoImage(file = 'floor.gif')
        self.wall = PhotoImage(file = 'wall.gif')

        # read Character images

        # Hero
        self.hero_right = ImageTk.PhotoImage(Image.open('hero-right.png'))
        self.hero_down = ImageTk.PhotoImage(Image.open('hero-down.png'))
        self.hero_left = ImageTk.PhotoImage(Image.open('hero-left.png'))
        self.hero_up = ImageTk.PhotoImage(Image.open('hero-up.png'))

    # draw area
    def draw_area(self, area):

        posX = 36
        posY = 36
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == '0':
                    self.canvas.create_image(posX + (j * 72), posY + (i * 72), image = self.floor)
                elif area[i][j] == '1':
                    self.canvas.create_image(posX + (j * 72), posY + (i * 72), image = self.wall)

    # draw hero
    def draw_hero(self, posX, posY):
        self.canvas.create_image(posX, posY, image = self.hero_down)

    def show(self):
	       self.root.mainloop()
