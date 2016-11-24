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
        self.key =key
        self.level = level

    # !!!!MOVE FUNCTION WILL BE HERE!!!!

class Hero(Character):
    def __init__(self, posX, posY, level, key):
        super(Hero, self).__init__(posX, posY, level, key)

        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)

class Skeleton(Character):
    def __init__(self,posX, posY, level, key):
        super(Skeleton, self).__init__(posX, posY, level, key)

        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)

    def moving_position(self, skeleton, area, boss):
        i = True
        while i:
            direction = randint(0, 3)
            if direction == 0:
                if skeleton.posX - 1 > 0 and area[skeleton.posY][skeleton.posX - 1] != '1' and (skeleton.posX - 1, skeleton.posY) != (boss.posX, boss.posY):
                    skeleton.posX -= 1
                    i = False
            elif direction == 1:
                if skeleton.posY - 1 >= 0 and area[skeleton.posY - 1][skeleton.posX] != '1' and (skeleton.posX, skeleton.posY - 1) != (boss.posX, boss.posY):
                    skeleton.posY -= 1
                    i = False
            elif direction == 2:
                if skeleton.posX + 1 < 9 and area[skeleton.posY][skeleton.posX + 1] != '1' and (skeleton.posX + 1, skeleton.posY) != (boss.posX, boss.posY):
                    skeleton.posX += 1
                    i = False
            elif direction == 3:
                if skeleton.posY + 1 < 10 and area[skeleton.posY + 1][skeleton.posX] != '1' and (skeleton.posX, skeleton.posY + 1) != (boss.posX, boss.posY):
                    skeleton.posY += 1
                    i = False
        return skeleton


class Boss(Character):
    def __init__(self, posX, posY, level, key):
        super(Boss, self).__init__(posX, posY, level, key)

        self.health = 20 + 3 * randint(1, 6)
        self.defend = 2 * randint(1, 6)
        self.strike = 5 + randint(1, 6)

    def moving_position(self, boss, area, skeleton):
        i = True

        while i:
            direction = randint(0, 3)
            if direction == 0:
                if boss.posX - 1 > 0 and area[boss.posY][boss.posX - 1] != '1' and (boss.posX - 1, boss.posY) not in skeleton:
                    boss.posX -= 1
                    i = False

            elif direction == 1:
                if boss.posY - 1 >= 0 and area[boss.posY - 1][boss.posX] != '1' and (boss.posX, boss.posY - 1) not in skeleton:
                    boss.posY -= 1
                    i = False

            elif direction == 2:
                if boss.posX + 1 < 9 and area[boss.posY][boss.posX + 1] != '1' and (boss.posX + 1, boss.posY) not in skeleton:
                    boss.posX += 1
                    i = False

            elif direction == 3:
                if boss.posY + 1 < 10 and area[boss.posY + 1][boss.posX] != '1' and (boss.posX, boss.posY + 1) not in skeleton:
                    boss.posY += 1
                    i = False

        return boss
