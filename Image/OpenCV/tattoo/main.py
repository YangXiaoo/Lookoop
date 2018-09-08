# 2018-9-8
# 标签检测主文件
import os
import cv2
import numpy as np
import sys
def main(descriptor_folder, query_image):
    """
    主文件
    descriptor_folder： 描述符文件目录
    query_image: 查询图片路径
    """
    descriptors = []
    for root, dirs, files in os.walk(descriptor_folder, topdown=False):
        for f in files:
            path = os.path.join(root, f)
            descriptors.append(path)
    print(descriptors)
    query = cv2.imread(query_image, 0)
    feature_detector = algorithm()
    query_kp, query_des = feature_detector.detectAndCompute(query, None)

    # create FLANN matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # minimum number of matches
    MIN_MATCH_COUNT = 10

    potential = {}

    for d in descriptors:
        matches = flann.knnMatch(query_des, np.load(d), k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)
        if len(good) > MIN_MATCH_COUNT:
            print("%s is match(%d)." % ("".join(d.split("\\")[-1].split(".")[0]), len(good)))
        else:
            print("%s is not match" % "".join(d.split("\\")[-1].split(".")[0]))
        potential[d] = len(good)
    max_matches = 0
    potential_object = None
    for i,j in potential.items():
        if j > max_matches:
            max_matches = j
            potential_object = "".join(d.split("\\")[-1].split(".")[0])

    print("potential object is %s" % potential_object)

def algorithm(alg="SIFT", par=None):
    """
    特征检测方法
    """
    algorithms = {
        "SIFT" : cv2.xfeatures2d.SIFT_create(),
        "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
        "ORB": cv2.ORB_create()
    }
    return algorithms[alg]



if __name__ == "__main__":
    descriptor_folder = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\tattoo\\description"
    query_image = "C:\\Study\\github\\Lookoop\\Image\\OpenCV\\image\\manowar_single.jpg"
    main(descriptor_folder, query_image)