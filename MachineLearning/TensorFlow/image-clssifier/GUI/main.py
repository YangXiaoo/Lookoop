# coding:utf-8
# 2019/9/21
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
CONF_MODEL_LIST_NAME = "modelList"


logger = util.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)   # 设置日志级别，设置INFO时时DEBUG不可见

class MyWindow(QMainWindow, ui_MainWindow.Ui_MainWindow):
    """主窗口"""
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
        self.modelDialog = ModelAddDialog() # 模型添加框

    def initComboBox(self):
        """训练模型下拉框初始化, 从设置中读取配置"""
        conf = util.getConfig(CONFIG_PATH)
        modelList = conf.options(CONF_MODEL_LIST_NAME)
        for m in modelList:
            curModelPath = conf.get(CONF_MODEL_LIST_NAME, m)
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
        util.recordAndPrint(logger, self.console, "[INFO] load picture, source : {}".format(fname))
        self.showPic.setScaledContents (True)   # 自适应
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
        """初始化弹窗"""
        self.child = ModelChildDialog()

    def initData(self):
        """初始化列表中的数据"""
        self.modelListView.clear()
        self.conf = util.getConfig(CONFIG_PATH)
        modelList = self.conf.options(CONF_MODEL_LIST_NAME)
        for m in modelList:
            curModelPath = self.conf.get(CONF_MODEL_LIST_NAME, m)
            self.modelListView.addItem("{}: '{}'".format(m, curModelPath))

    def delete(self):
        """删除列表中的数据"""
        for item in self.modelListView.selectedItems():
            removeItem = self.modelListView.takeItem(self.modelListView.row(item))
            try:
                boolean = self.conf.remove_option(CONF_MODEL_LIST_NAME, removeItem.text().split(":")[0])
                if boolean:
                    logger.info("[INFO] remove item: {} successful".format(removeItem.text().split(":")[0]))
                    self.modelListView.removeItemWidget(removeItem)
                    with open(CONFIG_PATH, 'w') as f:
                        self.conf.write(f)
                else:
                    logger.info("[WARNING] remove item:{} fail".format(removeItem.text().split(":")[0]))
            except Exception as e:
                logger.error("[ERROR] remove item:{} fail, trace: {}".format(removeItem.text().split(":")[0], str(e)))
        self.initData()

    def add(self):
        """添加模型"""
        self.child.open()
        self.initData()
        qe = QEventLoop()
        qe.exec_()


class ModelChildDialog(QMainWindow, ui_ModelAddDialogChild.Ui_modelChildDIalog):
    """模型添加的模态框"""
    def __init__(self):
        super(ModelChildDialog, self).__init__()
        self.setupUi(self)
        self.modelPath = None
        self.initOps()

    def initOps(self):
        """初始化信号槽"""
        self.modelAddOk.clicked.connect(self.accept)
        self.modelAddCancle.clicked.connect(self.cancel)
        self.filePathButton.clicked.connect(self.getFile)

    def accept(self):
        """确认"""
        modelName = self.modelNameInput.text()
        conf = util.getConfig(CONFIG_PATH)
        # print(modelName, self.modelPath)
        if modelName != None and self.modelPath != None:
            conf.set(CONF_MODEL_LIST_NAME, modelName, self.modelPath)
        with open(CONFIG_PATH, 'w') as f:
            conf.write(f)
        self.close()

    def cancel(self):
        """取消"""
        self.close()

    def getFile(self):
        """选择节点路径"""
        self.modelPath, _  = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"model file (*.pb)")
        # print(self.modelPath)

    def open(self):
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
