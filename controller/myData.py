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
    def __init__(self, _fc=2.4e9, _d0=1, _n=3, _step=5):
        """ TODO 属性都是列表，列表中的每个元素都是存放一批数据
        简单来说，相当于二维列表
        从图形界面接收的数据一般是字符串，存到这个类内全部要先转为数字或者其他对应的数据类型"""
        self.index = 0
        #-------------track------------
        self.type = []
        self.begin = []
        self.end = []
        self.center = []
        self.degree = []  # 圆弧轨道的弧度
        self.step = _step  # 测试点间隔
        self.step_num = 0  # 测试点数量
        # 这个是经过计算的轨道的坐标的x轴列表
        # TODO 相邻之间的两个点之间的距离是self.step
        self.track_list_x = []  # 轨道测试点的x轴坐标列表
        # 和y轴列表
        self.track_list_y = []
        self.track_list_xy = []

        # -----------scene------------
        self.scene = []
        # -----------AP---------------
        self.AP_power = 0
        self.AP_gain = 0
        self.AP_limit = 0
        self.AP_Max = 0
        self.AP_interval = 0
        self.AP_x = []  # 预设的可能的AP的横坐标列表
        self.AP_y = []
        self.AP_xy = []  # 预设的可能的AP组合成坐标形式的列表
        self.AP_current = []  # 当前ap的部署方案
        # -----------Rec--------------
        self.Rec_gain = 0
        self.Rec_sensitivity = 0  # 接收机的灵敏度
        self.Rec_SIR = 0  # 接收机的射频保护比(最小信干比)
        self.Rec_Outage = 0
        # ----------interval----------
        self.interf_power_1 = 0
        self.interf_power_2 = 0
        self.interf_coordinate_1 = []
        self.interf_coordinate_2 = []

        # ---------其他参数-------------
        self.fc = _fc  # 2.4G频率
        self.lamda = 3e8/self.fc  # 2.4G波长
        self.d0 = _d0  # 路径损耗参考距离
        self.n = _n  # 路径损耗指数
        self.threshold = 0.02  # 中断概率的最大阈值
        # 计算中断概率需要知道信号的方差
        self.sgma_AP = 2.5  # 目前先采用默认的大小
        self.sgma_interf1 = 2.5  # 目前先采用默认的大小
        self.sgma_interf2 = 2.5  # 目前先采用默认的大小


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

        else:
            _x, _y = myTrackTransfrom.get_shape(_type, begin=_begin, end=_end, step=5)
        self.track_list_x += _x#.append(_x)
        self.track_list_y += _y #.append(_y)
        for i in range(len(self.track_list_x)):
            self.track_list_xy.append([self.track_list_x[i], self.track_list_y[i]])
        return [self.track_list_x, self.track_list_y]

    # ------从gui界面获取数据的算法-----------------------------
    def set_track_data(self, index, _type, begin, end, center="/", degree="/"):
        """包括：直线型轨道和圆弧型轨道"""
        self.index = index  # 整型
        self.type.append(_type)  # 字符串
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
        self.AP_power = str2num(power)
        self.AP_gain = str2num(gain)
        self.AP_limit = str2num(limit)
        self.AP_interval = str2num(interval)
        # 得把get_AP_Max放在最后，否则无法使用他后面的数据
        self.get_AP_Max()


    def del_AP_data_all(self):
        """删除AP参数"""
        self.AP_power.clear()
        self.AP_gain.clear()
        #self.AP_limit.clear()
        self.AP_interval.clear()

    def set_Rec_data(self, gain, sensitivity, SIR, Outage):
        """获取接收机参数"""
        self.Rec_gain = str2num(gain)
        self.Rec_sensitivity = (str2num(sensitivity))
        self.Rec_SIR = str2num(SIR)
        self.Rec_Outage = (str2num(Outage))

    def del_Rec_data_all(self):
        """删除接收机参数"""
        self.Rec_gain.clear()
        self.Rec_sensitivity.clear()
        self.Rec_SIR.clear()
        self.Rec_Outage.clear()

    def set_interf_data(self, power_1, power_2, coordinate_1, coordinate_2):
        """获取干扰参数"""
        self.interf_power_1 = (str2num(power_1))
        self.interf_power_2 = (str2num(power_2))
        self.interf_coordinate_1 = str2coordinate(coordinate_1)
        self.interf_coordinate_2 = str2coordinate(coordinate_2)

    def del_interf_data_all(self):
        """删除干扰参数"""
        self.interf_power_1.clear()
        self.interf_power_2.clear()
        self.interf_coordinate_1.clear()
        self.interf_coordinate_2.clear()

# ---------------------- get 系列函数 ------------------------------
    def get_AP_Max(self):
        n = self.AP_interval/self.step  # 一个间隔之间有n个测试点
        self.step_num = len(self.track_list_x)
        self.AP_Max = int(self.step_num/n)
        return self.AP_Max

    def get_AP_list(self):
        """获取所有AP预设点的坐标信息"""
        # AP的坐标由测试点的坐标来确定，测试点的坐标间隔是step，那么interval/step个测试点之间正好相距interval
        _AP_range = np.arange(0, len(self.track_list_x), int(self.AP_interval/self.step))  # 求出预设坐标的索引列表
        for i in _AP_range:
            self.AP_x.append(self.track_list_x[i])
            self.AP_y.append(self.track_list_y[i])
        _xy = []
        for i in range(len(self.AP_x)):
            _xy.append([self.AP_x[i], self.AP_y[i]])

        self.AP_xy = _xy  # AP_xy是一个列表，每个元素是所有坐标列表

        return self.AP_x, self.AP_y, self.AP_xy

    def get_interf_list(self):
        """获取干扰点的坐标的x列表和y列表"""
        _interf_x_list = [self.interf_coordinate_1[0], self.interf_coordinate_2[0]]
        _interf_y_list = [self.interf_coordinate_1[1], self.interf_coordinate_2[1]]
        return _interf_x_list, _interf_y_list

    def get_AP_deploy(self, M):
        """获取AP所有可能的部署方案坐标
        M 是当前部署的ＡＰ数量
        返回值是_AP_current是列表a，[[1,2],[2,3],...[x,y]]
        列表a的每个元素由若干个坐标(2个元素的列表)组成
        而self.AP_current则是又若干个_AP_current组成"""
        self.get_AP_list()
        _AP_len = len(self.AP_x)
        _AP_current = list(itertools.combinations(self.AP_xy, M))  # 排列组合算法，AP_xy是一个列表，每个元素是一个坐标，即[[1,2],[2,3],[3,4]]
        # 返回的_AP_current是一个列表，每个元素是一个元组，每个元组是一种排列组合方案，元组的数量即排列组合的数量；元组内的元素即每种排列组合的具体方案，其元素类型同被排列组合的元素类型
        # 例如st(itertools.combinations([1,2,3],2),返回值就是[(1,2),(1,3),(2,3)]
        self.AP_current = _AP_current  # AP_current存放了
        return self.AP_current




app = QApplication(sys.argv).instance()
myController = DataContainer() # 单例对象