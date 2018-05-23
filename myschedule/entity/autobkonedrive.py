import onedrivesdk
import sys
import os
from onedrivesdk.helpers import GetAuthCodeServer

if __name__ == '__main__':
    # 同级不同目录包导入问题
    curdir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(curdir)
    sys.path.append("../..")
from myschedule.config import onedriveconfig
'''
自动同步备份OneDrive
'''


def ConnectOneDrive():
    client = onedrivesdk.get_default_client(client_id=onedriveconfig.CLIENT_ID,
                                            scopes=onedriveconfig.SCOPES)
    auth_url = client.auth_provider.get_auth_url(onedriveconfig.REDIRECT_URI)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, onedriveconfig.REDIRECT_URI)
    # Finally, authenticate!
    client.auth_provider.authenticate(
        code, onedriveconfig.REDIRECT_URI, onedriveconfig.CLIENT_SECRET)
    # Save the session for later
    client.auth_provider.save_session()

    item_id = "root"
    items = client.item(id=item_id).children.get()
    print("0: UP")
    count = 0
    for count, item in enumerate(items):
        print("{} {}".format(
            count+1, item.name if item.folder is None else "/"+item.name))


if __name__ == '__main__':
    bRet = ConnectOneDrive()
    print(str(bRet))
