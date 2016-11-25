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

    def start_pos(self, area, hero):
        self.hero = hero
        self.area = area
        i = False
        position = []
        while i == False:
            posX = randint(0, 9)
            posY = randint(0, 10)
            if self.area[posY][posX] == '0' and (posX, posY) != (self.hero.posX, self.hero.posY):
                i = True
        position.append(posX)
        position.append(posY)
        print(position)
        return position

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
        self.hero = fighters_list[0]
        self.enemy = fighters_list[1]
        self.hero_strike = self.hero.strike + 2 * randint(1, 6)
        self.enemy_strike = self.enemy.strike + 2 * randint(1, 6)
        while self.hero.health > 0 and self.enemy.health > 0:
            self.enemy.health -= self.hero_strike - self.enemy.defend
            self.hero.health -= self.enemy_strike - self.hero.defend
            self.hero.key = self.enemy.key
        fighters_list = [self.hero, self.enemy]
        return fighters_list
