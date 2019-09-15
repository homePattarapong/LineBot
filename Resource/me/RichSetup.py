from Project.Chatbot import channel_access_token



import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):

    richId = RegisRich(Rich_json = Richmenu_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())

if __name__ == '__main__':
    Richmenu_json = {
    "size": {
        "width": 2500,
        "height": 843
    },
    "selected": True,
    "name": "Rich Menu 1",
    "chatBarText": "Bulletin",
    "areas": [
        {
        "bounds": {
            "x": 84,
            "y": 68,
            "width": 701,
            "height": 717
        },
        "action": {
            "type": "uri",
            "uri": "https://github.com/Puttipong1234/Line_get_user"
        }
        },
        {
        "bounds": {
            "x": 870,
            "y": 59,
            "width": 760,
            "height": 726
        },
        "action": {
            "type": "postback",
            "text": "",
            "data": "10hrvideo"
        }
        },
        {
        "bounds": {
            "x": 1706,
            "y": 110,
            "width": 760,
            "height": 692
        },
        "action": {
            "type": "postback",
            "text": "",
            "data": "Q&A"
        }
        },
        {
        "bounds": {
            "x": 2103,
            "y": 8,
            "width": 397,
            "height": 89
        },
        "action": {
            "type": "uri",
            "uri": "tel:+66-90-984-6075"
        }
        }
    ]
    }



    CreateRichMenu(ImageFilePath='Resource/richmenu.jpeg',Rich_json=Richmenu_json,channel_access_token=channel_access_token)
    