import client
import server
import datetime

n_ch = 'NotReady'
print('接続チェック')
while(True):
    n_ch = input('接続を確認します\n\n1P\n\nが準備完了の場合”Ready”と入力してください：')
    if(n_ch == 'Ready'):
        break
#以下で接続チェック
    #dt_now = datetime.datetime.now()
    #path_add = dt_now.strftime('%Y%m%d%H%M%S')
    #path1 = '/Users/itoso/Desktop/codes/zemi/example.jpg' #追加した画像のパスをrename追加→送信 この時時間をclientのパスにも指定
    #path_curr = '/Users/itoso/Desktop/codes/zemi/example' + path_add + '.jpg'
    #os.rename(path1, path_curr)
    #photo_name = 'example'
#以上

#写真を撮影↓
photo_1 = ''#写真を保存した際のファイル名を取得
#以上

client(photo_1)#撮影した写真を送信
photo_1 = server()#受け取り待機

#編集↓
photo_1 = '' #編集後のファイル名を取得
#以上

client(photo_1) #送信
photo_1 = server()#受け取り待機

#表示
#以上