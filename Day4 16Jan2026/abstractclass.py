#abstract can have both abstract methods and normal methods
#Normal class cannot have abstract methods
#the abstract method defination can be implemented in other class but not in abstract class
from abc import ABC,abstractmethod
class shape(ABC):
    def display(self):
        print("This is non abstract method")
    @abstractmethod
    def area(self):
        print("abstract nethod")
class rectangle(shape):
    def area(self):
        print("Area Method")

r=rectangle()
r.area()
r.display()