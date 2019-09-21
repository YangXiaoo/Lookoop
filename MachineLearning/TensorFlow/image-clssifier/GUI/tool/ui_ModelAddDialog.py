# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModelListView(object):
    def setupUi(self, ModelListView):
        ModelListView.setObjectName("ModelListView")
        ModelListView.resize(433, 302)
        self.modelAddButton = QtWidgets.QPushButton(ModelListView)
        self.modelAddButton.setGeometry(QtCore.QRect(70, 250, 93, 28))
        self.modelAddButton.setObjectName("modelAddButton")
        self.modelDeleteButton = QtWidgets.QPushButton(ModelListView)
        self.modelDeleteButton.setGeometry(QtCore.QRect(260, 250, 93, 28))
        self.modelDeleteButton.setObjectName("modelDeleteButton")
        self.modelListView = QtWidgets.QListWidget(ModelListView)
        self.modelListView.setEnabled(True)
        self.modelListView.setGeometry(QtCore.QRect(40, 20, 361, 201))
        self.modelListView.setObjectName("modelListView")

        self.retranslateUi(ModelListView)
        QtCore.QMetaObject.connectSlotsByName(ModelListView)

    def retranslateUi(self, ModelListView):
        _translate = QtCore.QCoreApplication.translate
        ModelListView.setWindowTitle(_translate("ModelListView", "模型列表"))
        self.modelAddButton.setText(_translate("ModelListView", "添加"))
        self.modelDeleteButton.setText(_translate("ModelListView", "删除"))
