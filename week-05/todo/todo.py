import os.path

class Process:

    def __init__(self):
        self.task_list = []
        self.exist = True

    def add_item(self, task):
        if os.path.exists('tasks.csv') == False:
            f = open('tasks.csv', 'w')
            f.write(str(task))
            f.close
        else:
            f = open('tasks.csv', 'a')
            f.write(str(task))
            f.close


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
