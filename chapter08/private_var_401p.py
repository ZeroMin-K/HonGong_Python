import math 

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
circle = Circle(10)
print("circumference:", circle.get_circumference())
print("area:", circle.get_area())
print(circle.__radius)