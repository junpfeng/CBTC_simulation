import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from myAlogrithm import *
from myParse import *

class DataContainer():
    """将图形界面输入的各种
    数据统统进行封装"""
    def __init__(self):
        self.index = 0
        #-------------track------------
        self.type = []
        self.begin = []
        self.end = []
        self.center = []
        self.degree = []
        # 这个是经过计算的轨道的坐标的x轴列表
        self.track_list_x = []
        # 和y轴列表
        self.track_list_y = []

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

    # ------将直接获取的起点终点轨道坐标转换为轨道间隔坐标-----------
    def get_tracak_list(self, index=0):
        """返回轨道坐标的x轴和y轴"""
        _begin = str2coordinate(self.begin[index])
        _end = str2coordinate(self.end[index])
        _center = str2coordinate(self.center[index])
        _degree = str2coordinate(self.degree[index])
        _type = self.type[index]
        return myTrackTransfrom.get_shape(self, _type, begin=_begin, end=_end, center=_center, degree=_degree, step=5)

    # ------从gui界面获取数据的算法-----------------------------
    def set_track_data(self, index, type, begin, end, center="/", degree="/"):
        """包括：直线型轨道和圆弧型轨道"""
        self.index = index
        self.type.append(type)
        self.begin.append(begin)  # 得到的是字符串
        self.end.append(end)
        self.center.append(center)
        self.degree.append(degree)

    def del_track_data_all(self):
        """删除所有track相关的数据"""
        self.type.clear()
        self.begin.clear()
        self.end.clear()
        self.center.clear()
        self.degree.clear()

    def set_scene_data(self, scene):
        """获取场景参数"""
        self.scene.append(scene)

    def del_scene_data_all(self, scene):
        """删除场景参数"""
        self.scene.clear()

    def set_AP_data(self, power, gain, limit, interval):
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

    def set_Rec_data(self, gain, sensitivity, SIR, Outage):
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

    def set_interval_data(self, power_1, power_2, coordinate_1, coordinate_2):
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