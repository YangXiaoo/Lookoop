# coding:UTF-8
# 2018-11-2
# OTSU

import numpy as np
import os
import cv2
import datetime


__suffix = ["png", "jpg"]

def getFile(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file
    

def handle(dirs, out_dir, clip):
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = getFile(dirs)

    total = len(files)
    fail, success, skip, count = 0, 0, 0, 0

    for f in files:
        count += 1
        print(count, '/', total)
        img_dirs = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_dirs):
            skip += 1
            continue
        try:
            
            # 1. 读取图片, 切边处理
            img = cv2.imread(f, 0)
            x,w,y,h = clip
            img = img[x:w , y:h]

            # 2. 分割
            img= crop(img, img_dirs)
            h, w = img.shape
            
            # # 3. 归一化为256x256
            # img_new = normalization(img, w, h)

            # img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)

            # 6. 保存图片
            saveImage(img_dirs, img, "_new")

            # 控制台输出
            print("handled: ", f.split("\\")[-1])
            if count % 5 == 0 and count != total:
                end_time = datetime.datetime.now()
                expend = end_time - start_time
                print("\nexpend time:", expend, "\nexpected time: ", expend / count * total, '\n')
            success += 1
        
        except Exception as e:
            # 图片处理失败, 跳过图片保存目录: ./failed
            print("Error: " + str(e))
            
            failed_dir = os.path.join("\\".join(out_dir.split("\\")[:-1]), out_dir.split("\\")[-1] + "_failed")
            print("failed to handle %s, skiped.\nsaved in %s" % (f,failed_dir))
            if not os.path.isdir(failed_dir):
                os.mkdir(failed_dir)
            print(os.path.join(failed_dir, f.split("\\")[-1]))
            os.system("copy %s %s" % (f, os.path.join(failed_dir, f.split("\\")[-1])))
            fail += 1
            print()


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    print("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


def crop(img, img_dirs):
    img_w, img_h = img.shape
    saveImage(img_dirs, img, "_old")

    # 获得原图的自适应阈值图
    # adaptive = cv2.adaptiveThreshold(img, 255, ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    # 去噪
    img_med = cv2.medianBlur(img, 5)
    kernel = np.zeros((7,7), np.uint8)
    img = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)
    # saveImage(img_dirs, img, "_remove_noise") # 去除噪声的图片
    # 获得处理后的二值图像
    # 阈值
    sums = 0
    for i in range(img_w):
        for j in range(img_h):
            sums += img[i][j]
    thresh_value = sums // (img_w * img_h) * 0.86
    # print("\nthresh_value: ",thresh_value)
    threshold, threshed_img = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)
    # imgOtsu = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    kernel = np.zeros((7,7), np.uint8)
    threshed_img = cv2.morphologyEx(threshed_img, cv2.MORPH_OPEN, kernel)
    threshed_img = cv2.morphologyEx(threshed_img, cv2.MORPH_CLOSE, kernel)
    img_segement, thresh_img = maxContour(img, threshed_img)


    return img_segement


def saveImage(img_dirs, image, mid_name):
    """
    保存图像
    """
    basename = os.path.basename(img_dirs)
    file = os.path.splitext(basename)
    file_prefix = file[0]
    suffix = file[-1]
    image_file = os.path.join("\\".join(img_dirs.split("\\")[:-1]), file_prefix + mid_name + suffix)
    cv2.imwrite(image_file, image)



def waterBfs(img, old_image):
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


def maxContour(img, thresh):
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

d

if __name__ == '__main__':
    file_path = "C:\\Study\\test\\st"
    out_dir = "C:\\Study\\test\\histogram_mean_no_norm"
    handle(file_path, out_dir, (45,-45,45,-45))