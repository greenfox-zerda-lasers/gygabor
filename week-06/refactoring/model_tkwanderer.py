import csv
from random import randint, choice

class Area:

    def __init__(self):
        self.game_area = []
        self.read_area()

    # read Area map from area.csv
    def read_area(self):
        with open('../area.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                self.game_area.append(i[0].split(';'))
            csvfile.close()

class Character:
    def __init__(self):
        self.position = [0, 0]
        self.temp_pos = []
        self.health = 0
        self.defend = 0
        self.strike = 0
        self.key = 0
        self.level = 1
        self.direction = ''

    def pos(self, character_list, area):
        self.character_list = character_list
        self.area = area
        self.check_position = False
        while self.check_position == False:
            self.step()
            self.check_position = self.step_check()

    def step(self):
        if self.direction == '':
            self.position[0] = randint(0, 9)
            self.position[1] = randint(0, 10)
        elif self.direction == 'down':
            self.position[1] += 1
        elif self.direction == 'up':
            self.position[1] -= 1
        elif self.direction == 'left':
            self.position[0] -= 1
        elif self.direction == 'right':
            self.position[0] += 1

    def step_check(self):
        if self.direction == '':
            if self.area.game_area[self.position[1]][self.position[0]] == '0':
                for character in self.character_list:
                    if (self.position[0], self.position[1]) != (character.position[0], character.position[1]):
                        return True
            else:
                return False
        elif self.direction == 'down':
            if self.position[1] > 10 or self.area.game_area[self.position[1]][self.position[0]] == '1':
                self.position[1] -= 1
                return True
        elif self.direction == 'up':
            if self.position[1] < 0 or self.area.game_area[self.position[1]][self.position[0]] == '1':
                self.position[1] += 1
                return True
        elif self.direction == 'left':
            if self.position[0] < 0 or self.area.game_area[self.position[1]][self.position[0]] == '1':
                self.position[0] += 1
                return True
        elif self.direction == 'right':
            if self.position[0] > 9 or self.area.game_area[self.position[1]][self.position[0]] == '1':
                self.position[0] -= 1

            # else:
            #     for i in self.character_list:
            #         if (self.position[0], self.position[1]) == (i.position[0], i.position[1]):
            #             self.battle()
            #     return True

    def battle(self):
        pass
class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__()
        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)
        self.direction = 'down'

    def move_hero(self, direction, character_list, area):
        self.direction = direction
        self.pos(character_list, area)

class Boss(Character):
    def __init__(self, character_list, area):
        super(Boss, self).__init__()
        self.area = area
        self.character_list = character_list
        self.health = (2 * self.level * randint(1, 6)) + randint(1, 6)
        self.defend = (self.level // 2 * randint(1, 6)) + randint(1, 6) // 2
        self.strike = self.level * randint(1, 6) + self.level
        self.pos(character_list, self.area)

    def move_boss(self, character_list):
        self.direction = choice('up down left right'.split())
        self.pos(character_list, self.area)
        self.step_count = 0

class Skeleton(Character):
    def __init__(self, character_list, area):
        super(Skeleton, self).__init__()
        self.health = 2 * self.level * randint(1, 6)
        self.defend = self.level // 2 * randint(1, 6)
        self.strike = self.level * randint(1, 6)
        self.pos(character_list, area)
#     def boss_kill(self):
#         del self
#
# class Battle:
#
#     def battle_handling(self, fighters_list):
#         self.hero = fighters_list[0]
#         self.enemy = fighters_list[1]
#         self.hero_strike = self.hero.strike + 2 * randint(1, 6)
#         self.enemy_strike = self.enemy.strike + 2 * randint(1, 6)
#         while self.hero.health > 0 and self.enemy.health > 0:
#             self.enemy.health -= self.hero_strike - self.enemy.defend
#             self.hero.health -= self.enemy_strike - self.hero.defend
#             self.hero.key = self.enemy.key
#         fighters_list = [self.hero, self.enemy]
#         return fighters_list
