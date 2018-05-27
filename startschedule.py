import os
import sys
import logging
from myschedule.model import configlogger
from myschedule.entity import autostart

# 全局参数
g_SysConfig = {}


def GenerateSystemConfig(sysconfig):
    os.path.basename(sys.argv[0])
    # 程序所在目录
    sysconfig['CUR_DIR'] = os.path.dirname(os.path.abspath(__file__))
    # 日志目录
    sysconfig['LOG_DIR'] = os.path.join(sysconfig['CUR_DIR'], 'logs')
    # 数据存放目录
    sysconfig['DATA_DIR'] = os.path.join(sysconfig['CUR_DIR'], 'data')
    # 临时文件目录
    sysconfig['TEMP_DIR'] = os.path.join(sysconfig['CUR_DIR'], 'temp')
    # 检查路径存在
    for value in sysconfig.values():
        if not os.path.exists(value):
            os.makedirs(value)
    # 加载配置文件
    if 'CONFIG_FILE' not in sysconfig:
        sysconfig['CONFIG_FILE'] = os.path.join(
            sysconfig['CUR_DIR'], 'task.json')
    #


if __name__ == '__main__':
    # 获取路径信息
    GenerateSystemConfig(g_SysConfig)
    # 配置日志
    configlogger.ConfigLogger(g_SysConfig['LOG_DIR'])

    logger = logging.getLogger(__file__)
    logger.info("start schedule")
    # 检查开机启动
    starfile = os.path.abspath(__file__)
    autostart.ConfigAutoStart(starfile)
    logger.info("end schedule")
