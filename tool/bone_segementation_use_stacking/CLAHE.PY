import os
import cv2

def getCLAHE(img):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # 创建ClAHE对象
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    # 限制对比度的自适应阈值均衡化
    dst = clahe.apply(image)
    return dst
path = r"F:\RSNA\boneage-training-dataset"
store_path = r"F:\CLAHE-RSNA"
filename=os.listdir(path)
for i in filename:
    img_path = os.path.join(path, i)
    dst = getCLAHE(img_path)
    store = os.path.join(store_path, i)
    cv2.imwrite(store, dst)
