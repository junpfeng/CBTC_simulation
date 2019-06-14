import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from myAlogrithm import *
from myParse import *
import itertools  # 排列组合公式

class DataContainer():
    """将图形界面输入的各种
    数据统统进行封装"""
    def __init__(self, _fc=3e8, _f0=1, _n = 3):
        """ TODO 属性都是列表，列表中的每个元素都是存放一批数据
        简单来说，相当于二维列表"""
        self.index = 0
        #-------------track------------
        self.type = []
        self.begin = []
        self.end = []
        self.center = []
        self.degree = []  # 圆弧轨道的弧度
        self.step = []  # 测试点间隔
        self.step_num = []  # 测试点数量
        # 这个是经过计算的轨道的坐标的x轴列表
        # TODO 相邻之间的两个点之间的距离是self.step
        self.track_list_x = []  # 轨道测试点的x轴坐标列表
        # 和y轴列表
        self.track_list_y = []

        # -----------scene------------
        self.scene = []
        # -----------AP---------------
        self.AP_power = []
        self.AP_gain = []
        self.AP_limit = []
        self.AP_Max = []
        self.AP_interval = []
        self.AP_x = []  # 预设的可能的AP的横坐标列表
        self.AP_y = []
        self.AP_xy = []  # 预设的可能的AP组合成坐标形式的列表
        self.AP_current = []  # 当前ap的部署方案
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

        # ---------其他参数-------------
        self.fc = _fc  # 光速
        self.f0 = _f0  # 路径损耗参考距离
        self.n = _n  # 路径损耗指数

    # ------将直接获取的起点终点轨道坐标转换为轨道间隔坐标-----------
    def get_track_list(self, index=0):
        """返回轨道坐标的x轴和y轴"""
        _type = self.type[index]
        _begin = self.begin[index]
        _end = self.end[index]
        if _type == "圆弧型":
            _center = self.center[index]
            _degree = self.degree[index]
            _x, _y = myTrackTransfrom.get_shape(_type, begin=_begin, end=_end, center=_center, degree=_degree, step=5)
            self.track_list_x.append(_x)
            self.track_list_y.append(_y)
            return [self.track_list_x[index], self.track_list_y[index]]
        else:
            _x, _y = myTrackTransfrom.get_shape(_type, begin=_begin, end=_end, step=5)
            self.track_list_x.append(_x)
            self.track_list_y.append(_y)
            return [self.track_list_x[index], self.track_list_y[index]]

    # ------从gui界面获取数据的算法-----------------------------
    def set_track_data(self, index, type, begin, end, center="/", degree="/"):
        """包括：直线型轨道和圆弧型轨道"""
        self.index = index  # 整型
        self.type.append(type)  # 字符串
        self.begin.append(str2coordinate(begin))  # 得到的是字符串，转整型
        self.end.append(str2coordinate(end))
        self.center.append(str2coordinate(center))
        self.degree.append(angle2radian(degree))

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
        self.get_AP_Max()
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

    def get_AP_Max(self):
        n = self.AP_interval/self.step  # 一个间隔之间有n个测试点
        self.step_num[self.index] = len(self.track_list_x[self.index])
        self.AP_Max[self.index] = self.step_num[self.index]/n;
        return self.AP_Max[self.index]

    def get_AP_list(self):
        """获取所有AP预设点的坐标信息"""
        self.AP_x.append(np.arange(self.begin[self.index][0], self.begin[self.index][1], self.AP_interval/self.step))
        self.AP_y.append(np.arange(self.end[self.index][0], self.end[self.index][1], self.AP_interval / self.step))
        _xy = []
        for i in range(len(self.AP_x[self.index])):
            _xy.append([self.AP_x[self.index][i], self.AP_y[self.index[i]]])

        self.AP_xy.append(_xy)  # AP_xy是一个列表，每个元素是所有坐标列表

        return self.AP_x, self.AP_y, self.AP_xy

    def get_AP_deploy(self, M):
        """获取AP所有可能的部署方案坐标
        M 是当前部署的ＡＰ数量
        返回值是_AP_current是列表a，[[1,2],[2,3],...[x,y]]
        列表a的每个元素由若干个坐标(2个元素的列表)组成
        而self.AP_current则是又若干个_AP_current组成"""
        _AP_len = len(self.AP_x)
        _AP_current = list(itertools.combinations(self.AP_xy[self.index], M))
        self.AP_current.append(_AP_current)
        return _AP_current




app = QApplication(sys.argv).instance()
myController = DataContainer() # 单例对象