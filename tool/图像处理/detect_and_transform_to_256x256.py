# 2018-9-18
# update: 2018-9-24 # 使用漫水法
# update: 2018-9-25 # 优化一些代码
# 提取手掌并裁剪为256x256

# from matplotlib import pyplot as plt
import numpy as np
import os
import cv2

__suffix = ["png", "jpg"]


def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def tranPic(dirs, out_dir, thresh_value, iscrop=True):
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = file(dirs)

    total = len(files)
    fail = 0
    success = 0

    for f in files:
        img_name = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_name):
            print("Skip %s, because it was already processed." % f)
            continue
        try:
            img = cv2.imread(f, 0)
            # ret, img = cv2.threshold(img, 50, 255, 0)
            old_size = img.shape
            w, h = img.shape
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

            if w > h:
                gap = w - h
                fill = np.zeros([1, w], np.uint8)
                print(f, ", old image size:", old_size, ", fill_size:", fill.shape, ", new imgae size:", img.shape, ", w>h:", w, h)
                for i in range(gap//2):
                    img = np.concatenate((img,fill), axis = 0)
                for i in range(gap//2):
                    img = np.concatenate((fill, img), axis = 0)
                # gap = w - h
                # fill = np.zeros([w,gap//2], np.uint8)
                # img = np.concatenate((img,fill), axis = 0)
                # img = np.concatenate((fill, img), axis = 0)
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

    print("\n\ntotal: %d\nsuccessful: %d\nfailed: %d" %(total, success, fail))


def crop(img, img_name, f, thresh_value=80):
    """
    Img: 原图
    img_name: 图像存储路径
    f: 原图像路径
    thresh_value： 阈值
    """
    img_w, img_h = img.shape
    img_contour, max_contour = findMaxContour(img, thresh_value)
    # cv2.imshow("mask", img_contour) # test

    # 漫水法对轮廓进行处理
    print("\n漫水法...")
    # print(max_contour[0][0][1], max_contour[0][0][1] + 2) # 不可控
    seed_pt = (1, 1) # 种子放到外面, 最后处理的时候翻转
    # cv2.imwrite(img_name, img_contour) # test
    res = water(img_contour, img, seed_pt, img_name) 
    print("漫水法完成")


    # print(max_contour.shape) # test
    # 寻找轮廓的外接矩形
    x, y, w, h = cv2.boundingRect(max_contour)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20
    img_new = res[y:y+h, x:x+w]
    # print(x,y,w,h, img_new.shape, "----- old img: ", img_w, img_h) # test
    return img_new, img_new.shape[1], img_new.shape[0]


def water(img, old_image, seed_pt, fn, is_write=False):
    """
    漫水法，BFS
    """
    h, w = img.shape[:2]    # 得到图像的高和宽  

    # 掩码单通道8比特，长和宽都比输入图像多两个像素点，满水填充不会超出掩码的非零边缘 
    mask = np.zeros((h+2, w+2), np.uint8) 

    fixed_range = True  
    connectivity = 4  

    # 两个值可以更改
    lo = 20
    hi = 40
    
    flooded = img.copy()
    mask[:] = 0 # 掩码初始为全0    
    flags = connectivity    # 低位比特包含连通值, 4 (缺省) 或 8  
    if fixed_range:  
        flags |= cv2.FLOODFILL_FIXED_RANGE  # 考虑当前象素与种子象素之间的差（高比特也可以为0）  
    # 以白色进行漫水填充  
    cv2.floodFill(flooded, mask, seed_pt, (255, 255, 255), 
                 (lo,)*3, (hi,)*3, flags)  
      
    original = old_image

    # 将模板二值化0,1
    w, h = flooded.shape
    for i in range(w):
        for j in range(h):
            if flooded[i][j] != 0:
                flooded[i][j] = 0
            else:
                flooded[i][j] = 1

    res = np.multiply(flooded, original)
    # cv2.imwrite(fn, res)
    return res


def findMaxContour(img, thresh_value=100):
    img_w, img_h = img.shape

    # 模板，存储轮廓
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    # 阈值
    ret, thresh = cv2.threshold(img.copy() , thresh_value, 255, cv2.THRESH_BINARY)

    # 去噪
    kernel = np.zeros((3,3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

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
    img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 255,255), 1)
    return img_contour, max_contour


def checkContour(dirs, out_dir):
    """
    先对图像轮廓进行判断，这样更加快速
    未单独对轮廓进行处理，后续代码暂无
    测试使用!
    """
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = file(dirs)

    total = len(files)
    fail = 0
    success = 0

    for f in files:
        img_name = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_name):
            print("Skip %s, because it was already processed." % f)
            continue
        img = cv2.imread(f, 0)

        thresh_value = 100 # 更改此值对轮廓进行处理
        mask, max_contour = findMaxContour(img, thresh_value)
        img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 255,255), 1)
        # cv2.imshow("mask", img_contour) # test

        cv2.imwrite(img_name, img_contour)

def checkAndCompute(dirs, out_dir):
    """
    确保out_dir目录下面的文件已经备份并且轮廓质量较好
    """
    pass


if __name__ == '__main__':
    # dirs = "C:\\Study\\ImageHandle\\fail_to_trans\\fail\\" 
    # dirs = "C:\\Study\\test\\failed"

    dirs = "C:\\Study\\test\\image" # 原图片存储路径
    out_dir = "C:\\Study\\test\\out_pic" # 存储路径

    thresh_value = 70
    tranPic(dirs, out_dir, thresh_value)
    # a. 在out_dir路径中查看结果
    # b. 删除质量不好的图像
    # c. 修改thresh_value的值(每次减小10， 60时质量已经不怎好)
    # d. 运行
    # e. 重复a-d操作直到out_dir目录中的图片质量变好

    # # 检查轮廓质量
    # checkContour(dirs, out_dir)  