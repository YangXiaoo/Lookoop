# 2018-9-18
# update: 2018-9-24 # 使用漫水法
# update: 2018-9-25 # 优化一些代码, 增加边缘切片，中值滤波，等前处理
# update: 2018-9-26 # 使用BFS实现轮廓填充
# 提取手掌并裁剪为256x256

# from matplotlib import pyplot as plt
import numpy as np
import os
import cv2
import datetime

__suffix = ["png", "jpg"]


def loadPic(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def tranPic(dirs, out_dir, thresh_value=None, iscrop=True, clip=None):
    start_time = datetime.datetime.now()
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    # 1. 加载数据
    files = loadPic(dirs)

    total = len(files)
    fail = 0
    success = 0
    skip = 0

    # 遍历图片
    for f in files:
        img_name = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_name):
            # print("Skip %s, because it was already processed." % f)
            skip += 1
            continue
        try:
            img = cv2.imread(f, 0)

            # 切边处理
            if clip:
                x,w,y,h = clip
                img = img[x:w,y:h]

            # ret, img = cv2.threshold(img, 50, 255, 0)
            old_size = img.shape
            w, h = img.shape

            # 裁剪
            if iscrop:
                img, w, h = crop(img, img_name, f, thresh_value)
                if (h, w) == old_size: # 若没有找到轮廓则跳过
                    print("Error: Fail to find contours.")
            else:
                # 默认不裁剪时若遇到长宽大于2的图形自动裁剪
                if w//h > 2:
                    img, w, h = crop(img, img_name, f, thresh_value)
                    if (h, w) == old_size:
                        print("Error: Fail to find contours.")
                        
            img = np.array(img)

            # 将图片扩充为正方形
            if w > h:
                gap = w - h
                fill = np.zeros([1, w], np.uint8)
                print(f, ", old image size:", old_size, ", fill_size:", fill.shape, ", new imgae size:", img.shape, ", w>h:", w, h)
                for i in range(gap//2):
                    img = np.concatenate((img,fill), axis = 0)
                for i in range(gap//2):
                    img = np.concatenate((fill, img), axis = 0)
            elif w < h:
                gap = h - w
                fill = np.zeros([h, 1], np.uint8)
                print(f, ", old image size:", old_size, ", fill_size:", fill.shape, ", new imgae size:", img.shape, ", w<h:", w, h)
                for i in range(gap//2):
                    img = np.concatenate((img,fill), axis = 1)
                for i in range(gap//2):
                    img = np.concatenate((fill, img), axis = 1)
            else:
                pass

            img_new = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)
            img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)

            cv2.imwrite(img_name, img_new)
            print("handled: ", f.split("\\")[-1])
            success += 1

        except Exception as e:
            # 图片处理失败, 跳过图片保存目录: ./failed
            print("Error: " + str(e))
            
            failed_dir = os.path.join("\\".join(f.split("\\")[:-2]), "failed")
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


def crop(img, img_name, f, thresh_value=None):
    """
    Img: 原图
    img_name: 图像存储路径
    f: 原图像路径
    thresh_value： 阈值
    """
    # 获得图像长宽
    img_w, img_h = img.shape

    # 得到绘制在0矩阵上的轮廓和 最大轮廓矩阵
    img_contour, max_contour = findMaxContour(img, thresh_value)

    # BFS
    print("BFS...")
    res = waterBfs(img_contour, img)


    # 寻找轮廓的外接矩形
    x, y, w, h = cv2.boundingRect(max_contour)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20

    # 切片
    img_new = res[y:y+h, x:x+w]

    return img_new, img_new.shape[1], img_new.shape[0]


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
    return res


def findMaxContour(img, thresh_value=100):
    img_w, img_h = img.shape

    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    # 中值滤波处理
    img_med = cv2.medianBlur(img, 5)

    # 去噪, 腐蚀膨胀开运算
    kernel = np.zeros((7,7), np.uint8)
    thresh = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)

    # 阈值
    if not thresh_value:
        sums = 0
        for i in range(img_w):
            for j in range(img_h):
                sums += thresh[i][j]
        thresh_value = sums // (img_w * img_h) * 0.86
    print("\nthresh_value: ",thresh_value)

    # 模板，存储轮廓
    # 阈值
    ret, thresh = cv2.threshold(thresh , thresh_value, 255, cv2.THRESH_BINARY)
    kernel = np.zeros((7,7), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) # 闭运算，封闭小黑洞
    thresh = cv2.medianBlur(thresh, 5)
    # thresh = cv2.blur(thresh, (5,5))
    print(np.max(thresh))
    cv2.imwrite("C:\\Study\\test\\out_pic\\thresh.jpg", thresh)


    # 找轮廓
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

    # 寻找最大轮廓
    max_contour = None
    max_area = 0
    noise = 0.8 * img_w * img_h # 可能会识别边界, 但这样处理后会导致返回值为None
    for c in contours:
        # print(cv2.contourArea(c)) # test
        if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
            max_area = cv2.contourArea(c)
            max_contour = c

    # 将轮廓绘制在模板上
    img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 0,0), 1)
    cv2.imwrite("C:\\Study\\test\\out_pic\\t.jpg", img_contour)
    return img_contour, max_contour


if __name__ == '__main__':
    # dirs = "C:\\Study\\ImageHandle\\fail_to_trans\\fail\\" 
    # dirs = "C:\\Study\\test\\failed"

    dirs = "C:\\Study\\test\\image\\train-m" # 原图片存储路径
    out_dir = "C:\\Study\\test\\out_pic" # 存储路径

    # thresh_value = 70
    # tranPic(dirs, out_dir, thresh_value)
    tranPic(dirs, out_dir, thresh_value=None, clip=(30,-30,30,-30)) 

    # tranPic()使用:
    # 有白边：clip=(30,-30,30,-30) 若生成图片两边有白边则增大前两个参数(35,-35,30,-30)， 若上下有白边则增大后两个参数(30,-30,35,-35) 
    # 无白边则可以省略这个参数或者clip=None
    # 不输入thresh_value时会自动计算阈值, 下面调参时则需要输入
    # a. 在out_dir路径中查看结果
    # b. 删除质量不好的图像
    # c. 修改thresh_value的值(每次减小10， 60时质量已经不怎好)
    # d. 运行
    # e. 重复a-d操作直到out_dir目录中的图片质量变好

    # # 检查轮廓质量
    # checkContour(dirs, out_dir)  



#     a.  去除白色边框 //判断图像是否存在白色框线，如有则去除；

# b   区域生长：
# （1） 首先对图像进行中值滤波去除噪声，使用核为3x3的开运算去除噪点；
# （2） 阈值处理；(公式可以加一个)
# （3） 闭运算封闭图像中会产生的小黑洞；
# （4） 绘制与原图像大小相同的0矩阵模板，提取图像中所有封闭轮廓，寻找面积最大的封闭轮廓并将其绘制在模板上；
# c.  提取手型：
# （1） 从模板四个边往内搜索轮廓外区域, 并标记    
# （2） 将模板二值化，轮廓内的像素值为1，将原图与模板相乘即可获得手骨图像
# d.  对手掌进行适当裁剪(使其居中)、填充为正方形，按比例缩放，将图片大小全部统一为256X256；

# 区域生长
a. 去除白色边框 
b. 预处理
    1. 中值滤波
    2. 腐蚀膨胀开运算
    3. 公式求得阈值,将图像二值化
    4. 闭运算
    5. 得到预处理图像IMG
c. 区域生长
    1. row, col = size(IMG), 种子为 (row//2, col//2)
    2. False矩阵V=[row x col]
    3. 以手掌边缘为边界进行生长，手掌内像素值不为0的点(i, j      )进行标记V[i, j] = True
    4. 根据V, 将V[i, j]不为True的点IMG[i,j]置为0，得到新图NEW_IMG
d. 裁剪
    1. 根据NEW_IMG得到手掌轮廓外接矩形的长宽
    2. 裁剪NEW_IMG，使其居中，得到NEW_IMG_1
    3. 将NEW_IMG_1扩充为正方形(保证缩小为256x256时不失真)NEW_IMG_2
    4. 将NEW_IMG_2缩小为256x256大小



# # 最大连通区域
# a. 去除白色边框 
# b. 预处理
#     1. 中值滤波
#     2. 腐蚀膨胀开运算
#     3. 公式求得阈值,将图像二值化
#     4. 闭运算
#     5. 得到预处理图像IMG
# c. 最大连通区域
#     1. row, col = size(IMG), 创建False矩阵V=[row x col]
#     2. 遍历IMG, 将像素最多的连通区域作为最大连通区域并将对应的点(i,j)标记为V[i, j]=True(经过去噪二值处理最大连通区域必为手掌)
#     3. 遍历V，将V[i, j]==False对应的像素值置为0,得到手掌NEW_IMG
# d. 裁剪
#     1. 根据NEW_IMG得到手掌轮廓外接矩形的长宽
#     2. 裁剪NEW_IMG，使其居中，得到NEW_IMG_1
#     3. 将NEW_IMG_1扩充为正方形(保证缩小为256x256时不失真)NEW_IMG_2
#     4. 将NEW_IMG_2缩小为256x256大小