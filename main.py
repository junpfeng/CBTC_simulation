from PyQt5.QtWidgets import QApplication
import sys
from myMainWindow import mw
##----------- 目前程序运行从myMainWindow开始 ---------------

app = QApplication(sys.argv)

app.exit(app.exec_())