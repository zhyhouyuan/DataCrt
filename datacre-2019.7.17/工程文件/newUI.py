# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
##UI 文件，主窗口 包含了数据生成，及保存函数
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication,QGroupBox
from PyQt5.QtCore import QCoreApplication,pyqtSignal,QRegExp
from PyQt5.QtGui import QFont,QIcon,QRegExpValidator
from formation import Formation
import Plane
import math
import numpy
import matplot
import Radar
from Warship import Ship
import sip
import copy
import csv
class Ui_MainWindow(QMainWindow,object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 663) #设置窗口大小
        self.F = matplot.MyFigure([], [], width=1, height=1, dpi=60) #轨迹展示图
        # 初始化赋值,（航母的个数等还未初始化）！！
        self.planedata = []  #用于飞机数据保存
        self.shipdata = []   #用于航母数据保存
        self.actionArray = []  #飞机动作序列
        self.shipActionArray = [] #航母动作序列
        self.raddata = []        #飞机电磁数据
        self.num = 1             #计数
        self.savenum = 1         #保存次数计数
        self.formation = 1       #编队标志位
        self.checkedNum = 0      #飞机数量
        self.planeGap = 500      #编队距离
        self.mainShip = 1        #主舰数量默认为1
        self.destroyer = 0       ## 驱逐舰数量
        self.frigate = 0         #护卫舰数量
        self.sig1=0              #飞机初始位置是否设置，标志位
        self.sig2=0              #航母初始位置是否设置，标志位
        #以下为界面设计，QTdesigner自动生成的代码
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_4.addWidget(self.line_18, 0, 1, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_4.addWidget(self.line_19, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_9.addWidget(self.line_15, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 4, 0, 1, 3)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_5.addWidget(self.line_5, 1, 0, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 5, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 6, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.planetype = QtWidgets.QComboBox(self.centralwidget)
        self.planetype.setObjectName("planetype")
        self.planetype.addItem("")
        self.planetype.addItem("")
        self.planetype.addItem("")
        self.horizontalLayout.addWidget(self.planetype)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_5.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.formation = QtWidgets.QComboBox(self.centralwidget)
        self.formation.setObjectName("formation")
        self.formation.addItem("")
        self.formation.addItem("")
        self.horizontalLayout_3.addWidget(self.formation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")

        regx = QRegExp("^[0-9]{9}$") #只允许输入数字
        validator = QRegExpValidator(regx, self.lineEdit)
        self.lineEdit.setValidator(validator)

        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")

        validator = QRegExpValidator(regx, self.lineEdit_2)
        self.lineEdit_2.setValidator(validator)
        
        self.horizontalLayout_8.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        validator = QRegExpValidator(regx, self.lineEdit_3)
        self.lineEdit_3.setValidator(validator)
        
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.turn = QtWidgets.QPushButton(self.centralwidget)
        self.turn.setObjectName("turn")
        self.gridLayout.addWidget(self.turn, 3, 0, 1, 1)
        self.falldown = QtWidgets.QPushButton(self.centralwidget)
        self.falldown.setObjectName("falldown")
        self.gridLayout.addWidget(self.falldown, 4, 0, 1, 1)
        self.flying = QtWidgets.QPushButton(self.centralwidget)
        self.flying.setObjectName("flying")
        self.gridLayout.addWidget(self.flying, 1, 0, 1, 1)
        self.climb = QtWidgets.QPushButton(self.centralwidget)
        self.climb.setObjectName("climb")
        self.gridLayout.addWidget(self.climb, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 6, 1)
        self.delete1 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1.setStyleSheet("color: rgb(255, 0, 0);")
        self.delete1.setObjectName("delete1")
        self.gridLayout.addWidget(self.delete1, 5, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 5, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.numchecked = QtWidgets.QPushButton(self.centralwidget)
        self.numchecked.setStyleSheet("color: rgb(255, 0, 0);")
        self.numchecked.setObjectName("numchecked")
        self.horizontalLayout_2.addWidget(self.numchecked)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 3)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_5)
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_8.addWidget(self.line_16)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scheck1 = QtWidgets.QPushButton(self.centralwidget)
        self.scheck1.setStyleSheet("color: rgb(255, 0, 0);")
        self.scheck1.setObjectName("scheck1")
        self.gridLayout_3.addWidget(self.scheck1, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.scheck2 = QtWidgets.QPushButton(self.centralwidget)
        self.scheck2.setStyleSheet("color: rgb(255, 0, 0);")
        self.scheck2.setObjectName("scheck2")
        self.gridLayout_3.addWidget(self.scheck2, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_3.addWidget(self.spinBox_4, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 3, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_7.addWidget(self.line_13)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_7.addWidget(self.checkBox_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_6.addWidget(self.line_6)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        validator = QRegExpValidator(regx, self.lineEdit_5)
        self.lineEdit_5.setValidator(validator)
        
        self.gridLayout_6.addWidget(self.lineEdit_5, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")

        validator = QRegExpValidator(regx, self.lineEdit_6)
        self.lineEdit_6.setValidator(validator)
        self.gridLayout_6.addWidget(self.lineEdit_6, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 2, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        validator = QRegExpValidator(regx, self.lineEdit_4)
        self.lineEdit_4.setValidator(validator)
        self.gridLayout_6.addWidget(self.lineEdit_4, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.horizontalLayout_21.addLayout(self.verticalLayout_6)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_21.addWidget(self.line_12)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_7.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_7.addWidget(self.textEdit_2, 0, 2, 5, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_7.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.delete2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete2.setStyleSheet("color: rgb(255, 0, 0);")
        self.delete2.setObjectName("delete2")
        self.gridLayout_7.addWidget(self.delete2, 4, 1, 1, 1)
        self.horizontalLayout_21.addLayout(self.gridLayout_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_8.addWidget(self.line_14)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.horizontalLayout_6.addWidget(self.start)
        self.delete3 = QtWidgets.QPushButton(self.centralwidget)
        self.delete3.setStyleSheet("color:rgb(255, 58, 19)")
        self.delete3.setObjectName("delete3")
        self.horizontalLayout_6.addWidget(self.delete3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_9.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 3, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem10, 1, 1, 1, 1)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setObjectName("exitbutton")
        self.gridLayout_2.addWidget(self.exitbutton, 1, 5, 1, 1)
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.savebutton.setObjectName("savebutton")
        self.gridLayout_2.addWidget(self.savebutton, 1, 3, 1, 1)

        self.display = QtWidgets.QPushButton(self.centralwidget)
        self.display.setObjectName("display")
        self.gridLayout_2.addWidget(self.display, 1, 1, 1, 1)

        # self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        # self.groupBox.setObjectName("groupBox")
        # self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 6)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 6)

        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(2, 3)
        self.gridLayout_4.addLayout(self.gridLayout_9, 1, 1, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_4.addWidget(self.line_21, 2, 1, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout_4.addWidget(self.line_20, 3, 0, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_4.addWidget(self.line_17, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.gridlayout2 = QtWidgets.QGridLayout(self.groupBox)  # 继承容器

        self.retranslateUi(MainWindow)
        ##槽函数与按钮关联##
        #飞机四种动作按钮
        self.flying.clicked.connect(self.changeText)
        self.falldown.clicked.connect(self.changeText)
        self.turn.clicked.connect(self.changeText)
        self.climb.clicked.connect(self.changeText)
        #航母三种动作按钮
        self.pushButton_5.clicked.connect(self.changeText1)
        self.pushButton_8.clicked.connect(self.changeText1)
        self.pushButton_7.clicked.connect(self.changeText1)
        # self.pushButton_20.clicked.connect(self.changeText1)
        # self.pushButton_21.clicked.connect(self.changeText1)

        self.start.clicked.connect(self.startPlot)#生成数据按钮
        # 初始位置是否锁定
        self.checkBox.stateChanged.connect(self.changec1)
        self.checkBox_2.stateChanged.connect(self.changec2)

        # self.pushButton_4.clicked.connect(self.submitNum)
        #self.linearButton.clicked.connect(self.changeStatus)
        #self.diamondButton.clicked.connect(self.changeStatus)
        self.numchecked.clicked.connect(self.submitNum1)
        self.scheck1.clicked.connect(self.submitNum2)
        self.delete3.clicked.connect(self.delt) #撤销
        self.scheck2.clicked.connect(self.submitNum3)
        self.delete1.clicked.connect(self.deleteItem1)#删除飞机动作
        self.delete2.clicked.connect(self.deleteItem2)#删除航母动作
        self.savebutton.clicked.connect(self.save)#保存按钮
        self.exitbutton.clicked.connect(QCoreApplication.instance().quit)#退出

        # self.F.fig.canvas.mpl_connect('key_press_event', self.F.on_key_press)
        #self.F.fig.canvas.mpl_connect('motion_notify_event', self.OnMouseMotion)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #界面控件设置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "态势数据生成"))
        MainWindow.setWindowIcon(QIcon(".\planeicon.ico"))
        self.label_4.setText(_translate("MainWindow", "飞机种类："))
        self.planetype.setItemText(0, _translate("MainWindow", "侦察机"))
        self.planetype.setItemText(1, _translate("MainWindow", "预警机"))
        self.planetype.setItemText(2, _translate("MainWindow", "歼击机"))
        self.label_5.setText(_translate("MainWindow", "编队队形："))
        self.formation.setItemText(0, _translate("MainWindow", "菱形编队"))
        self.formation.setItemText(1, _translate("MainWindow", "跟随编队"))
        self.label_9.setText(_translate("MainWindow", "初始位置："))
        self.checkBox.setText(_translate("MainWindow", "AUTO"))
        self.label_12.setText(_translate("MainWindow", "X："))
        self.label_10.setText(_translate("MainWindow", "Y："))
        self.label_11.setText(_translate("MainWindow", "Z："))
        self.label.setText(_translate("MainWindow", "飞机动作："))
        self.turn.setText(_translate("MainWindow", "转弯"))
        self.falldown.setText(_translate("MainWindow", "俯冲"))
        self.flying.setText(_translate("MainWindow", "平飞"))
        self.climb.setText(_translate("MainWindow", "爬升"))
        self.delete1.setText(_translate("MainWindow", "清除"))
        self.label_3.setText(_translate("MainWindow", "飞机数量："))
        self.numchecked.setText(_translate("MainWindow", "√"))
        self.scheck1.setText(_translate("MainWindow", "√"))
        self.label_8.setText(_translate("MainWindow", "舰艇数量（主舰默认为1艘）"))
        self.label_7.setText(_translate("MainWindow", "驱逐舰："))
        self.scheck2.setText(_translate("MainWindow", "√"))
        self.label_6.setText(_translate("MainWindow", "护卫舰："))
        self.label_16.setText(_translate("MainWindow", "初始位置："))
        self.checkBox_2.setText(_translate("MainWindow", "AUTO"))
        self.label_14.setText(_translate("MainWindow", "Y："))
        self.label_15.setText(_translate("MainWindow", "Z："))
        self.label_13.setText(_translate("MainWindow", "X："))
        self.pushButton_5.setText(_translate("MainWindow", "直行"))
        self.pushButton_7.setText(_translate("MainWindow", "右转"))
        self.label_2.setText(_translate("MainWindow", "航母动作："))
        self.pushButton_8.setText(_translate("MainWindow", "左转"))
        self.delete2.setText(_translate("MainWindow", "清除"))
        self.start.setText(_translate("MainWindow", "生成数据"))
        self.delete3.setText(_translate("MainWindow", "撤销"))
        self.exitbutton.setText(_translate("MainWindow", "关闭"))
        self.savebutton.setText(_translate("MainWindow", "保存数据"))
        self.display.setText(_translate("MainWindow", "数据展示"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.lineEdit_6.setEnabled(0)
    #检测飞机初始位置是否为自动生成，若为自动则输入框锁定，标志位为1，否则输入框可输入，标志位为0
    def changec1(self):
        if self.checkBox.isChecked():
            self.lineEdit.setEnabled(0)
            self.lineEdit_2.setEnabled(0)
            self.lineEdit_3.setEnabled(0)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.sig1=1
        else:
            self.lineEdit.setEnabled(1)
            self.lineEdit_2.setEnabled(1)
            self.lineEdit_3.setEnabled(1)
            self.sig1=0
    #检测航母初始位置是否为自动生成，若为自动则输入框锁定，标志位为1，否则输入框可输入，标志位为0
    def changec2(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_5.setEnabled(0)
            self.lineEdit_4.setEnabled(0)
            self.lineEdit_6.setEnabled(0)
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.sig2=1

        else:
            self.lineEdit_4.setEnabled(1)
            self.lineEdit_5.setEnabled(1)
            #self.lineEdit_6.setEnabled(1)
            self.sig2=0
    #保存函数，
    def save(self):
        if self.num>1:
            #飞机数据保存
            for i in range (len(self.planedata)):
                self.dsaveplane(self.planedata[i],self.raddata[i],i+1)
            #航母数据保存
            for i in range(len(self.shipdata)):
                self.dsaveship(self.shipdata[i],i+1)
            self.savenum= self.savenum + 1 #每次保存后计数加一
    #飞机数据保存函数
    def dsaveplane(self,Q,p,k):#输入为：当前一组飞机轨迹数据，雷达数据，第K组飞机数据
        for i in range(len(Q)):#第i个飞机
            filename = "第"+str(self.savenum)+"次保存"+str(k) + "plane" + str(i+1) + '.csv' #文件名
            out = open(filename, 'a', newline='')
            csv_write = csv.writer(out, dialect='excel')
            C = ['X坐标', 'Y坐标', 'Z坐标', '距离', '角度', '仰角','航向角','速度','信号中心频率GHZ','功率密度mW每平方米','信号重复频率KHZ','占空比%','带宽MHZ','雷达模式']
            csv_write.writerow(C) #表头
            for j in range(len(Q[i])):#遍历当前飞机所有数据点
                csv_write.writerow(numpy.hstack((Q[i][j],p[i][j]))) #以一行为单位保存到CSV中
            QtWidgets.qApp.processEvents()
            out.close()
    #航母数据保存
    def dsaveship(self,Q,k):#输入为：当前一组航母数据，第K组航母数据
        for i in range(len(Q)): #第i个航母
            filename = "第"+str(self.savenum)+"次保存"+str(k) + "warship" + str(i+1) + '.csv'
            out = open(filename, 'a', newline='')
            csv_write = csv.writer(out, dialect='excel')
            C = ['X坐标', 'Y坐标','Z坐标','航向角', '速度', '切向加速度','法向加速度','距离','雷达1中心频率GHZ','功率密度mW每平方米','信号重复频率KHZ','占空比%','带宽MHZ','雷达模式','雷达2中心频率GHZ','功率密度mW每平方米','信号重复频率KHZ','占空比%','带宽MHZ','雷达模式','雷达3中心频率GHZ','功率密度mW每平方米','信号重复频率KHZ','占空比%','带宽MHZ','雷达模式']
            csv_write.writerow(C) #表头
            for j in range(len(Q[i])):
                csv_write.writerow(Q[i][j])
            QtWidgets.qApp.processEvents()
            out.close()
    #删除飞机动作
    def deleteItem1(self):

        self.actionArray = []

        self.textEdit.clear()
    #删除航母动作
    def deleteItem2(self):
        # content = self.textEdit.toRaisedText().replace(
        # content
        self.shipActionArray = []
        self.textEdit_2.clear()
    #获取飞机动作，添加到数组中
    def changeText(self):
        _translate = QtCore.QCoreApplication.translate
        sender=self.sender()
        # print(sender.text())
        if sender.text() == "平飞":
            self.textEdit.append("平飞")
            self.actionArray.append("直线")
        elif sender.text() == "爬升":
            self.textEdit.append("爬升")
            self.actionArray.append("爬升")
        elif sender.text() == "转弯":
            self.textEdit.append("转弯")
            self.actionArray.append("转弯")
        elif sender.text() == "俯冲":
            self.textEdit.append("俯冲")
            self.actionArray.append("俯冲")

    # 获取航母动作，添加到数组中
    def changeText1(self):
        _translate = QtCore.QCoreApplication.translate
        sender = self.sender()
        # print(sender.text())
        if sender.text() == "直行":
            self.textEdit_2.append("直行")
            self.shipActionArray.append("直行")
        elif sender.text() == "左转":
            self.textEdit_2.append("左转")
            self.shipActionArray.append("左转弯")
        elif sender.text() == "右转":
            self.textEdit_2.append("右转")
            self.shipActionArray.append("右转弯")


    def submitNum1(self):
        # 飞机数量
        self.checkedNum = self.spinBox.value()
        if self.spinBox.isEnabled():
            self.spinBox.setEnabled(0)
        else:
            self.spinBox.setEnabled(1)
    def submitNum2(self):
        # 驱逐舰数量
        self.destroyer = self.spinBox_2.value()
        if self.spinBox_2.isEnabled():
            self.spinBox_2.setEnabled(0)
        else:
            self.spinBox_2.setEnabled(1)
    def submitNum3(self):
        # 护卫舰数量
        self.frigate = self.spinBox_4.value()
        if self.spinBox_4.isEnabled():
            self.spinBox_4.setEnabled(0)
        else:
            self.spinBox_4.setEnabled(1)
    # 撤销函数，删除上一次生成的数据
    def delt(self):
        if self.num > 1:
            self.num = self.num - 1
            if len(self.planedata) > 0:
                del self.planedata[len(self.planedata) - 1]
            if len(self.shipdata) > 0:
                del self.shipdata[len(self.shipdata) - 1]
            if len(self.raddata) > 0:
                del self.raddata[len(self.raddata) - 1]
            #更新图像
            self.gridlayout2.removeWidget(self.F)
            sip.delete(self.F)
            self.F = matplot.MyFigure(0, 0)
            self.F.plot(self.planedata, self.shipdata)
            self.gridlayout2.addWidget(self.F, 0, 1)
    #生成数据及画图展示
    def startPlot(self):
        self.c = pyqtSignal()
        planeNum = self.checkedNum #飞机数量
        # 随机产生飞机初始坐标
        x=Plane.random.uniform(1000*self.num, 5000*self.num)
        y=Plane.random.uniform(1000*self.num, 5000*self.num)
        z= Plane.random.uniform(5000, 15000)
        if self.sig1 == 0:#输入自定义坐标，则使用输入的坐标
            if self.lineEdit.text()!='':
                x = int(self.lineEdit.text())
            if self.lineEdit_2.text() != '':
                y = int(self.lineEdit_2.text())
            if self.lineEdit_3.text() != '':
                z = int(self.lineEdit_3.text())
        #飞机初始位置数据
        p0=[x,y,z,Plane.random.uniform(0, math.pi), 0, Plane.random.uniform(150, 200), 0, 0]

        x2 = Plane.random.uniform(1000 * self.num, 5000 * self.num)
        y2 = Plane.random.uniform(1000 * self.num, 5000 * self.num)
        if self.sig2 == 0:#航母初始位置自定义
            if self.lineEdit_4.text() != '':
                x2 = int(self.lineEdit_4.text())
            if self.lineEdit_5.text() != '':
                y2 = int(self.lineEdit_5.text())
        #航母初始位置数据
        p1 = [x2,y2, 0,Plane.random.uniform(0, math.pi), 10, 0, 0, 0]
        planedata = []
        shipdata = []
        transdata=[]
        #航母数据生成
        if len(self.shipActionArray)>0:
            ship = Ship(self.shipActionArray, self.destroyer, self.frigate, p1)
            ship.creatrad()
            shipdata = copy.deepcopy(ship.Q_all)
        #飞机数据生成
        if len(self.actionArray) > 0 and planeNum>0:
            data = Plane.datac(self.actionArray, self.planetype.currentText(), p0, self.num)
            data.trackall()
            form = Formation()
            gap = self.planeGap #飞机间间隔
            #判断编队方式
            if self.formation.currentText()=="跟随编队":
                planedata = form.linearFormation(data.Q,planeNum,gap)
            if self.formation.currentText()=="菱形编队":
                planedata = form.diamondFormation(data.Q,planeNum,gap)
        if len(planedata)!=0:
            transdata =  copy.deepcopy(self.F.dtransf(planedata)) #飞机数据转换
            self.planedata.append(transdata) #把当前生成的数据加入到数组中，保存
        self.shipdata.append(shipdata)
        #更新图像
        self.gridlayout2.removeWidget(self.F)
        sip.delete(self.F)
        self.F = matplot.MyFigure([], [])
        self.F.plot(self.planedata,self.shipdata)
        self.gridlayout2.addWidget(self.F, 0, 1)
        #飞机的雷达数据
        if len(transdata) != 0:
            radatai=[]
            for kk in range(len(transdata)):#遍历每一架飞机
                distance = [x[3] for x in transdata[kk]]##当前飞机对我方的距离
                rad = Radar.datac(self.planetype.currentText(), len(transdata[kk]))
                rad.eledata(distance)
                radatai.append(rad.Q)
            self.raddata.append(radatai) #将雷达数据加入到数组保存
        self.num = self.num + 1  #计数加一

    # 鼠标事件
    # def OnClick(event):
    #     print(1)
    #     global Coords1x, Coords1y
    #     global Coords3x, Coords3y
    #     # ax = plt.gca()
    #     if event.button == 1:
    #         Coords1x = event.xdata
    #         Coords1y = event.ydata
    #     if event.button == 3:
    #         Coords3x = event.xdata
    #         Coords3y = event.ydata
    #
    # def OnMouseMotion(event):
    #     print(2)
    #     global Coords2x, Coords2y, x1, y1
    #     if event.button == 1:
    #         Coords2x = event.xdata
    #         Coords2y = event.ydata
    #         x1 = [Coords1x, Coords2x]
    #         y1 = [Coords1y, Coords2y]
    #         ax = matplot.plt.gca()
    #         lines = ax.plot(x1, y1, picker=20)
    #         ax.figure.canvas.draw()
    #         # 删除之前的线条，进行更新
    #         l = lines.pop(0)
    #         l.remove()
    #         del l
    #     elif event.button == 3:
    #         Coords4x = event.xdata
    #         Coords4y = event.ydata
    #         x2 = [Coords3x, Coords4x]
    #         y2 = [Coords3y, Coords4y]
    #         ax1 = matplot.plt.gca()
    #         # lines = ax1.plot(x1,y1,picker = 5)
    #         lines1 = ax1.plot(x2, y2, picker=20)
    #         ax1.figure.canvas.draw()
    #         # 删除之前的线条，进行更新
    #         l = lines1.pop(0)
    #         l.remove()
    #         del l