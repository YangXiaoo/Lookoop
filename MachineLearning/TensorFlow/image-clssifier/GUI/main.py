# coding:utf-8
# 2019/9/21
import sys
sys.path.append(r"C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier")
import logging
import pickle
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from keras import backend as K
import numpy as np 
import tensorflow as tf 


from tool import util, ui_MainWindow, ui_ModelAddDialog, ui_ModelAddDialogChild, helpDialog

# import classifier_collection as cc
# import test_image_classifier as tic 
from preprocessing import preprocessing_factory

r"""ui标签转换
pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_MainWindow.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_MainWindow.ui

pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialog.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialog.ui

pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialogChild.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\ui_ModelAddDialogChild.ui

pyuic5 -o C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\helpDialog.py C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\tool\helpDialog.ui

my tensorflow install path: C:/Users/Yauno/AppData/Local/conda/conda/envs/tensorflow

qtdesigner install path: C:\Users\Yauno\AppData\Local\conda\conda\envs\tensorflow\Lib\site-packages\pyqt5_tools\Qt\bin
"""

# 日志设置
LOGGER_PATH = r"C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\log"
logger = util.getLogger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)   # 设置日志级别，设置INFO时时DEBUG不可见

# 配置设置
CONFIG_PATH = r"C:\Study\github\Lookoops\MachineLearning\TensorFlow\image-clssifier\GUI\data\conf.txt"
CONF_MODEL_LIST_NAME = "modelList"
DEFAULT_LOAD_DIR = "defaultLoadDir"

PREDICT_MODEL_PATH = "" # 融合模型的路径
# MODEL_LIST = cc.getModelList()  # 模型列表
MODEL_LIST = [['vgg_16', 'vgg_16/fc8/squeezed:0', 224], ['inception_v3', 'InceptionV3/Predictions/Reshape_1:0', 299], ['pnasnet_large', 'final_layer/predictions:0', 331], ['resnet_v2_200', 'resnet_v2_200/predictions/Reshape_1:0', 224], ['inception_resnet_v2', 'InceptionResnetV2/Logits/Predictions:0', 299]]
LABEL_MAPPING_PATH = None   # 标签映射路径
GRAPH_DIR = None            # 图模型路径

class MyWindow(QMainWindow, ui_MainWindow.Ui_MainWindow):
    """主窗口"""
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.predictPic = None
        self.graphDir = GRAPH_DIR
        self.stackingModelPath = PREDICT_MODEL_PATH
        self.gap = 6    # 预测偏差
        self.labelMapPath = LABEL_MAPPING_PATH

        self.picDefaultLoadDir = 'c:\\'
        self.mainWindowIcon = "./data/icon.png"

        self.initMainWindow()

    def initMainWindow(self):
        """主窗口初始化"""
        self.setupUi(self)
        self.topWidget = QWidget()
        self.setWindowIcon(QIcon(self.mainWindowIcon))
        self.initComboBox()
        self.initData()
        self.menubar.triggered[QAction].connect(self.processtrigger)    # 菜单栏触发
        self.loadPic.clicked.connect(self.getFile)  # 图片加载
        self.reset.clicked.connect(self.resetFunc)  # 重置按钮
        self.predict.clicked.connect(self.predictFunc)  # 预测按钮
    
    def initComboBox(self):
        """训练模型下拉框初始化, 从设置中读取配置"""
        conf = util.getConfig(CONFIG_PATH)
        modelList = conf.options(CONF_MODEL_LIST_NAME)
        for m in modelList:
            curModelPath = conf.get(CONF_MODEL_LIST_NAME, m)
            self.comboBox.addItem(m)

    def initData(self):
        """初始化数据"""
        self.conf = util.getConfig(CONFIG_PATH)
        self.picDefaultLoadDir = self.conf.get(DEFAULT_LOAD_DIR, "pic-default-load-dir")

    def resetFunc(self):
        """重置操作"""
        self.printConsel("[INFO] reset inputs")
        self.predictPic = None
        self.showPic.setPixmap(QPixmap("")) # 图片重置

    def modelAddFunc(self):
        """setting菜单中的添加模型选项，添加模型名称以及模型对应路径"""
        self.modelDialog = ModelAddDialog() # 模型添加框
        self.modelDialog.open()
        qe = QEventLoop()
        qe.exec_()

    def printConsel(self, message):
        """打印消息到控制台"""
        util.recordAndPrint(logger, self.console, message)

    def initPdtModel(self):
        """初始化训练模型"""
        self.printConsel("[INFO] initialize prediction model.")
        self.pdtModel = Prediction(self.graphDir, self.stackingModelPath, self.labelMapPath)

    def pdtCheck(self):
        """预测前检查资源加载"""
        self.printConsel("[INFO] check resources load")
        if self.predictPic == None:
            self.printConsel("[ERROR] picture path is not exist, please check the path you input")
            return False

        return True

    def mockPredictFunc(self):
        """测试"""
        import random
        return os.path.basename(self.predictPic), random.randint(0,30)

    def predictFunc(self):
        """预测，使用Stacking继承学习方法直接预测.
        后面考虑通过选择其他方法进行预测"""
        if not self.pdtCheck():
            return 

        self.printConsel("[INFO] loading predict models.")
        # self.initPdtModel()
        # picName, picPdt = self.pdtModel.predictSinglePic(self.predictPic)
        picName, picPdt = self.mockPredictFunc()    # 测试界面 

        self.printConsel("[INFO] picture name: {}, estimate age: {} ± {} month".format(picName, picPdt, self.gap))

    def picDefaultLoadFunc(self):
        """图片默认加载目录"""
        self.printConsel("[INFO] set picture default load directory.")
        self.picDefaultLoadDir = QFileDialog.getExistingDirectory(self, "getExistingDirectory", "./")
        self.printConsel("[INFO] set picture default load directory successful, new directory is : {}".format(self.picDefaultLoadDir))

        # 保存
        self.conf.set(DEFAULT_LOAD_DIR, "pic-default-load-dir", self.picDefaultLoadDir)
        with open(CONFIG_PATH, 'w') as f:
            self.conf.write(f)

    def helpFunc(self):
        """帮助界面"""
        self.printConsel("[INFO] help")
        helpWin = helpWindow()
        helpWin.open()
        qe = QEventLoop()
        qe.exec_()

    def getFile(self):
        """加载图片"""
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', self.picDefaultLoadDir, "Image files (*.jpg *.png)")
        self.printConsel("[INFO] load picture, source : {}".format(fname))
        self.predictPic = fname
        self.showPic.setScaledContents (True)   # 自适应
        self.showPic.setPixmap(QPixmap(fname))

    def processtrigger(self, q):
        """信号槽触发"""
        curName = q.text()
        if curName == "添加模型":
            self.modelAddFunc()
        elif curName == "图片默认加载目录":
            self.picDefaultLoadFunc()
        elif curName == "退出":
            self.close()
        elif curName == "使用方法":
            self.helpFunc()


class ModelAddDialog(QMainWindow, ui_ModelAddDialog.Ui_ModelListView):
    """模型添加弹框"""
    def __init__(self):
        super(ModelAddDialog, self).__init__()
        self.setupUi(self)
        self.initData()
        self.initOps()

    def open(self):
        self.show()

    def initOps(self):
        self.modelAddButton.clicked.connect(self.add)
        self.modelDeleteButton.clicked.connect(self.delete)     

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
        self.child = ModelChildDialog()
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

    def open(self):
        self.show()


class helpWindow(QMainWindow, helpDialog.Ui_Dialog):
    """帮助界面"""
    def __init__(self):
        super(helpWindow, self).__init__()
        self.setupUi(self)
        self.helpButtonOk.clicked.connect(self.acceptFunc)

    def open(self):
        self.show()

    def acceptFunc(self):
        self.close()


class PredictionHandler(object):
    """预测基类"""
    def __init__(self, graphDir=None, stackingModelPath=None):
        self.picList = None # 预测图片列表
        self.frozenGraphName = "frozen_graph.pb"
        self.graphDir = graphDir
        self.stackingModel = None
        self.initData(stackingModelPath)

    def initData(self, stackingModelPath):
        """初始化数据和模型"""
        # self.picList = []   # 初始化图片列表
        self.stackingModel = self.loadModel(stackingModelPath)

    def loadModel(self, stackingModelPath):
        """加载模型"""
        return pickle.load(open(stackingModelPath,'rb'))

    def checkEnv(self):
        """预测前检查资源加载"""
        if self.picList == None:
            assert False, "picture path is empty"

        if self.graphDir == None:
            assert False, "model graph path is not exist"

        if self.stackingModel == None:
            assert False, "train model is not initialize"

    def preProcess(self, data, alpha = 0.99, isTotal = False):
        """数据均一化"""
        m, n = np.shape(data)
        ret = np.zeros((m, n))
        for i in range(m):
            total = np.sum(data[i, :])
            maxValue = np.max(data[i, :])
            for j in range(n):
                if isTotal:
                    ret[i, j] = data[i, j] / tatal * alpha
                else:
                    ret[i, j] = [data[i, j], 1][data[i, j] == 0] / maxValue * alpha
        return ret

    def createGraph(self, sess, modelPath):
        """创建图"""
        K.clear_session()
        tf.reset_default_graph()
        with tf.gfile.FastGFile(modelPath, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

    def pdtBySingleModel(self, modelPath, modelName, tensorName, picList, picSize):
        """单个模型预测"""
        self.createGraph(None, modelPath)
        pFn = preprocessing_factory.get_preprocessing(modelName, is_training=False)
        pdtOutput = {}  # 字典格式保存预测结果，{'2_m-1-1.9.png': prediction}
        with tf.Session() as sess:
            for picPath in picList:
                tensor = sess.graph.get_tensor_by_name(tensorName)
                baseName = os.path.basename(picPath)

                # 获得图像
                imgData = tf.gfile.FastGFile(picPath, 'rb').read()
                imgData = tf.image.decode_jpeg(imgData, channels=3)
                imgData = pFn(imgData, picSize, picSize)
                imgData = tf.expand_dims(imgData, 0)
                imgData = sess.run(imgData)

                try:
                    prediction = sess.run(tensor, {'input:0': imgData})
                    prediction = np.squeeze(prediction)
                    pdtOutput[baseName] = prediction
                except Exception as e:
                    print("[Error] %s" % str(e))

        return pdtOutput

    def getMeanOfModels(self):
        """获得多个模型预测结果，并返回预测均值"""
        pdt = {}
        for modelName, tesnorName, picSize in MODEL_LIST:
            curModelPdt = {}
            modeDir = os.path.join(self.graphDir, modelName) # 获得一个模型名称对应的目录
            classList = os.listdir(modeDir) # 获得当前模型名下面的多个训练模型
            for c in classList:
                modelPath = os.path.join(modeDir, c, self.frozenGraphName)  # 当前训练模型路径
                tmpPdt = self.pdtBySingleModel(modelPath, modelName, tensorName, self.picList, picSize)   # 单个模型预测单张图片
                for k,v in tmpPdt.items():
                    v = v.argmax()  # 获得数组中预测概率最高的索引
                    curModelPdt.get(k, []).append(v)

            # 获得当前模型对图片预测的均值
            count = len(classList)
            for k,v in curModelPdt:
                curModelPdt[k] = mean(v)    # 可能会报错 

            # 添加单个模型预测结果到pdt中
            for k,v in curModelPdt.items():
                if k not in pdt:
                    pdt[k] = [v]
                else:
                    pdt[k].append(v)
        
        picNameList, testFeature = [], []
        for k,v in pdt:
            picNameList.append(k)
            testFeature.append(v)
        testFeature = np.mat(testFeature)

        testFeature = self.preProcess(testFeature)

        return picNameList, testFeature

    def predicts(self, picPathList):
        """预测多张图片
        @param picPathList 路径,列表
        """
        self.picList = picPathList
        self.checkEnv() # 检测
        picNameList, testFeature = self.getMeanOfModels()
        pdtValue = self.stackingModel.predict()

        return picNameList, pdtValue

    def predictSinglePic(self, picPath):
        """预测单张图片
        @param picPath 路径,字符串
        """
        return self.predicts([picPath])
        
class Prediction(PredictionHandler):
    """预测实现类"""
    def __init__(self, graphDir=None, stackingModelPath=None, labelMapPath=None):
        super(Prediction, self).__init__(graphDir, stackingModelPath)
        self.labelMap = None
        self.labelMapPath = labelMapPath
        self.initLableMap()

    def initLableMap(self):
        """初始化标签映射字典"""
        self.labelMap = {}
        with open(self.labelMapPath, "r") as f:
            lines = f.readlines()
            for line in lines:
                k,v = line.split(" ")
                self.labelMap[k] = v

    def predictSinglePic(self, picPath):
        """重写父类预测方法"""
        picNameList, pdtValue = self.predicts([picPath]) 
        try:
            return picNameList[0], self.labelMap[int(pdtValue[0])]   # 若抛出异常
        except:
            assert False, "check label map"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())