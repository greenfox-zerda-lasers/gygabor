import os.path, csv

class Process:

    def __init__(self):
        self.task_list = []
        self.exist = True
        self.index = 0

    def add_item(self, task):
        if os.path.exists('tasks.csv') == False:

            with open('tasks.csv', 'w', newline='') as csvfile:
                f = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                f.writerow(task)
        else:

            with open('tasks.csv', 'ar', newline='') as csvfile:
                

                f = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                f.writerow(task)

    def remove_item(self):
        pass

    def list_item(self):
        if os.path.exists('tasks.csv') == False:
            self.exist = False
        else:
            f = open('tasks.csv', 'r')
            self.task_list = f.read()
            f.close()


    def doing_item(self):
        pass

    def review_item(self):
        pass

    def done_item(self):
        pass

    def write_file(self):
        pass

    def read_file(self):
        pass
