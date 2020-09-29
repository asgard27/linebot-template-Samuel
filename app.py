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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()

