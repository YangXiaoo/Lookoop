# 2018-9-24
from matplotlib import pyplot as plt
import numpy as np
# import matplotlib.pyplot as plt
import os
import cv2
# from crop_pic import file

__suffix = ["png", "jpg"]


def file(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file


def tranPic(dirs, out_dir, iscrop=True):
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = file(dirs)

    total = len(files)
    fail = 0
    success = 0

    for f in files:
        img_name = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_name):
            continue
        try:
            img = cv2.imread(f, 0)
            # ret, img = cv2.threshold(img, 50, 255, 0)
            old_size = img.shape
            w, h = img.shape
            if iscrop:
                img, w, h = crop(img, (w, h), img_name, f)
                print(w,h, old_size)
                if (h, w) == old_size: # 若没有找到轮廓则跳过
                    print("error")
            else:
                # 默认不裁剪时若遇到长宽大于2的图形自动裁剪
                if w//h > 2:
                    img, w, h = crop(img, (w, h), img_name, f)
                    if (h, w) == old_size:
                        print("error")
                        
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
            print("failed to handle %s, skiped." % f)
            failed_dir = os.path.join("\\".join(f.split("\\")[:-2]), "failed")
            if not os.path.isdir(failed_dir):
                os.mkdir(failed_dir)
            print(os.path.join(failed_dir, f.split("\\")[-1]))
            os.system("copy %s %s" % (f, os.path.join(failed_dir, f.split("\\")[-1])))
            fail += 1

    print("\n\ntotal: %d\nsuccessful: %d\nfailed: %d" %(total, success, fail))


def crop(img, size, img_name, f):
    img_w, img_h = size
    mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    ret, thresh = cv2.threshold(img.copy() , 100, 255, cv2.THRESH_BINARY)

    image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
    max_contour = None
    max_area = 0
    for c in contours:
        # print(cv2.contourArea(c))
        if cv2.contourArea(c) > max_area:
            max_area = cv2.contourArea(c)
            max_contour = c

    img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 255,255), 2)
    # cv2.imshow("mask", img_contour)

    print("漫水法开始")
    cv2.imwrite(img_name, img_contour)
    # 漫水法
    # water(img_name, f) 



    print("漫水法完成")
    print(max_contour.shape)
    x, y, w, h = cv2.boundingRect(max_contour)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20
    img_new = img[y:y+h, x:x+w]
    # print(x,y,w,h, img_new.shape, "----- old img: ", img_w, img_h)
    return img_new, img_new.shape[1], img_new.shape[0]


def water(fn, old_image):
    img = cv2.imread(fn, 0)  
    h, w = img.shape[:2]                 #得到图像的高和宽  
    mask = np.zeros((h+2, w+2), np.uint8)#掩码单通道8比特，长和宽都比输入图像多两
                                         #个像素点，满水填充不会超出掩码的非零边缘  
    seed_pt = None  
    fixed_range = True  
    connectivity = 4  
  
    def update(dummy=None):  
        if seed_pt is None:  
            cv2.imshow('floodfill', img)  
            return  
        flooded = img.copy()                      #以副本的形式进行填充，这样每次  
        mask[:] = 0                               #掩码初始为全0  
        lo = cv2.getTrackbarPos('lo', 'floodfill')#观察点像素邻域负差最大值  
        hi = cv2.getTrackbarPos('hi', 'floodfill')#观察点像素邻域正差最大值  
        flags = connectivity                      #低位比特包含连通值, 4 (缺省) 或 8  
        if fixed_range:  
            flags |= cv2.FLOODFILL_FIXED_RANGE    #考虑当前象素与种子象素之间的差（高比特也可以为0）  
        #以白色进行漫水填充  
        cv2.floodFill(flooded, mask, seed_pt, (255, 255, 255), 
                     (lo,)*3, (hi,)*3, flags)  
          
        # cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1)#选定基准点用红色圆点标出  
        cv2.imshow('floodfill', flooded)  
        original = cv2.imread(old_image, 0)
        w, h = flooded.shape
        for i in range(w):
            for j in range(h):
                if flooded[i][j] != 0:
                    flooded[i][j] = 1

        res = np.multiply(flooded, original)
        cv2.imwrite(fn, res)
  
    def onmouse(event, x, y, flags, param):  #鼠标响应函数  
        global seed_pt  
        if flags & cv2.EVENT_FLAG_LBUTTON:   #鼠标左键响应，选择漫水填充基准点  
            seed_pt = x, y  
            update()  
  
    print("ss")
    update()  
    cv2.setMouseCallback('floodfill', onmouse)  
    cv2.createTrackbar('lo', 'floodfill', 20, 255, update)  
    cv2.createTrackbar('hi', 'floodfill', 20, 255, update)  
    print("sfgfg")
    # while True:  
    #     ch = 0xFF & cv2.waitKey()  
    #     if ch == 27:  
    #         break  
    #     if ch == ord('f'):  
    #         fixed_range = not fixed_range   #选定时flags的高位比特位0，也就是邻域的
    #                                         #选定为当前像素与相邻像素的的差，这样的效果就是联通区域会很大  
    #         print ('using %s range' % ('floating', 'fixed')[fixed_range])  
    #         update()  
    #     if ch == ord('c'):  
    #         connectivity = 12-connectivity  #选择4方向或则8方向种子扩散  
    #         print ('connectivity =', connectivity ) 
    #         update() 
    cv2.waitKey() 

def test(dirs, out_dir):
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = file(dirs)

    total = len(files)
    fail = 0
    success = 0

    for f in files:
        img_name = os.path.join(out_dir, f.split("\\")[-1])
        if os.path.isfile(img_name):
            continue
        img = cv2.imread(f, 0)
        # ret, img = cv2.threshold(img, 50, 255, 0)
        old_size = img.shape
        w, h = img.shape
        img, w, h = crop(img, (w, h), img_name, f)
    for f in files:
        contour = os.path.join(out_dir, f.split("\\")[-1])
        water(contour, f)


if __name__ == '__main__':
    # dirs = "C:\\Study\\ImageHandle\\fail_to_trans\\fail\\" 
    dirs = "C:\\Study\\test\\image"
    # dirs = "C:\\Study\\test\\failed"
    out_dir = "C:\\Study\\test\\out_pic" # 存储路径
    # tranPic(dirs, out_dir)  
    test(dirs, out_dir)  


    # # test
    # img = cv2.imread("C:\\Study\\test\\image\\m_1.jpg", 0)
    # mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
    # ret, thresh = cv2.threshold(img.copy() , 100, 255, cv2.THRESH_BINARY)

    # image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
    # max_contour = None
    # max_area = 0
    # for c in contours:
    #     # print(cv2.contourArea(c))
    #     if cv2.contourArea(c) > max_area:
    #         max_area = cv2.contourArea(c)
    #         max_contour = c

    # img = cv2.drawContours(mask, max_contour, -1, (255 , 255,255), 2)
    # cv2.imshow("tt", img)
    # cv2.imwrite("C:\\Study\\test\\out_pic\\m_1.jpg", img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()