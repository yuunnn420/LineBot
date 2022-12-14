# TOC Project 2022
A Line bot based on a finite state machine with openAI and Google Cloud Vision API
> LINE PC version not supported because of rich menu

## Setup
#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### Run the sever
```sh
python src/app.py
```

## Finite State Machine
![fsm](./img/fsm.png)

## Features
### rich menu
* 點選 rich menu: 使用postback直接將data傳到後端
* ![rich_menu](./img/rich_menu.png)
### chat
* by openAI GPT3 model
* quick reply: 早安
![chat_1](./img/chat_1.png)
![chat_2](./img/chat_2.png)
### image generation
* by openAI Image generation
* quick reply: 有綠色眼睛的黑貓
![image_generation_1](./img/image_generation_1.png)
![image_generation_2](./img/image_generation_2.png)
### image reconition
* by Google Cloud Vision API
![image_reconition](./img/image_reconition.png)
## Reference
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)