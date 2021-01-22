import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.radius
    def get_area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(10)
print("Circumference:", circle.get_circumference())
print("area:", circle.get_area())
