import csv
from random import randint

class Area:

    def __init__(self):
        self.game_area = []

    # read Area map from area.csv
    def read_area(self):
        with open('area.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                self.game_area.append(i[0].split(';'))
            csvfile.close()

class Character:
    def __init__(self, posX, posY, level, key):
        self.posX = posX
        self.posY = posY
        self.health = 0
        self.defend = 0
        self.strike = 0
        self.key = key
        self.level = level

    def move_character(self, character, area):
        i = True
        while i:
            direction = randint(0, 3)
            if direction == 0:
                if character.posX - 1 > 0 and area[character.posY][character.posX - 1] != '1':
                    character.posX -= 1
                    i = False
            elif direction == 1:
                if character.posY - 1 >= 0 and area[character.posY - 1][character.posX] != '1':
                    character.posY -= 1
                    i = False
            elif direction == 2:
                if character.posX + 1 < 9 and area[character.posY][character.posX + 1] != '1':
                    character.posX += 1
                    i = False
            elif direction == 3:
                if character.posY + 1 < 10 and area[character.posY + 1][character.posX] != '1':
                    character.posY += 1
                    i = False
        return character

class Hero(Character):
    def __init__(self, posX, posY, level, key):
        super(Hero, self).__init__(posX, posY, level, key)

        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)

    def hero_level_up(self):
        self.health += randint(1, 6)
        self.defend += randint(1, 6)
        self.defend += randint(1, 6)

class Skeleton(Character):
    def __init__(self,posX, posY, level, key):
        super(Skeleton, self).__init__(posX, posY, level, key)

        self.health = 2 * self.level * randint(1, 6)
        self.defend = self.level // 2 * randint(1, 6)
        self.strike = self.level * randint(1, 6)

class Boss(Character):
    def __init__(self, posX, posY, level, key):
        super(Boss, self).__init__(posX, posY, level, key)

        self.health = (2 * self.level * randint(1, 6)) + randint(1, 6)
        self.defend = (self.level // 2 * randint(1, 6)) + randint(1, 6) // 2
        self.strike = self.level * randint(1, 6) + self.level

    def boss_kill(self):
        del self

class Battle:

    def battle_handling(self, fighters_list):
        hero = fighters_list[0]
        enemy = fighters_list[1]
        hero_strike = hero.strike + 2 * randint(1, 6)
        enemy_strike = enemy.strike + 2 * randint(1, 6)
        while hero.health > 0 and enemy.health > 0:
            enemy.health -= hero_strike - enemy.defend
            hero.health -= enemy_strike - hero.defend
            hero.key = enemy.key
        fighters_list = [hero, enemy]
        return fighters_list
