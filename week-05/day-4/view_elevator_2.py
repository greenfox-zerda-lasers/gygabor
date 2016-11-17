# Create a class the displays the Elevator art and navigation (list of commands)
import os

class Display:

    def draw_elevator(self, max_storey, elevator_storey, people_number):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('___________________________________')
        print('`._______________________________.\'')
        for i in range(max_storey, -1, -1):
            if i != 0 and i != elevator_storey:
                print ('  || ||       || ||       || ||')
            elif i != 0 and i == elevator_storey and people_number != 0:
                print ('  || || [_X_] || ||       || || ')
            elif i != 0 and i == elevator_storey and people_number == 0:
                print ('  || || [___] || ||       || || ')
            elif i == 0 and elevator_storey != i:
                print (' _||_||_______||_||_______||_||_')
            elif i == 0 and elevator_storey == i and people_number != 0:
                print (' _||_||_[_X_]_||_||_______||_||_')
            elif i == 0 and elevator_storey == i and people_number == 0:
                print (' _||_||_[___]_||_||_______||_||_')
        print('.\'_______________________________`.')
        print(people_number, ' people are in the elevator.')


    def display_options(self):

        print('____________________________')
        print('Choose an option:')
        print('[a] - add people')
        print('[r] - remove people')
        print('[0-9] - select storey')
        print('[q] - quit')
        print('____________________________')
