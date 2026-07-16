class employee:
    name ="kp"  # class attributes
    age = 19
    salary=100000

Name = employee() # name is object
#kp.name="prince" # instance attributes
print(Name.age,Name.salary)  

# istance attributes are powerfull than class attributes (preference first instance attributes)
# @staticmethod is a decorator use to no give a self arguments.