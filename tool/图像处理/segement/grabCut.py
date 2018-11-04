# coding:UTF-8
# 2018-11-1
# grabCut
# 前景分割手掌，比较费时

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
        mask = np.zeros(img.shape[:2],np.uint8) # mask
        h, w, _ =  img.shape

        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)

        rect = (int(w * 0.1), int(h * 0.1), int(w * 0.9), int(h * 0.9))

        # print(rect)
        cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        img = img*mask2[:,:,np.newaxis] # np.newaxis = None
        # cv2.imshow("img", img)
        # save
        out = os.path.join(out_dir, os.path.basename(f))
        cv2.imwrite(out, img)
        # break
    # cv2.waitKey()
    # cv2.destroyAllWindows()



if __name__ == '__main__':
    file_path = "C:\\Study\\test\\original"
    out_dir = "C:\\Study\\test\\grabCut"
    process(file_path, out_dir)