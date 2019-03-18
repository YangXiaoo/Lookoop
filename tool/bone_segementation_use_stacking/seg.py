# coding:utf-8
# 2019-3-17

# import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
import datetime
import logging
import pickle
from threading import Thread, Lock

from tool import util
from tool import model as models
from tool import api

# 日志设置
LOGGER_PATH = r"C:\Study\github\Lookoops\tool\bone_segementation_use_stacking\log"
logger = util.get_logger(LOGGER_PATH)
logger.setLevel(logging.DEBUG)   # 设置日志级别，设置INFO时时DEBUG不可见

fail, success, skip, count, total = 0, 0, 0, 0, 0   # 全局变量
start_time = datetime.datetime.now()                # 运行时间
lock = Lock()                                       # 锁


def _seg_test(dirs, out_dir, train_data_path, clip):
    """不使用线程"""
    global fail, success, skip, count, total
    logger.info("Getting data.")
    _train_raw, _labels = util.get_train_data(train_data_path, 2)
    logger.info("Training data.")
    # stack_model = models._test_train_model(_train_raw, _labels) 
    stack_model = models.train_model(_train_raw, _labels)

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = api.getFiles(dirs)
    total = len(files)
    threads = []
    for pic_path in files:
        info = "starting process : %s" % pic_path
        logger.info(info)
        img_dirs = os.path.join(out_dir, pic_path.split("\\")[-1])
        if os.path.isfile(api.getName(img_dirs, "_new")):
            skip += 1
            logger.warning("skip %s"% img_dirs)
            continue
        try:
            # 读取图片
            img = cv2.imread(pic_path, 0)
            # 切边
            x,w,y,h = clip
            img = img[x:w , y:h]
            # 获得预测值
            hist = api.getHistogram(img)
            _data = util.pre_process(hist)
            thresh_value = stack_model.predict(_data)
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
            count += 1
            success += 1
            logger.info("%s/%s done" % (count, total))
        except Exception as e:
            # 错误情况
            api.saveError(e, out_dir, img_dirs, logger)
            fail += 1


def _sub_seg(out_dir, pic_path, stack_model, clip):
    """线程任务"""
    global fail, success, skip, count, total
    info = "starting process : %s" % pic_path
    logger.info(info)
    img_dirs = os.path.join(out_dir, pic_path.split("\\")[-1])
    if os.path.isfile(api.getName(img_dirs, "_new")):
        skip += 1
        logger.warning("skip %s"% img_dirs)
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
        thresh_value = stack_model.predict(_data)
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
        api.saveImage(img_dirs, "_norm", img_new)
        count += 1
        success += 1
        logger.info("%s/%s done" % (count, total))
    except Exception as e:
        # 错误情况
        api.saveError(e, out_dir, img_dirs, logger)
        fail += 1


def seg(dirs, out_dir, train_data_path, clip, retrain=False):
    """分割主程序
    1. 训练模型
    2. 获取图片
    3. 多线程分割
    """
    global fail, success, skip, count, total
    logger.info("Getting data.")
    _train_raw, _labels = util.get_train_data(train_data_path, 2)
    model_save = "./data/pickle_model.dat"

    stack_model = None
    if not os.path.isfile(model_save):
        logger.info("There is no model save in %s, training model" % model_save)
        stack_model = models.train_model(_train_raw, _labels)
        logger.debug("train model time: %s" % str(datetime.datetime.now() - start_time))
        fp = open(model_save, "wb")
        pickle.dump(stack_model, fp)
        fp.close()
    else:
        if retrain:
            logger.info("model save in %s, but you choose to re-train" % model_save)
            stack_model = models.train_model(_train_raw, _labels)
            logger.debug("train model time: %s" % str(datetime.datetime.now() - start_time))
        else:
            logger.info("%s exists, load it." % model_save)
            stack_model = pickle.load(open(model_save,'rb'))

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    files = api.getFiles(dirs)
    total = len(files)
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
    logger.info("\ntotal: %d\nsuccessful: %d\nskip: %d\nfailed: %d\nExpend time: %s" %(total, success, skip, fail, expend))
    os.startfile(out_dir)


if __name__ == '__main__':
    file_path = r"C:\Study\test\bone\100" # r"C:\Study\test\bone\thread_test"
    out_dir = r"C:\Study\test\bone\sklearn"
    train_data_path = r"./data\data.txt"
    clip = (45,-45,45,-45)

    # _seg_test(file_path, out_dir, train_data_path, clip)  # 单线程
    seg(file_path, out_dir, train_data_path, clip)          # 多线程

    file_path = r"C:\Study\test\bone\100-gt"            # 标准分割图像目录路径
    out_dir = "C:\\Study\\test\\bone\\est_results_test" # 结果保存目录
    file_path_2 = r"C:\Study\test\bone\sklearn"         # 得到de分割图像路径
    logger.info("*"*80)
    # 写成类重构
    res = api.batchProcess(file_path, file_path_2, logger)
    api.printEst(res, "stack_model", logger)
    api.saveEst(res, "stack_model", out_dir, logger)