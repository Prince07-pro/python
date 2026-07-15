# sum(n)= n+sum(n-1)

def sum(n):
    if(n == 1): # base condition
        return 1
    return n + sum(n-1)
n = int(input("enter a number:"))

print(sum(n))