# LINE BOT

## SETUP

### credentials.jsonに `user_id`, `channel_secret` および `channel_access_token` を入力する
- 各種credntialsはLINE Developersのチャネル基本設定およびMessaging API設定を参照

## HOW TO USE

### 1-messagingAPI.ipynb    
#### メッセージを送信するだけのノートブック

1. 最上位セルの `!pip install line-bot-sdk` を実行しライブラリをインストール
    - このセルは1度実行すれば今後する必要はない
1. ライブラリをインポートし、LINE BOT APIにアクセス
1. Send Messageのセルを実行
    - 変数textの値を送信
1. Send Stampのセルを実行
    - スタンプ送信
1. Send Mapのセルを実行
    - 地図を送信
1. Get user profile
    - ユーザーのプロフィールを取得
1. Get followers
    - フォロワーの数を取得

### 2-returnMessage.ipynb
1. `Setup`以下の2つのセルを実行
    - ライブラリのインポートとcredentilasの取得
1. オウム返しセルを実行
    - ブラウザ上で `http://127.0.0.1:5000/`にアクセスし、 `hello world!`と表示されるのを確認
1. ターミナル上でngrokを起動する
    ```shell
    ngrok http 5000
    ```
1. 以下のような結果が返ってくるので、Forwardingの前部分（下記の例では `http://7c4d4d83.ngrok.io`)をコピーする
    ```shell
    ngrok by @inconshreveable                                                                        (Ctrl+C to quit)

    Session Status                online                                                                                              
    Session Expires               7 hours, 58 minutes                                                                                 
    Version                       2.3.34                                                                                              
    Region                        United States (us)                                                                                  
    Web Interface                 http://127.0.0.1:4040                                                                               
    Forwarding                    http://7c4d4d83.ngrok.io -> http://localhost:5000                                                   
    Forwarding                    https://7c4d4d83.ngrok.io -> http://localhost:5000                                                  

    Connections                   ttl     opn     rt1     rt5     p50     p90                                                         
                                  0       0       0.00    0.00    0.00    0.00   
    ```
1. LINE Developersのチャネルの基本設定画面で、Webhook URLに先ほどコピーしたURL (`http://7c4d4d83.ngrok.io`) + `/callback`を指定する
    <img width="1421" alt="image.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/490709/f4dd7429-4d8b-7edc-04fa-c185406961ad.png">

    - もしWebhook送信の設定が「利用しない」になっている場合は、「利用する」に編集
1. LINEでメッセージを送信し、オウム返しされることを確認する
    - もしできなかったら、別ターミナルを開きで下記コマンドで、ローカルサーバーを起動し、再度試してみてください
        ```shell
        python -m http.server 5000
        ```
1. LINEからメッセージを送信
    - 基本的にメッセージがそのまま返ってくる
    - 「おはよう」と送ると、「おはようございます」と返ってくる
    - 「スタンプ」と送ると、スタンプが送られてくる

### 3-omikuji.ipynb
1. 上記と同じように、全セルを実行し&ngrokを起動する
1. LINE上で「おみくじ」と送ると、ランダムで運勢が返ってくる

## CHALLENGE
### `src/`にいくつかソースコードを置いてあるので実装してみてください
- train_api.py/train_api.ipynb
    - 電車の運行情報をゲットするコード
    - `get_yamanote_line()`を呼び出すと山手線の運行情報がリアルタイムでゲットできる
- weather_api.py/weather_api.ipynb
    - 天気の情報をゲットするコード
    - `get_weather()`を呼び出すとその日の天気予報がゲットできる

#### train_apiを使用した実装例
1. `2-returnMessage.ipynb`もしくは`3-omikuji.ipynb`を複製
1. ライブラリのインポートとcredentialsの取得セルを実行
1. 新規セルを追加
1. `train_api.ipynb`内の`get_yamanote_line()`のセルをコピーする、もしくは`from src import train_api`を実行して`train_api.py`を呼び出して実行
1. LINE BOTを実装するセルの`def handle_message(event)`内に以下のように記述
    ```
    def handle_message(event):
        if event.message.text == "山手線":
        
            #ipynbファイルのセルをコピーして実行した場合
            train_info = get_yamanote_line()
            #        or
            #pythonファイルをimportした場合
            train_info = train_api.get_yamanote_line()

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=train_info)
            )
        else:
           ...
    ```
1. ngrok起動してLINEで「山手線」とメッセージを送る
    - 山手線の運行情報が返ってくる

\* **weather_apiを使用する場合は、https://openweathermap.org/ のアカウント登録が必要です**

## LIBRARY
- line-bot-sdk:
    - PythonでLINE Messaging APIを使用するためのSDK(ソフトウェア開発キット）
    - https://pypi.org/project/line-bot-sdk/
    - https://github.com/line/line-bot-sdk-python
- flask:
    - Python用の軽量なWebアプリケーションフレームワーク
    - WebサイトやWebアプリケーションを作るための機能を提供する
    - https://pypi.org/project/Flask/
    - https://a2c.bitbucket.io/flask/
- requests:
    - PythonのHTTP通信ライブラリ
    - Webサイトの情報取得や画像の収集などを行うことができる
    - https://requests-docs-ja.readthedocs.io/en/latest/
- pandas:
    - Pythonでデータ解析を行うための機能を持ったライブラリで、数表や時系列データを操作するためのデータ構造を作ったり演算を行うことができる
    - https://pypi.org/project/pandas/
    - https://pandas.pydata.org/pandas-docs/stable/
