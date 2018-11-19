# coding:UTF-8
import cv2
import numpy as np
import DBSCAN

img = cv2.imread("C:\\Study\\test\\1ssssssss\\m-5-6.8.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_m, gray_n = np.shape(gray)
def func(algorithm, par=None):
    algorithms = {
        "SIFT" : cv2.xfeatures2d.SIFT_create(),
        "SURF": cv2.xfeatures2d.SURF_create(float(par) if par else 4000),
        "ORB": cv2.ORB_create()
    }
    return algorithms[algorithm]

f = "SIFT"
alg = func(f)
keypoints, descriptor = alg.detectAndCompute(gray, None)
points2f = cv2.KeyPoint_convert(keypoints) 
# print(points2f)
# print(keypoints)

# dummy = np.zeros(gray.shape)
# for i in points2f:
#   # print(i[0], i[1])
#   cv2.circle(dummy, tuple(i), 2, (51, 163, 236), 1) #33

eps = DBSCAN.epsilon(points2f, 10)
# 3、利用DBSCAN算法进行训练
types, sub_class = DBSCAN.dbscan(points2f, eps, 10)
cluster = {}
# print(np.shape(sub_class))
sub_m, sub_n = np.shape(sub_class)
for i in range(sub_m):
    for j in range(sub_n):
        cluster[sub_class[i, j]] = cluster.get(sub_class[i,j], 1) + sub_class[i,j]
print(cluster)
max_cluster_class,max_total = 0, 0
for k,v in cluster.items():
    if v > max_total:
        max_cluster_class, max_total = k, v

max_cluster = [] # 存储簇类的坐标
print("key_point: ", np.shape(points2f))
for i in range(sub_m):
    for j in range(sub_n):
        # print(sub_class[i, j], max_cluster_class)
        if sub_class[i, j] == max_cluster_class:
            max_cluster.append([int(points2f[j, 0]), int(points2f[j, 1])])


dummy = np.zeros(gray.shape)
for i in max_cluster:
    # print(i[0], i[1])
    cv2.circle(dummy, tuple(i), 3, (255, 255, 255), 2) #33
cv2.imwrite("cluster.png", dummy)


# 根据特征点获得周围像素的值，半径为5
points = []
r = 2
for x in max_cluster:
    i, j = x
    for m in range(i - r, i + r):
        for n in range(j - r, j + r):
            if [m, n] not in points:
                points.append([m, n])

pixel_value = []
for x in points:
    if int(x[0]) >= gray_m or x[1] >= gray_n: continue
    if gray[int(x[0]), int(x[1])] != 0:
        pixel_value.append(gray[int(x[0]), int(x[1])])
pixel_mean = sum(pixel_value) // max_total


print("pixel_mean: ", pixel_mean)
# print(pixel_value)
least_value = sorted(pixel_value)[int(max_total*0.2)]
print("least_value:", least_value)

threshold, thrshed_img = cv2.threshold(gray, least_value, 255, cv2.THRESH_BINARY)

cv2.imwrite("thrshed_img.png", thrshed_img)




# print(dummy.shape)
# img = cv2.drawKeypoints(image=img, outImage=dummy, keypoints=keypoints, color=(51, 163, 236))
# cv2.imshow(f, img)

# # print(dummy.max())max_cluster
# cv2.waitKey()
# cv2.destroyAllWindows()
