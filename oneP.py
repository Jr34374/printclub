import client
import server
import time

n_ch = 'NotReady'
print('接続チェック')
while(True):
    n_ch = input('接続を確認します\n\n準備完了の場合”Ready”と入力してください：')
    if(n_ch == 'Ready'):
        break

ex_pic_name = server()#写真の受け取り

#受け取った写真を表示↓

#写真を撮影


#写真を合成

photo_2 = ''#合成後の写真のファイル名を取得

client(photo_2)#合成後の写真を送信

photo_2 = server()#受け取り待機

#編集
photo_2 = ''#編集後の写真のファイル名を取得

client(photo_2)#送信

#表示
