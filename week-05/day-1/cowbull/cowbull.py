import random

class Player:
    def __init__(self):
        self.name = ''
        self.state = 'playing'

class Cab:

    def __init__(self, player):
        self.player = player
        self.number = []
        self.guess_number = ''
        self.game_running = False
        self.cows = 0
        self.bulls = 0

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
                self.game_running = False
                self.state = 'finished'
                self.restart()
            else:
                print('cows: ' + str(self.cows))
                print('bulls: ' + str(self.bulls))
                self.cows = 0
                self.bulls = 0
                self.user_guess()

    def user_guess(self):
        self.guess_number = list(input('Give me a four digit number (press \'q\', if you want to quit+):'))
        if 'q' in self.guess_number:
            self.restart()
        elif len(self.guess_number) > 3:
            print ('Only four digits please!')
            self.game_loop()
        elif self.guess_number.isdigit() == False:
            print ('Only digits please!')
            self.game_loop()

        for j in range(len(self.guess_number)):

            if self.guess_number[j] in self.number:

                if self.guess_number[j] == self.number[j]:
                    self.cows += 1
                else:
                    self.bulls += 1

    def restart(self):
        while not self.game_running:
            print('Do you want restart the game?' )
            answer = str(input('(Y)es or (N)o?'))
            if answer.lower() == 'n':
                self.start()
            elif answer.lower() == 'y':
                print( 'see_ya' )
                self.game_running = False
                break
            else:
                print( 'false_yn' )



player = Player()
game = Cab(player)
