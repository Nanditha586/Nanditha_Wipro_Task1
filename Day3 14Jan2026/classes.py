class student:
    name="jack"
    dept="cse"
    gender='male'
    age=25
s1=student()
print(s1.name)
print(s1.dept)
print(s1.gender)
print(s1.age)

class employee:
    def __init__(self,name,dept,gender,age):
        self.name=name
        self.dept=dept
        self.gender=gender
        self.age=age
e1=employee("james",'eee','male',21)
print(e1.name,e1.dept,e1.gender,e1.age)
