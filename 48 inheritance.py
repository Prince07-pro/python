class  employee:
    company="kp"
    name="prince"
    def show(self):
        print(f" the name of employee {self.name} and the company is {self.company}")

class programmer(employee): # inharitance from employee to programmer
    company="kp 2"
    langauge="python"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.langauge} langauge")

a=employee()
b=programmer()

a.show()
b.showlanguage()


# syntax of multilevel inheritance
# class a:
# class b(a):
# class c(b):