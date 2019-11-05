# coding:utf-8
import os
import logging
import logging.handlers
import datetime
import time

def getLogger(logger_path):
    """设置日志"""
    if logger_path:
        mkdirs(logger_path)
        
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    all_log = os.path.join(logger_path, "all.log")
    error_log = os.path.join(logger_path, "error.log")


    rf_handler = logging.handlers.TimedRotatingFileHandler(all_log, when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    f_handler = logging.FileHandler(error_log)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s - [%(levelname)s] %(message)s"))

    logger.addHandler(rf_handler)
    logger.addHandler(f_handler)
    logger.addHandler(console)

    return logger