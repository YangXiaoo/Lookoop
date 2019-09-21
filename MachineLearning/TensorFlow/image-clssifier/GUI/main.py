# coding:utf-8
import sys
import logging

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from tool import util, ui_MainWindow, ui_ModelAddDialog, ui_ModelAddDialogChild
r"""ui标签转换
pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_MainWindow.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_MainWindow.ui

pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialog.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialog.ui

pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialogChild.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialogChild.ui
"""

# 日志设置
LOGGER_PATH = r"C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\log"
CONFIG_PATH = r"C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\data\conf.txt"
logger = util.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)   # 设置日志级别，设置INFO时时DEBUG不可见

# class Main(QMainWindow):
#   def __init__(self):
#       super().__init__()
#       self.setWindowTitle("骨龄预测")
#       self.resize(700, 500)
#       bar = self.menuBar()
#       file = bar.addMenu("File")
#       file.addAction("New")
#       save = QAction("Save",self)
#       save.setShortcut("Ctrl+S")
#       file.addAction(save)
#       edit = file.addMenu("Edit")
#       edit.addAction("copy")
#       edit.addAction("paste")
#       quit = QAction("Quit",self)
#       file.addAction(quit)
#       file.triggered[QAction].connect(self.processtrigger) 
        
#       self.initMainWindow()

#   def initMainWindow(self):
#       widget = QWidget()

#       hlayout =  QHBoxLayout(self)
#       vlayout =  QVBoxLayout(self)
#       glayout = QGridLayout(self)

#       self.compute = QPushButton("计算")
#       self.reset = QPushButton("重置")
#       hlayout.addWidget(self.compute)
#       hlayout.addWidget(self.reset)

#       self.loadPic = QPushButton("加载图片")
#       self.loadPic.clicked.connect(self.getfile)
#       hlayout.addWidget(self.loadPic)
#       self.showPic = QLabel("")

#       glayout.addWidget(self.loadPic, 0, 0)
#       glayout.addWidget(self.compute, 1, 0)
#       glayout.addWidget(self.reset, 1, 1)

#       glayout.addWidget(self.showPic, 0, 2)

#       widget.setLayout(glayout)
#       self.setCentralWidget(widget)


        
#   def processtrigger(self,q):
#       print( q.text()+" is triggered" )

#   def getfile(self):
#       fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
#       self.showPic.setPixmap(QPixmap(fname))

class MyWindow(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.initMainWindow()
        self.initComboBox()
        self.initDialog()

    def initMainWindow(self):
        """主窗口初始化"""
        self.menubar.triggered[QAction].connect(self.processtrigger)
        self.loadPic.clicked.connect(self.getFile)  # 图片加载
        self.reset.clicked.connect(self.resetFunc)  # 重置按钮

    def initDialog(self):
        """模态框初始化"""
        self.modelDialog = ModelAddDialog()

    def initComboBox(self):
        """训练模型下拉框初始化, 从设置中读取配置"""
        curDataName = "modelList"
        conf = util.getConfig(CONFIG_PATH)
        modelList = conf.options(curDataName)
        for m in modelList:
            curModelPath = conf.get(curDataName, m)
            self.comboBox.addItem(m)

    def resetFunc(self):
        """重置操作"""
        self.showPic.setPixmap(QPixmap("")) # 图片重置

    def modelAddFunc(self):
        """setting菜单中的添加模型选项，添加模型名称以及模型对应路径"""
        self.modelDialog.open()
        qe = QEventLoop()
        qe.exec_()

    def getFile(self):
        """加载图片"""
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
        util.recordAndPrint(logger, self.console, "[INFO] load picture filename: {}".format(fname))
        self.showPic.setScaledContents (True)
        self.showPic.setPixmap(QPixmap(fname))

    def processtrigger(self, q):
        """信号槽触发"""
        print( q.text()+" is triggered" )
        if q.text() == "添加模型":
            self.modelAddFunc()

class ModelAddDialog(QMainWindow, ui_ModelAddDialog.Ui_ModelListView):
    """模型添加弹框"""
    def __init__(self):
        super(ModelAddDialog, self).__init__()
        self.setupUi(self)
        self.initData()
        self.initOps()
        self.initChild()

    def open(self):
        self.show()

    def initOps(self):
        self.modelAddButton.clicked.connect(self.add)
        self.modelDeleteButton.clicked.connect(self.delete)

    def initChild(self):
        self.child = ModelChildDialog()

    def initData(self):
        """初始化列表中的数据"""
        curDataName = "modelList"
        conf = util.getConfig(CONFIG_PATH)
        modelList = conf.options(curDataName)
        for m in modelList:
            curModelPath = conf.get(curDataName, m)
            self.modelListView.addItem("{}: '{}'".format(m, curModelPath))

    def delete(self):
        for item in self.modelListView.ContentList.selectedItems():
            self.modelListView.ContentList.takeItem(self.modelListView.ContentList.row(item))

    def add(self):
        self.child.open()
        qe = QEventLoop()
        qe.exec_()
        self.initData()


class ModelChildDialog(QMainWindow, ui_ModelAddDialogChild.Ui_modelChildDIalog):
    def __init__(self):
        super(ModelChildDialog, self).__init__()
        self.setupUi(self)
        self.modelPath = None
        self.initOps()

    def initOps(self):
        self.modelAddOk.clicked.connect(self.accept)
        self.modelAddCancle.clicked.connect(self.cancel)
        self.filePathButton.clicked.connect(self.getFile)

    def accept(self):
        """确认"""
        modelName = self.modelNameInput.text()
        curDataName = "modelList"
        conf = util.getConfig(CONFIG_PATH)
        print(modelName, self.modelPath)
        if modelName != None and self.modelPath != None:
            conf.set(curDataName, modelName, self.modelPath)
        with open(CONFIG_PATH, 'w') as f:
            conf.write(f)

    def cancel(self):
        pass

    def getFile(self):
        """加载图片"""
        self.modelPath, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"model file (*.pb)")
        print(self.modelPath)

    def open(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
