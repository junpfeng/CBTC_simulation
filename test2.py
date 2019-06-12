from PyQt5.QtCore import *
from test1 import b


class A(QObject):
    def fun(self):
        print("A")


a = A()
if __name__ == "__main__":

    a.fun()
