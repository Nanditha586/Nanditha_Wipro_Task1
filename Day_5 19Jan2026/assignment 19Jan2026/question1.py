class Vehicle:
    def start(self):
        print("This is base class Vehicle")
#single inheritance
class Car(Vehicle):
    count=0
    def __init__(self,name):
        self.name=name
        Car.count+=1
        print("Car Name=",self.name)

    def starting(self):
        print("this is the starting class")
#multiple inheritance
class Model(Car):
    def model_name(self,name):
        self.name=name
        print("model of the car is=",self.name)

m=Model("Hyundai")
m.start()
m.starting()
m.model_name("San")

c=Model("Suzuki")
c.start()
c.starting()
c.model_name("Swift")

print("Count=",Car.count)