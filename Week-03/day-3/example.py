class Rectangle():
  a = 0
  b = 0

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def get_circumference(self):
    return self.a * 2 + self.b * 2

rect1 = Rectangle(40, 50)
rect2 = Rectangle(20, 30)
print(rect1.get_circumference())
print(rect2.get_circumference())
