import model_tkwanderer, view_tkwanderer
from tkinter import *

class Tkwanderer:

    def __init__(self):
        self.view = view_tkwanderer.Display()
        self.map = model_tkwanderer.Map()
        self.map_read = []

        self.display_map()

    def display_map(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 800, height = 800)
        self.canvas.pack()

        self.map.read_map()
        self.view.draw_map(self.map.game_map)

        self.root.mainloop()

game = Tkwanderer()
