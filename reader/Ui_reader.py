# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\jgggithubpythonfiles\jggpython\reader\reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from bs4 import BeautifulSoup
import requests,urllib.request

import sys,time,os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 721, 221))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(90, 65, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(490, 60, 151, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(220, 120, 261, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 60, 261, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(480, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.msg)   #为选择按钮绑定msg函数的按键
        self.pushButton.clicked.connect(self.getDatas)#为确定按钮绑定getdatas的按键
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 270, 721, 271))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 681, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0,item)
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1,item)
        self.tableWidget.setColumnWidth(0,130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 171, 21))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(100, 50, 591, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.itemClicked.connect(self.itemClick)#绑定列表单击方法
        self.tableWidget.itemClicked.connect(self.tableClick)#绑定表格单击方法
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        root=QFileInfo(__file__).absolutePath()
        
        MainWindow.setWindowIcon(QtGui.QIcon(root+'/note.ico'))   #设置当前路径的窗体图标
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label.setText(_translate("MainWindow", "请选择抓取期数："))
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        self.label_3.setText(_translate("MainWindow", "(期数范围为01----24)"))
        self.lineEdit.setText(_translate("MainWindow", "D:\\jgggithubpythonfiles\\jggpython\\reader"))
        self.lineEdit_2.setText(_translate("MainWindow", "2019-11"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "选择"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按日期显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "按名称显示"))

    def msg(self):
        try:
            self.dir_path=QFileDialog.getExistingDirectory(None,"选择路径",os.getcwd())
            self.lineEdit.setText(self.dir_path)
            
        except Exception as e:
            print(e)    
    def GetData(self,url,path):#通过beautifulsoup解析html数据
        soup=self.urlTosoup(url)
        link=soup.select('.booklist a')
        path=path+"\\"+self.date+"\\"
        if not os.path.isdir(path):
            os.mkdir(path)
        for item in link:
            articleUrl=self.baseurl+item['href']
            articleSoup=self.urlTosoup(articleUrl)
            title=str(articleSoup.find("h1")),lstrip("<h1>",rstrip("</h1>"))
            author=str(articleSoup.find(id="pub_date")).strip()     #strip 表示去除首位空白
            fileName=path+title+'.txt'
            newFile=open(fileName,"w")
            newFile.write("<<"+title+">>\n\n") #加标题再换行
            newFile.write(author+"\n\n")
            content=articleSoup.select(".blkContainerSblkCon p") #获取所有文章内容
            for c in content:#遍历所有文章写入内容
                text=c.text
                newFile.write(text)
            newFile.close()
        QMessageBox.information(None,"提示",self.date+"的读者文章保存完成",QMessageBox.Ok)    

    def urlTosoup(self,url):    #爬取数据
        reshtml=requests.get(url)
        soup=BeautifulSoup(reshtml,"html.parser")
        return soup
    def getFiles(self):#获取指定路径下所有文件
        self.list=os.listdir(self.lineEdit.text()+'\\'+self.lineEdit_2.text())

    def bindTable(self):#将文件显示再Table中
        for i in range(0,len(self.list)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(self.lineEdit_2.text()))  #设置第一列为期数
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(self.list[i]))  
    def bindList(self):#将文件显示在list列表中
        for i in range(0,len(self.list)):
            self.item=QtWidgets.QListWidgetItem(self.listWidget)#创建列表项
            self.item.setIcon(QtGui.QIcon('note.ico'))
            self.item.setText(str(self.list[i])[0:5]+'...')
            self.item.setToolTip(self.list[i])#设置提示文字
            self.item.setFlags(Qtcore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    def getDatas(self):
        try:
            while True:
                self.date=self.lineEdit_2.text()#记录用户选择的期数
                self.baseurl='http://www.52duzhe.com'+self.date.replace('-','-')+'/'
                urlList=self.baseurl+'index.html'
                self.GetData(urlList,self.lineEdit.text()) 
        except Exception as e:
            print(e)

                    
        self.getFiles()
        self.bindList()
        self.bindTable()
    def itemClick(self,item):
        os.startfile(self.lineEdit.text()+'\\'+self.lineEdit_2.text()+'\\'+item.toolTip())#打开

    def tableClick(self,item):
        os.startfile(self.lineEdit.text()+'\\'+self.lineEdit_2.text()+'\\'+item.text())    




if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()   
    sys.exit(app.exec_())
