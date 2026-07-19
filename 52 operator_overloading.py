# addition for p1.__add__(p2) p1+p2
# substraction p1.__sub__(P2) p1-p2
#multiiplication p1.__mul__(P2) p1*p2
#divison p1.__truediv__(P2) p1/p2
#p1.__floordiv__(p2) p1//p2


class number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
    def __mul__(self,num):
        return self.n*num.n # operator overloading

n = number(1)
m = number(2)

print(n + m,n*m)
