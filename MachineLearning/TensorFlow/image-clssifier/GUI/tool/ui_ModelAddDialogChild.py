# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialogChild.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modelChildDIalog(object):
    def setupUi(self, modelChildDIalog):
        modelChildDIalog.setObjectName("modelChildDIalog")
        modelChildDIalog.resize(400, 236)
        self.modelAddOk = QtWidgets.QPushButton(modelChildDIalog)
        self.modelAddOk.setGeometry(QtCore.QRect(70, 180, 93, 28))
        self.modelAddOk.setObjectName("modelAddOk")
        self.label_2 = QtWidgets.QLabel(modelChildDIalog)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 72, 21))
        self.label_2.setObjectName("label_2")
        self.filePathButton = QtWidgets.QPushButton(modelChildDIalog)
        self.filePathButton.setGeometry(QtCore.QRect(170, 90, 111, 41))
        self.filePathButton.setObjectName("filePathButton")
        self.modelAddCancle = QtWidgets.QPushButton(modelChildDIalog)
        self.modelAddCancle.setGeometry(QtCore.QRect(230, 180, 93, 28))
        self.modelAddCancle.setObjectName("modelAddCancle")
        self.modelNameInput = QtWidgets.QLineEdit(modelChildDIalog)
        self.modelNameInput.setGeometry(QtCore.QRect(170, 40, 161, 31))
        self.modelNameInput.setObjectName("modelNameInput")
        self.label = QtWidgets.QLabel(modelChildDIalog)
        self.label.setGeometry(QtCore.QRect(70, 50, 72, 21))
        self.label.setObjectName("label")

        self.retranslateUi(modelChildDIalog)
        QtCore.QMetaObject.connectSlotsByName(modelChildDIalog)

    def retranslateUi(self, modelChildDIalog):
        _translate = QtCore.QCoreApplication.translate
        modelChildDIalog.setWindowTitle(_translate("modelChildDIalog", "添加模型"))
        self.modelAddOk.setText(_translate("modelChildDIalog", "确定"))
        self.label_2.setText(_translate("modelChildDIalog", "模型路径"))
        self.filePathButton.setText(_translate("modelChildDIalog", "点击加载"))
        self.modelAddCancle.setText(_translate("modelChildDIalog", "取消"))
        self.label.setText(_translate("modelChildDIalog", "模型名"))
