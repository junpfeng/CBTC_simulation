import ui_mainwindow as uim
import myData
import pyqtgraph as pg
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# -------子窗口类--------

class SubWidgetInterf(QWidget):
    """干扰基站子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("干扰基站参数")
        self.resize(200, 200)
        self.Interf_widget()

    def Interf_widget(self):
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30, 30, 200, 200))
        """干扰基站的参数有四个：两个坐标和两个发射功率"""
        self.label_power_1 = QLabel(self)
        self.lineEdit_power_1 = QLineEdit(self)
        self.button_coordinate_1 = QPushButton(self)
        self.lineEdit_coordinate_1 = QLineEdit(self)
        self.label_power_2 = QLabel(self)
        self.lineEdit_power_2 = QLineEdit(self)
        self.button_coordinate_2 = QPushButton(self)
        self.lineEdit_coordinate_2 = QLineEdit(self)
        # 添加名称
        self.label_power_1.setText("第一个干扰功率")
        self.label_power_2.setText("第二个干扰功率")
        self.button_coordinate_1.setText("第一个干扰坐标")
        self.button_coordinate_2.setText("第一个干扰坐标")
        # 按键绑定槽函数
        self.button_coordinate_1.clicked.connect(self.slot_button_coordinate_1)
        self.button_coordinate_2.clicked.connect(self.slot_button_coordinate_2)

        # 加入珊格布局
        layout.addRow(self.label_power_1, self.lineEdit_power_1)
        layout.addRow(self.label_power_2, self.lineEdit_power_2)
        layout.addRow(self.button_coordinate_1, self.lineEdit_coordinate_1)
        layout.addRow(self.button_coordinate_2, self.lineEdit_coordinate_2)
        # 启动珊格布局
        self.setLayout(layout)

    # -----------槽函数----------------
    def slot_button_coordinate_1(self):
        # 在方法内定义的局部变量
        text, ok = QInputDialog.getText(self, '输入坐标(x,y)', '第一个干扰坐标(x,y)')
        if ok and text:
            self.lineEdit_end.setText(text)

    def slot_button_coordinate_2(self):
        text, ok = QInputDialog.getText(self, '输入坐标(x,y)', '第二个干扰坐标(x,y)')
        if ok and text:
            self.lineEdit_end.setText(text)

class SubWidgetRec(QWidget):
    """接收机参数子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("接收机参数")
        self.resize(200, 200)
        self.Rec_widget()

    def Rec_widget(self):
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30, 30, 200, 200))
        """接收机参数"""
        self.label_gain = QLabel(self)
        self.label_sensitivity = QLabel(self)
        self.label_SIR = QLabel(self)
        self.label_Outage = QLabel(self)
        self.lineEdit_gain = QLineEdit(self)
        self.lineEdit_sensitivity = QLineEdit(self)
        self.lineEdit_SIR = QLineEdit(self)
        self.lineEdit_Outage = QLineEdit(self)
        self.button_sure = QPushButton(self)
        self.button_cancel = QPushButton(self)
        self.button_sure.clicked.connect(self.slot_button_sure)
        self.button_cancel.clicked.connect(self.slot_button_cancel)
        # 添加名称
        self.label_gain.setText("接受增益dB")
        self.label_sensitivity.setText("灵敏度dBm")
        self.label_SIR.setText("信干比下限")
        self.label_Outage.setText("中断概率下限")
        self.button_sure.setText("确定")
        self.button_cancel.setText("取消")
        # 加入珊格布局
        layout.addRow(self.label_gain, self.lineEdit_gain)
        layout.addRow(self.label_sensitivity, self.lineEdit_sensitivity)
        layout.addRow(self.label_SIR, self.lineEdit_SIR)
        layout.addRow(self.label_Outage, self.lineEdit_Outage)
        layout.addRow(self.button_sure, self.button_cancel)
        # 启动珊格布局
        self.setLayout(layout)

    def slot_button_sure(self):
        print("sure")
        myData.myDataContainer.get_Rec_data(self.lineEdit_gain.text(),
                                     self.lineEdit_sensitivity.text(),
                                     self.lineEdit_SIR.text(),
                                     self.lineEdit_Outage.text())
    def slot_button_cancel(self):
        print("cancel")

class SubWidgetAP(QWidget):
    """AP参数子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AP参数")
        self.resize(200, 200)
        self.AP_widget()

    def AP_widget(self):
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30,30,200,200))
        """AP参数设置有4个，一个是发射功率，发射增益
        以及AP部署的最低数量，AP的部署间隔"""
        self.label_power = QLabel(self)
        self.label_gain = QLabel(self)
        self.label_limit = QLabel(self)
        self.label_interval = QLabel(self)
        self.lineEdit_power = QLineEdit(self)
        self.lineEdit_gain = QLineEdit(self)
        self.lineEdit_limit = QLineEdit(self)
        self.lineEdit_interval = QLineEdit(self)
        self.button_sure = QPushButton(self)
        self.button_cancel = QPushButton(self)
        # 添加名称
        self.label_power.setText("发射功率dBm")
        self.label_gain.setText("发射增益dB")
        self.label_limit.setText("AP数量下限")
        self.label_interval.setText("AP部署间隔m")
        self.button_sure.setText("确定")
        self.button_cancel.setText("取消")
        # 加入珊格布局
        layout.addRow(self.label_power, self.lineEdit_power)
        layout.addRow(self.label_gain, self.lineEdit_gain)
        layout.addRow(self.label_limit, self.lineEdit_limit)
        layout.addRow(self.label_interval, self.lineEdit_interval)
        layout.addRow(self.button_sure, self.button_cancel)
        # 启动珊格布局
        self.setLayout(layout)

    # ----------槽函数--------------
    def slot_button_sure(self):
        print("sure")
        myData.myDataContainer.get_AP_data(self.lineEdit_power.text(),
                                    self.lineEdit_gain.text(),
                                    self.lineEdit_limit.text(),
                                    self.lineEdit_interval.text())

    def slot_button_cancel(self):
        print("cancel")


class SubWidgetScene(QWidget):
    """场景添加子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("场景选择")
        self.resize(200, 200)
        self.scene_widget()

    def scene_widget(self):
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30,30,200,200))
        # 场景选择，使用下拉框
        self.combox_scene = QComboBox(self)
        self.combox_scene.addItems(("平原", "外部导入"))
        layout.addRow(self.combox_scene)

        # 取消和确定
        self.button_sure = QPushButton(self)
        self.button_cancel = QPushButton(self)
        self.button_sure.setText("确定")
        self.button_cancel.setText("取消")
        self.button_sure.clicked.connect(self.slot_button_sure)
        self.button_cancel.clicked.connect(self.slot_button_cancel)
        layout.addRow(self.button_sure, self.button_cancel)

        self.setLayout(layout)


    #--------槽函数群----------------------
    def slot_button_sure(self):
        print("sure")
        myData.myDataContainer.get_scene_data(self.combox_scene.currentText())

    def slot_button_cancel(self):
        print("cancel")


class SubWidgetTrack(QWidget):
    # 信号必须是类属性才行
    graph_signal = pyqtSignal()
    """轨道添加子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('轨道参数')  # 这个是父类QWidget的方法
        self.resize(200, 100)
        self.track_widget()  # 实际上，就相当于将track_widget里的内容直接定义在__init__方法中
        self.index = 0
        # 定义信号

#        self.graph_signal.connect(myWM.mw.slot_graph_paint())

    def track_widget(self, type="圆弧型", begin="(0,0)", end="(100,100)", center="(0,100)", degree="90"):

        # 建立一个珊格布局对象
        layout = QFormLayout()
        layout.setGeometry(QRect(20, 20, 160, 160))
        # 轨道类型
        self.button_type = QPushButton(self)
        self.button_type.resize(100, 30)
        self.button_type.setText("轨道类型")
        self.button_type.clicked.connect(self.slot_button_type)
        self.lineEdit_type = QLineEdit()
        layout.addRow(self.button_type, self.lineEdit_type)
        # 轨道起点
        self.button_begin = QPushButton(self)
        self.button_begin.resize(100, 30)
        self.button_begin.setText("轨道起点")
        self.button_begin.clicked.connect(self.slot_button_begin)
        self.lineEdit_begin = QLineEdit()
        layout.addRow(self.button_begin, self.lineEdit_begin)
        # 轨道终点
        self.button_end = QPushButton(self)
        self.button_end.resize(100, 30)
        self.button_end.setText("轨道终点")
        self.button_end.clicked.connect(self.slot_button_end)
        self.lineEdit_end = QLineEdit()
        layout.addRow(self.button_end, self.lineEdit_end)
        # 圆心坐标
        self.button_center = QPushButton(self)
        self.button_center.resize(100, 30)
        self.button_center.setText("圆心坐标")
        self.button_center.clicked.connect(self.slot_button_center)
        self.lineEdit_center = QLineEdit()
        layout.addRow(self.button_center, self.lineEdit_center)
        # 圆心角
        self.button_degree = QPushButton(self)
        self.button_degree.resize(100, 30)
        self.button_degree.setText("圆心角(角度值)")
        self.button_degree.clicked.connect(self.slot_button_degree)
        self.lineEdit_degree = QLineEdit()
        layout.addRow(self.button_degree, self.lineEdit_degree)

        # 设置默认值
        self.lineEdit_type.setText(type)
        self.lineEdit_begin.setText(begin)
        self.lineEdit_end.setText(end)
        self.lineEdit_center.setText(center)
        self.lineEdit_degree.setText(degree)


        # 确定 取消
        self.button_sure = QPushButton(self)
        self.button_sure.resize(100, 30)
        self.button_sure.setText("确定")
        self.button_sure.clicked.connect(self.slot_track_sure)
        self.button_cancel = QPushButton(self)
        self.button_cancel.resize(100, 30)
        self.button_cancel.setText("取消")
        self.button_cancel.clicked.connect(self.slot_track_cancel)

        self.button_delete = QPushButton(self)
        self.button_delete.resize(100, 30)
        self.button_delete.setText("删除所有轨道")
        self.button_delete.clicked.connect(self.slot_track_delete)
        layout.addRow(self.button_sure, self.button_cancel)
        layout.addRow(self.button_delete)

        # 启动珊格布局
        self.setLayout(layout)


#------------槽函数群-----------------------
    # ------轨道参数设置的输入对话框槽函数-------
    def slot_button_type(self):
        items = ("圆弧型", "直线型")
        item, ok = QInputDialog.getItem(self, '请选择轨道类型', '轨道类型列表', items)
        if ok and item:
            self.lineEdit_type.setText(item)

    def slot_button_begin(self):
        text, ok =QInputDialog.getText(self, '输入坐标(x,y)', '输入坐标起点(x,y)')
        if ok and text:
            self.lineEdit_begin.setText(text)

    def slot_button_end(self):
        text, ok =QInputDialog.getText(self, '输入坐标(x,y)', '输入坐标终点(x,y)')
        if ok and text:
            self.lineEdit_end.setText(text)

    def slot_button_center(self):
        text, ok =QInputDialog.getText(self, '输入圆心坐标', '输入圆心坐标(x,y)')
        if ok and text:
            self.lineEdit_center.setText(text)

    def slot_button_degree(self):
        text, ok =QInputDialog.getText(self, '输入圆心角', '输入圆心角(角度值)')
        if ok and text:
            self.lineEdit_degree.setText(text)

    def slot_track_sure(self):
        print("sure")
        if self.lineEdit_type.text() == "圆弧型":
            myData.myDataContainer.set_track_data(self.index,
                                           self.lineEdit_type.text(),
                                            self.lineEdit_begin.text(),
                                            self.lineEdit_end.text(),
                                            center=self.lineEdit_center.text(),
                                            degree=self.lineEdit_degree.text())#self.lineEdit_degree.text())
            # 将这些数据绘制轨道图
            x, y = myData.myDataContainer.get_track_list(index=self.index)
            mw.graph_paint(x, y)
            self.index = self.index + 1



        else:
            myData.myDataContainer.set_track_data(self.index,
                                                  self.lineEdit_type.text(),
                                           self.lineEdit_begin.text(),
                                           self.lineEdit_end.text())
            """在graph上绘制出路线,这里的绘制全部是散点图因此，下面绘图函数的输入应当是路线散点"""
            x, y = myData.myDataContainer.get_track_list(index=self.index)
            mw.graph_paint(x, y)
            self.index = self.index + 1



    def slot_track_cancel(self):
        print("cancel")

    def slot_track_delete(self):
        print("delete")


"""继承QMainWindow非常重要"""
class MainWindow(QMainWindow, uim.Ui_MainWindow):
    def __init__(self):
        """init方法和普通方法不同，得好好研究一下
        还有要研究一下，使用super和直接使用QMainWindow.__init__()的区别
        此处若不使用super就会出错"""
        super().__init__()

        # 设置graph的前景色和背景色
        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        # 初始化唯一的画笔

        # self.myMainWindow = QMainWindow()
        # self.my_setup(self.myMainWindow)

        #self.myMainWindow.show()

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

    def slot_graph_paint(self):
        list_x, list_y = myData.myDataContainer.get_track_list()
        self.graph_paint(list_x, list_y)


"""总结可以作为符号的字符：o、x、+"""
if __name__ == "__main__":
    # 在建立窗口实例对象之前，必须建立QApplication对象，这是为什么
    app = QApplication(sys.argv).instance()
    # 只在模块文件内定义了一个全局的对象，其他文件内只使用该对象，而不创建新对象
    # 实际上就是一个单例对象
    mySubWidgetTrack = SubWidgetTrack()
    mySubWidgetScene = SubWidgetScene()
    mySubWidgetAP = SubWidgetAP()
    mySubWidgetRec = SubWidgetRec()
    mySubWidgetInterf = SubWidgetInterf()

    myQmainwindow = QMainWindow()

    mw = MainWindow()
    mw.my_setup(mw)
    mw.show()
    app.exit(app.exec_())

