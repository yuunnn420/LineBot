import os
import sys
import json
import requests

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from utils import *
from machine import create_machine

load_dotenv()

# Unique FSM for each user
machines = {}

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
rich_menu_id = os.getenv("RICHMENUID", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route('/')
def hello():
    return 'meow'

# Simple callback endpoint for testing connection
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:

        # Create a machine for new user
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()

        if isinstance(event, MessageEvent):
            if isinstance(event.message, StickerMessage):  
                packageId = json_data['events'][0]['message']['packageId']
                stickerId = json_data['events'][0]['message']['stickerId']   
                send_sticker(event.reply_token, packageId, stickerId)  
                continue
            if machines[event.source.user_id].state=="user": 
                send_sticker(event.reply_token, '789', '10885')  
                continue
            if isinstance(event.message, TextMessage) and isinstance(event.message.text, str) and (machines[event.source.user_id].state=="ChatGPT" or machines[event.source.user_id].state=="image_generation"):
                machines[event.source.user_id].advance(event)
                continue
            elif isinstance(event.message, ImageMessage) and machines[event.source.user_id].state=="cloud_vision":
                machines[event.source.user_id].advance(event)
                continue
            else:
                send_sticker(event.reply_token, '789', '10885')  
                continue
        
        if isinstance(event, PostbackEvent):
            machines[event.source.user_id].advance(event)
            continue

        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
    
    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    fsm = create_machine()
    fsm.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("./fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
