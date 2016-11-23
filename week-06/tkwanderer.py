import model_tkwanderer, view_tkwanderer
from tkinter import *
import PIL

class Tkwanderer:

    def __init__(self):
        self.view = view_tkwanderer.Display()
        self.area = model_tkwanderer.Area()
        self.hero = model_tkwanderer.Hero(0, 0)
        self.area_read = []
        self.running = False
        self.step = 50
        self.start()

    def start(self):
        self.view.canvas.delete("all")
        self.display_area()
        self.game()

    def game(self):

        self.display_hero()
        self.input_handling()

        self.view.show()
    # draw area
    def display_area(self):
        self.area.read_area()
        self.view.draw_area(self.area.game_area)

    # draw hero
    def display_hero(self):
        self.view.draw_hero(self.hero.posX * self.step, self.hero.posY * self.step)


    def input_handling(self):
        self.view.root.bind('<Up>', self.move_up_hero)
        self.view.root.bind('<Down>', self.move_down_hero)
        self.view.root.bind('<Left>', self.move_left_hero)
        self.view.root.bind('<Right>', self.move_right_hero)

    def move_up_hero(self, event):
        self.hero.posY -= 1
        self.start()

    def move_down_hero(self, event):
        self.hero.posY += 1
        self.start()

    def move_left_hero(self, event):
        self.hero.posX -= 1
        self.start()

    def move_right_hero(self, event):
        self.hero.posX += 1
        self.start()

game = Tkwanderer()
