# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadPic = QtWidgets.QPushButton(self.centralwidget)
        self.loadPic.setGeometry(QtCore.QRect(160, 70, 101, 28))
        self.loadPic.setAutoFillBackground(False)
        self.loadPic.setObjectName("loadPic")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 140, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 140, 72, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.showPic = QtWidgets.QLabel(self.centralwidget)
        self.showPic.setGeometry(QtCore.QRect(480, 40, 251, 241))
        self.showPic.setFrameShape(QtWidgets.QFrame.Box)
        self.showPic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.showPic.setAlignment(QtCore.Qt.AlignCenter)
        self.showPic.setObjectName("showPic")
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(110, 220, 93, 28))
        self.predict.setObjectName("predict")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(230, 220, 93, 28))
        self.reset.setObjectName("reset")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(70, 340, 661, 191))
        self.console.setObjectName("console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.modelAdd = QtWidgets.QAction(MainWindow)
        self.modelAdd.setObjectName("modelAdd")
        self.tutorial = QtWidgets.QAction(MainWindow)
        self.tutorial.setObjectName("tutorial")
        self.defaultLoadPath = QtWidgets.QAction(MainWindow)
        self.defaultLoadPath.setObjectName("defaultLoadPath")
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.modelAdd)
        self.menu_2.addAction(self.defaultLoadPath)
        self.menu_3.addAction(self.tutorial)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "骨龄预测"))
        self.loadPic.setText(_translate("MainWindow", "加载图片"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Stacking方法"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VGG"))
        self.label_2.setText(_translate("MainWindow", "选择方法："))
        self.showPic.setText(_translate("MainWindow", "图像显示"))
        self.predict.setText(_translate("MainWindow", "预测"))
        self.reset.setText(_translate("MainWindow", "重置"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输出控制台</p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.modelAdd.setText(_translate("MainWindow", "添加模型"))
        self.tutorial.setText(_translate("MainWindow", "使用方法"))
        self.defaultLoadPath.setText(_translate("MainWindow", "默认加载路径"))
