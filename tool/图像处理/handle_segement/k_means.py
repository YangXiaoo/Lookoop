# coding:UTF-8
# 2018-11-20
from sklearn.cluster import KMeans
import numpy as np
import PIL.Image as image


def loadData(filePath):
    f = open(filePath, 'rb')
    data = []
    img = image.open(f) #PIL.Image.open(图片路径）
    m, n = img.size
    for i in range(m):
        for j in range(n):
            x,y,z = img.getpixel((i, j)) #过去每个像素点的rgb值
            data.append([x/256.0, y/256.0,z/256.0])#将其归一化

    f.close()
    return np.mat(data), m, n

imgData, row, col  = loadData("C:\\Study\\test\\1ssssssss\\m-5-6.8.png")
km = KMeans(n_clusters=2)
label = km.fit_predict(imgData)
label = label.reshape([row, col]) #细节

pic_new = image.new("L", (row, col))

for i in range(row):
    for j in range(col):
        pic_new.putpixel((i, j),int(256/(label[i][j] + 1))) #填充每个点的灰度值

print(row, col)
print(pic_new)
pic_new.save("gg.jpg", "JPEG")
