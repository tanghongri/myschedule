import os
import logging
from logging.handlers import RotatingFileHandler
'''
配置全局日志
'''


def ConfigLogger(logdir):
    # root
    if not os.path.exists(logdir):
        os.makedirs(logdir)

    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
    rHandler = RotatingFileHandler("log.txt", maxBytes=1*1024)
    rHandler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)
