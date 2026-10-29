#Write a program to create a base class that consists of two functions -
# one to display a value, and another function is an abstract method. 
#Next, create a subclass that consists of a method similar to the 
#abstract method. 
#Finally, showcase how Abstraction is being implemented in this example.

from abc import ABC , abstractmethod
class Numbers(ABC):
    def display(self):
        print(11)
    @abstractmethod
    def show(self):
        pass
class Roman_Numbers(Numbers):
    def show(self):
        print("XI")

num = Roman_Numbers()
num.show()
