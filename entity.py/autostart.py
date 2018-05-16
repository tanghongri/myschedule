import platform
import logging
'''
配置开机自启动
'''
logger = logging.getLogger(__file__)


def WindowsAutoStart():
    return True


def ConfigAutoStart():
    osname = platform.system()
    if osname == 'Windows':
        return WindowsAutoStart()
    else:
        logger.error("unsupport system: "+osname)
        return False


if __name__ == '__main__':
    bRet = ConfigAutoStart()
    print(str(bRet))
