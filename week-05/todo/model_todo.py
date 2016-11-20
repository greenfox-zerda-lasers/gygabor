import os.path, csv

class Process:

    def __init__(self):
        self.task_list = []
        self.exist = True
        self.index = 0
        self.line = 0
        self.read = []

    def add_item(self, task):
        print (task)
        if os.path.exists('tasks.csv') == False:
            with open('tasks.csv', 'w', newline='') as csvfile:
                f = csv.writer(csvfile, delimiter=',')
                print(f.line_num)
                f.writerow([1, task, '0'])
                csvfile.close()
        else:
            with open('tasks.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in enumerate(reader):
                    self.index = row[0] + 2
                csvfile.close()
            with open('tasks.csv', 'a', newline='') as csvfile:
                f = csv.writer(csvfile, delimiter=',')
                f.writerow([self.index, task, '0'])

                csvfile.close()

    def remove_item(self, index):
        # print (int(index[0]))
        with open('tasks.csv', 'r') as csvfile:

            self.read = csvfile.read()
        print (self.read)
            # for row in f:
            #     if int(row[0]) == int(index[0]):
            #         self.line = row[0]
            # csvfile.close()
        csvfile.close()
        with open('tasks.csv', 'w') as csvfile:
            f = csv.writer(csvfile)
            for row in self.read:
                print(row)
                if index == self.read[0]:
                    self.read.pop(row)
            for i in self.read:
                f.writerow([i])
            csvfile.close()

    def list_item(self):
        if os.path.exists('tasks.csv') == False:
            self.exist = False
        else:
            f = open('tasks.csv', 'r')
            self.task_list = f.read()
            f.close()




    def check_item(self):
        pass
