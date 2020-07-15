#-*- coding: utf-8 -*-
__author__ = 'zhy'
#界面画图文件，以及数据转换函数
#-*-coding:utf-8-*-
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import numpy
import math
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):

    def __init__(self,Q=[],P=[],width=20, height=20, dpi=60,):
        self.Q = Q
        self.P = P
        self.rat=0#放大比例
        self.color=['r','y','g','b','c','k','m']
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)

        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        #self.axes=Axes3D(self.fig)

        self.axes = self.fig.add_subplot(111,projection='3d')
        # self.fig.canvas.mpl_connect('button_press_event', self.on_key_press)
        #坐标范围
        self.x=[0,0]
        self.y=[0,0]
        self.z=[0,0]

    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plot(self,Q,p):

        xmin=xmax=0
        ymin=ymax=0
        #画飞机轨迹
        for ij in range(len(Q)):
            self.Q = Q[ij]

            for i in range (len(self.Q)):
                #获取位置坐标
                X = [j[0] for j in self.Q[i]]
                Y = [j[1] for j in self.Q[i]]
                Z = [j[2] for j in self.Q[i]]
            #self.axes=self.fig.add_subplot(111, projection='3d')
                #self.axes.plot_wireframe(X,Y,Z)
                self.axes.scatter(X[0:1], Y[0:1], Z[0:1],c="k",marker="x") #起始位置
                self.axes.plot(X[:], Y[:], Z[:],c=self.color[i%7]) #分配不同颜色
                self.axes.scatter(X[len(X)-2:len(X)-1], Y[len(X)-2:len(X)-1], Z[len(X)-2:len(X)-1],c="k",marker="^")#终点
                #获得坐标的最大范围
                xmin=min(min(X[:]),xmin)
                xmax=max(max(X[:]),xmax)
                ymin = min(min(Y[:]),ymin)
                ymax = max(max(Y[:]),ymax)
        #画航母轨迹
        for ij in range(len(p)):
            self.P = p[ij]
            for i in range(len(self.P)):
                X = [j[0] for j in self.P[i]]
                Y = [j[1] for j in self.P[i]]
                Z = [j[2] for j in self.P[i]]
                # self.axes=self.fig.add_subplot(111, projection='3d')
                # self.axes.plot_wireframe(X,Y,Z)
                self.axes.scatter(X[0:1], Y[0:1], Z[0:1], c="k", marker="x")
                self.axes.plot(X[:], Y[:], Z[:], c=self.color[i % 7])
                self.axes.scatter(X[len(X) - 2:len(X) - 1], Y[len(X) - 2:len(X) - 1], Z[len(X) - 2:len(X) - 1], c="k",
                                  marker="^")
                xmin = min(min(X[:]), xmin)
                xmax = max(max(X[:]), xmax)
                ymin = min(min(Y[:]), ymin)
                ymax = max(max(Y[:]), ymax)
        self.x=[xmin,xmax]
        self.y=[ymin,ymax]
        self.z=[0,15000]
        xx,yy=numpy.meshgrid(self.x,self.y)#设置坐标范围
        zz=xx*0
        self.axes.plot_surface(xx,yy,zz,cmap=plt.cm.YlGnBu_r,alpha=0.2)#画海平面
        self.axes.set_zlabel('Z')  # 坐标轴
        self.axes.set_ylabel('Y')
        self.axes.set_xlabel('X')
        #self.axes.set_xlim(100, 5000)
        #self.axes.set_ylim(100, 5000)
        self.axes.set_zlim(0,15000)
        self.Xlen=xmax-xmin
        self.Ylen=ymax-ymin
        self.Zlen=15000
        # plt.legend(loc='upper right')
    #数据转换函数
    def dtransf(self,data):
        Fdata=[]
        for i in range(len(data)):
            datamid=[]
            for j in data[i]:
                data0 = [0, 0, 0, 0, 0,0,0,0]
                data0[0] = j[0] #X坐标
                data0[1] = j[1] #y坐标
                data0[2] = j[2] #z坐标
                data0[3]=numpy.sqrt(j[0]*j[0]+j[1]*j[1]+j[2]*j[2])##求与原点的距离
                #计算对方相对于原点的运动夹角
                if j[1]>0:#1、2象限
                    data0[4]=math.pi-math.atan(j[0]/j[1])+j[3]
                else:
                    data0[4] = - math.atan(j[0] / j[1]) + j[3]
                #夹角在0-2π之间
                if data0[4] >= 2 * math.pi:
                    data0[4] =data0[4]  - 2 * math.pi
                elif data0[4]  < 0:
                    data0[4] = data0[4] + 2 * math.pi
                if data0[4]>math.pi:#映射到0-π
                    data0[4]=math.pi*2-data0[4]
                data0[5]=math.atan(data0[2]/data0[3])#计算仰角
                data0[6]=j[3] #航向角
                data0[7]=j[5] #速度
                #保留4位小数
                for ii in range (len(data0)):
                    data0[ii]=float('%.4f' % data0[ii])

                datamid.append(data0)
            Fdata.append(datamid)
        return Fdata

    # def mousePressEvent(self, e):  ##重载一下鼠标点击事件
    #      # 右键放大
    #      if e.buttons() == QtCore.Qt.RightButton:
    #          self.axes.set_xlim(1000,5000)
    #          self.axes.set_ylim(1000, 5000)
    #          print(1)
    # def on_key_press(self,event):
    #     if event.button == 3:
    #         self.rat+=1
    #         C1x = event.xdata
    #         C1y = event.ydata
    #         print(C1x,C1y)
    #         #C1z = event.zdata
    #         self.enlarge(C1x,C1y)
    #     if self.rat>7:
    #         self.rat=1
    # def enlarge(self,x,y):
    #     print(1)
        # if self.rat>=1:
        #     self.axes.set_xlim(x-self.Xlen/self.rat, x+self.Xlen/self.rat)
        #     self.axes.set_ylim(y-self.Ylen/self.rat, y+self.Ylen/self.rat)
        #     #self.axes.set_zlim(z-self.Ylen/self.rat, z+self.Zlen/self.rat)
        # else:
        #     self.axes.set_xlim(self.x[0],self.x[1])
        #     self.axes.set_ylim(self.y[0],self.y[1])
        #     #self.axes.set_zlim(self.z[0],self.z[1])
