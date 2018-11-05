# coding:UTF-8
# 2018-10-30
# 分割模型
# https://blog.csdn.net/rainustop/article/details/80398134

from api import getFiles, batchProcess

if __name__ == '__main__':
    file_path = "C:\\Study\\test\\est_model\\standard" # 标准分割图像目录路径
    
    # 方法一比较
    print("回归法")
    file_path_1 = "C:\\Study\\test\\est_model\\regression" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_1)
    for k, v in res.items():
        print("picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f" % (k, v[0], v[1], v[2]))

    # 方法二比较
    print("直方图均值")
    file_path_2 = "C:\\Study\\test\\est_model\\mean" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_2)
    for k, v in res.items():
        print("picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f" % (k, v[0], v[1], v[2]))

    # 方法3比较
    print("最大熵")
    file_path_2 = "C:\\Study\\test\\est_model\\entropy" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_2)
    for k, v in res.items():
        print("picture: %s , accuracy rate: %5f , error rate:  %5f , loss rate: %5f" % (k, v[0], v[1], v[2]))
