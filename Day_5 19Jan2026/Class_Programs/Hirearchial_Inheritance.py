class A:
    def showA(self):
        print("showA")
class B(A):
    def showB(self):
        print("showB")
class C(A):
    def showC(self):
        print("showC")

b=B()
b.showA()
b.showB()
c=C()
c.showA()
c.showC()
