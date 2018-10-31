# coding:UTF-8
# 2018-10-30
# 分割模型
# https://blog.csdn.net/rainustop/article/details/80398134
import cv2
import numpy as np 
import os

__suffix = ["png", "jpg"]

def getFiles(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def getArea(pic_file):
    """
    a. 读取图片
    b. 计算分割后手掌像素点个数
    return: 总的面积，分割出来的图像像素点索引
    """
    # print("reading imgage...")
    img = cv2.imread(pic_file, 0)
    m, n = np.shape(img)
    area = 0
    index = np.mat(np.zeros((m, n)))
    for i in range(m):
        for j in range(m):
            if img[i][j] != 0:
                area += 1
                index[i, j] = 1

    return area, index


def getAccuracyRate(Rs, Ts):
    """
    分割精度
    Rs:手工勾画的分割图像的参考面积
    Ts:算法分割得到的图像的真实面积
    """
    SA = (1- abs(Rs - Ts) / Rs)
    return SA


def getErrorRate(Os, Rs):
    """
    过分割率
    Os:本不应该包含在分割结果中的像素点个数，实际却在分割结果中的像素点个数
    Rs:手工勾画的分割图像的参考面积
    """
    OR = (Os / (Rs + Os))
    return OR


def getLossRate(Us, Rs, Os):
    """
    欠分割率：在GT图像参考面积之中欠缺的像素点的比率
    Us: 本应该在分割结果中的像素点的个数，实际却不在分割结果中的像素点的个数
    """
    UR = (Us / (Rs + Os))
    return UR


def getErrorPoints(standard, actual):
    """
    计算本不应该包含在分割结果中的像素点个数，实际上却在分割结果中的像素点个数
    standard:标准分割像素点索引，矩阵
    actual: 实际分割像素点索引，矩阵
    """
    error_count = 0
    m, n = np.shape(standard)
    for i in range(m):
        for j in range(n):
            if standard[i, j] == 0 and actual[i, j] == 1:
                error_count += 1
    return error_count


def getLossPoints(standard, actual):
    """
    计算本应该在分割结果中的像素点的个数，实际却不在分割结果中的像素点的个数
    standard:标准分割像素点索引，矩阵
    actual: 实际分割像素点索引，矩
    """
    loss_count = 0
    m, n = np.shape(standard)
    for i in range(m):
        for j in range(n):
            if standard[i, j] == 1 and actual[i, j] == 0:
                loss_count += 1
    return loss_count

def getAccuracy(standard_file, file_path):
    """
    standard_file:标准分割图像的路径
    file_path:使用不同方法得到的图片路径
    return: 分割精度，过分割率，欠分割率
    """
    # print("get accuracy...")
    area, index = getArea(standard_file)
    area_new, index_new = getArea(file_path)
    error_count = getErrorPoints(index, index_new)
    loss_count = getLossPoints(index, index_new)
    # 计算该方法下的分割精度，过分割率，欠分割率
    accuracy_rate = getAccuracyRate(area, area_new)
    error_rate = getErrorRate(error_count, area)
    loss_rate = getLossRate(loss_count, area, error_count)
    return accuracy_rate, error_rate, loss_rate


def batchProcess(file_path_1, file_path_2):
    """
    file_path_1:标准分割图像路径
    file_path_2：使用不同方法分割后的图像路径
    要求： 两个目录下面的图像个数、名称要一一对应
    return : {"pic_1":[accuracy_rate, error_rate, loss_rate]}
    """
    files_1 = sorted(getFiles(file_path_1))
    files_2 = sorted(getFiles(file_path_2))
    len_files = len(files_1)
    res = {}
    # 逐一处理
    for i in range(len_files):
        accuracy_rate, error_rate, loss_rate = getAccuracy(files_1[i], files_2[i])
        # print(files_2[i])
        basename = os.path.basename(files_1[i])
        pic_name = os.path.splitext(basename)[0]
        res[pic_name] = [accuracy_rate, error_rate, loss_rate]

    return res


if __name__ == '__main__':
    file_path = "C:\\Study\\test\\stand" # 标准分割图像目录路径
    file_path_1 = "C:\\Study\\test\\way_1" # 方法一得到分割图像路径

    # 方法一比较
    res = batchProcess(file_path, file_path_1)
    for k, v in res.items():
        print("picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f" % (k, v[0], v[1], v[2]))

    # 方法二比较
    # ...


