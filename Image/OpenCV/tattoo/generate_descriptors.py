# 2018-9-8
# 生成匹配描述符文件
import os
import cv2
import numpy as np
import sys
def create(dirpath):
    """
    读取文件使用saveDate函数建立描述符文件
    """
    # file = []
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for f in files:
            path = os.path.join(root, f)
    #         file.append(path)
    # for f in file:
    #     saveData(dirpath, f, "SIFT")
            saveData(dirpath, path)

def saveData(dirpath, file, algorithm="SIFT", par=None):
    """
    创建描述符文件
    """
    algorithms = {
        "SIFT" : cv2.xfeatures2d.SIFT_create(),
        "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
        "ORB": cv2.ORB_create()
    }
    feature_detector = algorithms[algorithm]

    img = cv2.imread(file, 0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kp, des = feature_detector.detectAndCompute(img, None)

    # 描述符目录
    new_folder = "\\".join(dirpath.split("/")[:-1])
    if not new_folder:
        new_folder = "\\".join(dirpath.split("\\")[:-1])
    new_folder += "\\description"
    if not os.path.isdir(new_folder):
        os.makedirs(new_folder)

    # 生成的描述符文件路径
    descriptor_file = os.path.join(new_folder, file.split("\\")[-1].replace("jpg", "npy"))

    np.save(descriptor_file, des)

if __name__ == "__main__":
    dirpath = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\tattoo\\labels"
    create(dirpath)