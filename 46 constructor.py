# __ start it called dunder method , (automatic called only (__init__))

class employee:
    name ="kp"  
    age = 19
    salary=100000
    def __init__(self,name,age,salary): #constructor 
        self.name=name
        self.age=age
        self.salary=salary
        print(" i am a dunder constructor")


Name = employee("prince",20,1000000) 
print(Name.name,Name.age,Name.salary)  