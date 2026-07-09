a="Prince"

#  1 lenght
lenght=len(a)
print(lenght)

#  2 end and start
print(a.startswith("P"))

print(a.endswith("ce"))

# 3 count

print(a.count("i"))

print(a.count("ince"))

# 4 capatilize

print(a.capitalize())

# 5 find

print(a.find("c"))

# 6 replace


print(a.replace("i","p")) # (old word, new word)


# format function

name = "Prince"
age  = 17
print("my name is {} and age is {}." .format(name,age))


# f-string
print(f"my name is {"Prince"} and age is {19}")