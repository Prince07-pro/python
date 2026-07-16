# read and close
f = open("44 file.txt","r")
data = f.read()
print(data)
f.close()

#   write

a="\n heyy prince looks like handsome" 
f = open("44 file.txt","w") #also make a new file
f.write(a)
f.close()

# readlines() use to read line by line
# rb is read binary
# appending
f = open("44 file.txt","a")
f.write(a)
f.close()


# with statement

#f = open("44 file.txt","r")
#data = f.read()
#print(data)
#f.close()

with open("44 file.txt") as f:
    print(f.read())