# 将实物场景分成四类：轨道类、AP类、列车类、干扰基站类
# 最好是设计为单例类
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import math


class TrackTransfrom(object):

    def __init__(self,
                 line_list=list(range(3)),
                 circle_list=list(range(5)),
                 track_dic={},
                 step=5,
                 interval=120,  # AP间隔
                 tracknum=1):
        self.__LineList = line_list
        self.__CircleList = circle_list
        self.__TrackDic = track_dic
        self.__Step = step
        self.__Interval = interval
        self.__TrackNum = tracknum

    def plot_test(self, x, y):
        plt.figure()
        plt.scatter(x, y, marker="x")
        plt.show()

    def get_shape(self, _type, begin=[], end=[], center=[], degree=1, step=1):
        if _type == "圆弧型":
            return self.get_circle(begin=begin, end=end, center=center, degree=degree, step=step)
        elif _type == "直线型":
            return self.get_line(begin=begin, end=end, step=step)

    def get_line(self, begin, end, step):
        """begin是起点坐标、end是终点坐标、step是步长"""
        x1 = begin[0]
        y1 = begin[1]
        x2 = end[0]
        y2 = end[1]
        k = (y2 - y1)/(x2 - x1)
        # 使用sympy可以求解解析解, 将b变成符号b, 求解b
        # 得到直线轨道方程
        b = sy.symbols("b")
        b = sy.solve(k*x1 + b - y1, b)
        b = b[0]
        # 再根据步长，计算出步长所在点的坐标(勾股定理求解）
        # 由于直线上固定步长的横纵坐标间距是相同的，
        # 故只需要求出一段横坐标间隔，其他都一样
        x = sy.symbols("x")
        x = sy.solve(pow(x,2) + pow(k*x, 2) - pow(self.__Step,2))
        # 由于勾股定理是解二次方程，可以有两个解，取正数解作为间距
        if (x[1] > 0):
            x = x[1]
        else:
            x = x[2]

        # 以x为横坐标间隔下，可以将直线轨道分为多少段
        num = abs(x2 - x1) / x  # 横坐标可以被分为多少段
        xn = np.linspace(x1, x2, num=num)

        # 计算所有x坐标对应的y坐标
        yn = list()
        for i in range(len(xn)):
            tmp = k*i + b
            yn.append(tmp)

        return [xn, yn]

    def get_circle(self, begin, end, center, degree, step):
        """begin、end是起终点坐标，center是圆心坐标、degree圆心角、step是步长"""
        bgx = begin[0]
        bgy = begin[1]
        edx = end[0]
        edy = end[1]

        # 首先求实际的可能的圆心坐标和半径
        cenx, ceny = sy.symbols('cenx,ceny')
        res = sy.solve([pow(bgx-cenx, 2) + pow(bgy-ceny, 2)
                        - pow(edx-cenx, 2) - pow(edy-ceny, 2),
                        (bgx-cenx)*(edx-cenx) + (bgy-ceny)*(edy-ceny)
                        - ((bgx-cenx)**2 + (bgy-ceny)**2)**0.5
                        * ((edx-cenx)**2 + (edy-ceny)**2)**0.5*math.cos(degree)])  # degree是弧度制
        # 由于是解二次方程，因此有两个解，通过比较哪个解靠近center，就认为是真正的圆心
        if ((res[0][cenx] - center[0])**2
            + (res[0][ceny] - center[1])**2) <= ((res[0][cenx] - center[0])**2
            + (res[0][ceny] - center[1])**2):
            cenx = res[0][cenx]
            ceny = res[0][ceny]
        else:
            cenx = res[1][cenx]
            ceny = res[1][ceny]

        # 求圆弧的起点、终点与x轴之间的夹角
        alpha = np.array([bgx-cenx, bgy-ceny])
        beta = np.array([edx-cenx, edy-ceny])
        gama = np.array([1, 0])
        r = math.sqrt(alpha[0]**2 + alpha[1]**2)  #r是圆弧半径
        theta0 = math.acos(np.dot(alpha, gama) / math.sqrt(alpha[0] ** 2 + alpha[1] ** 2)
                           * math.sqrt(gama[0] ** 2 + gama[1] ** 2))
        theta1 = math.acos(np.dot(gama, beta) / math.sqrt(beta[0] ** 2 + beta[1] ** 2)
                           * math.sqrt(gama[0] ** 2 + gama[1] ** 2))

        # 判断圆心角的正负, 这段存疑

        if alpha[1] >= 0:
            theta0 = abs(theta0)
        elif alpha[1] <= 0:
            theta0 = -theta0
        thet0 = min(theta0, theta1)
        thet1 = max(theta0, theta1)
        # 获取等间隔的角度（间隔为0.01)
        if thet1 - thet0 >= math.pi:
            thet0 = thet0 + 2*math.pi
            theta = np.arange(thet1, thet0, 0.01)
        else:
            theta = np.arange(thet0, thet1, 0.01)
        # 使用参数方程表示圆
        # x = r*math.cos(theta) + cenx
        # y = r*math.sin(theta) + ceny
        # 根据路径间隔获取角度间隔，数学依据：周长 = 2*pi*r
        deta_theta = step/r
        xn = []
        yn = []
        for thetan in np.arange(thet0, thet1, deta_theta):
            x = r * math.cos(thetan) + cenx
            y = r * math.sin(thetan) + ceny
            xn.append(x)
            yn.append(y)

        return [xn, yn]

    # def set_step(self, step):
    #     self.__Step = step


# class MyTrain(object):
#     """列车类包括：列车的接受增益、中断阈值、射频保护比（SIR）"""
#     """灵敏度"""
#
#     def __init__(self,
#                  rec_pow = 0,
#                  rec_gain = 0,
#                  threshold = 0,
#                  min_sir = 0,
#                  sensitivity = 0):
#         self.__RecPow = rec_pow
#         self.__RecGain = rec_gain
#         self.__threshold = threshold
#         self.__MinSIR = min_sir
#         self.__sensitivity = sensitivity
#
#
# class MyInterference(object):
#     """干扰基站的坐标、干扰功率"""
#     def __init__(self,
#                  position=[0, 0],
#                  power=24.8):
#         self.__position = position
#         self.__power = power


# class MyAP(object):
#     """AP类包括：发射功率、发射增益、AP的坐标"""
#     def __init__(self,
#                  power=0,
#                  gain=0,
#                  position=[0, 0]
#                  ):
#         self.__power = power
#         self.__gain = gain
#         self.__position = position


# 虚拟场景分为5类：目前主要使用外部导入类和平原这两种
#
# class ScenePlain(object):
#     def __init__(self,
#                  refer=1,
#                  exp=3,
#                  variance=2.75,  # 对数方差
#                  ):
#         self.refer = refer
#         self.exp = exp
#         self.variance = variance
#
#     def log_distance_model(self):
#         #
#         pass
#
#
# class ExImporter(object):
#     """外部导入器，导入每个点上的干扰功率"""
#     def __init__(self, ):
#         pass
#
#     def txt_parse(self, txt):
#         # 提取boyu输出文件中的干扰功率部分
#         pass

myTrackTransfrom = TrackTransfrom()

if __name__ == "__main__":

    x, y = myTrackTransfrom.get_circle([10,0], [0,10], [0, 0], 3.14/2, 1)
    myTrackTransfrom.plot_test(x, y)