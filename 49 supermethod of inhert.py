class employee:
    def __init__(self):
        print("employee")
    a=1

class coder(employee):
    def __init__(self):
        print("coder")
        super().__init__()
    b=2

o=employee()
print(o.a)
o=coder()
print(o.a,o.b)