class View:

    def dis_list(self, task_list, f_exist):
        if f_exist is False:
            print('No todos for today!')
        else:
            print(task_list)
