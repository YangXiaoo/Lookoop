# -*- coding: UTF-8 -*-

# 获取手写数据。
# 28*28的图片对象。每个图片对象根据需求是否转化为长度为784的横向量
# 每个对象的标签为0-9的数字，one-hot编码成10维的向量
import numpy as np

# 数据加载器基类。派生出图片加载器和标签加载器
class Loader(object):
    # 初始化加载器。path: 数据文件路径。count: 文件中的样本个数
    def __init__(self, path, count):
        self.path = path
        self.count = count

    # 读取文件内容
    def get_file_content(self):
        print(self.path)
        f = open(self.path, 'rb')
        content = f.read()  # 读取字节流
        f.close()
        return content  # 字节数组

    # 将unsigned byte字符转换为整数。python3中bytes的每个分量读取就会变成int
    # def to_int(self, byte):
    #     return struct.unpack('B', byte)[0]

# 图像数据加载器
class ImageLoader(Loader):
    # 内部函数，从文件字节数组中获取第index个图像数据。文件中包含所有样本图片的数据。
    def get_picture(self, content, index):
        start = index * 28 * 28 + 16  # 文件头16字节，后面每28*28个字节为一个图片数据
        picture = []
        for i in range(28):
            picture.append([])  # 图片添加一行像素
            for j in range(28):
                byte1 = content[start + i * 28 + j]
                picture[i].append(byte1)  # python3中本来就是int
                # picture[i].append(self.to_int(byte1))  # 添加一行的每一个像素
        return picture   # 图片为[[x,x,x..][x,x,x...][x,x,x...][x,x,x...]]的列表

    # 将图像数据转化为784的行向量形式
    def get_one_sample(self, picture):
        sample = []
        for i in range(28):
            for j in range(28):
                sample.append(picture[i][j])
        return sample

    # 加载数据文件，获得全部样本的输入向量。onerow表示是否将每张图片转化为行向量，to2表示是否转化为0,1矩阵
    def load(self,onerow=False):
        content = self.get_file_content()  # 获取文件字节数组
        data_set = []
        for index in range(self.count):  #遍历每一个样本
            onepic =self.get_picture(content, index)  # 从样本数据集中获取第index个样本的图片数据，返回的是二维数组
            if onerow: onepic = self.get_one_sample(onepic)  # 将图像转化为一维向量形式
            data_set.append(onepic)
        return data_set

# 标签数据加载器
class LabelLoader(Loader):
    # 加载数据文件，获得全部样本的标签向量
    def load(self):
        content = self.get_file_content()   # 获取文件字节数组
        labels = []
        for index in range(self.count):  #遍历每一个样本
            onelabel = content[index + 8]   # 文件头有8个字节
            onelabelvec = self.norm(onelabel) #one-hot编码
            labels.append(onelabelvec)
        return labels

    # 内部函数，one-hot编码。将一个值转换为10维标签向量
    def norm(self, label):
        label_vec = []
        # label_value = self.to_int(label)
        label_value = label  # python3中直接就是int
        for i in range(10):
            if i == label_value:
                label_vec.append(1)
            else:
                label_vec.append(0)
        return label_vec

# 获得训练数据集。onerow表示是否将每张图片转化为行向量
def get_training_data_set(num,onerow=False):
    image_loader = ImageLoader('train-images.idx3-ubyte', num)  # 参数为文件路径和加载的样本数量
    label_loader = LabelLoader('train-labels.idx1-ubyte', num)  # 参数为文件路径和加载的样本数量
    return image_loader.load(onerow), label_loader.load()

# 获得测试数据集。onerow表示是否将每张图片转化为行向量
def get_test_data_set(num,onerow=False):
    image_loader = ImageLoader('t10k-images.idx3-ubyte', num)  # 参数为文件路径和加载的样本数量
    label_loader = LabelLoader('t10k-labels.idx1-ubyte', num)  # 参数为文件路径和加载的样本数量
    return image_loader.load(onerow), label_loader.load()


# 将一行784的行向量，打印成图形的样式
def printimg(onepic):
    onepic=onepic.reshape(28,28)
    for i in range(28):
        for j in range(28):
            if onepic[i,j]==0: print('  ',end='')
            else: print('* ',end='')
        print('')


if __name__=="__main__":
    train_data_set, train_labels = get_training_data_set(100)  # 加载训练样本数据集，和one-hot编码后的样本标签数据集
    train_data_set = np.array(train_data_set)       #.astype(bool).astype(int)    #可以将图片简化为黑白图片
    train_labels = np.array(train_labels)
    onepic = train_data_set[12]  # 取一个样本
    printimg(onepic)  # 打印出来这一行所显示的图片
    print(train_labels[12].argmax())  # 打印样本标签
