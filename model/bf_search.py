import numpy as np
from myData import myController
import itertools
import math
a = list(itertools.combinations([[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8], [1,9]],4))
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

        # 几个其他比较重要的参数
        self.


    def get_distance(self, _xy1, _xy2):
        """获取两个坐标之间的欧式距离"""
        return math.sqrt((_xy1[0] - _xy2[0])**2 + (_xy1[1] - _xy2[1])**2)

    def bf_search(self):
        """穷举法：
        输入参数：AP数量下限、上限、AP的预设点坐标(x,y,(x,y))
        输入参数：轨道的x和y轴坐标、轨道测试点的数量、干扰坐标、
        (参数原则，能传参的，绝不计算，加快运行速度）"""
        for i in np.arange(self.controller.AP_limit, self.controller.AP_Max, 1):
            _AP_current_num = i
            # 获取当前AP部署数量下的所有可能AP部署方案
            _AP_current_xy = self.controller.get_AP_deploy(_AP_current_num)


            # 对当前部署数量下的每种方案进行仿真
            for j in range(_AP_current_num):

                # 对于当前部署方案，遍历整个轨道
                for k in range(self.controller.step_num):
                    # 首先计算当前测试点与两个干扰之间的距离
                    _distance_interf_1 = self.get_distance(self.controller.AP_list_xy[k], self.controller.interf_coordinate_1)
                    _distance_interf_2 = self.get_distance(self.controller.AP_list_xy[k], self.controller.interf_coordiante_2)

                    # 确定当前测试点接入哪个AP，接入原则是靠近哪个就接入哪个
                    _distance_AP = []
                    for m in range(_AP_current_num):
                        _distance_AP.append(self.get_distance([self.controller.track_list_x[m], self.controller.track_list_y[m]], self.controller.AP_list_xy[m]))

                    # 最短的距离为当前测试点与AP之间的通信距离
                    _distance_AP_current = min(_distance_AP)
                    pass

    def get_outage(self, _distance_AP_current, _distance_interf_1, _distance_interf_2):
        """输入参数是当前与AP以及两个干扰点之间的距离，信道模型参数，接收机和发射机参数、信号功率参数"""
        #   目前测试阶段，先不使用外部方式，而是全部使用平原的场景
        _rec_AP_power = self.get_average_power(_distance_AP_current, (self.AP_power + self.AP_gain), self.Rec_gain)

    def get_average_power(self, _distance, power, gain, callback):
        """这个是标准的平原的对数路径损耗模型"""
        # 防止距离过小
        if _distance < 1 :
            _distance = 1
        k = (self.fc/(4*math.pi*self.f0))**self.n
        ave = power + gain - 10 * self.n * math.log10(k)
        return ave




        # 防止距离过小
        if _distance_AP_current < 1 :
            _distance_AP_current = 1


# 单例
myModel = model(myController)

if __name__ == "__main__":
    print(myModel.get_distance([1,2], [12,312]))

