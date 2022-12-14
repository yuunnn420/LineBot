# TOC Project 2022
Develop a Line bot based on a finite state machine with OpenAI and Google Cloud Vision API

Does not support LINE PC version because of rich menu
## Bot information
* Bot basic ID: @723zdtoa
* QR code

    <img src="./img/QRcode.png" width="500">

* Greeting messages

    <img src="./img/greeting_message.png" width="500">


## Setup
#### Secret Data
You should generate a `./src/.env` file to set Environment Variables refer to `./src/.env.sample`.

You should generate a  `./key.json` file of Google Cloud Keys.

#### Rich Menu
You should generate a rich menu by [req_rich_menu.ipynb](./src/req_rich_menu.ipynb).

#### Run
```sh
python src/app.py
```

## Finite State Machine
![fsm](./img/fsm.png)

## Features
### Rich Menu
* 點選 rich menu: 使用postback直接將data傳到後端
* Rich menu不支援電腦版

<img src="./img/rich_menu.png" width="500">

### Chat
* By OpenAI GPT3 model
* Quick reply: 早安

<img src="./img/chat_1.png" width="500"> 

<img src="./img/chat_2.png" width="500">

### Image Generation
* By OpenAI Image generation
* Quick reply: 有綠色眼睛的黑貓

<img src="./img/image_generation_1.png" width="500">
<img src="./img/image_generation_2.png" width="500">

### Image Reconition
* By Google Cloud Vision API

<img src="./img/image_regconition.png" width="500">

### Sticker Parrot
* user傳送[line官方sticker message](https://developers.line.biz/en/docs/messaging-api/sticker-list/): 回傳相同貼圖
* user傳送**非**line官方sticker message: invalid command

<img src="./img/sticker_parrot.png" width="500">

### Error Handle
#### Invalid Command

<img src="./img/error_1.png" width="500">

#### Reject by OpenAI
> OpenAI拒絕生成敏感圖片

<img src="./img/error_2.png" width="500">

#### Cannot recognize image

<img src="./img/error_3.png" width="500">

## Bonus
* Deploy
    * GCP - Google cloud platform
        * server: [https://lynn.cf](https://lynn.cf)
* Extra functionality or technics
    * Line API
        * Postback Event
        * Sticker Message
        * Image Message
        * Rich Menu
        * Quick Reply
    * image
    * Machine learning
        * OpenAI
        * Google Cloud Vision API
## Reference
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)

[OpenAI](https://openai.com/)

[Google Cloud Vision API](https://cloud.google.com/vision)