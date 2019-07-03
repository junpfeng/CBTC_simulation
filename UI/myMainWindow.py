import ui_mainwindow as uim
import myData
import pyqtgraph as pg
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import model.bf_search as bf


# -----菜单栏窗口类-------

class SubMenuConfig(QWidget):
    """菜单栏子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("configure")
        self.resize(200,200)
        self.Config_widget()

    def Config_widget(self, _track_step = 5):
        # 珊格布局对象
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30, 30, 200, 200))

        self.label_step = QLabel(self)
        self.lineEdit_step = QLineEdit(self)
        self.lineEdit_step.setText(str(_track_step))
        self.label_step.setText("轨道测试点间距")

        self.button_sure = QPushButton(self)
        self.button_cancel = QPushButton(self)
        self.button_sure.setText("确定")
        self.button_cancel.setText("取消")
        # 放入珊格布局
        layout.addRow(self.label_step, self.lineEdit_step)
        layout.addRow(self.button_sure, self.button_cancel)

        #  绑定槽函数
        self.button_sure.clicked.connect(self.slot_button_sure)
        self.button_cancel.clicked.connect(self.slot_button_cancel)

    # ------- 槽函数群 ---------------
    def slot_button_sure(self):
        try:
            _step = self.lineEdit_step.text()
            # 修改轨道测试点间距
            myData.myController.set_track_step(_step=_step)
        except Exception as res:
            mw.slot_edit_disp("configure输入出错：" + str(res))

        self.close()

    def slot_button_cancel(self):
        self.close()



# -------子窗口类--------

class SubWidgetInterf(QWidget):
    """干扰基站子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("干扰基站参数")
        self.resize(200, 200)
        self.Interf_widget()
        self.interf_num = 0

    def Interf_widget(self, Interf1_coordinate=(100, 110), Interf2_coordinate=(0, -8), Interf1_power=30, Interf2_power=30):
        """注意这里的坐标使用圆括号"""
        layout = QFormLayout(self)
        layout.setGeometry(QRect(30, 30, 200, 200))
        """干扰基站的参数有四个：两个坐标和两个发射功率"""
        self.label_power = QLabel(self)
        self.lineEdit_power = QLineEdit(self)
        self.button_coordinate = QPushButton(self)
        self.lineEdit_coordinate = QLineEdit(self)

        self.button_sure = QPushButton(self)
        self.button_cancel = QPushButton(self)

        # 添加默认值
        self.lineEdit_coordinate.setText(str(Interf1_coordinate))
        self.lineEdit_coordinate.setText(str(Interf2_coordinate))
        self.lineEdit_power.setText(str(Interf1_power))
        self.lineEdit_power.setText(str(Interf2_power))

        # 添加名称
        self.label_power.setText("干扰源功率dbm")
        self.button_coordinate.setText("干扰源坐标")
        self.button_sure.setText("添加")
        self.button_cancel.setText("取消")

        # 按键绑定槽函数
        self.button_coordinate.clicked.connect(self.slot_button_coordinate)
        self.button_sure.clicked.connect(self.slot_button_sure)
        self.button_cancel.clicked.connect(self.slot_button_cancel)

        # 加入珊格布局
        layout.addRow(self.label_power, self.lineEdit_power)
        layout.addRow(self.button_coordinate, self.lineEdit_coordinate)
        layout.addRow(self.button_sure, self.button_cancel)
        # 启动珊格布局
        self.setLayout(layout)

    # -----------槽函数----------------
    def slot_button_coordinate(self):
        # 在方法内定义的局部变量
        text, ok = QInputDialog.getText(self, '输入坐标(x,y)', '第一个干扰坐标(x,y)')
        if ok and text:
            self.lineEdit_end.setText(text)

    def slot_button_sure(self):
        """只允许最多添加两个干扰点，目前。
        使用一个干扰计数变量来记录"""
        try:
            if self.interf_num >= 2:  # 防止直接调用这个函数，而不是通过信号和槽
                return

            myData.myController.set_interf_data(self.lineEdit_power.text(),
                                                self.lineEdit_coordinate.text())
            # 将这些数据绘制轨道图
            x, y = myData.myController.get_interf_list()
            mw.graph_paint([x[self.interf_num]], [y[self.interf_num]], symbol='+')

            self.interf_num += 1  # 记录输入干扰基站的数量
            if self.interf_num >= 2:  # 已经记录了两个干扰点了，
                self.button_sure.setEnabled(False)
            else:
                self.button_sure.setEnabled(True)
        except Exception as res:
            mw.slot_edit_disp("干扰基站参数输入错误：" + str(res))

        self.close()  # 关闭窗口

    def slot_button_cancel(self):
        print("取消")
        self.close()  # 关闭窗口


class SubWidgetRec(QWidget):
    """接收机参数子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("接收机参数")
        self.resize(200, 200)
        self.Rec_widget()

    def Rec_widget(self, Rec_gain=13, Rec_sen=-100, Rec_SIR=-5, Rec_Outage=0.02):
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
        # 添加默认值
        self.lineEdit_gain.setText(str(Rec_gain))
        self.lineEdit_sensitivity.setText(str(Rec_sen))
        self.lineEdit_SIR.setText(str(Rec_SIR))
        self.lineEdit_Outage.setText(str(Rec_Outage))
        # 添加名称
        self.label_gain.setText("接收增益dB")
        self.label_sensitivity.setText("灵敏度dBm")
        self.label_SIR.setText("信干比下限")
        self.label_Outage.setText("中断概率上限")
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
        try:
            myData.myController.set_Rec_data(self.lineEdit_gain.text(),
                                                self.lineEdit_sensitivity.text(),
                                                self.lineEdit_SIR.text(),
                                                self.lineEdit_Outage.text())
        except Exception as res:
            mw.slot_edit_disp("接收机参数输入错误：" + str(res))

        self.close()  # 关闭窗口

    def slot_button_cancel(self):
        print("cancel")

class SubWidgetAP(QWidget):
    """AP参数子窗口"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AP参数")
        self.resize(200, 200)
        self.AP_widget()

    def AP_widget(self, AP_power=44.8, AP_gain=13, AP_limit=1, AP_interval=60):
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

        # 设置默认值
        self.lineEdit_power.setText(str(AP_power))
        self.lineEdit_gain.setText(str(AP_gain))
        self.lineEdit_limit.setText(str(AP_limit))
        self.lineEdit_interval.setText(str(AP_interval))

        self.button_sure = QPushButton(self)
        self.button_sure.clicked.connect(self.slot_button_sure)
        self.button_cancel = QPushButton(self)
        self.button_cancel.clicked.connect(self.slot_button_cancel)
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
        try:
            myData.myController.set_AP_data(self.lineEdit_power.text(),
                                               self.lineEdit_gain.text(),
                                               self.lineEdit_limit.text(),
                                               self.lineEdit_interval.text())
        except Exception as res:
            mw.slot_edit_disp("AP参数输入出错：" + str(res))
        self.close()  # 关闭窗口

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
        self.combox_scene.addItems(("自由空间路径损耗", "外部导入"))
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
        myData.myController.set_scene_data(self.combox_scene.currentText())
        self.close()  # 关闭窗口

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

    def track_widget(self, type="圆弧型", begin="(100,80)", end="(200,300)", center="(100,300)", degree="90"):

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
        self.button_sure.setText("添加")
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
            if item == "直线型":  # 屏蔽圆心坐标和圆心角
                self.lineEdit_center.setEnabled(False)
                self.lineEdit_degree.setEnabled(False)
                self.button_center.setEnabled(False)
                self.button_degree.setEnabled(False)
            else:
                self.lineEdit_center.setEnabled(True)
                self.lineEdit_degree.setEnabled(True)
                self.button_center.setEnabled(True)
                self.button_degree.setEnabled(True)

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
        try:
            if self.lineEdit_type.text() == "圆弧型":
                myData.myController.set_track_data(self.index,
                                                      self.lineEdit_type.text(),
                                                      self.lineEdit_begin.text(),
                                                      self.lineEdit_end.text(),
                                                      center=self.lineEdit_center.text(),
                                                      degree=self.lineEdit_degree.text())#self.lineEdit_degree.text())
                # 将这些数据绘制轨道图
                x, y = myData.myController.get_track_list(index=self.index)
                mw.graph_paint(x, y)
              #  self.index = self.index + 1
            else:
                myData.myController.set_track_data(self.index,
                                                      self.lineEdit_type.text(),
                                                      self.lineEdit_begin.text(),
                                                      self.lineEdit_end.text())
                """在graph上绘制出路线,这里的绘制全部是散点图因此，下面绘图函数的输入应当是路线散点"""
                x, y = myData.myController.get_track_list(index=self.index)
                mw.graph_paint(x, y)
        except Exception as res:
            mw.slot_edit_disp("轨道参数输入出错：" + str(res))
        self.close()  # 关闭窗口



    def slot_track_cancel(self):
        print("cancel")
        self.close()

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

        # 确认配置按钮
        self.button_import.clicked.connect(self.slot_button_import)
        # 开始仿真按钮--这个单独作为一个线程
        self.button_run.clicked.connect(self.slot_button_run)
        # reset按钮
        self.button_reset.clicked.connect(self.slot_button_reset)
        # 配置菜单栏
        self.actionAP.triggered.connect(self.slot_menu_config)

        #------其他初始化设置------------
        self.slot_edit_disp("运行中")

   # 设置画图界面
    def graph_paint(self, x_list, y_list, symbol="x"):
        """ x_list和y_list分别是x轴和y轴的数据列表 """
        self.myPlt.plot(x_list, y_list, pen=None,
                        name="Red curve", symbol=symbol)
        self.myPlt.showGrid(x=True, y=True)

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

    def slot_button_import(self):
        print("import")
        mySubWidgetTrack.slot_track_sure()
        mySubWidgetRec.slot_button_sure()
        mySubWidgetScene.slot_button_sure()
        mySubWidgetAP.slot_button_sure()
        mySubWidgetInterf.slot_button_sure()

    def slot_button_run(self):
        print("开始仿真")
        # 防止没输入数据，就误操作按下运行
        if myData.myController.is_track_empty() or myData.myController.is_AP_empty():
            self.slot_edit_disp("请先配置参数")
            return
        # 一旦运行，必须reset之后才能重新运行
        mw.button_run.setEnabled(False)
        self.slot_edit_disp("仿真中...")
        bf.myModel.bf_search()
        for i in range(len(myData.myController.AP_current)):
            self.graph_paint([myData.myController.AP_current[i][0]], [myData.myController.AP_current[i][1]], symbol="o")
        self.slot_edit_disp("仿真结束")

    def slot_button_reset(self):
        """1.清除控制器内的所有缓存数据、2.清空绘图界面、3.接触干扰基站的灰色按钮"""
        # 轨道配置参数
        myData.myController.del_track_data_all()
        # 场景选择参数
        myData.myController.del_scene_data_all()
        # AP参数
        myData.myController.del_AP_data_all()
        # 接收机参数
        myData.myController.del_Rec_data_all()
        # 干扰基站参数
        myData.myController.del_interf_data_all()
        #清空绘图
        self.myPlt.clear()  # 之所以没有方法提示，是因为他不知道该对象从哪个类来的

        # 是能干扰基站添加按钮
        mySubWidgetInterf.interf_num = 0
        mySubWidgetInterf.button_sure.setEnabled(True)
        # textedit 显示正在运行
        self.slot_edit_disp("正在运行")
        # 使能运行按钮
        mw.button_run.setEnabled(True)

    # ------------ 菜单栏槽函数群 --------------
    def slot_menu_config(self):
        mySubMenuConfig.show()

    def slot_edit_disp(self, _str):
        self.textEdit_disp.setText(_str)



mySubWidgetTrack = SubWidgetTrack()
mySubWidgetScene = SubWidgetScene()
mySubWidgetAP = SubWidgetAP()
mySubWidgetRec = SubWidgetRec()
mySubWidgetInterf = SubWidgetInterf()
mySubMenuConfig = SubMenuConfig()
mw = MainWindow()


"""总结可以作为符号的字符：o、x、+"""
if __name__ == "__main__":
    # 在建立窗口实例对象之前，必须建立QApplication对象，这是为什么
    app = QApplication(sys.argv).instance()
    # 只在模块文件内定义了一个全局的对象，其他文件内只使用该对象，而不创建新对象
    # 实际上就是一个单例对象
    # mySubWidgetTrack = SubWidgetTrack()
    # mySubWidgetScene = SubWidgetScene()
    # mySubWidgetAP = SubWidgetAP()
    # mySubWidgetRec = SubWidgetRec()
    # mySubWidgetInterf = SubWidgetInterf()
    # mySubMenuConfig = SubMenuConfig()
    #
    # myQmainwindow = QMainWindow()
    #
    # mw = MainWindow()
    # mw.my_setup(mw)
    # mw.show()
    app.exit(app.exec_())

