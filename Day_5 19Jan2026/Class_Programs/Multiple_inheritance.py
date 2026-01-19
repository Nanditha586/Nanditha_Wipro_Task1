#python takes method resolution order i.which ever class is defined first that methods are called
class A:
    def showA(self):
        print("showA")
class B:
    def showB(self):
        print("showB")
    def showA(self):
        print("showA in C class")
class C(B,A):
    def showC(self):
        print("showC")

c=C()
c.showA()
c.showB()
c.showC()
