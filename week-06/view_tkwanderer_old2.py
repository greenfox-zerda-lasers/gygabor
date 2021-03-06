from tkinter import *
from PIL import ImageTk, Image

class Display:

    def __init__(self):

        self.root = Tk()
        self.canvas = Canvas(self.root, width = 500, height = 800)
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

        # Skeleton
        self.skeleton = ImageTk.PhotoImage(self.image_resize(Image.open('img/skel.gif')))

        # Boss
        self.boss = ImageTk.PhotoImage(self.image_resize(Image.open('img/boss.png')))

    # resize images
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
    def draw_hero(self, posX, posY, direction):
        if direction == 'up':
            self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_up, tag = 'hero')
        if direction == 'down':
            self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_down, tag = 'hero')
        if direction == 'left':
            self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_left, tag = 'hero')
        if direction == 'right':
            self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_right, tag = 'hero')

    # draw skeleton
    def draw_skeleton(self, posX, posY):

        self.canvas.create_image(posX, posY, anchor = NW, image = self.skeleton, tag = 'skeleton')

    # draw boss
    def draw_boss(self, posX, posY):
        self.canvas.create_image(posX, posY, anchor = NW, image = self.boss, tag = 'boss')

    def draw_stats(self, hero, skeleton, boss):
        hero_text = 'Hero (Level ' + str(hero.level) + ') HP: ' + str(hero.health) +' DP: ' +str(hero.defend) + ' SP: ' + str(hero.strike)
        boss_text = 'Boss (Level ' + str(boss.level) + ') HP: ' + str(boss.health) +' DP: ' +str(boss.defend) + ' SP: ' + str(boss.strike)

        self.canvas.create_text(10, 570, anchor = NW, text = hero_text, tag = 'hero_stat')
        self.canvas.create_text(10, 590, anchor = NW, text = boss_text, tag = 'boss_stat')
        for i in range(len(skeleton)):
            skeleton_text = 'Skeleton '+ str(i+ 1) +' (Level ' + str(skeleton[i].level) + ') HP: ' + str(skeleton[i].health) +' DP: ' + str(skeleton[i].defend) + ' SP: ' + str(skeleton[i].strike)
            self.canvas.create_text(10, 610 + i * 20 , anchor = NW, text = skeleton_text, tag = 'skeleton_stat')
    # mainloop
    def show(self):
	    self.root.mainloop()
