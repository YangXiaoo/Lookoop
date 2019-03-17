# coding:utf-8
# 1. 读取原训练数据转换为pd格式
# 2. 对数据进行处理
# 3. 可视化一波，清洗数据
# 4. 使用不同分类方法，选择最佳参数
# 5. 使用stacking训练模型
# 6. 读取待分割图像，预测，分割

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 






def seg(train_data_path):
    """分割主程序
    1. 训练模型
    2. 获取图片
    3. 多线程分割
    """
    _train_raw, _labels = get_train_data(train_data_path, 2)
    stack_model = train_model(_train_raw, _labels)