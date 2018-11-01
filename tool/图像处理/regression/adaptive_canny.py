# coding:UTF-8
# 2018-11-1
# 自适应阈值+canny

import numpy as np
import os
import cv2

__suffix = ["png", "jpg"]

def getFile(dirpath):
    file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if name.split(".")[-1] in __suffix:
                file.append(path)
    return file

def process(file_path, out_dir):
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = getFile(file_path)
    for f in files:
        print(f)
        img = cv2.imread(f, 0)
        m, n = np.shape(img)
        mask = np.zeros((m, n))
        img_med = cv2.medianBlur(img, 5)

        # 去噪, 腐蚀膨胀开运算
        kernel = np.zeros((7,7), np.uint8)
        img = cv2.morphologyEx(img_med, cv2.MORPH_OPEN, kernel)
        adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
        edges = cv2.Canny(img, 20, 25)
        
        img = cv2.morphologyEx(edges, cv2.MORPH_OPEN, kernel)
        # # 中值滤波处理
        # # img_med = cv2.medianBlur(edges, 3)
        # minLineLength = 3
        # maxLineGap = 20
        # lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength,maxLineGap)
        # for x1,y1,x2,y2 in lines[0]:
        #   cv2.line(edges,(x1,y1),(x2,y2),(0,255,0),3)
        cv2.imshow("img", img)
        # kernel = np.zeros((3,3), np.uint8)
        # thresh = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # 找轮廓
        image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

        # 寻找最大轮廓
        max_contour = None
        max_area = 0
        noise = 0.8 * m * n # 可能会识别边界, 但这样处理后会导致返回值为None
        for c in contours:
            # print(cv2.contourArea(c)) # test
            if cv2.contourArea(c) > max_area and cv2.contourArea(c) < noise:
                max_area = cv2.contourArea(c)
                max_contour = c

        # 将轮廓绘制在模板上
        img_contour = cv2.drawContours(mask, max_contour, -1, (255 , 0,0), 1)
        # cv2.imshow("img", img_contour)
        # save
        out = os.path.join(out_dir, os.path.basename(f))
        # cv2.imwrite(out, img_contour)
        break
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    file_path = "C:\\Study\\test\\original"
    out_dir = "C:\\Study\\test\\canny"
    process(file_path, out_dir)