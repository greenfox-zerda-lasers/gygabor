from random_words import RandomWords
import os


class Game:

    def __init__(self):
        self.random_text = ''
        self.game_running = False
        self.result = []
        self.guess_false = 0

        self.start()

    def start(self):
        self.game_running = True
        self.guess_false = 0
        self.result = []
        rw = RandomWords()
        rw.random_word()
        self.random_text = rw.random_word()
        for i in range(len(self.random_text)):
            self.result.append('_')

        self.random_text = list(self.random_text)

        self.game_loop()

    def game_loop(self):
        while self.game_running:
            if self.guess_false == 6:
                self.game_running = False
                self.draw()
                self.restart()
            elif self.random_text == self.result:
                print(self.result)
                print('CONGRATULATION' )
                self.game_running = False
                self.restart()
            else:
                self.get_guess()


    def get_guess(self):
        self.draw()
        print (self.result)
        guess = str(input('Give me a letter:'))

        if guess in self.random_text:
            for i in range(len(self.random_text)):
                if guess == self.random_text[i]:
                    self.result[i] = guess
        else:
            self.guess_false += 1

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.guess_false == 0:
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            # print(self.random_text)
        elif self.guess_false == 1:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            # print(self.random_text)
        elif self.guess_false == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /       ")
            print ("|             ")
            print ("|             ")
            # print(self.random_text)
        elif self.guess_false == 3:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|      ")
            print ("|             ")
            print ("|             ")
        elif self.guess_false == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
        elif self.guess_false == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
            print ("GAME OVER!")

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

hangman_game = Game()
