class employee:
    a = 1
    def show(self):
        print(f" the value  is  {self.a}")                
      
    @property # anywhere return
    def name(self):
        return f"the name is {self.ename}"
    
    @name.setter
    def name(self,value):
        self.ename= value

e = employee()
e.a=45

e.name="prince"
print(e.name)

e.show()