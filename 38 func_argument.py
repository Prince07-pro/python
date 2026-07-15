def fun(name): # name as argument
    print("heyy "+ name)
    return 7
     


a =fun("prince")

# default argument

def fun(name,ending="thank you!"): 
    print("heyy "+ name)
    print(ending)

fun("prince","thanks")
fun("rohan") # default parameter