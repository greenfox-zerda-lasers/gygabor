import sys, getopt

class Item:
    pass

    def __init__(self):
        pass

    def io_handling(self):
        try:
            self.opts, self.args = getopt.getopt(sys.argv[1:], 'l:a:r:c')
        except getopt.GetoptError:
            print('err')
            # usage()
            # sys.exit()

        for o,a in self.opts:
            if o == '-l':
                print(a)
            if o == '-a':
                print(a)
            if o == '-r':
                print(a)
            if o == '-c':
                print(a)
            else:
                print('err')
                # usage()
                # sys.exit()

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def list_item(self):
        pass

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


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
