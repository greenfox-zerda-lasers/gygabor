import model_tkwanderer, view_tkwanderer
from tkinter import *
from random import randint

class Tkwanderer:

    def __init__(self):
        self.view = view_tkwanderer.Display()
        self.area = model_tkwanderer.Area()
        self.hero = model_tkwanderer.Hero(0, 0)
        self.area_read = []
        self.direction = 'down'
        self.skeleton_number = 3
        self.skeleton = []
        self.step = 50
        self.boss_exist = False
        self.boss = ''
        self.move_enemy = True

        self.start()

    def start(self):
        self.display_area()
        self.boss_instantiate()
        self.skeleton_instantiate()
        self.game()

    def game(self):
        self.view.canvas.delete('hero', 'skeleton', 'boss')
        self.display_hero()
        self.display_boss()
        self.display_skeleton()
        self.input_handling()
        self.move_skeleton()

        self.view.show()

    # instantiate boss
    def boss_instantiate(self):
        while self.boss_exist == False:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area.game_area[posY][posX] == '0' and (posX, posY) != (self.hero.posX, self.hero.posY):
                self.boss = model_tkwanderer.Boss(posX, posY)
                self.boss_exist = True

    # instantiate skeleton
    def skeleton_instantiate(self):
        while self.skeleton_number > 0:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area.game_area[posY][posX] == '0' and (posX, posY) != (self.hero.posX, self.hero.posY) and (posX, posY) != (self.boss.posX, self.boss.posY):
                i = model_tkwanderer.Skeleton(posX, posY)
                self.skeleton.append(i)
                self.skeleton_number -= 1

    # draw area
    def display_area(self):
        self.area.read_area()
        self.view.draw_area(self.area.game_area)

    # draw hero
    def display_hero(self):
        self.view.draw_hero(self.hero.posX * self.step, self.hero.posY * self.step, self.direction)

    # draw skeletons
    def display_skeleton(self):
        for i in self.skeleton:
            self.view.draw_skeleton(i.posX * self.step, i.posY * self.step)

    # draw boss
    def display_boss(self):
        self.view.draw_boss(self.boss.posX * self.step, self.boss.posY * self.step)

    # input handling
    def input_handling(self):
        self.view.root.bind('<Up>', self.move_up_hero)
        self.view.root.bind('<Down>', self.move_down_hero)
        self.view.root.bind('<Left>', self.move_left_hero)
        self.view.root.bind('<Right>', self.move_right_hero)

    # moving hero
    def move_up_hero(self, event):
        if self.hero.posY - 1 < 0 or self.area.game_area[self.hero.posY - 1][self.hero.posX] == '1':
            self.direction = 'up'
            self.game()
        else:
            self.hero.posY -= 1
            self.direction = 'up'
            self.game()

    def move_down_hero(self, event):
        if self.hero.posY + 1 > 10 or self.area.game_area[self.hero.posY + 1][self.hero.posX] == '1':
            self.direction = 'down'
            self.game()

        else:
            self.hero.posY += 1
            self.direction = 'down'
            self.game()

    def move_left_hero(self, event):
        if self.hero.posX - 1 < 0 or self.area.game_area[self.hero.posY][self.hero.posX - 1] == '1':
            self.direction = 'left'
            self.game()
        else:
            self.hero.posX -= 1
            self.direction = 'left'
            self.game()

    def move_right_hero(self, event):
        if self.hero.posX + 1 > 9 or self.area.game_area[self.hero.posY][self.hero.posX + 1] == '1':
            self.direction = 'right'
            self.game()
        else:
            self.hero.posX += 1
            self.direction = 'right'
            self.game()

    def move_skeleton(self):
        i = len(self.skeleton)-1
        while i >= 0:
            direction = randint(0, 3)
            skel = self.skeleton[i]
            if direction == 0:
                if skel.posX - 1 > 0 and self.area.game_area[skel.posY][skel.posX - 1] != '1' and (skel.posX - 1, skel.posY) != (self.boss.posX, self.boss.posY):
                    self.skeleton[i].posX -= 1
                    i -= 1

            elif direction == 1:
                if skel.posY - 1 >= 0 and self.area.game_area[skel.posY - 1][skel.posX] != '1' and (skel.posX, skel.posY - 1) != (self.boss.posX, self.boss.posY):
                    self.skeleton[i].posY -= 1
                    i -= 1

            elif direction == 2:
                if skel.posX + 1 < 9 and self.area.game_area[skel.posY][skel.posX + 1] != '1' and (skel.posX + 1, skel.posY) != (self.boss.posX, self.boss.posY):
                    self.skeleton[i].posX += 1
                    i -= 1

            elif direction == 3:
                if skel.posY + 1 < 10 and self.area.game_area[skel.posY + 1][skel.posX] != '1' and (skel.posX, skel.posY + 1) != (self.boss.posX, self.boss.posY):
                    self.skeleton[i].posY += 1
                    i -= 1


game = Tkwanderer()
