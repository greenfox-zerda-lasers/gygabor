# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects
import view_elevator, model_elevator, os, time

class Controller:

    def __init__(self):
        self.running = False
        self.elevator = view_elevator.Display()
        self.model = model_elevator.Elevator()
        self.input_letter = ''
        self.new_storey = 0
        self.people_number = 0
        self.position = True
        self.people_number_check = True

        self.input_handling()

    def input_handling(self):

        self.running = True
        while self.running:

            if 
            self.elevator.draw_elevator(self.model.elevator_high, int(self.model.elevator_storey), self.model.number_of_people)
            self.model.elevator_storey += 1
            self.elevator.draw_elevator(self.model.elevator_high, int(self.model.elevator_storey), self.model.number_of_people)
            self.position = self.model.position_handling(self.input_letter)


            self.elevator.display_options()

            self.input_letter = input()

            if self.input_letter == 'a':
                self.people_number = int(input('How many people do you want to add?'))
                self.people_number_check = self.model.add_people(self.people_number)
                if self.people_number_check:
                    print (self.people_number, ' people added.')
                else:
                    print ('Too many people! Maximum number of people: ', self.model.max_number_people)
                    input('Press Enter to continue')
            elif self.input_letter == 'r':
                self.people_number = int(input('How many people do you want to remove?'))
                self.people_number_check = self.model.remove_people(self.people_number)
                if self.people_number_check:
                    print (self.people_number, ' people removed.')
                else:
                    print ('Number of People can not be less than 0!')
                    input('Press Enter to continue')
            elif self.input_letter.isdigit():
                self.new_storey = int(self.input_letter)
                if self.position is False:
                    print('Wrong number! Accepted number is between ', 0,'-', self.model.elevator_high)
                    input('Press Enter to continue')
            elif self.input_letter == 'q':
                print( 'bye' )
                break
            else:
                print ('Not accepted letter. Please choose the proper option!')
                input('Press Enter to continue')

elevator = Controller()
