 # methods
m ={

  "prince" : 100,
  "shubham" : 100,
  "vansh" : 100
}

print(m , type(m))

#item

print(m.items())

# keys

print(m.keys())

# update

m.update({"vansh" : 99})
print(m)


# get 

print(m.get("prince"))

# two type
print(m.get("prince")) # its same both but
print(m["prince"])


print(m.get("prince2")) # return none
#print(m["prince2"]) # return error

#pop

m.pop("shubham")
print(m,type(m))

 # other method