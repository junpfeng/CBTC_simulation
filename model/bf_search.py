import numpy as np
import sympy as sp  # 符号运算和微积分
from myData import myController
import itertools
import math
import scipy as scp
from scipy import integrate
a = list(itertools.combinations([[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8], [1,9]],4))  # 自动计算排列组合的模块
print(a)
print(len(a))

#
# for i in np.arange(myDataContainer.AP_limit,myDataContainer.AP_Max,1):
#
class model():
    """模型类---数据处理"""
    def __init__(self, controller):
        # 浅层复制一份控制器
        self.controller = controller
        self.pass_flg = 1
        # 几个其他比较重要的参数
       # self.


    def get_distance(self, _xy1, _xy2):
        """获取两个坐标之间的欧式距离"""
        _distance = math.sqrt((_xy1[0] - _xy2[0])**2 + (_xy1[1] - _xy2[1])**2)
        if _distance < 1:  # 防止距离过紧，导致近场效应
            _distance = 1
        return _distance

    def bf_search(self):
        """穷举法：
        输入参数：AP数量下限、上限、AP的预设点坐标(x,y,(x,y))
        输入参数：轨道的x和y轴坐标、轨道测试点的数量、干扰坐标、
        (参数原则，能传参的，绝不计算，加快运行速度）
        计算完成得到的结果："""
        self.pass_flg = 1  # pass_flg的标志置位

        # 对于每一种AP的数量
        # 之所以AP_Max要加1,是由于np.arange的运算性质决定
        for i in np.arange(self.controller.AP_limit, self.controller.AP_Max + 1, 1):
            _AP_current_num = i
            # 获取当前AP部署数量下的所有可能AP部署方案
            _AP_current_xy = self.controller.get_AP_deploy(_AP_current_num)

            # 对当前部署数量下的每种方案进行仿真
            for j in range(len(_AP_current_xy)):
                # 首先将当前方案记录下来（是一个元组形式）
                self.controller.AP_current = _AP_current_xy[j]
                # 对于每种方案，都首先假设其是符合条件的
                self.pass_flg = 1
                # 对于当前部署方案，遍历整个轨道
                for k in range(self.controller.step_num):
                    # 首先计算当前测试点与两个干扰之间的距离
                    _distance_interf_1 = self.get_distance(self.controller.track_list_xy[k], self.controller.interf_coordinate_1)
                    _distance_interf_2 = self.get_distance(self.controller.track_list_xy[k], self.controller.interf_coordinate_2)

                    # 确定当前测试点接入哪个AP，接入原则是靠近哪个就接入哪个
                    _distance_AP = []
                    for m in range(len(self.controller.AP_current)):
                        _distance_AP.append(self.get_distance(self.controller.track_list_xy[k], self.controller.AP_current[m]))

                    # 最短的距离为当前测试点与AP之间的通信距离
                    _distance_AP_current = min(_distance_AP)
                    _Pout2 = self.get_outage(_distance_AP_current, _distance_interf_1, _distance_interf_2)

                    # 如果当前测试点的中断概率大于了阈值，则当前部署方案作废
                    if (_Pout2 > self.controller.threshold):
                        self.pass_flg = 0
                        self.controller.Rec_Outage = 0  # 清空之前的记录
                        break
                    # 当前测试点通过，继续
                    self.controller.Rec_Outage = _Pout2

                # 当全部测试点的中断概率均小于阈值，则认为当前方案通过，不继续执行接下来的方案了
                # 全部测试点都通过，pass_flg没有被清0
                if self.pass_flg == 1:
                    break  # 停止继续

            if self.pass_flg == 1:
                break  # 停止继续





    def get_outage(self, _distance_AP_current, _distance_interf_1, _distance_interf_2):
        """输入参数是当前与AP以及两个干扰点之间的距离，信道模型参数，接收机和发射机参数、信号功率参数"""
        #   目前测试阶段，先不使用外部方式，而是全部使用平原的场景
        _rec_AP_power = self.get_average_power(_distance_AP_current, (self.controller.AP_power + self.controller.AP_gain), self.controller.Rec_gain)
        _rec_interf1_power = self.get_average_power(_distance_interf_1, self.controller.interf_power_1, self.controller.Rec_gain)
        _rec_interf2_power = self.get_average_power(_distance_interf_2, self.controller.interf_power_2, self.controller.Rec_gain)

        #  中断概率的计算需要知道来自AP和两个干扰点的信号的方差
        _sgma_AP = self.controller.sgma_AP
        _sgma_interf1 = self.controller.sgma_interf1
        _sgma_interf2 = self.controller.sgma_interf2
        _Sm = self.controller.Rec_sensitivity  # 灵敏度
        _SIR = self.controller.Rec_SIR  # 最小信干比

        # ---------- 定义一些计算中断概率需要的变量-------
        u1, v, u3 = sp.symbols("u1, v, u3")
        _alpha = _rec_AP_power - _Sm
        _tao = _rec_AP_power - (_rec_interf1_power + _SIR)
        _tao1 = _rec_AP_power - (_rec_interf2_power + _SIR)

        # ----------公式部分拆解
        Pout2_1 = (1/2)*math.erfc(_alpha/(math.sqrt(2)*_sgma_AP))  #

        # 积分上下限拆解
        Pout2_2_down = (-_alpha)/(math.sqrt(2)*_sgma_AP)
        Pout2_2_up = 700  # 数值积分必须给出具体数，采用10000表示inf
        Pout2_3_1_down = (-_alpha)/(math.sqrt(2)*_sgma_AP)
        Pout2_3_1_up = 700  # math.inf
        Pout2_3_2_down = -700  # math.inf
        # 使用闭包定义积分上限
        def Pout2_3_2_up(v):
            return (_sgma_AP / _sgma_interf1) * v + _tao / (math.sqrt(2) * _sgma_interf1)

        # -----------整合计算公式-------
        # python积分方法：sp.integrate(exp, (积分变量, 下限, 上限)),符号运算无法得到数值解
        # x = sp.symbols("x")
        # 将表达式定义为函数，给scipy.integrate.quad()函数使用，采用闭包方式
        def fun1(x):
            return math.exp(-x**2)*math.erfc((_sgma_AP/_sgma_interf1)*x + _tao/(math.sqrt(2)*_sgma_interf1))

        # 将z1放到下面fun2这个函数中，否则z1作为一个符号表达式，无法被数值积分
        # z1 = 10*sp.log((10**((sp.sqrt(2)*_sgma_AP*v + _tao)/10)) - (10**((sp.sqrt(2)*_sgma_interf1*u3)/10))) - _tao + _tao1
        # 定义闭包
        def fun2(u3, v):
            z1 = 10 * math.log10((10 ** ((math.sqrt(2) * _sgma_AP * v + _tao) / 10)) - (10 ** ((math.sqrt(2) * _sgma_interf1 * u3) / 10))) - _tao + _tao1
            return math.exp(-v**2)*math.exp(-u3**2)*math.erfc(z1/(math.sqrt(2)*_sgma_interf2))

        Pout2 = Pout2_1 + \
                ((1/2)*math.pi)*integrate.dblquad(fun2, Pout2_3_1_down, Pout2_3_1_up, Pout2_3_2_down, Pout2_3_2_up)[0] + \
                (1/(2*math.sqrt(math.pi)))*integrate.quad(fun1, Pout2_2_down, Pout2_2_up)[0]   # 积分函数返回的是列表，第一个元素是积分值

        return Pout2

    def get_average_power(self, _distance, power, gain):
        """这个是标准的平原的对数路径损耗模型"""
        # 防止距离过小
        if _distance < 1:
            _distance = 1
        k = (self.controller.lamda/(4*math.pi*self.controller.d0))**self.controller.n
        ave = power + gain - 10 * self.controller.n * math.log10(abs(_distance)/self.controller.d0)+10*math.log10(k)
        return ave



# 单例
myModel = model(myController)

if __name__ == "__main__":
    print(myModel.get_distance([1,2], [12,312]))

