# coding:utf-8
# 2019-3-17

import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
import datetime
from threading import Thread, Lock
from tool import util
from tool import model as models
from tool import api

# 日志设置
_LOGGER_PATH = ""
logger = util.get_logger(_LOGGER_PATH)
# logger.debug('debug message: %s' % i)
# logger.info('info message: %s' % i)
# logger.warning('warning message: %s' % i)
# logger.error('error message: %s' % i)
# logger.critical('critical message: %s' % i)

fail, success, skip, count, total = 0, 0, 0, 0, 0
start_time = datetime.datetime.now()
lock = Lock()


def _sub_seg(out_dir, pic_path, stack_model, clip):
    global fail, success, skip, count, total
    info = "starting process : %s" % pic_path
    logger.info(info)
    img_dirs = os.path.join(out_dir, pic_path.split("\\")[-1])
    if os.path.isfile(api.getName(img_dirs, "_new")):
        lock.acquire()
        skip += 1
        logger.warning("skip %s"% img_dirs)
        lock.release()
        return 
    try:
        # 读取图片
        img = cv2.imread(pic_path, 0)
        # 切边
        x,w,y,h = clip
        img = img[x:w , y:h]
        # 获得预测值
        hist = api.getHistogram(img)
        _data = util.pre_process(hist)
        lock.acquire()
        thresh_value = stack_model.predict(_data)
        lock.release()
        logger.debug('predict threshold value: %s' % thresh_value)
        # 二值化
        threshold, thrshed_img = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)
        # 使用区域生长法分割
        logger.debug('using region growing to segmentate img')
        img_segement, thresh_img = api.regionGrowing(img, thrshed_img)
        # 保存
        api.saveImage(img_dirs, "_new", img_segement)

        # 去除多余边缘
        logger.debug('remove margin')
        img_remove_margin = api.moveMargin(img_segement, thresh_img)
        api.saveImage(img_dirs, "_remove_margin", img_remove_margin)

        # 扩充为正方形并缩小为256x256
        # logger.debug('call normalization to require size')
        img_new = api.normalization(img_remove_margin)
        api.saveImage(img_dirs, "_new", img_new)
        lock.acquire()
        count += 1
        success += 1
        logger.info("%s/%s done" % (count, total))
    except Exception as e:
        # 错误情况
        lock.acquire()
        api.saveError(e, out_dir, img_dirs, logger)
        fail += 1
    
    lock.release()


def seg(dirs, out_dir, train_data_path, clip):
    """分割主程序
    1. 训练模型
    2. 获取图片
    3. 多线程分割
    """
    global fail, success, skip, count, total
    logger.info("Getting data.")
    _train_raw, _labels = util.get_train_data(train_data_path, 2)
    logger.info("Training data.")
    stack_model = models._test_train_model(_train_raw, _labels)

    
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = api.getFiles(dirs)
    lock.acquire()
    total = len(files)
    lock.release()
    threads = []

    for f in files:
        t = Thread(target=_sub_seg, args=(out_dir, f, stack_model, clip))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


    end_time = datetime.datetime.now()
    expend = end_time - start_time
    logger.info("\n\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


if __name__ == '__main__':
    file_path = r"C:\Study\test\bone\1ssssssss"
    out_dir = r"C:\Study\test\bone\sklearn_test"
    train_data_path = r"C:\Study\test\bone\data.txt"
    clip = (45,-45,45,-45)

    seg(file_path, out_dir, train_data_path, clip)

    file_path = "C:\\Study\\test\\bone\\100-gt" # 标准分割图像目录路径
    out_dir = "C:\\Study\\test\\bone\\est_results_test" # 结果保存目录
    file_path_2 = r"C:\Study\test\bone\sklearn_test" # 方法一得到分割图像路径

    res = api.batchProcess(file_path, file_path_2)
    api.printEst(res, "stack_model", logger)
    api.saveEst(res, "stack_model", out_dir, logger)