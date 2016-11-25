import model_tkwanderer, view_tkwanderer
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
        self.boss = ''
        self.boss_exist = True
        self.move_enemy = 1

        self.start()

    def start(self):
        self.display_area()
        self.boss_instantiate()
        self.skeleton_instantiate()
        self.game()

    def game(self):
        self.view.canvas.delete('hero', 'skeleton', 'boss', 'stat', 'skeleton_stat')
        self.display_character()
        self.display_stats()
        self.input_handling()
        self.battle_process()

        self.view.show()

    # instantiate boss
    def boss_instantiate(self):
        position = self.hero.start_pos(self.area.game_area, self.hero)
        self.boss = model_tkwanderer.Boss(position[0], position[1], self.level, self.key)

    # instantiate skeleton
    def skeleton_instantiate(self):
        for i in range(self.skeleton_number):
            position = self.hero.start_pos(self.area.game_area, self.hero)
            j = model_tkwanderer.Skeleton(position[0], position[1], self.level, self.key)
            self.skeleton.append(j)
            self.skeleton[0].key = 1

    # draw area
    def display_area(self):
        self.area.read_area()
        self.view.draw_area(self.area.game_area)

    def display_character(self):
        self.view.draw_hero(self.hero.posX * self.step, self.hero.posY * self.step, self.direction)

        if self.move_enemy == 2:
            print(self.move_enemy)
            self.move_skeleton()
            if self.boss_exist == True:
                self.move_boss()
            self.move_enemy = 0
        elif self.move_enemy == 0:
            self.move_enemy = 1

        for i in self.skeleton:
            self.view.draw_skeleton(i.posX * self.step, i.posY * self.step)
        if self.boss_exist == True:
            self.view.draw_boss(self.boss.posX * self.step, self.boss.posY * self.step)

    # draw stats
    def display_stats(self):
        if self.boss_exist == True:
            characters = [self.hero, self.boss]
        else:
            characters = [self.hero]
        self.view.draw_stats(characters, self.skeleton)

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
            self.skeleton[i] = self.skeleton[i].move_character(self.skeleton[i], self.area.game_area)

    def move_boss(self):
            self.boss = self.boss.move_character(self.boss, self.area.game_area)

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
                break
        if self.boss_exist == True and (self.hero.posX, self.hero.posY) == (self.boss.posX, self.boss.posY):
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
                break
        if self.boss.health <= 0:
            del self.boss
            self.boss_exist = False

    def game_end(self):
        print('game over')

game = Tkwanderer()
