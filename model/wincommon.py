'''
Windows下通用方法
'''
import subprocess


def GetExePath(exename):
    #获取命令绝对路径
    # 返回 exitcode, output
    return subprocess.getstatusoutput('where ' + exename)


if __name__ == '__main__':
    exitcode, output = GetExePath('python')
    if exitcode:
        print('[ERROR]')
    else:
        print('[SUCESS]')
    print(str(exitcode))
    print(str(output))
