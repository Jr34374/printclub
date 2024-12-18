import netifaces as ni
import psutil
import os
import socket

def get_ip_server() -> list:
    if os.name == "nt":
        # Windows
        return socket.gethostbyname_ex(socket.gethostname())[2]
        pass
    else:
        # それ以外
        result = []
        address_list = psutil.net_if_addrs()
        for nic in address_list.keys():
            ni.ifaddresses(nic)
            try:
                ip = ni.ifaddresses(nic)[ni.AF_INET][0]['addr']
                if ip not in ["127.0.0.1"]:
                    result.append(ip)
            except KeyError as err:
                pass
        return result


# 配列の一番目の要素を取得
def getipv4():
    print(get_ip_server())
    ip_list = get_ip_server()
    
    if ip_list:  # リストが空でないかチェック
        first_ip = ip_list[0]
        print(f"最初のIPアドレス: {first_ip}")
        return first_ip
    else:
        print("IPアドレスが見つかりませんでした")
        

#getipv4()