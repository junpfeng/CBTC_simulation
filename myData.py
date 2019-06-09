import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DataContainer():
    """将图形界面输入的各种
    数据统统进行封装"""
    def __init__(self):
        #-------------track------------
        self.type = []
        self.start = []
        self.end = []
        self.center = []
        self.degree = []
        # -----------scene------------
        self.scene = []
        # -----------AP---------------
        self.AP_power = []
        self.AP_gain = []
        self.AP_limit = []
        self.AP_interval = []
        # -----------Rec--------------
        self.Rec_gain = []
        self.Rec_sensitivity = []
        self.Rec_SIR = []
        self.Rec_Outage = []
        # ----------interval----------
        self.interf_power_1 = []
        self.interf_power_2 = []
        self.interf_coordinate_1 = []
        self.interf_coordinate_2 = []

    def get_track_data(self, type, start, end, center="/", degree="/"):
        """包括：直线型轨道和圆弧型轨道"""
        self.type.append(type)
        self.start.append(start)
        self.end.append(end)
        self.center.append(center)
        self.degree.append(degree)

    def del_track_data_all(self):
        """删除所有track相关的数据"""
        self.type.clear()
        self.start.clear()
        self.end.clear()
        self.center.clear()
        self.degree.clear()

    def get_scene_data(self, scene):
        """获取场景参数"""
        self.scene.append(scene)

    def del_scene_data_all(self, scene):
        """删除场景参数"""
        self.scene.clear()

    def get_AP_data(self, power, gain, limit, interval):
        """获取AP参数"""
        self.AP_power.append(power)
        self.AP_gain.append(gain)
        self.AP_limit.append(limit)
        self.AP_interval.append(interval)

    def del_AP_data_all(self):
        """删除AP参数"""
        self.AP_power.clear()
        self.AP_gain.clear()
        self.AP_limit.clear()
        self.AP_interval.clear()

    def get_Rec_data(self, gain, sensitivity, SIR, Outage):
        """获取接收机参数"""
        self.Rec_gain.append(gain)
        self.Rec_sensitivity.append(sensitivity)
        self.Rec_SIR.append(SIR)
        self.Rec_Outage.append(Outage)

    def del_Rec_data_all(self):
        """删除接收机参数"""
        self.Rec_gain.clear()
        self.Rec_sensitivity.clear()
        self.Rec_SIR.clear()
        self.Rec_Outage.clear()

    def get_interval_data(self, power_1, power_2, coordinate_1, coordinate_2):
        """获取干扰参数"""
        self.interf_power_1.append(power_1)
        self.interf_power_2.append(power_2)
        self.interf_coordinate_1.append(coordinate_1)
        self.interf_coordinate_2.append(coordinate_2)

    def del_interval_data_all(self):
        """删除干扰参数"""
        self.interf_power_1.clear()
        self.interf_power_2.clear()
        self.interf_coordinate_1.clear()
        self.interf_coordinate_2.clear()



app = QApplication(sys.argv).instance()
myDataContainer = DataContainer()