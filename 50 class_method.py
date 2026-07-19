# @ start method also called decorator
class employee:
    a=1
    @classmethod # classmethod use to show a  class attribute , use acls not a self
    def show(cls):
        print(f"the value is {cls.a}")

e = employee()
e.a=45

e.show()