
[代码在这里](https://github.com/YangXiaoo/Lookoop/tree/master/MachineLearning/TensorFlow/image-clssifier "代码这里")

## 代码结构
![代码结构图](http://yangxiao.online/static/files/20190109-222738-13b9/TIM截图20190109222659.png "代码结构图")
# 1. 数据处理
数据来源于[kaggle-boneage](https://www.kaggle.com/kmader/rsna-bone-age "kaggle-boneage")
## 1.1 数据抽取
从下载的数据中使用`tool/get_lables.py`将图像分为male与female并将每个性别分为训练集与验证集如下图：

![数据抽取](http://yangxiao.online/static/files/20190109-223816-ed61/TIM截图20190109223809.png "数据抽取")
## 1.2 数据扩充
使用`tool/pic_data_augmentation.py`对图像进行数据扩充。
## 1.3 数据划分
使用`tool/disposal.py`将图像进行k-fold处理，结果如图：

这里将数据分为5分，每份数据有训练集与测试集。

![k-fold](http://yangxiao.online/static/files/20190109-225308-7f4b/TIM截图20190109225216.png "k-fold")

![数据集与测试集](http://yangxiao.online/static/files/20190109-225400-0e43/TIM截图20190109225226.png "数据集与测试集")

![最后结果](http://yangxiao.online/static/files/20190109-225429-6dcb/TIM截图20190109225246.png "最后结果")
## 1.4 数据转换
使用`data_convert.py`将上一步中每一个fold数据转换为TFrecord格式，结果如图，这里需要对5个文件夹下面的数据进行转换，这里只显示一个：

![tf格式数据](http://yangxiao.online/static/files/20190109-225622-8810/TIM截图20190109225615.png "tf格式数据")

# 2. 训练
使用`train_image_classifier.py`进行训练。

关键参数有：
`train_dir`: 存放日志，模型自动保存的路径
`dataset_name`：数据读取模块，其值对应着`datasets\`下面的程序名，可以自己编写
`dataset_split_name` : 读取TF数据集中含该名称的数据
`dataset_dir`:TF数据集目录，1.4步中生成数据目录
`model_name`:使用模型名，对应着`net/`下的模型文件
`max_number_of_steps`:最大迭代数
`checkpoint_path`: ckpt模型路径，`None`表示不使用微调

# 3. 验证
使用`eval_image_classifier.py`验证精确度。
这里可以得到总的精确度，但不能获得单张图片输出

# 4. 导出模型
使用`export_inference_graph.py`之后再使用`freeze_graph.py`

# 5. 测试并获得每个测试集的数据
`test_image_classifier.py`获得每张图片未使用argmax的输出结果并与其标签数据一起保存到指定路径，等待最后模型融合。

# 6. 使用Softmax进行融合获得最终模型
暂无


