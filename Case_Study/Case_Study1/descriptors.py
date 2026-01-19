#descriptors
class Validate_Marks():
    def __set__(self,instance,value):
        if any(m<0 or m>100 for m in value):
            raise ValueError("Marks can only be between 0 and 100")
        instance.__dict__['marks']=value
    def __get__(self,instance,owner):
        return instance.__dict__.get('marks',[])

class Salary_Access():
    def __get__(self,instance,owner):
        raise ValueError("Access Denied, Salary is confidential")
    def __set__(self,instance,value):
        if value<0:
            raise ValueError("Salary must be greater than 0 and positive")
        instance.__dict__['_salary']=value
