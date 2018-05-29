'''
测试使用
'''


class testclass(object):
    def __init__(self):
        pass

    def msg_register(self, msgType,
                     isFriendChat=False, isGroupChat=False, isMpChat=False):
        print("before ...")
        print("after ...")

        def _msg_register(fn):
            print("_msg_register")
            return fn
        return _msg_register  


aaa = testclass()

@aaa.msg_register('123')
def func(msg):
    print("func was called")
