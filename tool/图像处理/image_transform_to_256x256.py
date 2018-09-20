# 2018-9-18
# update: 2018-8-20
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

    total = len(files)
    fail = 0
    success = 0

    for f in files:
        try:
            img = cv2.imread(f, 0)
            old_size = img.shape
            w, h = img.shape
            if iscrop:
                img, w, h = crop(img, (w, h))
                if (h, w) == old_size: # 若没有找到轮廓则跳过
                    print(xxxxxx)
            else:
                # 默认不裁剪时若遇到长宽大于2的图形自动裁剪
                if w//h > 2:
                    img, w, h = crop(img, (w, h))
                    if (h, w) == old_size:
                        print(xxxxxx)
                        
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

            img_name = os.path.join(out_dir, f.split("\\")[-1])
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


def crop(img, size):
    img_w, img_h = size
    image, contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    max_contour = None
    max_area = 0
    for c in contours:
        if cv2.contourArea(c) > max_area:
            max_area = cv2.contourArea(c)
            max_contour = c

    x, y, w, h = cv2.boundingRect(max_contour)
    if x >= 10 and y >= 10 and x+w <= img_w and y+h <= img_h:
        x -= 10
        y -= 10
        w += 20
        h += 20
    img_new = img[y:y+h, x:x+w]
    # print(x,y,w,h, img_new.shape, "----- old img: ", img_w, img_h)
    return img_new, img_new.shape[1], img_new.shape[0]


if __name__ == '__main__':
    # dirs = "C:\\Study\\ImageHandle\\fail_to_trans\\fail\\" 
    dirs = "C:\\Study\\test\\image"
    # dirs = "C:\\Study\\test\\failed"
    out_dir = "C:\\Study\\test\\out_pic" # 存储路径
    tranPic(dirs, out_dir)  
