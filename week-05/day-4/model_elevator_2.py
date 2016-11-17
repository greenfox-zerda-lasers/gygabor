# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Elevator:
    def __init__(self):
        self.number_of_people = 0
        self.max_number_people = 8
        self.storey = -1
        self.old_storey = 0
        self.elevator_high = 10
        self.elevator_min = 0


    def add_people(self, number):
        if number < self.max_number_people:
            self.number_of_people += number
            return True
        else:
            return False

    def remove_people(self, number):
        if number >= 0 and self.number_of_people - number >= 0:
            self.number_of_people -= number
            return True
        else:
            return False

    def position_handling(self, storey):
        if self.elevator_high < int(storey):
            return False
        else:
            self.old_storey = self.storey
            self.storey = storey
            return True
