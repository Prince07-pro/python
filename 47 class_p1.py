from random import randint # random no. give 

class train:
    
    def __init__(self,name,age,mobile_no):
        self.name=name
        self.age=age
        self.mobile_no=mobile_no  ## (__)mobile_no is called private attribute (__)
   
    def __init__(self,trainno):
        self.trainno=trainno  

    def book(self,fro,to): # from and to is key word
        print(f"ticket is booked in train no:{self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"ticket fare in train no :{self.trainno} is running on time ")

    def gatefare(self,fro,to):
        print(f" ticket fare in train no:{self.trainno} from {fro} to {to} is {randint(10000,20000)}")


t=train(11111) 
t.book("a","d")   
t.getstatus()
t.gatefare("a","d")