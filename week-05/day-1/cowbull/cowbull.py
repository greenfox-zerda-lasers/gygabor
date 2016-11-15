import random

class Cab():


    def __init__(self):

        self.number = random_number()
        print (self.number)

    def random_number(self):
        number = []
        while len(number) != 4:
            j = random.randrange(0, 9)
            if not j in number:
                number.append(j)
            return number

    def which_state(self, result):
        if result is True:
            state = 'finished'
        else:
            state = 'playing'
        return state

    def count_guess(self):
        return count += 1

    def user_guess(self):
        


number = Cab()
