from PyQt5.QtCore import *
#from test1 import b


class A(QObject):
    def fun(self):
        print("A")

def a(a):
    a = 2
    print(a)




if __name__ == "__main__":
    x = 1
    y = 3
    a(x)
    print(x,y)
