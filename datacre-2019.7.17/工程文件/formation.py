import numpy
import copy
import math
class Formation(object):
# 拿到主机的航迹数据，二维数组
    # formationType——队形，跟随队形或者菱形队形
    # leaderCord——主机坐标
    # num——机群数量，除了主机其余为僚机
    # 用圆的思想来处理，半径设置为1km
    # math.pi/6 是30度的意思
    # 生成菱形队形的方法
    def diamondFormation(self,leaderCord,num = 1,r = 500):
        # 更改角度
        beta = math.pi / 6
        deth = 0
        C=[]
        # 第一个存的是主机数据
        C.append(leaderCord)
        if num == 1:
            leftNum = 0
            rightNum = 0
        else:
            if (num-1) % 2 == 0:
                # 偶数架撩机，那么让左侧和右侧飞机数量相同
                leftNum = (int)((num - 1) / 2)
                rightNum = (int)((num - 1) / 2)
            else:
                # 奇数架僚机，那么让左边的僚机多一个
                leftNum = (int)((num - 2)/2 + 1)
                rightNum = (int)((num - 2) / 2)
            
        # 对左侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(leftNum):
            # 每架飞机有存储自己航迹的二维数组
            diamondTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理左侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane+1)*r)*math.sin(math.pi + beta + newDot[3])
                newDot[0] = newDot[0] + ((plane+1)*r)*math.sin(math.pi + beta)
                # newDot[1] = newDot[1] + ((plane+1)*r)*math.cos(math.pi + beta + newDot[3])
                newDot[1] = newDot[1] + ((plane+1)*r)*math.cos(math.pi + beta)
                newDot[2] = newDot[2] - (plane+1)*deth
                # 单个点处理完成后，将其放在航迹数组里
                diamondTrace.append(newDot)
            C.append(diamondTrace)
            # 出第一层循环以后将该飞机的航迹数组生成文件或者输出

        # 对右侧每架飞机的循环，循环一次出一个飞机的航迹文件
        for plane in range(rightNum):
            # 每架飞机有存储自己航迹的二维数组
            diamondTrace = []
            # 对每架飞机里的每个点做处理
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理右侧飞机的xy轴坐标
                # newDot[0] = newDot[0] + ((plane+1) * r) * math.sin(math.pi - beta + newDot[3])
                newDot[0] = newDot[0] + ((plane+1) * r) * math.sin(math.pi - beta)
                # newDot[1] = newDot[1] + ((plane+1) * r) * math.cos(math.pi - beta + newDot[3])
                newDot[1] = newDot[1] + ((plane+1) * r) * math.cos(math.pi - beta)
                newDot[2] = newDot[2] - (plane+1)*deth
                # 单个点处理完成后，将其放在航迹数组里
                diamondTrace.append(newDot)
            C.append(diamondTrace)
        return C
    # 生成跟随的线性编队
    def linearFormation(self, leaderCord, number = 1, r = 500):
        deth = 0
        C=[]
        C.append(leaderCord)
        # 对每架飞机做循环，要输出一个这架飞机的航迹文件
        # if number == 1:
        num = number - 1
        # else:
        #     num = number
        for plane in range(num):
            lineartrace = []
            for dot in leaderCord:
                newDot = copy.deepcopy(dot)
                # 处理跟随飞机的xy坐标
                # newDot[0] = newDot[0] + (plane+1)*r * math.sin(math.pi  + newDot[3])
                newDot[0] = newDot[0] + (plane+1)*r * math.sin(math.pi)
                # newDot[1] = newDot[1] + (plane+1)*r * math.cos(math.pi  + newDot[3])
                newDot[1] = newDot[1] + (plane+1)*r * math.cos(math.pi)
                newDot[2] = newDot[2] - (plane+1) * deth
            # 坐标处理完毕，将点迹信息放入航迹数组中
                lineartrace.append(newDot)
            C.append(lineartrace)
        return C