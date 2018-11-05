# coding:UTF-8
# 2018-11-5
# 分割过程中一些基本操作封装

import os
import cv2
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


__suffix = ["png", "jpg"]
__total = 256

def loadPic(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def loadData(file_path, gap=1):
    '''
    导入训练数据
    数据格式
    [[0	41	33	176	58	95	193	615	922	1193	...		]
    [...]
    ...
    [...]]
    file_path: 数据文件
    gap: 参数减少倍数
    '''
    # 将标签添加到数据中
    f = open(file_path)
    feature = []
    label = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        for i in range(2, len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        feature.append(feature_tmp)
        label.append(float(lines[-1]))
    f.close()

    # 调整数据
    fea = []
    for i in feature:
        index = 0
        tmp = []
        while index < __total:
            tmp.append(sum(i[index : index + gap])/gap)
            index += gap
        fea.append(tmp)
    print(len(fea[0]))

    return np.mat(fea), np.mat(label).T


def getThreshValue(img, weight):
    """
    根据权重预测阈值
    """
    img = moveNoise(img, 7) # 去噪
    histogram = getHistogram(img) # 获得直方图
    data = np.mat(histogram) # 转换为矩阵类型
    v = int((data * weight)[0, 0]) # 预测最佳阈值
    # 对阈值进行判断, 去除漂移值
    if v > mean_value * 0.9:
        v = int(mean_value * 0.9)
    if v < mean_value * 0.6:
        v = int(mean_value * 0.6)
    return v


def moveNoise(img, kernel_size):
	"""
	二值处理前去除噪点
	"""
	img_med = cv2.medianBlur(img, 5)
    kernel = np.zeros((7,7), np.uint8)
    thresh = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)
    return thresh


def getMean(img):
	"""
	获得图像像素均值
	"""
	img_w, img_h = np.shape(img)
	sums = 0
    for i in range(img_w):
        for j in range(img_h):
            sums += img[i][j]
    mean_value = sums // (img_w * img_h)

    return mean_value


def getCov(img, mean_value):
	"""
	获得图像像素标准均方差
	"""
	img_w, img_h = np.shape(img)
	sum_diff = 0
    for i in range(img_w):
        for j in range(img_h):
            diff = float((mean_value - img[i][j]) * (mean_value - img[i][j]))
            sum_diff += diff
    variance = int((sum_diff // (img_w * img_h))**0.5)

    return variance


def getHistogram(img):
	"""
	获得图像直方图统计
	"""
	img_w, img_h = np.shape(img)
	histogram = [1 for _ in range(256)]
    for i in range(img_w):
        for j in range(img_h):
            histogram[img[i][j]] += 1

    return histogram


def saveImage(img_dirs, mid_name, image):
    """
    保存图像
    img_dirs:保存目录
    mid_name:新保存图片后缀
    image:图像
    """
    basename = os.path.basename(img_dirs)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    suffix = file[-1]
    image_file = os.path.join("\\".join(img_dirs.split("\\")[:-1]), file_prefix + mid_name + suffix)
    cv2.imwrite(image_file, image)


def getData(file_path, new_file, out_file):
    '''
    导入训练数据
    file_path: 标签文件
    new_file: 数据文件
    将数据合成保存到out_file文件中
    '''
    # 获得数据标签   
    f = open(file_path)
    feature = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        for i in range(len(lines)):
            feature_tmp.append(lines[i])
        feature.append(feature_tmp)
    f.close()

    # 将标签添加到数据中
    new_f = open(new_file)
    new_feature = []
    label = []
    row = 0
    for line in new_f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        # print(row, float(feature[row][0]), float(lines[0]))
        if  row < len(feature) and float(feature[row][0]) == float(lines[0]):
            for i in range(len(lines) - 1):
                feature_tmp.append(lines[i])
            new_feature.append(feature_tmp)
            label.append(feature[row][-1])
            row += 1
    new_f.close()

    n_f = open(out_file, "w")
    m = len(new_feature)
    for i in range(m):
        n_f.write("\t".join(new_feature[i]) + '\t' + str(label[i]) + '\n')

    n_f.close()


def maxRegionGrowing(img, thresh):
	"""
	最大连通域进行分割
	Img: 待分割图
	thresh:二值图
	"""
    # 最大连通区域
    print("finding maximum region...")
    m, n = thresh.shape
    visited = [[False for _ in range(n)] for _ in range(m)]

    max_area = 0 # 最大连通点个数
    max_visited = [] # 连通区域记录
    for i in range(m):
        for j in range(n):
            queue = []
            if visited[i][j] or thresh[i][j] == 0:
                continue
            else:
                tmp_area = 0
                tmp_visited = [[False for _ in range(n)] for _ in range(m)]
                queue.append([i, j])
                visited[i][j] = True
                tmp_visited[i][j] = True
                while len(queue) != 0:
                    row, col = queue.pop()
                    if row > 1 and not visited[row - 1][col] and thresh[row - 1][col] != 0:
                        queue.append([row - 1, col])
                        visited[row - 1][col] = True
                        tmp_visited[row - 1][col] = True
                        tmp_area += 1

                    # 往右搜索
                    if row + 1 < m and not visited[row + 1][col] and thresh[row + 1][col] != 0:
                        queue.append([row + 1, col])
                        visited[row + 1][col] = True
                        tmp_visited[row + 1][col] = True
                        tmp_area += 1

                    # 往上搜索
                    if col - 1 >= 0 and not visited[row][col - 1] and thresh[row][col - 1] != 0:
                        queue.append([row, col -1])
                        visited[row][col - 1] = True
                        tmp_visited[row][col - 1] = True
                        tmp_area += 1

                    # 往下搜搜
                    if col + 1 < n and not visited[row][col + 1] and thresh[row][col + 1] != 0:
                        queue.append([row, col + 1])
                        visited[row][col + 1] = True
                        tmp_visited[row][col + 1] = True
                        tmp_area += 1 

                if tmp_area > max_area:
                    max_visited = tmp_visited
                    max_area = tmp_area
    for i in range(m):
        for j in range(n):
            if not max_visited[i][j]:
                img[i][j] = 0
                thresh[i][j] = 0
    return img_new, thresh


def regionGrowing(img, thresh):
    """
    区域生长
    """
    m, n = thresh.shape
    r, c = m // 2, n // 2 # 种子起始点
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = []
    queue.append([r, c])
    visited[r][c] = True
    while len(queue) != 0:
        row, col = queue.pop()
        if row > 1 and not visited[row - 1][col] and thresh[row - 1][col] != 0:
            queue.append([row - 1, col])
            visited[row - 1][col] = True

        # 往右搜索
        if row + 1 < m and not visited[row + 1][col] and thresh[row + 1][col] != 0:
            queue.append([row + 1, col])
            visited[row + 1][col] = True

        # 往上搜索
        if col - 1 >= 0 and not visited[row][col - 1] and thresh[row][col - 1] != 0:
            queue.append([row, col -1])
            visited[row][col - 1] = True

        # 往下搜搜
        if col + 1 < n and not visited[row][col + 1] and thresh[row][col + 1] != 0:
            queue.append([row, col + 1])
            visited[row][col + 1] = True  

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                thresh[i][j] = 0
                img[i][j] = 0

    return img, thresh


def waterBfs(img, old_image):
	"""
	获取最大轮廓后进行分割
	img: 轮廓
	old_img:待分割图
	返回：分割图，二值图
	"""
    row, col = img.shape
    # 得到rowxcol的矩阵[[False, False...], ..., [False, False...]]
    visited = [[False for _ in range(col)] for _ in range(row)] 
    queue = [] # 存放每一次遍历的起点
    def bfs(img, row, col, visited):
        m, n = img.shape
        queue.append([row, col])
        visited[row][col] = True 

        while len(queue) != 0:
            row, col = queue.pop()
            # print(len(queue))
            
            # 往左搜索
            if row >= 1 and not visited[row - 1][col] and img[row - 1][col] == 0:
                queue.append([row - 1, col])
                visited[row - 1][col] = True

            # 往右搜索
            if row + 1 < m and not visited[row + 1][col] and img[row + 1][col] == 0:
                queue.append([row + 1, col])
                visited[row + 1][col] = True

            # 往上搜索
            if col - 1 >= 0 and not visited[row][col - 1] and img[row][col - 1] == 0:
                queue.append([row, col -1])
                visited[row][col - 1] = True

            # 往下搜搜
            if col + 1 < n and not visited[row][col + 1] and img[row][col + 1] == 0:
                queue.append([row, col + 1])
                visited[row][col + 1] = True

    # 第一行与最后一行开始
    for c in range(col):
        if not visited[0][c] and img[0][c] == 0:
            bfs(img, 0, c, visited)
        if not visited[-1][c] and img[-1][c] == 0:
            bfs(img, row - 1, c, visited)


    for r in range(row):
        if not visited[r][0] and img[r][0] == 0:
            bfs(img, r, 0, visited)
        if not visited[r][-1] and img[r][-1] == 0:
            bfs(img, r, col - 1, visited)

    # 将模板二值化0,1
    for i in range(row):
        for j in range(col):
            if not visited[i][j]:
                img[i][j] = 1

    # 原图与模板相乘
    res = np.multiply(img, old_image)
    return res, img


def normalization(img):
    """
    归一化
    """
    w, h = np.shape(img)
    if w > h:
        gap = w - h
        fill = np.zeros([1, w], np.uint8)
        for i in range(gap//2):
            img = np.concatenate((img,fill), axis = 0)
        for i in range(gap//2):
            img = np.concatenate((fill, img), axis = 0)
    elif w < h:
        gap = h - w
        fill = np.zeros([h, 1], np.uint8)
        for i in range(gap//2):
            img = np.concatenate((img,fill), axis = 1)
        for i in range(gap//2):
            img = np.concatenate((fill, img), axis = 1)
    else:
        pass

    img_new = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)

    return img_new


def printToConsole(start_time, f, count, total, gap):
	"""
	打印信息
	"""
    print("handled: ", f.split("\\")[-1])
    if count % gap == 0 and count != total:
        end_time = datetime.datetime.now()
        expend = end_time - start_time
        print("\nexpend time:", expend, "\nexpected time: ", expend / count * total, '\n')


def saveError(e, out_dir, f):
	"""
	当出现错误时打印错误并保存未处理的图片到指定目录
	"""
	print("Error: " + str(e))    
    failed_dir = os.path.join("\\".join(out_dir.split("\\")[:-1]), out_dir.split("\\")[-1] + "_failed")
    print("failed to handle %s, skiped.\nsaved in %s" % (f,failed_dir))
    if not os.path.isdir(failed_dir):
        os.mkdir(failed_dir)
    print(os.path.join(failed_dir, f.split("\\")[-1]))
    os.system("copy %s %s" % (f, os.path.join(failed_dir, f.split("\\")[-1])))


def moveMargin(img, threshed_img):
	"""
	去除多余的边缘
	img:已经分割好的图片
	threshed_img:分割图片对应得二值图
	"""
	img_w, img_h = np.shape(img)
    x, y, w, h = cv2.boundingRect(threshed_img)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20
    return img[y:y+h, x:x+w]


def maxContour(img, thresh):
	"""
	获得最大轮廓
	返回分割后的图像和对应的二值图
	"""
    img_w, img_h = img.shape
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    # 找轮廓
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

    # 寻找最大轮廓
    max_contour = None
    max_area = 0
    noise = 0.8 * img_w * img_h # 可能会识别边界, 但这样处理后会导致返回值为None
    for c in contours:
        if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
            max_area = cv2.contourArea(c)
            max_contour = c

    img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 0,0), 1)
    res, img =  waterBfs(img_contour, img)
    threshed = np.multiply(img, thresh)
    return res, threshed


def maxEntrop(img):
	"""
	根据信息熵获得最佳阈值
	img：灰度图像
	return : 最佳阈值
	"""
    histogram = [0] * 256
    m, n = np.shape(img)

    max_entropy = -1
    threshed = 0
    total_pixel = m * n 
    # 计算阈值
    for i in range(m):
        for j in range(n):
            histogram[img[i, j]] += 1

    for i in range(256):
        # 计算Pt
        p_t = 0
        for x in range(i):
            p_t += histogram[x]

        # 计算背景熵
        H_B = 0
        for x in range(i):
            if histogram[x] != 0:
                pi_pt = histogram[x] / p_t
                H_B += - pi_pt * np.log(pi_pt)

        # 计算物体熵
        H_O = 0
        for x in range(i, 250):
            if histogram[x] != 0:
                pi_1_pt = histogram[x] / (total_pixel - p_t)
                H_O += - pi_1_pt * np.log(pi_1_pt)

        total_entrop = H_O + H_B
        if total_entrop > max_entropy:
            max_entropy = total_entrop
            threshed  = i 

    return threshed


def ratation(res):
    img_w, img_h = np.shape(res)
    image, contours, hier = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
    # 寻找最大轮廓
    max_contour = None
    max_area = 0
    noise = 0.8 * img_w * img_h # 可能会识别边界, 但这样处理后会导致返回值为None
    for c in contours:
        # print(cv2.contourArea(c)) # test
        if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
            max_area = cv2.contourArea(c)
            max_contour = c
    width, height = cv2.minAreaRect(max_contour)[1]
    rect = cv2.minAreaRect(max_contour)
    box = cv2.boxPoints(rect)  # 获取最小外接矩形的4个顶点
    box = np.int0(box)

    if 0 not in box.ravel():
        # 旋转角度
        theta = cv2.minAreaRect(max_contour)[2]
        # if abs(theta) <= 45:
        print('图片的旋转角度为%s.'%theta)
        sign = 1
        if theta < 0:
            sign = -1
        if abs(theta) > 45:
            angle = sign * (abs(theta) - 90)
        else:
            angle = theta

    center = (img_w//2, img_h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    res = cv2.warpAffine(res, M, (img_w*4, img_h*4), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return res


def grabCut(img):
	"""
	根据grabCut算法分割前景
	"""
    mask = np.zeros(img.shape[:2],np.uint8) # mask
    h, w, _ =  img.shape

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))

    # print(rect)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis] # np.newaxis = None
    return img


def watershed(img):
	"""
	使用分水岭进行图像分割
	"""
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 4)

    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=4)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    return img


def plotScatter(data, labels, w, lim, save_name):
	"""
	绘制散点图; 横坐标真实值，纵坐标预测值
	data : 数据
	labels:标签
	w:mat 权重
	lim:[(), ()] x,y轴范围
	save_name: 散点图保存名称
	"""
    actual_x = [] # 绘制直线的x轴坐标
    predict_x = [] # 绘制预测值的x坐标
    for i in labels:
        actual_x.append(int(i[0]))
        predict_x.append(i[0])
    actual_y = actual_x # 直线的y坐标

    # 得到预测值
    predition = data * w
    predict_y = [] # 预测值的y坐标
    for i in predition:
        predict_y.append(i[0])
    color = np.arctan2(predict_y, predict_x)
    # 绘制散点图
    plt.scatter(predict_x, predict_y, s = 10, c = color, alpha = 1)
    # 设置坐标轴范围
    plt.xlim(lim[0])
    plt.ylim(lim[1])

    plt.xlabel("actual value")
    plt.ylabel("prediction")
    plt.plot(actual_x, actual_y)
    plt.savefig(save_name)
    plt.show()


##############################################
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
        for j in range(n):
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
        print(files_1[i])
        accuracy_rate, error_rate, loss_rate = getAccuracy(files_1[i], files_2[i])
        # print(files_2[i])
        basename = os.path.basename(files_1[i])
        pic_name = os.path.splitext(basename)[0]
        res[pic_name] = [accuracy_rate, error_rate, loss_rate]

    return res