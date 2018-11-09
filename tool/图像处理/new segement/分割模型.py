# coding:UTF-8
# 2018-10-30
# 分割模型
# https://blog.csdn.net/rainustop/article/details/80398134

from api import getFiles, batchProcess, printEst, saveEst

if __name__ == '__main__':
    file_path = "C:\\Study\\test\\100-gt" # 标准分割图像目录路径
    out_dir = "C:\\Study\\test\\est_results" #结果保存目录
    # 方法一比较
    print("回归法")
    file_path_1 = "C:\\Study\\test\\regression_no_norm" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_1)
    printEst(res, "回归法")
    saveEst(res, "回归法", out_dir)

    # 方法二比较
    print("直方图均值")
    file_path_2 = "C:\\Study\\test\\histogram_no_norm" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_2)
    printEst(res, "直方图均值")
    saveEst(res, "直方图均值", out_dir)
    
    # 方法3比较
    print("最大熵")
    file_path_2 = "C:\\Study\\test\\maxEntrop_without_norm" # 方法一得到分割图像路径
    res = batchProcess(file_path, file_path_2)
    printEst(res, "最大熵")
    saveEst(res, "最大熵", out_dir)
    # file_path = "C:\\Study\\test\\s" # 标准分割图像目录路径
    # out_dir = "C:\\Study\\test\\est_results" #结果保存目录
    # # 方法一比较
    # print("回归法")
    # file_path_1 = "C:\\Study\\test\\r" # 方法一得到分割图像路径
    # res = batchProcess(file_path, file_path_1)
    # printEst(res, "回归法")
    # saveEst(res, "回归法", out_dir)

    # # 方法二比较
    # print("直方图均值")
    # file_path_2 = "C:\\Study\\test\\h" # 方法一得到分割图像路径
    # res = batchProcess(file_path, file_path_2)
    # printEst(res, "直方图均值")
    # saveEst(res, "直方图均值", out_dir)
    
    # # 方法3比较
    # print("最大熵")
    # file_path_2 = "C:\\Study\\test\\m" # 方法一得到分割图像路径
    # res = batchProcess(file_path, file_path_2)
    # printEst(res, "最大熵")
    # saveEst(res, "最大熵", out_dir)