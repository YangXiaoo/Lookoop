# coding:UTF-8
# 2018-11-9
# BP

from api import neuralNetwork, loadData, handleHistogram
import numpy
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def test():

    inputNodes = 256
    hiddenNodes = 1000
    outputNodes = 150 # 输出的值个数
    learningRate = 0.1

    net = neuralNetwork(inputNodes, hiddenNodes, outputNodes, learningRate)

    # 读取训练数据集
    data, labels = loadData("new_data.txt")
    data = handleHistogram(data)
    m, n = numpy.shape(data)
    ######## 训练 #########
    iteration = 50 # 迭代次数
    for it in range(iteration):
        for i in range(m):
            inputs = data[i, :] + 0.01
            targets = numpy.zeros(outputNodes) + 0.0001 # 初始化输出节点，避免0
            targets[int(labels[i, 0])] = 0.99 # 将数据的每个标签的值置为0.99(避免1)， 数据标签为0-155
            # 避免0和1是因为激活函数生成0和1是不可能
            
            net.train(inputs, targets)
            # print(targets, int(labels[i, 0]), inputs)
        #     break
        # break
        print("完成第 ", it, "次迭代")


    #############  测试 ##############
    predict_y = []
    result = [] # 存储test结果
    for i in range(m):

        inputs = data[i, :] + 0.01
        
        outputs = net.test(inputs)

        label = numpy.argmax(outputs) # 找出最大索引，若训练正确则索引即为标签值
        predict_y.append(int(label))
        # print(label, labels[i, 0])
        # print(outputs)
        if label == labels[i, 0]:
            print("第 ", i, "成功！")
            result.append(1)
        else:
            print("第 ", i, "失败！")
            result.append(0)
        # break

    # 最终准确率
    result_array = numpy.asarray(result) # asarray不会深度拷贝数组，占用内存少
    print("识别率 = ", result_array.sum() / result_array.size)


    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in labels:
        actual_x.append(int(i[0]))
        predict_x.append(int(i[0]))
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    
    color = numpy.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim([0, 150])
    plt.ylim([0, 150])

    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y)
    plt.savefig("bp")
    plt.show()

if __name__ == '__main__':
    test()