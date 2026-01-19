class Calculator():
    def calculate(self,a,b):
        print("Calculator class addition=",a+b)

class AdvancedCalculator(Calculator):
    def calculate(self,a,b):
        print("Advanced class multiplication=",a*b)
obj=[Calculator(),AdvancedCalculator()]
for o in obj:
    o.calculate(7,5)

class Custom:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value + other.value
c1=Custom(52)
c2=Custom(53)
print(c1+c2)
