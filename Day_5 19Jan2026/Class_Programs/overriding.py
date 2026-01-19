class Animal:
    def sound(self):
        print("Animal's sound")
class Dog(Animal):
    def sound(self):
        print("Dog's sound")
class Cat(Animal):
    def sound(self):
        print("Cat's sound")
obj=[Dog(),Cat()]
for i in obj:
    i.sound()

