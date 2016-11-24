import model_tkwanderer_old2, view_tkwanderer_old2
from random import randint

class Tkwanderer:

    def __init__(self):
        self.level = 1
        self.key = 0
        self.view = view_tkwanderer.Display()
        self.area = model_tkwanderer.Area()
        self.hero = model_tkwanderer.Hero(0, 0, self.level, self.key)
        self.battle = model_tkwanderer.Battle()
        self.area_read = []
        self.direction = 'down'
        self.skeleton_number = 3
        self.skeleton = []
        self.step = 50
        self.boss_exist = False
        self.boss = ''
        self.move_enemy = 1

        self.start()

    def start(self):
        self.display_area()
        self.boss_instantiate()
        self.skeleton_instantiate()
        self.game()

    def game(self):
        self.view.canvas.delete('hero', 'skeleton', 'boss', 'hero_stat', 'skeleton_stat', 'boss_stat')
        self.display_hero()

        if self.move_enemy == 2:
            self.move_skeleton()
            self.move_boss()
            self.move_enemy = 0
        elif self.move_enemy == 0:
            self.move_enemy = 1

        self.display_boss()
        self.display_skeleton()
        self.display_stats()
        self.input_handling()
        self.battle_process()

        self.view.show()

    # instantiate boss
    def boss_instantiate(self):
        while self.boss_exist == False:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area.game_area[posY][posX] == '0' and (posX, posY) != (self.hero.posX, self.hero.posY):
                self.boss = model_tkwanderer.Boss(posX, posY, self.level, self.key)
                self.boss_exist = True

    # instantiate skeleton
    def skeleton_instantiate(self):
        while self.skeleton_number > 0:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area.game_area[posY][posX] == '0' and (posX, posY) != (self.hero.posX, self.hero.posY) and (posX, posY) != (self.boss.posX, self.boss.posY):
                if self.skeleton_number == 1:
                    self.key = 1
                else:
                    self.key = 0
                i = model_tkwanderer.Skeleton(posX, posY, self.level, self.key)
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

    # draw stats
    def display_stats(self):
        self.view.draw_stats(self.hero, self.skeleton, self.boss)

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
            self.move_enemy += 1
            self.game()

    def move_down_hero(self, event):
        if self.hero.posY + 1 > 10 or self.area.game_area[self.hero.posY + 1][self.hero.posX] == '1':
            self.direction = 'down'
            self.game()
        else:
            self.hero.posY += 1
            self.direction = 'down'
            self.move_enemy += 1
            self.game()

    def move_left_hero(self, event):
        if self.hero.posX - 1 < 0 or self.area.game_area[self.hero.posY][self.hero.posX - 1] == '1':
            self.direction = 'left'
            self.game()
        else:
            self.hero.posX -= 1
            self.direction = 'left'
            self.move_enemy += 1
            self.game()

    def move_right_hero(self, event):
        if self.hero.posX + 1 > 9 or self.area.game_area[self.hero.posY][self.hero.posX + 1] == '1':
            self.direction = 'right'
            self.game()
        else:
            self.hero.posX += 1
            self.direction = 'right'
            self.move_enemy += 1
            self.game()

    def move_skeleton(self):
        for i in range(len(self.skeleton)):
            self.skeleton[i] = self.skeleton[i].moving_position(self.skeleton[i], self.area.game_area, self.boss)

    def move_boss(self):
            self.boss = self.boss.moving_position(self.boss, self.area.game_area, self.skeleton)

    def battle_process(self):
        battle_list = []
        battle_list.append(self.hero)
        for i in range(len(self.skeleton)):
            if (self.hero.posX, self.hero.posY) == (self.skeleton[i].posX, self.skeleton[i].posY):
                battle_list.append(self.skeleton[i])
                battle_list = self.battle.battle_handling(battle_list)
                self.hero = battle_list[0]
                self.skeleton[i] = battle_list[1]
                self.level_up()
        if (self.hero.posX, self.hero.posY) == (self.boss.posX, self.boss.posY):
            battle_list.append(self.boss)
            battle_list = self.battle.battle_handling(battle_list)
            self.hero = battle_list[0]
            self.boss = battle_list[1]
            self.level_up()

    def level_up(self):
        if self.hero.health == 0:
            self.game_end()
        else:
            self.hero.hero_level_up()
        for i in range(len(self.skeleton)):
            if self.skeleton[i].health <= 0:
                self.skeleton.pop(i)
        if self.boss.health <= 0:




    def game_end(self):
        print('game over')

game = Tkwanderer()
