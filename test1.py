#from test2 import a


class B():

    def __init__(self):
        self.a = A()
        pass

    def fun(self):
        print("B")
        self.a.fun()



class A():

    def fun(self):
        print("A")



b = B()
b.fun()
