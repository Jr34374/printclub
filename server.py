import socket
import os
import getAddress

def server_check():#通信確認用
    #socketのセットアップ
    current_ip = getAddress.getipv4()

    HOST = current_ip  # サーバーPCのIPアドレス
    PORT = 9000        # 使用するポート番号
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    while(True):
        
        conn, address = sock.accept
        try:
            #リクエスト内容を取得
            req = conn.recv(1024).decode()
            print(f"Connection: {address}")
            print(f"Request: {req}")
            
            #レスポンス
            conn.send(bytes(f"response {address}", 'utf-8'))
        except:
            print("Error")
        finally:
            conn.close()


def server_pic():#returnに写真のファイル名(Path用)
    # サーバーPCのIPアドレスとポート イーサネット アダプター イーサーネット:ipv4
    current_ip = getAddress.getipv4()

    HOST = current_ip  # サーバーPCのIPアドレス
    PORT = 9000        # 使用するポート番号

    # ソケットのセットアップ
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"サーバー起動: {HOST}:{PORT}")
    print("クライアントを待っています...")

    # クライアントの接続を待つ
    conn, addr = server_socket.accept()
    print(f"クライアント接続: {addr}")

    # ファイル名とサイズの受信
    file_info = conn.recv(1024).decode()
    file_name, file_size = file_info.split('|')
    file_size = int(file_size)

    # 画像データの受信
    with open(file_name, 'wb') as f:
        received = 0
        while received < file_size:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
            received += len(data)

    print(f"画像 {file_name} を受信しました ({received} バイト)")
    conn.close()
    server_socket.close()
    return file_name
#server()