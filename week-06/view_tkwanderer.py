from tkinter import *
from PIL import ImageTk, Image

class Display:

    def __init__(self):

        self.root = Tk()
        self.canvas = Canvas(self.root, width = 600, height = 800)
        self.canvas.pack()

        # read Area images
        self.floor = ImageTk.PhotoImage(self.image_resize(Image.open('img/floor.png')))
        self.wall = ImageTk.PhotoImage(self.image_resize(Image.open('img/wall.png')))

        # read Character images
        # Hero
        self.hero_right = ImageTk.PhotoImage(self.image_resize(Image.open('img/hero-right.png')))
        self.hero_down = ImageTk.PhotoImage(self.image_resize(Image.open('img/hero-down.png')))
        self.hero_left = ImageTk.PhotoImage(self.image_resize(Image.open('img/hero-left.png')))
        self.hero_up = ImageTk.PhotoImage(self.image_resize(Image.open('img/hero-up.png')))

    def image_resize(self, image):
        image = image.resize((50, 50), Image.ANTIALIAS)
        return image

    # draw area
    def draw_area(self, area):

        posX = 25
        posY = 25
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == '0':
                    self.canvas.create_image(posX + (j * 50), posY + (i * 50), image = self.floor)
                elif area[i][j] == '1':
                    self.canvas.create_image(posX + (j * 50), posY + (i * 50), image = self.wall)

    # draw hero
    def draw_hero(self, posX, posY):
        self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_down, tag = 'hero')

    def show(self):
	    self.root.mainloop()
