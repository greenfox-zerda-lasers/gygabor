from tkinter import *

class Display:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width = 800, height = 800)
        self.canvas.pack()

        self.floor = PhotoImage(file = 'floor.gif')
        self.wall = PhotoImage(file = 'wall.gif')


    def draw_map(self, game_map):

        x = 36
        y = 36
        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                print(game_map[i][j])
                if game_map[i][j] == '0':
                    self.canvas.create_image(x + (j * 72), y + (i * 72), image = self.floor)
                elif game_map[i][j] == '1':
                    self.canvas.create_image(x + (j * 72), y + (i * 72), image = self.wall)
