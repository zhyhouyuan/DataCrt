# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#子窗口文件
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(671, 534)
        #T=len(self.planedata[0])

        self.label = QtWidgets.QLabel('', self)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")



        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据显示"))
        #self.label.setText(_translate("Dialog", "数据加载中......."))
        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Form", "行"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("Form", "列"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))

        self.pushButton.setText(_translate("Form", "退出"))
    #表格展示飞机数据
    def changedata(self,data,radata):
        _translate = QtCore.QCoreApplication.translate
        C = ['X坐标', 'Y坐标', 'Z坐标', '距离', '角度', '仰角', '航向角', '速度', '信号中心频率GHZ', '功率密度mW每平方米', '信号重复频率KHZ', '占空比%',
             '带宽MHZ', '雷达模式'] #表头
        num = len(data)
        H = len(C)
        for t in range(num):#遍历每一组飞机组
            for k in range (len(data[t])):#遍历当前组每一架飞机
                #添加一页
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.gridLayout = QtWidgets.QGridLayout(self.tab)
                self.gridLayout.setObjectName("gridLayout")
                self.tableWidget = QtWidgets.QTableWidget(self.tab)
                self.tableWidget.setObjectName("tableWidget")
                T=len(data[t][k])
                #设置表格的行数和列数
                self.tableWidget.setColumnCount(H)
                self.tableWidget.setRowCount(T)
                self.tableWidget.setHorizontalHeaderLabels(C)#设置表头
                # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)#设置不可写
                for i in range (T):#遍历每一行
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(i, item)
                    self.tableWidget.verticalHeaderItem(i).setText(_translate("Form", str(i)))#标上行数
                    self.tableWidget.setRowHeight(i, 30)#设置行高
                    for j in range (H):#遍历所有数据维度
                        if j<len(data[t][k][i]):#写入飞机轨迹数据
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str( data[t][k][i][j])))
                        else:#写入飞机雷达数据
                            jj=j-len(data[t][k][i])
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str( radata[t][k][i][jj])))
                    QtWidgets.qApp.processEvents()#多线程
                    self.label.setGeometry((self.width() - 300) / 2, (self.height() - 300) / 2, 300, 300)#设置loading图标位置

                self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab, "")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form",  str(t+1)+"-plane" + str(k+1)))#设置当前页名
    #展示航母数据，写入方式与飞机数据相似
    def changedata2(self,data):
        _translate = QtCore.QCoreApplication.translate
        #表头
        C = ['X坐标', 'Y坐标', 'Z坐标', '航向角', '速度', '切向加速度', '法向加速度', '距离', '雷达1中心频率GHZ', '功率密度mW每平方米', '信号重复频率KHZ', '占空比%',
             '带宽MHZ', '雷达模式', '雷达2中心频率GHZ', '功率密度mW每平方米', '信号重复频率KHZ', '占空比%', '带宽MHZ', '雷达模式', '雷达3中心频率GHZ',
             '功率密度mW每平方米', '信号重复频率KHZ', '占空比%', '带宽MHZ', '雷达模式']
        num = len(data)
        H = len(C)
        for t in range(num):
            for k in range (len(data[t])):
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.gridLayout = QtWidgets.QGridLayout(self.tab)
                self.gridLayout.setObjectName("gridLayout")
                self.tableWidget = QtWidgets.QTableWidget(self.tab)
                self.tableWidget.setObjectName("tableWidget")
                T=len(data[t][k])
                self.tableWidget.setColumnCount(H)
                self.tableWidget.setRowCount(T)
                self.tableWidget.setHorizontalHeaderLabels(C)
                # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                for i in range (T):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setVerticalHeaderItem(i, item)
                    self.tableWidget.verticalHeaderItem(i).setText(_translate("Form", str(i)))
                    self.tableWidget.setRowHeight(i, 30)
                    for j in range (H):
                        self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[t][k][i][j])))
                    QtWidgets.qApp.processEvents()
                    self.label.setGeometry((self.width() - 300) / 2, (self.height() - 300) / 2, 300, 300)

                self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
                self.tabWidget.addTab(self.tab, "")
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form",  str(t+1)+"-warship" + str(k+1)))