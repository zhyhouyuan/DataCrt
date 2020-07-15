#-*- coding: utf-8 -*-
__author__ = 'zhy'
#######################################################
##飞机轨迹生成文件，包括直线，转弯，爬升，俯冲，飞机种类包括侦察机，预警机，歼击机
############
import numpy as np
import math
import random
from matplotlib import pyplot as plt
class datac(object):
    def __init__(self, action, com,p0,num):
        self.action = action #动作序列
        self.p0= p0          #初始数据
        self.com=com         #飞机的种类
        self.Q=[]            #用来保存生成的数据

        self.va1=[190,20,35]   #飞机最大速度，最大加速度，最大爬升率参数
        self.va2 = [810,40,100]
        self.va3 = [180,20,35]
        self.num=num            #飞机数量

    #加速度生成函数
    def creata(self,t,amax,aa): #aa是加加速度，设为常数
        if t<=(2*math.sqrt(amax/aa)):
            a=amax-aa*math.pow((t-math.sqrt(amax/aa)),2)
        else:
            a=0
        return a
    #爬升俯冲时间生成函数，爬升时当前高度越高，则将要爬升的高度越小即时间越短，反之，时间越长。俯冲可类比之
    def creatT(self, z, Fz):
        t = 0
        if Fz < 0:  #判断是俯冲
            if z<=10000:
                t = 20 * math.exp((z - 10000) / 3000)
            else:
                t= 20 * (2-math.exp((10000-z) / 3000))
        elif Fz > 0: #判断是爬升
            if z<=10000:
                t = 20 * (2-math.exp((z - 10000) / 3000))
            else:
                t= 20 * math.exp((10000-z) / 3000)
        #时间较小则忽略不计，即当前高度不允许爬升或俯冲
        if t>=1:
            return t
        else:
            return 0
    #直线动作函数
    def trackline(self,p0,t,F,amax,aa,vmax):
        p1=p0
        for i in range(int(t*100)):   #每0.01秒产生一个数据
            data=[0,0,0,0,0,0,0,0]
            for j in range(len(p1)):
                data[j]=p1[j]
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0] #X坐标
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1] #Y坐标
            p1[5] = p1[5] + 1/ 100 * p1[6]                    #速度
            p1[4]=0                                           #俯仰角
            p1[7]=0                                           #法向加速度
            if (F>0)&(p1[5]<=vmax):         #加速不超过最大速度
                p1[6] = self.creata(1/100*i,amax,aa)          #切向加速度
            elif (F<0)&(p1[5]>70):         #减速
                p1[6] =0 - self.creata(1/ 100 * i, amax, aa)
            else:        #匀速
                p1[6]=0
            self.Q.append(data)

        return 0

    def trackturn(self,p0, t, a):
        p1=p0
        # F = random.randint(-1, 2)
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0, 0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            p1[0] = p1[5] * 1/100 * (math.sin(p1[3])) + p1[0]
            p1[1] = p1[5] * 1/100 * (math.cos(p1[3])) + p1[1]
            p1[3] = (p1[3] + 1/100 * a/p1[5])  #a 法向加速度

            # 航向角在0-2π内
            if p1[3]>=2*math.pi:
                p1[3]=p1[3]-2*math.pi
            if p1[3]<0:
                p1[3]=p1[3]+2*math.pi
            p1[5] = p1[5] + 1/ 100 * p1[6]  # 切向加速度
            # if (F>0)&(p1[5]<=vmax):         #加速
            #      p1[6] = self.creata(1/100*i,amax,aa)
            # elif (F<0)&(p1[5]>70):         #减速
            #      p1[6] =0 - self.creata(1/ 100 * i, amax, aa)
            # else:        #匀速
            #      p1[6]=0
            p1[7]=a
            self.Q.append(data)
        return 0
    #爬升俯冲动作函数
    def trackdive(self,p0, t, a1,a2,t1,VZmax):
        t11=0
        p1=p0
        for i in range(int(t * 100)):
            data = [0, 0, 0, 0, 0, 0, 0,0]
            for j in range(len(p1)):
                data[j] = p1[j]
            p1[0] = p1[5] * 1/100 * math.sin(p1[3])*math.cos(p1[4]) + p1[0]
            p1[1] = p1[5] * 1/100 * math.cos(p1[3])*math.cos(p1[4]) + p1[1]
            p1[2] = p1[5] * 1/100 * math.sin(p1[4]) + p1[2]
            p1[6] = 0                       #切向加速度
            p1[5] = p1[5] + 1/100*p1[6]
            if (i/100<t1)&(p1[5]*math.sin(p1[4])<VZmax):   #第一段动作俯仰角变化
                p1[7] = a1
                p1[4] = p1[4] + 1/ 100 * p1[7]/ p1[5]
                t11=i/100
            elif i/100>=(t-t11)-2/100:                #第三段动作俯仰角回变
                p1[7] = a2
                p1[4] = p1[4] + 1 / 100 * a2 / p1[5]
            else :                                      #中间动作以一定角度直线下降
                p1[7]=0
            self.Q.append(data)
        return 0

    #轨迹生成函数
    def trackall(self):
        if self.com == "侦察机": #判断机型得到对应参数
            aa = 3
            amax = self.va1[1]
            vmax = self.va1[0]
            VZmax=self.va1[2]
            for i in range(len(self.action)):
                if self.action[i]=="直线":
                    t=random.random()*10+5  #生成运动时间
                    F=random.randint(-1,2)  #生成状态（加速，减速，匀速）
                    self.trackline(self.p0, t,F,amax, aa,vmax)
                if self.action[i] == "转弯":
                    t = random.random()*10+10
                    a= random.uniform(10,20)*random.randrange(-1,2,2) #生成切向加速度
                    self.trackturn(self.p0, t, a)
                if self.action[i] == '俯冲':
                    t = self.creatT(self.p0[2], -1)  #生成运动时间
                    t1 = random.uniform(t / 4, t / 2) #生成第一段动作运动时间
                    #t2=t-t1
                    a1 = 0-random.uniform(5, 10)
                    a2=0-a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)
                if self.action[i] == '爬升':
                    t = self.creatT(self.p0[2], 1)     #生成运动时间
                    t1 = random.uniform(t / 4, t / 2)  #生成第一段动作运动时间
                    a1 = random.uniform(5,10)
                    a2 = 0 - a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)

        if self.com == "歼击机":
            aa = 3
            amax = self.va2[1]
            vmax = self.va2[0]
            VZmax=self.va2[2]
            for i in range(len(self.action)):
                if self.action[i]=="直线":
                    t=random.random()*10+5
                    F=random.randint(-1,2)
                    self.trackline(self.p0, t,F,amax, aa,vmax)
                if self.action[i] == "转弯":
                    t = random.random() * 10+5
                    a= random.uniform(10,20)*random.randrange(-1,2,2)
                    self.trackturn(self.p0, t, a)
                if self.action[i] == '俯冲':
                    t = self.creatT(self.p0[2], -1)
                    t1 = random.uniform(t / 4, t / 2)
                    t2=t-t1
                    a1 = 0-random.uniform(5,10)
                    a2=0-a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)
                if self.action[i] == '爬升':
                    t = self.creatT(self.p0[2], 1)
                    t1 = random.uniform(t / 4, t / 2)
                    a1 = random.uniform(5,10)
                    a2 = 0 - a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)

        if self.com == "预警机":
            aa = 3
            amax = self.va3[1]
            vmax=self.va3[0]
            VZmax=self.va3[2]
            for i in range(len(self.action)):
                if self.action[i]=="直线":
                    t=random.random()*10+5
                    F=random.randint(-1,2)
                    self.trackline(self.p0, t,F,amax, aa,vmax)
                if self.action[i] == "转弯":
                    t = random.random() * 10+5
                    a= random.uniform(10,20)*random.randrange(-1,2,2)
                    self.trackturn(self.p0, t, a)
                if self.action[i] == '俯冲':
                    t=self.creatT(self.p0[2],-1)
                    t1=random.uniform(t/4,t/2)
                    a1 = 0-random.uniform(5,10)
                    a2=0-a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)
                if self.action[i] == '爬升':
                    t = self.creatT(self.p0[2], 1)
                    t1 = random.uniform(t / 4, t / 2)
                    a1 = random.uniform(5,10)
                    a2 = 0 - a1
                    self.trackdive(self.p0, t, a1, a2, t1, VZmax)

        return 0


