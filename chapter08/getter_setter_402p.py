import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.radius = value

circle = Circle(10)
print("circum:", circle.get_circumference())
print("area:", circle.get_area())

print(circle.get_radius())
circle.set_radius(2)

print("circum:", circle.get_circumference())
print("area:", circle.get_area())
