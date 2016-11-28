import csv
from random import randint

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
        self.posX = 0
        self.posY = 0
        self.health = 0
        self.defend = 0
        self.strike = 0
        self.key = 0
        self.level = 1

    def pos(self, character_list, area):
        self.character_list = character_list
        self.area = area
        i = False
        position = []
        while i == False:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area.game_area[posY][posX] == '0' and (posX, posY) != (0, 0) and (posX, posY) != (self.character_list[i - 1].posX, self.character_list[i - 1].posY):
                    i = True
        position.append(posX)
        position.append(posY)
        return position


class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__()
        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)

class Boss(Character):
    def __init__(self, character_list, area):
        super(Boss, self).__init__()
        self.character_list = character_list
        self.health = 2 * randint(1, 6)
        self.defend = randint(1, 6)
        self.strike = randint(1, 6)
        position = self.pos(character_list, area)
        self.posX = position[0]
        self.posY = position[1]

class Skeleton(Character):
    def __init__(self, character_list, area):
        super(Skeleton, self).__init__()
        self.health = 2 * randint(1, 6)
        self.defend = randint(1, 6)
        self.strike = randint(1, 6)
        position = self.pos(character_list, area)
        self.posX = position[0]
        self.posY = position[1]

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
