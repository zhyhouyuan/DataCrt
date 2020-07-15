#-*- coding: utf-8 -*-
__author__ = 'zhy'
import numpy as np
import math
import random
class datac(object):
    def __init__(self,com,amount):
        self.amount=amount
        self.r=[]       #保存距离，用来计算功率密度
        self.com=com    #飞机类型
        self.Q=[]       #保存数据
        ##下面为几个频率波段，数组包括最大值和最小值
        self.L=[1,2]
        self.S=[2,4]
        self.C=[4,8]
        self.X=[8,12]
        self.K=[18 ,27]
        self.Ka=[27,40]
        self.UHF=[0.3,1]
        #发生功率，参数包括峰值功率和平均功率KW
        self.power_1=[60,10]
        self.power_2 = [80, 30]
        self.power_3 = [20, 15]
        self.dutycycle=[0.2,1.5] #占空比的范围
        self.repfre=[100,10000]  #重复频率与信号频率的比例范围
        self.bw=[0.2,0.4]   #带宽的比例系数
        self.state=['EA','EP','ES']#三种模式
        self.G=100 #天线增益
        #self.fai=0.5
        self.As=1#接收面积
    #雷达数据生成函数
    def creatrad(self,fre0,power0,mod,set):#输入频率波段，功率参数，当前雷达模式，复位系数
        setrad=0 #标志位
        t=0       #计数
        duty=random.uniform(self.dutycycle[0],self.dutycycle[1])  #占空比参数
        repet=random.uniform(self.repfre[0],self.repfre[1])       #重复频率系数
        mood=mod
        power=power0
        for i in range(self.amount): #在每个时间点做数据生成
            data=[0,0,0,0,0,'--']
            #根据模式选择不同的频率波段
            if mood == 'EA':
                fre=fre0[0]
            elif mood == 'EP':
                fre=fre0[1]
            else:
                fre=fre0[2]
            if setrad==0:
                data[0]=random.uniform(fre[0],fre[1])  #信号中心频率
                #data[1] = power[1] + power[1] / 2 * random.uniform(-1, 1)
                data[1]=self.G*(power[1]+power[1]/2*random.uniform(-1,1))/\
                        (4*math.pi*self.r[i]*self.r[i])*1000000   ##功率密度与发生功率及距离有关
                data[2]=data[0]/repet*1000    #重复频率
                data[3]=duty                  #占空比
                data[4]=data[0]*random.uniform(self.bw[0],self.bw[1])   #带宽
                data[5]=mood                  #模式
                #保留四位小数
                for ii in range (len(data)-1):
                    data[ii]=float('%.4f' % data[ii])
                if data[1]<0:
                    data[1]=power[1]
                t=t+1  #计数
                # #概率改变标志位
                setrad_1=int(random.uniform(0,t)/2000)
                if setrad_1>0:
                    t=0
                    setrad=1
            else:  #标志位为0 不产生数据
                data=[0,0,0,0,0,'--']
                t=t+1
                setrad_2 = int(random.uniform(0, t) / set)
                mood=random.choice(self.state)

                if setrad_2 > 0:
                    duty = random.uniform(self.dutycycle[0], self.dutycycle[1])
                    repet = random.uniform(self.repfre[0], self.repfre[1])
                    t = 0
                    setrad = 0
            self.Q.append(data)
    ##飞机雷达数据生成
    def eledata(self,distance):
        self.r=distance
        self.Q=[]
        L = random.choice(self.state) #初始模式选择
        # 不同飞机分配不同雷达波段
        if self.com=="侦察机":
            fre=[self.L,self.S,self.UHF]
            self.creatrad(fre,self.power_1,L,200)
        if self.com == "预警机":
            fre = [self.C, self.X, self.S]
            self.creatrad(fre, self.power_2, L,200)
        if self.com == "歼击机":
            fre = [self.S, self.K, self.Ka]
            self.creatrad(fre, self.power_3, L,200)
    #航母雷达数据生成
    def shipradata(self,st,dis):#输入复位系数，距离
        self.Q=[]
        self.r=dis
        L = random.choice(self.state)
        if self.com == "母舰":
            fre = [self.L, self.S, self.UHF]
            self.creatrad(fre, self.power_1, L,st)
        if self.com == "驱逐舰":
            fre = [self.C, self.X, self.S]
            self.creatrad(fre, self.power_2, L,st)
        if self.com == "护卫舰":
            fre = [self.S, self.K, self.Ka]
            self.creatrad(fre, self.power_3, L,st)
