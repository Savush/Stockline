'''
上傳圖片
'''
import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = '51c011c2454f727'
client_secret = '3af8801cea206a0d67c3a29bb05f96a28ea5bea5'
album_id = 'tJlat3h'
access_token = 'e6b9901d272bbf15b61632c69251df9922125b11'
refresh_token = '7f6717a78344df17ed1bb0a7dfe4e5c59807d44a'

def showImgur(fileName):
        # 連接imgur
        client= ImgurClient(client_id, client_secret, access_token, refresh_token)
    
        # 連接需要的參數
        config = {
            'album': album_id, # 相簿名稱
            'name': fileName, # 圖片名稱
            'title': fileName, # 圖片標題
            'description': str(datetime.date.today()) # 備註，這邊打日期時間
            }
        
        # 開始上傳檔案
        try:
            print("[log:INFO]Uploading image... ")
            imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
            #string to dict
            print("[log:INFO]Done upload. ")
        except :
            # 如果失敗回傳"失敗"這張圖
            imgurl = 'https://i.imgur.com/RFmkvQX.jpg'
            print("[log:ERROR]Unable upload ! ")
            
        
        return imgurl
