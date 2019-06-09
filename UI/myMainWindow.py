from ui_mainwindow import *
from myData import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget
import sys

from sub_widget import *

"""继承QMainWindow非常重要"""
class myMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """init方法和普通方法不同，得好好研究一下
        还有要研究一下，使用super和直接使用QMainWindow.__init__()的区别
        此处若不使用super就会出错"""
        super().__init__()


    def my_setup(self, mainwindow):
        self.setupUi(mainwindow)
        """绑定按钮的槽函数"""
        # 轨道和场景参数设置按钮
        self.button_track.clicked.connect(self.slot_button_track)
        self.button_scene.clicked.connect(self.slot_button_scene)
        # 接收机和发射机参数设置按钮
        self.button_ap.clicked.connect(self.slot_button_ap)
        self.button_rec.clicked.connect(self.slot_button_rec)
        # 干扰基站参数设置按钮
        self.button_interf.clicked.connect(self.slot_button_interf)

    # 槽函数群
    def slot_button_track(self):
        # 创建一个输入对话框
        print("button_track_slot")
        mySubWidgetTrack.show()

    def slot_button_scene(self):
        print("scnen")
        mySubWidgetScene.show()

    def slot_button_ap(self):
        # 创建一个输入对话框
        print("button_track_ap")
        mySubWidgetAP.show()

    def slot_button_rec(self):
        print("rec")
        mySubWidgetRec.show()

    def slot_button_interf(self):
        # 创建一个输入对话框
        print("button_track_interf")
        mySubWidgetInterf.show()

# -------对话框控件-------------
    def getItem_track(self):
        items = ('C','C++','Ruby','Python','Java')
        item, ok =QInputDialog.getMultiLineText(self,
                                                "项目介绍",
                                                "介绍",
                                                "服务外包第三方公司\n")
        if ok and item:
            print("对话框输入成功")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = myMainWindow()
    qmw = QMainWindow()
    mw.my_setup(qmw)
    qmw.show()
    app.exit(app.exec_())

