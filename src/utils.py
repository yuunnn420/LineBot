import os
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import *

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

free_packageIds = ['446', '789', '1070', '6136', '6325', '6359', '6362', '6370', '6632', '8515', '8522', '8525', '11537', '11538', '11539']

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    
    return "OK" 

def send_image_url(reply_token, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def quick_reply(reply_token, text, label):
    line_bot_api.reply_message(reply_token,
    TextSendMessage(
        text=text,
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label=label, text=label)
                )])))

def send_sticker(reply_token, packageId, stickerId):
    if packageId not in free_packageIds:
        packageId = '789'
        stickerId = '10885'
    sticker_message = StickerSendMessage(sticker_id=stickerId, package_id=packageId)
    line_bot_api.reply_message(reply_token, sticker_message) 

def save_image(id):
    send_image = line_bot_api.get_message_content(id)
    path = 'img/' + id + '.png'
    with open(path, 'wb') as fd:
        for chenk in send_image.iter_content():
            fd.write(chenk)
"""
def send_button_message(id, text, buttons):
    pass
"""
