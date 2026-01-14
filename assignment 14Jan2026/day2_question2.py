class Employee:
    def __set__(self,name,salary):
        self.name=name
        self.salary=salary
    def __get__(self,name,salary):
        return self.salary,self.name

class Test:
    x