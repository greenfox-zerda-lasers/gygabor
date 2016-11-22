import csv

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

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

class Hero(Character):
    pass
