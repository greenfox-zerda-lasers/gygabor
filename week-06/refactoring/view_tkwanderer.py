from tkinter import *
from PIL import ImageTk, Image

class Display:

    def __init__(self):

        self.root = Tk()
        self.canvas = Canvas(self.root, width = 500, height = 800)
        self.canvas.pack()

        # read Area images
        self.floor = ImageTk.PhotoImage(self.image_resize(Image.open('../img/floor.png')))
        self.wall = ImageTk.PhotoImage(self.image_resize(Image.open('../img/wall.png')))

        # read Character images
        # Hero
        self.hero_right = ImageTk.PhotoImage(self.image_resize(Image.open('../img/hero-right.png')))
        self.hero_down = ImageTk.PhotoImage(self.image_resize(Image.open('../img/hero-down.png')))
        self.hero_left = ImageTk.PhotoImage(self.image_resize(Image.open('../img/hero-left.png')))
        self.hero_up = ImageTk.PhotoImage(self.image_resize(Image.open('../img/hero-up.png')))

        # Skeleton
        self.skeleton = ImageTk.PhotoImage(self.image_resize(Image.open('../img/skel.gif')))

        # Boss
        self.boss = ImageTk.PhotoImage(self.image_resize(Image.open('../img/boss.png')))

    # resize images
    def image_resize(self, image):
        image = image.resize((50, 50), Image.ANTIALIAS)
        return image

    # draw area
    def draw_area(self, area):
        for i in range(len(area.game_area)):
            for j in range(len(area.game_area[i])):
                if area.game_area[i][j] == '0':
                    self.canvas.create_image((j * 50), (i * 50), anchor = NW, image = self.floor)
                elif area.game_area[i][j] == '1':
                    self.canvas.create_image((j * 50), (i * 50), anchor = NW, image = self.wall)

    # draw characters

    def display(self, character_list):
        for i in range(len(character_list)):
            if i == 0:
                if character_list[i].direction == 'up':
                    self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.hero_up, tag = 'character')
                elif character_list[i].direction == 'down':
                    self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.hero_down, tag = 'character')
                elif character_list[i].direction == 'left':
                    self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.hero_left, tag = 'character')
                elif character_list[i].direction == 'right':
                    self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.hero_right, tag = 'character')
            elif i == 1:
                self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.boss, tag = 'character')
            else:
                self.canvas.create_image(character_list[i].position[0] * 50, character_list[i].position[1]* 50, anchor = NW, image = self.skeleton, tag = 'character')

    # def draw_hero(self, posX, posY, direction):
    #     if direction == 'up':
    #         self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_up, tag = 'hero')
    #     if direction == 'down':
    #         self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_down, tag = 'hero')
    #     if direction == 'left':
    #         self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_left, tag = 'hero')
    #     if direction == 'right':
    #         self.canvas.create_image(posX, posY, anchor = NW, image = self.hero_right, tag = 'hero')
    #
    # # draw skeleton
    # def draw_skeleton(self, posX, posY):
    #     self.canvas.create_image(posX, posY, anchor = NW, image = self.skeleton, tag = 'skeleton')
    #
    # # draw boss
    # def draw_boss(self, posX, posY):
    #     self.canvas.create_image(posX, posY, anchor = NW, image = self.boss, tag = 'boss')
    #
    # def draw_stats(self, characters, skeleton):
    #     for i in range(len(characters)):
    #         if i == 0:
    #             text = 'Hero (Level ' + str(characters[i].level) + ') HP: ' + str(characters[i].health) +' DP: ' +str(characters[i].defend) + ' SP: ' + str(characters[i].strike)
    #         elif i == 1:
    #             text = 'Boss (Level ' + str(characters[i].level) + ') HP: ' + str(characters[i].health) +' DP: ' +str(characters[i].defend) + ' SP: ' + str(characters[i].strike)
    #         self.canvas.create_text(10, 570 + i * 20, anchor = NW, text = text, tag = 'stat')
    #
    #     for i in range(len(skeleton)):
    #         skeleton_text = 'Skeleton '+ str(i+ 1) +' (Level ' + str(skeleton[i].level) + ') HP: ' + str(skeleton[i].health) +' DP: ' + str(skeleton[i].defend) + ' SP: ' + str(skeleton[i].strike)
    #         self.canvas.create_text(10, 610 + i * 20, anchor = NW, text = skeleton_text, tag = 'skeleton_stat')
    # # mainloop
    def show(self):
	    self.root.mainloop()
