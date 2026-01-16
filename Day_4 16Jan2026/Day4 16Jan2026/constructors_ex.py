class employee:
    #constructor:It is used to initiate the object.It contains one parameter 'name'
    def __init__(self,name):
        self.name=name
        print("Contructor is called")
    #destructor: It is used to deleted the object
    def __del__(self):
        print("Destructor is called")

e=employee("Rahul")