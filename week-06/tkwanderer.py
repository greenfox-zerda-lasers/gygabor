import model_tkwanderer, view_tkwanderer
from tkinter import *
import PIL

class Tkwanderer:

    def __init__(self):
        self.view = view_tkwanderer.Display()
        self.area = model_tkwanderer.Area()
        self.hero = model_tkwanderer.Hero(32, 32)
        self.area_read = []

        self.start()

    def start(self):
        self.display_area()
        self.display_hero()
        self.view.show()

    # draw area
    def display_area(self):
        self.area.read_area()
        self.view.draw_area(self.area.game_area)

    def display_hero(self):
        self.view.draw_hero(self.hero.posX, self.hero.posY)

    def game_loop(self):
        pass


game = Tkwanderer()
