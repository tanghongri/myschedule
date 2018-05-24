import sys
import os
import shutil
import onedrivesdk
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
    code = GetAuthCodeServer.get_auth_code(
        auth_url, onedriveconfig.REDIRECT_URI)
    # Finally, authenticate!
    client.auth_provider.authenticate(
        code, onedriveconfig.REDIRECT_URI, onedriveconfig.CLIENT_SECRET)
    # Save the session for later
    # client.auth_provider.save_session()
    return client


def list_changes(client, item_id, token):
    collection_page = client.item(id=item_id).delta(token).get()
    for item in collection_page:
        print(item.name)

    print("TOKEN: {}".format(collection_page.token))


def Download(client, item_id, tardir):
    items = client.item(id=item_id).children.get()

    for item in items:
        if item.folder:
            subdir = os.path.join(tardir, item.name)
            os.makedirs(subdir)
            Download(client, item.id, subdir)
        else:
            client.item(id=item.id).download(os.path.join(tardir, item.name))


def FullBack(client, backdir):
    # 创建临时目录
    Temp_Dir = os.path.join(backdir, 'temp')
    if os.path.exists(Temp_Dir):
        if os.path.isdir(Temp_Dir):
            shutil.rmtree(Temp_Dir)
        else:
            os.remove(Temp_Dir)
    os.makedirs(Temp_Dir)

    item_id = "root"
    Download(client, item_id, Temp_Dir)



    # OneDrive客户端连接
if __name__ == '__main__':
    onedriveclient = ConnectOneDrive()
    item_id = "root"
    token = ''

    list_changes(onedriveclient, item_id, token)
    # 全量备份
    backdir = r'G:\云同步\OneDrive'
    FullBack(onedriveclient, backdir)
