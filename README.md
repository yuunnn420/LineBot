# TOC Project 2022
A Line bot based on a finite state machine with openAI and Google Cloud Vision API
> LINE PC version not supported because of rich menu

## Setup
#### Secret Data
You should generate a `./src/.env` file to set Environment Variables refer to `./src/.env.sample`.

You should generate a  `./key.json` file of Google Cloud Keys.

#### Rich Menu
You should generate rich menu by [req_rich_menu.ipynb](./src/req_rich_menu.ipynb).

#### Run
```sh
python src/app.py
```

## Finite State Machine
![fsm](./img/fsm.png)

## Features
### Rich Menu
* 點選 rich menu: 使用postback直接將data傳到後端

<img src="./img/rich_menu.png" width="500">

### Chat
* by openAI GPT3 model
* quick reply: 早安

<img src="./img/chat_1.png" width="500"> 

<img src="./img/chat_2.png" width="500">

### Image Generation
* by openAI Image generation
* quick reply: 有綠色眼睛的黑貓

<img src="./img/image_generation_1.png" width="500">
<img src="./img/image_generation_2.png" width="500">

### Image Reconition
* by Google Cloud Vision API

<img src="./img/image_regconition.png" width="500">

### Sticker Parrot
* 若user傳送[line官方sticker message](https://developers.line.biz/en/docs/messaging-api/sticker-list/) -> 回傳相同貼圖
* 若user傳送**非**line官方sticker message -> invalid command

<img src="./img/sticker_parrot.png" width="500">

### Error Handle
#### Invalid Command

<img src="./img/error_1.png" width="500">

#### Reject by openAI
> openAI拒絕生成敏感圖片

<img src="./img/error_2.png" width="500">


## Reference
[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)

[openAI](https://openai.com/)

[Google Cloud Vision API](https://cloud.google.com/vision)
