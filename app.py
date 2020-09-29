from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os

app = Flask(__name__)

line_bot_api = LineBotApi("r4HKt9COHnXG5cE3eX4wNvFH7rHXh6CSTuIJF37YMCPnNIgP9Cnku8T+5BsTXzu0rHQO0MKbQPjJceyic3Z7JFUQ68uJNq4yQe/puz11ZPG16H4d/DZPcSulNi5lOQmzNqp9Zuj4up/fd24XDDdseQdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("cc6705eadfa7b4f1a9ccd67df09ed1b1")

@app.route("/")
def root():
    return 'OK'

@app.route("/callback",methods=['POST'])
def callback():
    sign = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, sign)
    except InvalidSignatureError:
        print("Invalid signature. Check token and/or secret")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print(type(msg))
    msg = msg.encode('utf-8')  
    if event.message.text == "文字":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    elif event.message.text == "貼圖":
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=3, sticker_id=183))
    elif event.message.text == "圖片":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='圖片網址', preview_image_url='圖片網址'))
    elif event.message.text == "影片":
        line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='影片網址', preview_image_url='預覽圖片網址'))
    elif event.message.text == "音訊":
        line_bot_api.reply_message(event.reply_token,AudioSendMessage(original_content_url='音訊網址', duration=100000))
    return 'OK2'
    
    
if __name__ == "__main__":
    app.run()

