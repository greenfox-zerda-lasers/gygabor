import sys, getopt, model_todo, view_todo

class Todo:


    def __init__(self):
        self.model = model_todo.Process()
        self.view = view_todo.View()
        self.task = []

        self.io_handling()

    def io_handling(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "larc")
        except getopt.GetoptError as err:
            print (str(err))
            sys.exit(2)

        for a in opts:
            if a == ('-l', ''):
                self.model.list_item()
                self.view.dis_list(self.model.task_list, self.model.exist)
            elif a == ('-a', ''):
                self.task.append(input('Give me a task:'))
                self.model.add_item(self.task)
            elif a == '-r':
                pass
            elif a == '-c':
                pass
            else:
                assert False, "unhandled option"
                sys.exit(1)

user_day = Todo()
