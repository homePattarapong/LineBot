import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = 'bcc904f365ae3e31da515cd0c8b56094'
channel_access_token = 'mWqgvXKjtK1PYF26zy+JE4BRDjfRsVGsx+GJxLwHpGpdeCb/iawFLhjM4V8UCxl7cypkvtp4CVqPBsB979BeO9dilNx22+c8QBaDUV+7zMmzIlrDs5YmX6XIarkxXZdu/UeBvf6J6dcu9OjvB+emrQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature'] #check ว่ามาจาก Line รึเปล่า

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent,message=TextMessage)  #Decerator?
def message_text(event):

    Reply_token = event.reply_token ### reply token
    text_fromUser = event.message.text ## message from user

    #################### 1
    # Text_tosend1 = TextSendMessage(text='uncle engineer 01',quick_reply=None)
    # Text_tosend2 = TextSendMessage(text='uncle engineer 02',quick_reply=None)
   
    # image_message = ImageSendMessage(
    #     original_content_url='https://cdn.majorcineplex.com/uploads/movie/2686/thumb_2686.jpg',
    #     preview_image_url='https://www.logolynx.com/images/logolynx/04/04788b7d8705912db91b77cedfb16073.jpeg'
    # )
    # sticker_message = StickerSendMessage(
    #   package_id='1',
    #   sticker_id='1'
    # )

    # line_bot_api.reply_message(
    #     Reply_token,
    #     messages = [Text_tosend1,Text_tosend2,sticker_message,image_message]
    # )

    #################### 2
    # if 'price' in text_fromUser:
    #     from Resource.bxAPI import GetBxPrice
    #     price = GetBxPrice()
    #     text_tosend = TextSendMessage(text=str(price))
    #     line_bot_api.reply_message(Reply_token,text_tosend)


    #################### 3
    if 'เช็คราคา' in text_fromUser:
        from Resource.bxAPI import GetBxPrice
        from random import randint
        num = randint(1,10)
        data = GetBxPrice(num) ## เก็บจำนวนข้อมูล

        from Resource.FlexMessage import setbubble , setCarousel

        flex = setCarousel(data)

        from Resource.reply import SetMenuMessage_Object , send_flex

        flex = SetMenuMessage_Object(flex)
        
        send_flex(Reply_token,file_data=flex,bot_access_key=channel_access_token)
    
    else:
        text_list = [
            'ฉันไม่เข้าใจที่คุณพูด กรุณาลองใหม่อีกครั้งค่ะ',
            'ขออภัย ฉันไม่เข้าใจจริงๆค่ะ ลองใหม่อีกครั้งนะค่ะ',
            'ขอโทษค่ะ ไม่ทราบว่า มีความหมายอย่างไรค่ะ',
            'กรุณาลองพิมพ์ใหม่ได้ไหมค่ะ'
        ]

        from random import choice
        text_data = choice(text_list)
        text = TextSendMessage(text=text_data)
        line_bot_api.reply_message(Reply_token,text)


@handler.add(FollowEvent)
def RegisRichmenu(event):
    userid = event.source.user_id
    disname = line_bot_api.get_profile(user_id=userid).display_name
    
    button_1 = QuickReplyButton(action=MessageAction(label='เช็คราคา',text='เช็คราคา'))
    button_2 = QuickReplyButton(action=MessageAction(label='เช็คข่าวสาร',text='เช็คข่าวสาร'))

    qbtn = QuickReply(items=[button_1,button_2])

    text = TextSendMessage(text='สวัสดีคุณ {} ยินดีต้องรับสู่บริการแชทบอท'.format(disname))
    text_2 = TextSendMessage(text='กรุณาเลือกเมนูที่ท่านต้องการ',quick_reply=qbtn)

    ## link richmenu
    line_bot_api.link_rich_menu_to_user(userid,'richmenu-92038dcd8b9f40190587bd269f031da2')
    ## reply message when user 
    line_bot_api.reply_message(event.reply_token,messages=[text,text_2])



#    print(Reply_token)
#    print(event.message.text)
    



if __name__ == "__main__":
    app.run(port=2000)
