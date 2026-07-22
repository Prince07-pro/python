from functools import reduce
l=[1,2,3,4,5,6]

s=lambda x:x*x
s2=map(s,l) # map function use to one function use to all item in same list or etc...
print(list(s2))

#filter ex
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyeven =filter(even,l)
print(list(onlyeven))

# reduce ex

def mul(self,n):
     return n*n

print(reduce(mul,l))
