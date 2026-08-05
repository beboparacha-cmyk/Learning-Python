from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def move(self):
        print("I can crawl and bark")
    
class Cat(Animal):
    def move(self):
        print("I can crawl and meow")
    
class Cow(Animal):
    def move(self):
        print("I can crawl and Moo")

class Human(Animal):
    def move(self):
        print("I can walk/run and talk")

D = Dog()
D.move()

C = Cat()
C.move()

M = Cow()
M.move()

H = Human()
H.move()  