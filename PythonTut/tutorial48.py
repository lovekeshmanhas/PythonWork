# abstract base class @abstractmethod
#from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod # 3.4+ python version

#class Shape(metaclass=ABCMeta):
class Shape(ABC):     # 3.4+ python version
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 4

    def printArea(self):
        return self.length * self.breadth

rect1 = Rectangle()

print(rect1.printArea())