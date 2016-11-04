# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student:

    def __init__(self):
        self.grade = []
        self.summa = 0

    def add_grade(self, grade):
        if grade <= 5:
            self.grade.append(grade)
        else:
            print ('invalid number')

    def get_average(self):
        for i in self.grade:
            self.summa += i

        return (self.summa / len(self.grade))

joe = Student()
joe.add_grade(4)
joe.add_grade(2)
joe.add_grade(6)
joe.add_grade(2)
joe.add_grade(4)


print(joe.get_average())
