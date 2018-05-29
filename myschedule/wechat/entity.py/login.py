import itchat
import json
import os
from itchat.content import *
'''
微信登陆
'''
newInstance = itchat.new_instance()
# qr码保持位置
picDir = ''


@newInstance.msg_register(TEXT)
def reply(msg):
    print(str(msg.text))
    return msg.text


def qrCallback(uuid, status, qrcode):
    global picDir
    if picDir:
        with open(picDir, 'wb') as f:
            f.write(qrcode)


def loginCallback():
    global picDir
    if picDir:
        if os.path.exists(picDir):
            os.remove(picDir)


def exitCallback():
    pass


def WechatLogin(sysconfig, name):
    if 'wechat_statusStorageDir' in sysconfig:
        statusStorageDir = sysconfig['wechat_statusStorageDir']
        if not os.path.exists(statusStorageDir):
            os.makedirs(statusStorageDir)
        # statusStorageDir实际为文件
        statusStorageDir = statusStorageDir + '/' + name + '.pkl'
    global picDir
    if 'wechat_picDir' in sysconfig:
        picDir = sysconfig['wechat_picDir']
        if not os.path.exists(picDir):
            os.makedirs(picDir)
        picDir = picDir + '/' + name + '.png'
    newInstance.auto_login(
        hotReload=True, statusStorageDir=statusStorageDir, qrCallback=qrCallback, loginCallback=loginCallback, exitCallback=exitCallback)
    newInstance.run()


if __name__ == '__main__':
    sysconfig = {'wechat_picDir': r'F:\myschedule\temp\wechat\onedrive',
                 'wechat_statusStorageDir': r'F:\myschedule\temp\wechat\status'}
    with open(r'F:\myschedule\task.json', 'r') as jsonfile:
        taskjosn = json.load(jsonfile)
        for task in taskjosn:
            if task['model'] != 'wechat':
                continue
            for operation in task['operations']:
                if operation['action'] == 'login':
                    WechatLogin(sysconfig, task['taskname'])
