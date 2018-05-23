import os
import logging
from myschedule.model import configlogger
from myschedule.entity import autostart

if __name__ == '__main__':
    curdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curdir)
    # 配置日志
    logdir = os.path.join(curdir, 'logs')
    configlogger.ConfigLogger(logdir)

    logger = logging.getLogger(__file__)
    logger.info("start schedule")
    # 检查开机启动
    starfile = os.path.abspath(__file__)
    autostart.ConfigAutoStart(starfile)
    logger.info("end schedule")
