# coding:UTF-8
# 2018-10-16
# Mean Shift
# https://www.cnblogs.com/xfzhang/p/7261172.html
# https://blog.csdn.net/jzwong/article/details/78830600

# Mean shift 算法是基于核密度估计的爬山算法，可用于聚类、图像分割、跟踪等

"""
假设在一个多维空间中有很多数据点需要进行聚类，Mean Shift的过程如下：

1、在未被标记的数据点中随机选择一个点作为中心center；

2、找出离center距离在bandwidth之内的所有点，记做集合M，认为这些点属于簇c。同时，把这些求内点属于这个类的概率加1，这个参数将用于最后步骤的分类

3、以center为中心点，计算从center开始到集合M中每个元素的向量, 将这些向量相加，得到向量shift。

4、center = center+shift。即center沿着shift的方向移动, 移动距离是||shift||。

5、重复步骤2、3、4，直到shift的大小很小（就是迭代到收敛），记住此时的center。注意，这个迭代过程中遇到的点都应该归类到簇c。

6、如果收敛时当前簇c的center与其它已经存在的簇c2中心的距离小于阈值，那么把c2和c合并。否则，把c作为新的聚类，增加1类。

6、重复1、2、3、4、5直到所有的点都被标记访问。

7、分类：根据每个类，对每个点的访问频率，取访问频率最大的那个类，作为当前点集的所属类。

简单的说，mean shift就是沿着密度上升的方向寻找同属一个簇的数据点。
"""



import math
import numpy as np

MIN_DISTANCE = 0.000001  # mini error

def loadData(path, feature_num=2):
    '''
    导入数据
    '''
    f = open(path)
    data = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        data_tmp = []
        if len(lines) != feature_num:  # 判断特征的个数是否正确
            continue
        for i in range(feature_num):
            data_tmp.append(float(lines[i]))
        data.append(data_tmp)
    f.close()
    return data


def gaussianKernel(distance, bandwidth):
    '''
    高斯核函数
    input:  distance(mat):欧式距离
            bandwidth(int):核函数的带宽
    output: gaussian_val(mat):高斯函数值
    '''
    m = np.shape(distance)[0]  # 样本个数
    right = np.mat(np.zeros((m, 1)))  # mX1的矩阵
    for i in xrange(m):
        right[i, 0] = (-0.5 * distance[i] * distance[i].T) / (bandwidth * bandwidth)
        right[i, 0] = np.exp(right[i, 0])
    left = 1 / (bandwidth * math.sqrt(2 * math.pi))
    
    gaussian_val = left * right
    return gaussian_val


def eulerDistance(vecA, vecB):
    """
    计算欧式距离
    """
    total = (vecA - vecB) * (vecA - vecB).T
    return math.sqrt(total)


def shiftPoint(point, points, kernel_bandwidth):
    """
    计算均值漂移点
    """
    points = np.mat(points)
    m = np.shape(points)[0]

    # 计算point到points中每个点的欧拉距离
    point_dist = np.mat(np.zeros((m, 1)))
    for i in range(m):
        point_dist[i, 0] = eulerDistance(point, points[i])

    # 计算高斯核
    point_weight = gaussianKernel(point_dist, kernel_bandwidth) # m x 1

    # 计算分母
    sum_all = 0.0
    for i in range(m):
        sum_all += point_weight[i, 0]

    # for i in range(m):
    #     points[i] = point - points[i]
    # 均值偏移
    point_shift = point_weight.T * points / sum_all
    return point_shift


def groupPoints(mean_shift_points):
    """
    计算所属的类别, 分类
    """
    group_assignment = []
    m, n = np.shape(mean_shift_points)
    index = 0
    index_dict = {}
    for i in range(m):
        # 每一行的数据
        item = []
        for j in range(n):
            # %5.2f ： 将中心限定在一个范围
            item.append(str(("%5.2f" % mean_shift_points[i, j])))
        
        item_1 = "_".join(item)
        if item_1 not in index_dict:
            index_dict[item_1] = index
            index += 1
    
    for i in range(m):
        item = []
        for j in range(n):
            item.append(str(("%5.2f" % mean_shift_points[i, j])))

        item_1 = "_".join(item)
        group_assignment.append(index_dict[item_1])

    return group_assignment


def trainMeanShift(points, kernel_bandwidth=2):
    """
    计算mean shift 模型
    """
    mean_shift_points = np.mat(points)
    max_min_dist = 1
    it = 0
    m = np.shape(mean_shift_points)[0]  # 样本的个数
    need_shift = [True] * m  # 标记是否需要漂移

    while max_min_dist > MIN_DISTANCE:
        max_min_dist = 0
        it += 1
        print("it: ", it)
        for i in range(m):
            # 判断每一个点是否需要漂移
            if not need_shift[i]:
                continue

            p = mean_shift_points[i]
            p_start = p
            # 计算均值漂移点
            p_new = shiftPoint(p, points, kernel_bandwidth)

            # 计算该点与漂移点之间的距离
            dist = eulerDistance(p_new, p_start)

            if dist > max_min_dist:
                max_min_dist = dist
            if dist < MIN_DISTANCE:
                # 不需要移动
                need_shift[i] = False

            mean_shift_points[i] = p_new

    group = groupPoints(mean_shift_points)

    return np.mat(points), mean_shift_points, group


if __name__ == "__main__":
    # 导入数据集
    print("loading data...")
    data = loadData("data", 2)
    # 训练，h=2
    print("training...")
    points, shift_points, cluster = trainMeanShift(data, 2)
    print(points, shift_points, cluster)
    # # 保存所属的类别文件
    # print "----------3.1.save sub ------------"
    # save_result("sub_1", np.mat(cluster))
    # print "----------3.2.save center ------------"
    # # 保存聚类中心
    # save_result("center_1", shift_points) 

