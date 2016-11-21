import csv

class Map:

    def __init__(self):
        self.game_map = []

    def read_map(self):
        with open('map.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for i in reader:
                self.game_map.append(i[0].split(';'))
            csvfile.close()
