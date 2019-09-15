import pprint
#import json
from flask import Flask , request
## การเข้าผ่าน ไฟล์ทั่วไป from folder.filename import function
from Resource.wolf import search_wiki

app = Flask(__name__)

#Line Access token
access_token = 'mWqgvXKjtK1PYF26zy+JE4BRDjfRsVGsx+GJxLwHpGpdeCb/iawFLhjM4V8UCxl7cypkvtp4CVqPBsB979BeO9dilNx22+c8QBaDUV+7zMmzIlrDs5YmX6XIarkxXZdu/UeBvf6J6dcu9OjvB+emrQdB04t89/1O/w1cDnyilFU='

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook',methods=['POST','GET'])
def webhook():
    if request.method == 'POST' :
        #pp = pprint.PrettyPrinter(indent=3)
        ### dictionary from line
        data = request.json
        #data_show = pp.pprint(data)
        #pprint(data_show)

        ### extract text from line
        
        

        text_fromline = data['events'][0]['message']['text']
        ## ค้นหาคำจาก wikipedia
        result = search_wiki(text_fromline)
        print(text_fromline)

        ### import function from file reply.py
        from reply import ReplyMessage
        ReplyMessage(Reply_token=data['events'][0]['replyToken'],
        TextMessage=result,
        Line_Access_Token = access_token
        )


        return 'OK'
    elif request.method == 'GET':
        return 'นี่คือหน้าเว็บสำหรับรับ Package'


if __name__ == "__main__":
    app.run(port=2000)
