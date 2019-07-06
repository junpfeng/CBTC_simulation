import threading
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class myQThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("QThread")

if __name__ == "__main__":
    """现象：本来是顺序执行，但是结果5个l am sorry一下子全部出现"""
    myT = myQThread()
    myT.start()