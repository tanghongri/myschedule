import os
import logging
from model import configlogger


if __name__ == '__main__':
    curdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curdir)
    logdir = os.path.join(curdir, 'logs')
    configlogger.ConfigLogger(logdir)
    logger = logging.getLogger(__file__)
    logger.info("start schedule")