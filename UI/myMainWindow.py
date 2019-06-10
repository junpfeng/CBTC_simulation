from ui_mainwindow import *
from myData import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QWidget
import sys
import numpy as np
import pyqtgraph as pg

from sub_widget import *

"""继承QMainWindow非常重要"""
class myMainWindow(Ui_MainWindow):
    def __init__(self):
        """init方法和普通方法不同，得好好研究一下
        还有要研究一下，使用super和直接使用QMainWindow.__init__()的区别
        此处若不使用super就会出错"""
        super().__init__()

        # 设置graph的前景色和背景色
        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        # 初始化唯一的画笔

        self.myMainWindow = QMainWindow()
        self.my_setup(self.myMainWindow)

        self.myMainWindow.show()


    # mainwindow是传入的参数，一般为QMainWindow对象
    def my_setup(self, mainwindow):
        """调用这个函数setupUi，会丰富myMainWindow的内容
        给他增加ui_mainwindown类内的成员"""
        self.setupUi(mainwindow)
        # 初始化画笔
        self.myPlt = self.mainGraph.addPlot(title="场景绘制")
        """绑定按钮的槽函数"""
        # 轨道和场景参数设置按钮
        self.button_track.clicked.connect(self.slot_button_track)
        self.button_scene.clicked.connect(self.slot_button_scene)
        # 接收机和发射机参数设置按钮
        self.button_ap.clicked.connect(self.slot_button_ap)
        self.button_rec.clicked.connect(self.slot_button_rec)
        # 干扰基站参数设置按钮
        self.button_interf.clicked.connect(self.slot_button_interf)

        #self.my_graph([1,2], [3,4])

    # 设置画图界面
    def graph_paint(self, x_list, y_list, symbol="o"):

        self.myPlt.plot(x_list, y_list, pen=None,
                  name="Red curve", symbol=symbol)

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


app = QApplication(sys.argv)
mw = myMainWindow()
"""总结可以作为符号的字符：o、x、+"""
if __name__ == "__main__":

    app.exit(app.exec_())

