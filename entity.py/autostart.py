import platform
import logging
import winreg
# 添加搜索路径
import sys
sys.path.append("../myschedule")

'''
配置开机自启动
暂时弃用，由安装脚本控制开机启动
'''
logger = logging.getLogger(__file__)


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
        # key存在，valuename不存在或错误的情况创建
        try:
            key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,
                                   'Software\Microsoft\Windows\CurrentVersion\Run', access=winreg.KEY_WRITE)
            winreg.SetValueEx(key, valuename, 0, winreg.REG_SZ, tarvalue)
        except OSError:
            logger.exception('WindowsAutoStart')
            return False
    return True


def ConfigAutoStart(startpath):
    osname = platform.system()
    if osname == 'Windows':
        return WindowsAutoStart(startpath)
    else:
        logger.error("unsupport system: "+osname)
        return False


if __name__ == '__main__':
    bRet = ConfigAutoStart('test1')
    print(str(bRet))
