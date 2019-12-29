import sys
import os
from flask import Flask, request
import random, json, requests
from src import train_api
from argparse import ArgumentParser

# line用ライブラリ
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
)

app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# LINE APIおよびWebhookの接続
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)



# Flaskのルート設定
@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 「おみくじ」と打つとランダムで運勢が返ってくる
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text == "おみくじ":
        omikuji = random.choice(["大吉", "中吉", "小吉", "吉", "凶", "大凶"])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=omikuji)
        )
    elif event.message.text == "山手線":
        train_info = train_api.get_yamanote_line()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=train_info)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="う〜ん、わかりません")
        )


#------------------------
if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)