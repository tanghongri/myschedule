import platform
import logging
import os
# 添加搜索路径
import sys



if sys.version_info[0] == 3:
    import winreg as winreg
else:
    import _winreg as winreg

'''
配置开机自启动
暂时弃用，由安装脚本控制开机启动
'''
logger = logging.getLogger(__file__)


def WindowsCreateAutoStart(valuename, value):
    if windowsuac.is_admin():
        # key存在，valuename不存在或错误的情况创建
        try:
            key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,
                                   'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_WRITE)
            winreg.SetValueEx(key, valuename, 0, winreg.REG_SZ, value)
        except OSError:
            logger.exception('WindowsAutoStart')
            return False
        pass
    else:
        logger.error('need administrative privileges')
        windowsuac.Pass_Uac(os.path.realpath(__file__) + ' ' + value)
    return True


def WindowsAutoStart(tarvalue, valuename='myschedule1'):
    # 检查注册表启动项是否存在
    key = None
    vlaue = None
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,
                               'Software\Microsoft\Windows\CurrentVersion\Run')
    except OSError:
        logger.exception('WindowsAutoStart')
        return False
    try:
        vlaue, type = winreg.QueryValueEx(key, valuename)
        if type != winreg.REG_SZ or vlaue != tarvalue:
            vlaue = None
    except OSError:
        pass
    if vlaue == None:
        return WindowsCreateAutoStart(valuename, tarvalue)
    return True


def ConfigAutoStart(startpath):
    osname = platform.system()
    if osname == 'Windows':
        return WindowsAutoStart(startpath)
    else:
        logger.error("unsupport system: "+osname)
        return False


if __name__ == '__main__':
    curdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curdir)
    sys.path.append("..")
    from model import windowsuac
    argc = len(sys.argv)
    if argc == 2:
        ConfigAutoStart(sys.argv[1])
    else:
        bRet = ConfigAutoStart('test1')
        print(str(bRet))
