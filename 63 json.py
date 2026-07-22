import json
p = {"name":"IBM","salary":50000,"city":"mumbai"}
r=json.dumps(p) #json module basically convert (list or dictionary) to json string and vice-versa.
print(p)
type(r)

d=json.loads('{"name":"IBM","salary":50000,"city":"mumbai"}')
print(d)  #loads is convert json string to python obj.
type(d)

file = open("data.json","w")
json.dump({"name":"IBM","salary":50000,"city":"mumbai"},file)
file.close() #dump is write a json data in file.

file = open("data.json","r")
json.load(file) #load use to read a file a json data
file.close()