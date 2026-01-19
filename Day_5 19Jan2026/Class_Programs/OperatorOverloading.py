class box1:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value
b1=box1(50)
b2=box1(100)
b3=box1(200)
print(b1+b2)
print(b1+b3)