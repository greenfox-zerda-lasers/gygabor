import random

class Player:
    def __init__(self):
        self.name = ''
        self.state = 'playing'

class Cab:

    def __init__(self, player):
        self.player = player
        self.number = []
        self.guess = -1
        self.guess_number = -1
        self.game_running = False
        self.cows = 0
        self.bulls = 0
        self.guess_count = 0

        self.start()

    def start(self):
        self.game_running = True
        while len(self.number) != 4:
            j = random.choice('0123456789')
            if not j in self.number:
                self.number.append(j)

        print ( 'What\'s your name?' )
        self.player_name = input()
        self.game_loop()

    def game_loop(self):
        print (self.number)
        while self.game_running:
            if self.number == self.guess_number:
                print( 'You win!' )
                print(self.guess_count )
                self.game_running = False
                self.state = 'finished'
                self.guess_count += 1
                self.restart()
            else:
                print('cows: ' + str(self.cows))
                print('bulls: ' + str(self.bulls))

                self.guess_count += 1
                self.user_guess()

    def user_guess(self):
        self.guess_number = list(input('Give me a four digit number:'))
        self.cows += 0
        self.bulls += 0
        for j in range(len(self.guess_number)):
            print(self.guess_number)
            print(self.number)
            if self.guess_number[j] in self.number:

                if self.guess_number[j] == self.number[j]:
                    self.cows += 1
                else:
                    self.bulls += 1


    def restart(self):
        while not self.game_running:
            print('restart_question' )
            answer = str(input('(Y)es or (N)o?'))
            if answer.lower() == 'y':
                self.start()
            elif answer.lower() == 'n':
                print( 'see_ya' )
                break # END OF GAME
            else:
                print( 'false_yn' )



player = Player()
game = Cab(player)
