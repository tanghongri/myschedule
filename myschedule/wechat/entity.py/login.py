import itchat
from itchat.content import *
'''
微信登陆
'''


newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')


@newInstance.msg_register(TEXT)
def reply(msg):
    return msg.text


newInstance.run()


def WechatLogin():
    pass
