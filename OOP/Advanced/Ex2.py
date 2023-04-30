from abc import ABC, abstractmethod
import math

class ShapeInterface(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Shape(ShapeInterface):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.name == other.name
        return False

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius



circle1 = Circle(5)
print("Circle 1 Area:", circle1.area())
print("Circle 1 Perimeter:", circle1.perimeter())

circle2 = Circle(7)
print("Circle 2 Area:", circle2.area())
print("Circle 2 Perimeter:", circle2.perimeter())

print("Circle 1 == Circle 2:", circle1.__eq__(circle2))

class Square(Shape):
    def __init__(self, side_length):
        super().__init__("Square")
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length

square = Square(3)
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())

print("Square == Circle 1:", square.__eq__(circle1))
