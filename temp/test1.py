#from test2 import a


class B():

    def __init__(self, A):
        self.a = A
        pass

    def fun(self):
        print("B")
        print(self.a.x)
        self.a.x = 3
        print(self.a.x)
        self.a.fun()



class A():
    def __init__(self):
        self.x = 1
    def fun(self):
        print("A")
        print(self.x)



a = A()
b = B(a)
a.fun()
b.fun()
a.fun()
