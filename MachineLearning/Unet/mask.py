# coding:utf-8
# 2019-1-19
# mask

import os
import cv2
import numpy as np

from data_factory import *


def preprocessing(img):
    """
    读预处理图像进行处理
    使用聚类, 阈值判断, 最大连通区域
    Args:
        img : type(mat or array),image
    Returns:
        img : type(mat or array),image
    """
    # 方法一
    # imged = 1
    # img[img > imged] = 1
    # img[img < imged] = 0
    # return img

    # 方法二
    img = img[:,:,0].copy()
    # print(img.shape)
    m, n = img.shape
    r, c = m // 2, n // 2 # 种子起始点
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = []
    queue.append([r, c])
    visited[r][c] = True
    while len(queue) != 0:
        row, col = queue.pop()
        if row > 1 and not visited[row - 1][col] and img[row - 1][col] != 0:
            queue.append([row - 1, col])
            visited[row - 1][col] = True

        if row + 1 < m and not visited[row + 1][col] and img[row + 1][col] != 0:
            queue.append([row + 1, col])
            visited[row + 1][col] = True

        if col - 1 >= 0 and not visited[row][col - 1] and img[row][col - 1] != 0:
            queue.append([row, col -1])
            visited[row][col - 1] = True

        if col + 1 < n and not visited[row][col + 1] and img[row][col + 1] != 0:
            queue.append([row, col + 1])
            visited[row][col + 1] = True  

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                img[i][j] = 0
            else:
                img[i][j] = 1

    image = np.expand_dims(img, axis=2)
    image = np.concatenate((image, image, image), axis=-1)

    return image



def mian(original_pic_dir,
        prediction_pic_dir,
        output_dir,
        mask_ouput_dir,
        img_size=224):
    """
    使用预测的结果对原图像进行处理

    Args:
        original_pic_dir : 经过归一化后原图像路径
        prediction_pic_dir ： 由unet预测保存的图像路径
        output_dir ： 保存图像路径
        mask_output_dir : 预测图像处理后保存目录
        img_size : 输出图像尺寸

    Retures: None
    """
    
    # original_pic = get_files(original_pic_path)
    # original_pic = get_files(original_pic_path)

    pic_name_list = os.listdir(original_pic_dir)

    for k,f in enumerate(pic_name_list):
        print("[INFO] processing %s" % f)
        original_pic_path = os.path.join(original_pic_dir, f)
        prediction_pic_path = os.path.join(prediction_pic_dir, f)

        original_img = cv2.imread(original_pic_path)
        prediction_img = cv2.imread(prediction_pic_path)

        prediction_img = preprocessing(prediction_img) # 暂时未完成

        # mask_img = prediction_img.copy()
        # mask_img[mask_img == 1] = 256
        # mask_img_path = os.path.join(mask_output_dir, f)
        # cv2.imwrite(mask_img_path, mask_img)

        new_img = np.multiply(original_img, prediction_img)
        new_img = cv2.resize(new_img, (img_size, img_size), interpolation=cv2.INTER_LINEAR)

        new_img_path = os.path.join(output_dir, f)
        cv2.imwrite(new_img_path, new_img)


        # test
        # if k == 10:
        #   break




if __name__ == '__main__':
    original_pic_dir = r'D:\deep_learning\unet\100-test_norm'
    prediction_pic_dir = r'D:\deep_learning\unet\image_prediction_test'
    output_dir = r'D:\deep_learning\unet\image_result'
    mask_output_dir = r'D:\deep_learning\unet\image_mask'
    img_size = 224

    mkdir([output_dir, mask_output_dir])

    mian(original_pic_dir,
        prediction_pic_dir,
        output_dir,
        mask_output_dir,
        img_size)