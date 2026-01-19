class calc:
    def add(self,a,b=0.,c=0):
        return a+b+c
c=calc()
print(c.add(5))
print(c.add(1,2))
print(c.add(3,4,8))