from abc import ABC, abstractmethod
from math import pow, sqrt

class CalculatorInterface(ABC):
    @abstractmethod
    def add(self, x, y):
        pass
    
    @abstractmethod
    def subtract(self, x, y):
        pass
    
    @abstractmethod
    def multiply(self, x, y):
        pass
    
    @abstractmethod
    def divide(self, x, y):
        pass
    
    @abstractmethod
    def power(self, x, y):
        pass
    
    @abstractmethod
    def square_root(self, x):
        pass


class BaseCalculator(CalculatorInterface):
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y


class MathCalculator(BaseCalculator):
    def power(self, x, y):
        return pow(x, y)
    
    def square_root(self, x):
        return sqrt(x)


class MagicCalculator(MathCalculator):
    def __init__(self):
        self._result = 0
    
    def __str__(self):
        return str(self._result)
    
    def __add__(self, num):
        self._result = self.add(self._result, num)

    def __sub__(self, num):
        self._result = self.subtract(self._result, num)

    def __mul__(self, num):
        self._result = self.multiply(self._result, num)
    
    def __truediv__(self, num):
        self._result = self.divide(self._result, num)

    def __pow__(self, num):
        self._result = self.power(self._result, num)

    def __sqrt__(self):
        self._result = self.square_root(self._result)


calculator = MagicCalculator()
print(calculator)  

calculator.__add__(5)
print(calculator) 

calculator.__mul__(2)
print(calculator)  

calculator.__sqrt__()
print(calculator) 
