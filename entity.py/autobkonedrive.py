import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
'''
自动同步备份OneDrive
'''
def ConnectOneDrive():
    redirect_uri = "http://localhost:8080/"
    client_secret = "QFNK76~@%vbycgcsUNZ263@"

    client = onedrivesdk.get_default_client(client_id='c8d949d1-04d3-4636-9204-71c8d94f5ef6',
                                            scopes=['wl.signin',
                                                    'wl.offline_access',
                                                    'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    # Block thread until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    # Finally, authenticate!
    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    item_id = "root"
    items = client.item(id=item_id).children.get()
    print("0: UP")
    count = 0
    for count, item in enumerate(items):
        print("{} {}".format(count+1, item.name if item.folder is None else "/"+item.name))


if __name__ == '__main__':
    bRet = ConnectOneDrive()
    print(str(bRet))