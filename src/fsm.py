from transitions.extensions import GraphMachine

from utils import *

import os
import io
import openai
from opencc import OpenCC
from google.cloud import vision

# from pychatgpt import Chat, Options, OpenAI
# from revChatGPT.revChatGPT import Chatbot

openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"key.json"
client = vision.ImageAnnotatorClient()

# session_token = os.getenv("SESSION_TOKEN")
# cf_clearance = os.getenv("CF_CLEARANCE"),
# config = {
#     "session_token": session_token,
#     "cf_clearance": cf_clearance,
#     "user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
# chatbot = Chatbot(config, conversation_id=None)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs): 
        self.machine = GraphMachine(model=self, **machine_configs)
        self.cc = OpenCC('s2twp')
        # self.options = Options()
        # # self.options.proxies = ''
        # self.chat = Chat(email=OPENAI_EMAIL, password=OPENAI_PASSWORD, options=self.options)
    
    def is_message(self, event):
        return isinstance(event, MessageEvent)
    
    def is_image(self, event):
        return isinstance(event, MessageEvent) and isinstance(event.message, ImageMessage)

    def is_going_to_ChatGPT(self, event):
        if isinstance(event, PostbackEvent):
            return event.postback.data=="chat"
        else: return 0

    def is_going_to_image_generation(self, event):
        if isinstance(event, PostbackEvent):
            return event.postback.data=="image generatoin"
        else: return 0

    def is_going_to_cloud_vision(self, event):
        if isinstance(event, PostbackEvent):
            return event.postback.data=="cloud vision"
        else: 
            return 0
    
    def on_enter_ChatGPT(self, event):
        print("I'm entering ChatGPT")
        if isinstance(event, MessageEvent):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=event.message.text,
                temperature=0.9,
                max_tokens=999,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )
            print(response)
            res = self.cc.convert(response["choices"][0]["text"])
            print(res)
            print(len(res))
            i = 0
            while res[i] != '\n':
                i += 1
                if i == len(res):
                    break
            if i < len(res):
                res = res[i:].strip()
                if res == '':
                    res = 'meow'
            send_text_message(event.reply_token, res)
            # response = chatbot.get_chat_response(event.message.text, output="text")
            # print(response)
            # send_text_message(event.reply_token, self.cc.convert(response['message']))
            # res = self.chat.ask(event.message.text)
            # print(res)
            # send_text_message(event.reply_token, self.cc.convert(res[0]))
        elif isinstance(event, PostbackEvent):
            quick_reply(event.reply_token, "已啟動聊天模式", '早安')

    def on_enter_image_generation(self, event):
        print("I'm entering image_generation")
        if isinstance(event, MessageEvent):
            try:
                response = openai.Image.create(
                prompt=event.message.text,
                n=1,
                size="256x256"
                )
                image_url = response['data'][0]['url']
                print(image_url)
                send_image_url(event.reply_token ,image_url)
            except openai.error.InvalidRequestError:
                send_sticker(event.reply_token, '789', '10860')
        elif isinstance(event, PostbackEvent):
            quick_reply(event.reply_token, "已啟動影像生成模式", "有綠色眼睛的黑貓")

    def on_enter_cloud_vision(self, event):
        print("I'm entering cloud_vision")
        if isinstance(event, MessageEvent):
            if isinstance(event.message, ImageMessage):  
                save_image(event.message.id)
                with io.open("img/" + event.message.id + ".png", 'rb') as image_file:
                    content = image_file.read()
                image = vision.Image(content=content)
                response = client.label_detection(image=image)
                labels = response.label_annotations
                if labels == []:
                    send_sticker(event.reply_token, '789', '10877')
                else:
                    res = ''
                    flag = 0
                    for label in labels:
                        if(flag):
                            res+='\n'
                        flag = 1
                        res += str(label.description)+" "+"{:.2f}".format(label.score)[2:]+"%"
                    send_text_message(event.reply_token ,res)
                os.remove("img/" + event.message.id + ".png")
        if isinstance(event, PostbackEvent):
            send_text_message(event.reply_token, "已啟動影像辨識模式\n請傳送圖片")
    
    def on_exit_ChatGPT(self, event):
        print("Leaving ChatGPT")

    def on_exit_image_generation(self, event):
        print("Leaving image_generation")

    def on_exit_cloud_vision(self, event):
        print("Leaving cloud_vision")
