import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
# 添加搜索路径
import sys
sys.path.append("../myschedule")
import config
'''
自动同步备份OneDrive
'''


def ConnectOneDrive():
    client = onedrivesdk.get_default_client(client_id=config.CLIENT_ID,
                                            scopes=config.SCOPES)
    auth_url = client.auth_provider.get_auth_url(config.REDIRECT_URI)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, config.REDIRECT_URI)
    # Finally, authenticate!
    client.auth_provider.authenticate(code, config.REDIRECT_URI, config.CLIENT_SECRET)
    # Save the session for later
    client.auth_provider.save_session()

    item_id = "root"
    items = client.item(id=item_id).children.get()
    print("0: UP")
    count = 0
    for count, item in enumerate(items):
        print("{} {}".format(count+1, item.name if item.folder is None else "/"+item.name))


if __name__ == '__main__':
    bRet = ConnectOneDrive()
    print(str(bRet))
