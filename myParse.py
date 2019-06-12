# 用作的文件的特定解析以及字符串的解析
# 使用面向过程直接写方法

def str2coordinate(str):
    """将坐标的字符串拆成x的值和y的值"""
    # 首先去除str两边的空字符串
    str.strip()

    str = str.split(',')
    str0 = str[0].split('(')[1]
    str1 = str[1].split(')')[0]
    # 目前先不进行异常处理
    if str0.isdecimal():
        num0 = int(str0)
    else:
        num0 = float(str0)

    if str1.isdecimal():
        num1 = int(str1)
    else:
        num1 = float(str1)

    return num0, num1

def str2num(str):
    """将字符串变成整数"""
    if str.isdecimal():
        return int(str)
    else:
        return float(str)

def file2list(filename):
    """将zby的输出文件中，提取出有用的一列"""
    pass  # 等文件GUI做出来再做

def angle2radian(str):
    angle = float(str)
    radian = angle/180*3.14
    return radian


if __name__ == "__main__":

    l = [1,2]
    x,y = str2coordinate("(12,123.213)")
    l.append([x,y])
    print(l)
    print(str2num("21.1"))