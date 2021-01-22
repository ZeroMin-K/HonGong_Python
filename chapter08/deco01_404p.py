import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("Length is only positive")
        self.__radius = value

circle = Circle(10)
print("radius:", circle.radius)
circle.radius = 2
print("radius2:", circle.radius)

circle.radius = -10