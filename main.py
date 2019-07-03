from myMainWindow import *
import threading
##----------- 目前程序运行从myMainWindow开始 ---------------
# 在建立窗口实例对象之前，必须建立QApplication对象，这是为什么
app = QApplication(sys.argv).instance()
# 只在模块文件内定义了一个全局的对象，其他文件内只使用该对象，而不创建新对象
# 实际上就是一个单例对象

mw.my_setup(mw)
mw.show()
app.exit(app.exec_())