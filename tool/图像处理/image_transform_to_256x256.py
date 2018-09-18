# 2018-9-18
# 将图片转换为256x256并转换为三通道
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

    for f in files:
        img = cv2.imread(f, 0)
        if iscrop:
            img = crop(img)
        w, h = img.shape
        img = np.array(img)
        if w > h:
            gap = w - h
            fill = np.zeros([w,1], np.uint8)
            # print(fill.shape, img.shape)
            for i in range(gap//2):
                img = np.concatenate((img,fill), axis = 1)
            for i in range(gap//2):
                img = np.concatenate((fill, img), axis = 1)
            # gap = w - h
            # fill = np.zeros([w,gap//2], np.uint8)
            # img = np.concatenate((img,fill), axis = 1)
            # img = np.concatenate((fill, img), axis = 1)
        else:
            gap = h - w
            fill = np.zeros([1,h], np.uint8)
            for i in range(gap//2):
                img = np.concatenate((img,fill), axis = 0)
            for i in range(gap//2):
                img = np.concatenate((fill, img), axis = 0)


        img_new = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)
        img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)

        img_name = os.path.join(out_dir, f.split("\\")[-1])
        cv2.imwrite(img_name, img_new)
        print("handle: ", f.split("\\")[-1])


def crop(img):
    image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_contour = None
    max_area = 0
    for c in contours:
        if cv2.contourArea(c) > max_area:
            max_area = cv2.contourArea(c)
            max_contour = c

    x, y, w, h = cv2.boundingRect(max_contour)
    x -= 10
    y -= 10
    w += 20
    h += 20
    img_new = img[y:y+h, x:x+w]

    return img_new


if __name__ == '__main__':
    dirs = "C:\\Study\\test\\image" 
    out_dir = "C:\\Study\\test\\out_pic" # 存储路径
    tranPic(dirs, out_dir)  
