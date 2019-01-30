# coding=utf-8
# 2019-1-29
# https://www.cnblogs.com/yyds/p/6901864.html


import logging
import logging.handlers
import datetime
import time

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))


console = logging.StreamHandler()ffffffe 
console.setLevel(logging.DEBUG)
console.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line: %(lineno)d] - %(levelname)s - %(message)s"))


logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(console)

for i in range(10):
	logger.debug('debug message: %s' % i)
	logger.info('info message: %s' % i)
	logger.warning('warning message: %s' % i)
	logger.error('error message: %s' % i)
	logger.critical('critical message: %s' % i)
	time.sleep(1)
