import socket
import os

def client_pic(current_path):#引数は画像のファイル名example.jpg
    # サーバーPCのIPアドレスとポート イーサネット アダプター イーサーネット:ipv4
    HOST = '169.254.78.149'    # 接続したHOSTのIPアドレス

    PORT = 9000

    # 送信するファイル
    file_path = current_path
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # ソケットのセットアップ
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # ファイル名とサイズを送信
    file_info = f"{file_name}|{file_size}"
    client_socket.sendall(file_info.encode())

    # ファイルデータの送信
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            client_socket.sendall(chunk)

    print(f"画像 {file_name} を送信しました ({file_size} バイト)")
    client_socket.close()
    
#client('example.jpg')