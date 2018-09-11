# 2018-9-10
# 函数
import cv2
import numpy as np

def resize(img, scale_factor):
    """
    缩小图像尺寸
    """
    return cv2.resize(img, (int(img.shape[1] * (1 / scale_factor)), int(img.shape[0] * (1 / scale_factor))), interpolation=cv2.INTER_AREA)


def pyramid(image, scale=1.5, min_size=(200, 80)):
    """
    图像金字塔
    """
    yield image

    while True:
        image = resize(image, scale)
        if image.shape[0] < min_size[1] or image.shape[1] < min_size[0]:
            break

    yield image



def slidingWindow(image, step, window_size):
    """
    滑动窗口
    """
    for y in range(0, image.shape[0], step):
        for x in range(0, image.shape[1], step):
            yield (x, y, image[y : y + window_size[1], x : x + window_size[0]])



def nonMaxSuppressionFast(boxes, overlapThresh):
    """
    非最大抑制。
    图像中可能包含被检测多次的对象, 若将这些检测作为结果则不准确, 这时需要采取非最大抑制来解决。

    思路：
    对输入矩形按评分排序， 从最高的矩阵开始，消除所有重叠超过一定阈值的矩形，消除规则是计算相交区域，并看这些相交区域是否大于某一阈值。
    """
    if len(boxes) == 0:
        return []

    # numpy.dtype.kind
    # A character code (one of ‘biufcmMOSUV’) identifying the general kind of data.
    # b boolean
    # i signed integer
    # u unsigned integer
    # f floating-point
    # c complex floating-point
    # m timedelta
    # M datetime
    # O object
    # S (byte-)string
    # U Unicode
    # V void
    if boxes.dtype.kind == "i":
        # 因为要做除法，所以转换为浮点型
        boxes = boxes.astype("float")


    # 分别获得矩形四个点坐标以及对于评分
    x1 = boxes[ : , 0]
    y1 = boxes[ : , 1]
    x2 = boxes[ : , 2]
    y2 = boxes[ : , 3]  
    scores = boxes[ : , 4]  

    # 获得矩形面积
    area = (x2 - x1 + 1) * (y2 - y1 + 1)

    # 排序评分, 由大到小
    idxs = np.argsort(scores)[::-1]

    pick = [] # 存储符合的矩形

    while len(idxs) > 0:
        last = len(idxs) - 1
        # i = scores.index(idxs[last])
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))
    print("pick:  ",pick)
    return boxes[pick].astype("int")

