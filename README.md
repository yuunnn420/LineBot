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

<img src="./img/rich_menu.png" width="500">

### chat
* by openAI GPT3 model
* quick reply: 早安

<img src="./img/chat_1.png" width="500"> 

<img src="./img/chat_2.png" width="500">

### image generation
* by openAI Image generation
* quick reply: 有綠色眼睛的黑貓

<img src="./img/image_generation_1.png" width="500">
<img src="./img/image_generation_2.png" width="500">

### image reconition
* by Google Cloud Vision API

<img src="./img/image_regconition.png" width="500">

## Reference
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
