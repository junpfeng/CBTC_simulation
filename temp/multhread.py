import threading
import time

def saySorry():
    print("l am sorry")
    time.sleep(1)


if __name__ == "__main__":
    """现象：本来是顺序执行，但是结果5个l am sorry一下子全部出现"""
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()