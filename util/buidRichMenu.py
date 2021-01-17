#%%
import requests
import json

headers = {"Authorization":"Bearer O9TTZvWLwNwhN3KzcmQfIAUiCzeFRCCxel7SJto/B168OcWNORKFCpxIQCY9mFgV4UXmD6+O74MBfRocYQoiW4MTiymTrTrCAjXbphF+aMlwgCd65o1kH+S3rnnHyee1KJd4p2fpxhcfb6fX+oV9HgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 1200, "height": 405},
    "selected": "true",
    "name": "點選此處以使用功能",
    "chatBarText": "點選此處以使用功能",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 300, "height": 405},
          "action": {"type": "message", "text": "自傳"}
        },
        {
          "bounds": {"x": 300, "y": 0, "width": 300, "height": 405},
          "action": {"type": "message", "text": "作品集"}
        },
        {
          "bounds": {"x": 600, "y": 0, "width": 300, "height": 405},
          "action": {"type": "message", "text": "聯絡方式"}
        },
        {
          "bounds": {"x": 900, "y": 0, "width": 300, "height": 405},
          "action": {"type": "message", "text": "MORE"}
        }
    ]
  }


req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                        headers=headers,data=json.dumps(body).encode('utf-8'))

req_data = req.json()

print(req_data['richMenuId'])
id = req_data['richMenuId']
#%%
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('O9TTZvWLwNwhN3KzcmQfIAUiCzeFRCCxel7SJto/B168OcWNORKFCpxIQCY9mFgV4UXmD6+O74MBfRocYQoiW4MTiymTrTrCAjXbphF+aMlwgCd65o1kH+S3rnnHyee1KJd4p2fpxhcfb6fX+oV9HgdB04t89/1O/w1cDnyilFU=')

with open("new_richM.png", 'rb') as f:
    line_bot_api.set_rich_menu_image(id, "image/png", f)

import requests

headers = {"Authorization":"Bearer O9TTZvWLwNwhN3KzcmQfIAUiCzeFRCCxel7SJto/B168OcWNORKFCpxIQCY9mFgV4UXmD6+O74MBfRocYQoiW4MTiymTrTrCAjXbphF+aMlwgCd65o1kH+S3rnnHyee1KJd4p2fpxhcfb6fX+oV9HgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json","Content-Type":"application/json"}

req = requests.request('POST', ' https://api.line.me/v2/bot/user/all/richmenu/richmenu-f6e8f227c406b8f63344b851ba91c5b8', 
                       headers=headers)

print(req.text)


# %%
headers = {"Authorization":"Bearer O9TTZvWLwNwhN3KzcmQfIAUiCzeFRCCxel7SJto/B168OcWNORKFCpxIQCY9mFgV4UXmD6+O74MBfRocYQoiW4MTiymTrTrCAjXbphF+aMlwgCd65o1kH+S3rnnHyee1KJd4p2fpxhcfb6fX+oV9HgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json","Content-Type":"application/json"}
req = requests.request('POST', ' https://api.line.me/v2/bot/user/' + 'U2649922b5604a80e08b0f9dba91f9029' + '/richmenu/' + 'richmenu-0a9ab22894face43826ff3b3a67babcc', 
                        headers=headers)

# %%
headers = {"Authorization":"Bearer O9TTZvWLwNwhN3KzcmQfIAUiCzeFRCCxel7SJto/B168OcWNORKFCpxIQCY9mFgV4UXmD6+O74MBfRocYQoiW4MTiymTrTrCAjXbphF+aMlwgCd65o1kH+S3rnnHyee1KJd4p2fpxhcfb6fX+oV9HgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json","Content-Type":"application/json"}

req = requests.request('POST', ' https://api.line.me/v2/bot/user/all/richmenu/richmenu-4757251da9425e3eda6c531f4ff41b45', 
                       headers=headers)
# %%
line_bot_api.delete_rich_menu('richmenu-4757251da9425e3eda6c531f4ff41b45')
# %%
rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)
# %%
