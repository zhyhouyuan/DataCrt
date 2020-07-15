#-*- coding: utf-8 -*-
__author__ = 'zhy'
#######################################################
##航母轨迹生成文件，包括直线，转弯，种类包括护卫舰，巡航舰，主舰
############
import numpy as np
import math
import copy
import random
import Radar
class Ship(object):
    def __init__(self, action, num1,num2,p0):
        self.action = action
        self.p0= p0 #初始位置数据
        self.num=[num1,num2] ##驱逐舰和护卫舰的数量
        self.Q_Centre=[]     #用于保存主舰的态势数据
        self.Q_all=[]        #用保存所有航母的态势数据

        self.va1=[30,1.5]   #速度30节，加速度
        self.V_jie=0.514    #节与米每秒 单位转换系数
        self.radarnum=3     #每个航母搭载的雷达数量
    def creata(self,t,amax,aa):#aa是加加速度，假设为常数
        if t<=(2*math.sqrt(amax/aa)):
            a=amax-aa*math.pow((t-math.sqrt(amax/aa)),2)
        else:
            a=0
        return a
    ##直线动作函数
    def trackline(self,p0,t,F,amax,aa,vmax):
        p1=p0
        p1[2]=0 #Z坐标为0
        for i in range(int(t*100)):
            data=[0,0,0,0,0,0,0,0]
            for j in range(len(p1)):
                data[j]=p1[j]
            p1[0] = p1[4] * 1/100 * (math.sin(p1[3])) + p1[0]
            p1[1] = p1[4] * 1/100 * (math.cos(p1[3])) + p1[1]
            p1[4] = p1[4] + 1/ 100 * p1[5]
            p1[6]=0
            if (F>0)&(p1[4]<=vmax):         #加速
                p1[5] = self.creata(1/100*i,amax,aa)
            elif (F<0)&(p1[4]>0):         #减速
                p1[5] =0 - self.creata(1/ 100 * i, amax, aa)
            else:        #匀速
                p1[5]=0
            if p1[4]<0:#速度最小为0
                p1[4]=0
            data[7] = np.sqrt(data[0] * data[0] + data[1] * data[1])  # 与原点的距离
            self.Q_Centre.append(data)
        return 0
    #转弯动作函数
    def trackturn(self,p0, t, a):
        p1=p0
        p1[2]=0
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0,0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            p1[0] = p1[4] * 1/100 * (math.sin(p1[3])) + p1[0] #X坐标
            p1[1] = p1[4] * 1/100 * (math.cos(p1[3])) + p1[1]  #Y坐标
            p1[3] = (p1[3] + 1/100 * a/p1[4]) % (2*math.pi) #a 法向加速度，计算航向角
            p1[4] = p1[4] + 1/ 100 * p1[5]  # 切向加速度
            if (p1[4]<=0)&(p1[4]>=self.va1[0]*self.V_jie):         #约束速度范围
                p1[5]=0
                if p1[4]<0:#速度最小为0
                    p1[4]=0
            p1[6]=a
            data[7] = np.sqrt(data[0] * data[0] + data[1] * data[1])#计算距离
            self.Q_Centre.append(data)
        return 0
    #主舰轨迹生成函数
    def shiptrack(self):
        vmax=self.va1[0]*self.V_jie #最大速度
        amax=self.va1[1]*self.V_jie #最大加速度
        aa=0.5
        for i in range(len(self.action)):
            if self.action[i] == "直行":
                t = random.random() * 10 + 5
                F = random.randint(-1, 1)
                self.trackline(self.p0, t, F, amax, aa, vmax)
            if self.action[i] == "左转弯":
                t = random.random() * 10 + 5
                a = -random.uniform(1, 2)
                self.trackturn(self.p0, t, a)
            if self.action[i] == "右转弯":
                t = random.random() * 10 + 5
                a = random.uniform(1, 2)
                self.trackturn(self.p0, t, a)
    #其他航母轨迹，以主舰为中心
    def othertrack(self):
        self.shiptrack()
        self.Q_all.append(self.Q_Centre)
        r1=1900#与主舰的距离
        r2=random.uniform(22,46)*100#与主舰的距离
        for i in range (self.num[0]):  #驱逐舰
            shipdata=copy.deepcopy(self.Q_Centre)  #深拷贝
            for j in range(len(self.Q_Centre)):  #遍历主舰的轨迹数据
                #计算X,Y坐标，航向角
                shipdata[j][0] = self.Q_Centre[j][0]+math.sin(2*i*math.pi/self.num[0])*r2
                shipdata[j][1] = self.Q_Centre[j][1]+ math.cos(2*i*math.pi/self.num[0]) * r2
                shipdata[j][7]=np.sqrt(shipdata[j][0] * shipdata[j][0] + shipdata[j][1] * shipdata[j][1])
            self.Q_all.append(shipdata)
        for i in range(self.num[1]): #护卫舰
            shipdata = []
            for j in self.Q_Centre:
                shipoint = copy.deepcopy(j)
                shipoint[0] = j[0] + math.sin( 2 * i * math.pi / self.num[1]) * r1
                shipoint[1] = j[1] + math.cos( 2 * i * math.pi / self.num[1]) * r1
                shipoint[7] = np.sqrt(shipoint[0] * shipoint[0] + shipoint[1] * shipoint[1])
                shipdata.append(shipoint)
            self.Q_all.append(shipdata)
        #所有数据保留4位小数
        for ii in range(len(self.Q_all)):
            for jj in range(len(self.Q_all[ii])):
                for kk in range(len(self.Q_all[ii][jj])):
                    self.Q_all[ii][jj][kk]=float('% .4f' % self.Q_all[ii][jj][kk])
    def creatrad(self):

        self.othertrack()
        #for i in range (len(self.Q_Centre)):
        distance = [x[7] for x in self.Q_Centre] #主舰离原点距离
        shiprad=Radar.datac('母舰',len(self.Q_Centre))
        #主舰的雷达数据
        for i in range(self.radarnum):#雷达数量
            shiprad.shipradata(100*(i+1),distance)
            for ii in range (len(self.Q_all[0])):
                for iii in shiprad.Q[ii]:
                    self.Q_all[0][ii].append(iii)
        # 驱逐舰的雷达数据
        shiprad.com='驱逐舰'
        for i in range(self.num[0]):
            distance = [x[7] for x in self.Q_all[i + 1]]
            for j in range(self.radarnum):
                shiprad.shipradata(100*(j+1),distance)
                for ii in range(len(self.Q_all[0])):
                    for iii in shiprad.Q[ii]:
                        self.Q_all[i+1][ii].append(iii)
        # 护卫舰的雷达数据
        shiprad.com='护卫舰'
        for i in range(self.num[1]):
            distance = [x[7] for x in self.Q_all[i +self.num[0]+ 1]]
            for j in range(self.radarnum):
                shiprad.shipradata(100*(j+1),distance)
                for ii in range(len(self.Q_all[0])):
                    for iii in shiprad.Q[ii]:
                        self.Q_all[i+self.num[0]+1][ii].append(iii)