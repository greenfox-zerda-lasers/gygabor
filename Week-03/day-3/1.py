# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle:
    def __init__(self, radius):
       self.radius = radius

    def get_circumference(self):
        return (2 * self.radius)*3.14

    def get_area(self):
        return self.radius * self.radius * 3.14

circle = Circle(4)
print(circle.get_circumference())
print(circle.get_area())
