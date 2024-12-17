import client
import server

n_ch = 'NotReady'
print('接続チェック')
while(True):
    n_ch = input('接続を確認します\n\n1P\n\nが準備完了の場合”Ready”と入力してください：')
    if(n_ch == 'Ready'):
        break
    
#接続チェック↓
if __name__ == '__main__':
    for i in range(10):
        client.client_check(f"Request: {i}")


#写真を撮影↓
photo_1 = ''#写真を保存した際のファイル名を取得
#以上

client.client_pic(photo_1)#撮影した写真を送信
photo_1 = server.server_pic()#受け取り待機

#編集↓
photo_1 = '' #編集後のファイル名を取得
#以上

client.client_pic(photo_1) #送信
photo_1 = server. server_pic()#受け取り待機

#表示

#以上
