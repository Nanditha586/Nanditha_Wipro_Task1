#class is the blue print
#object is the instance of the class
class Student:
    def display(self):
        print("this is the student class")
s1=Student()
s1.display()

class Calculator:
    def add(self,a,b):
        print("sum=",a+b)
c=Calculator()
c.add(5,6)
