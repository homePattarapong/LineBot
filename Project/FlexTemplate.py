flexdata = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://scontent.fbkk5-5.fna.fbcdn.net/v/t1.0-9/70042096_1324815221024878_7944924465140334592_n.jpg?_nc_cat=100&_nc_oc=AQlkIPthYqlSsrH2XJF_21rG9QqqKxmuQnrvLLcQQtPrX7Q5ppVDKrXkX8reS0r5hVM&_nc_ht=scontent.fbkk5-5.fna&oh=864d5c7da18dda82fe8cfe285fe99e36&oe=5E013C54",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "ตอนที่ 1",
              "size": "xxl",
              "align": "start",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "บอทดึงราคาหุ้น/ข้อมูลจากเว็บ",
              "size": "md",
              "weight": "regular",
              "color": "#AFAFAF",
              "wrap": True
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ดูวิดิโอ",
                "uri": "https://www.facebook.com/UncleEngineer/"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "SOURCE CODE",
                "uri": "https://www.facebook.com/UncleEngineer/"
              }
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://scontent.fbkk5-5.fna.fbcdn.net/v/t1.0-9/70042096_1324815221024878_7944924465140334592_n.jpg?_nc_cat=100&_nc_oc=AQlkIPthYqlSsrH2XJF_21rG9QqqKxmuQnrvLLcQQtPrX7Q5ppVDKrXkX8reS0r5hVM&_nc_ht=scontent.fbkk5-5.fna&oh=864d5c7da18dda82fe8cfe285fe99e36&oe=5E013C54",
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover"
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": "ตอนที่ 2",
              "size": "xxl",
              "align": "start",
              "weight": "bold"
            },
            {
              "type": "text",
              "text": "บอทขายของ/ปิดการขายอัตโนมัติ",
              "size": "md",
              "weight": "regular",
              "color": "#AFAFAF",
              "wrap": True
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "ดูวิดิโอ",
                "uri": "https://www.facebook.com/UncleEngineer/"
              },
              "style": "primary"
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "SOURCE CODE",
                "uri": "https://www.facebook.com/UncleEngineer/"
              }
            }
          ]
        }
      },
      {
        "type": "bubble",
        "body": {
          "type": "box",
          "layout": "vertical",
          "spacing": "sm",
          "contents": [
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "Coming Soon",
                "uri": "https://www.facebook.com/UncleEngineer/"
              },
              "flex": 1,
              "gravity": "center"
            }
          ]
        }
      }
    ]
  }
}

import json , requests

def SetMenuMessage_Object(Message_data,Quick_Reply = False):
    file_data = {"replyToken":'', "messages": []}
    data = file_data['messages'].append(Message_data)
    return file_data

def send_flex(reply_token,file_data,bot_access_key):
    
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(bot_access_key)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization}

    file_data['replyToken'] = reply_token
    #### dumps file จาก dict ให้เป็น json
    file_data = json.dumps(file_data)
    r = requests.post(LINE_API, headers=headers, data=file_data) # ส่งข้อมูล

    return 200