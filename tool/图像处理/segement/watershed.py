# coding:UTF-8
# 2018-11-1
# watershed
# 分水岭算法

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
        img = cv2.imread(f)
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
        # cv2.imshow("img", img)
        # save
        out = os.path.join(out_dir, os.path.basename(f))
        cv2.imwrite(out, img)
        # break
    # cv2.waitKey()
    # cv2.destroyAllWindows()



if __name__ == '__main__':
    file_path = "C:\\Study\\test\\original"
    out_dir = "C:\\Study\\test\\watershed"
    process(file_path, out_dir)