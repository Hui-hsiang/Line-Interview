# Line Bot
from flask import Flask, request, abort, render_template
from urllib.request import urlopen
from config import line_channel_access_token, line_channel_secret
from datetime import date
#from oauth2client.service_account import ServiceAccountCredentials
from enum import Enum
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
import random
import requests
import json
################################

from linebot.models import *



app = Flask(__name__)

class states(Enum):
    START = 0
    QUSTION = 1
    DIV = 2
    UNLOGIN = 3
    LOGIN = 4
    PETSQUSTION = 5
class User():
    def __init__(self, id):
        self.user_id = id
        self.state = states.START.value
        self.quastionCount = 0
        self.div_id = 0
        self.identity = 0
        self.name =""
        self.score = 0


def welcome_flex():
    
    content = [
        {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://i.imgur.com/jUSHZll.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
            },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "黃暉翔",
                "color": "#4969c3",
                "weight": "bold",
                "size": "xl"
                },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "21 歲\n" + 
                            "⼤安⾼⼯ 2014/9~2017/6\n" + 
                            "電⼦科 ｜ ⾼職畢業\n" + 
                            "台灣科技⼤學 2017/9~2021/6\n" + 
                            "資訊⼯程系｜⽬前就讀\n",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                        }
                        ]
                    }
                ]
                }
                ]
            },
        },
        {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://i.imgur.com/jUSHZll.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": "http://linecorp.com/"
            }
            },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "特殊經歷",
                "color": "#4969c3",
                "weight": "bold",
                "size": "xl"
                },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "46屆全國技能競賽北區 ⼯業電⼦職類 第五名\n" + 
                            "46屆全國技能競賽暨44屆國際技能競賽國⼿選拔賽 ⼯業電⼦職類 佳作\n" + 
                            "全國⾼級中等學校專業群科106年專題及創意製作競賽 專題組電機與電⼦群佳作 \n" + 
                            "LINE FRESH 2020 校園競賽 ⿊客松組 第三名\n" + 
                            "2020放視⼤賞 ⾏動應⽤類——軟體內容組 銀獎 未來式互動盆栽與植物交友盒\n",
                            "戰國策競賽 資誠數位創新組-最佳學⽣組\n",
                            "ＡＩＡ國際事務交流社 活動長\n",
                            "資訊⼯程系學會 機動組\n",
                            "國際志⼯ 隊輔組\n",
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                        }
                        ]
                    }
                ]
                }
                ]
            },
        }    
        ]
    return content
def rank_flex():
    rank = 1
    today = date.today()
    user_sep = []
    docs = db.collection('sales').order_by('profit',direction=firestore.Query.DESCENDING).get()
    for i in docs:
        r_doc = i.to_dict()
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "第" + str(rank) + "名",
                "size": "sm",
                "color": "#555555",
                "flex": 0
            }
            ]
        }
        user_sep.append(content)
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "業務員: " + r_doc["name"],
                "size": "sm",
                "color": "#555555"
            }
            ]
        }
        user_sep.append(content)
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "分潤金額: " + str(r_doc["profit"]),
                "size": "sm",
                "color": "#555555"
            }
            ]
        }
        user_sep.append(content)
        content = {
            "type": "separator",
            "margin": "xxl"
        }
        user_sep.append(content)
        rank += 1


    contents ={
        "type": "bubble",
        "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": str(today),
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
        },
        {
            "type": "text",
            "text": "業績英雄榜",
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
        },
        {
            "type": "separator",
            "margin": "xxl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": user_sep
        }
        ]
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
    }
    return contents 
def listOfservice_flex(user_id):
    docs = db.collection("transaction").where('customerID','==', user_id).order_by("date", direction=firestore.Query.DESCENDING).get()
    service = []
    
    for i in docs:
        r_doc = i.to_dict()
        name = r_doc['customerNAME']
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": i.id,
                "size": "sm",
                "color": "#1DB446",
                "flex": 0
            }
            ]
        }
        service.append(content)
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": str(r_doc["date"]),
                "size": "sm",
                "color": "#555555"
            }
            ]
        }
        service.append(content)
        content = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": str(r_doc["product"]),
                "size": "sm",
                "color": "#555555"
            }
            ]
        }
        service.append(content)
        content = {
            "type": "separator",
            "margin": "xxl"
        }
        service.append(content)
        


    contents ={
        "type": "bubble",
        "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": name,
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
        },
        {
            "type": "text",
            "text": "保單紀錄",
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
        },
        {
            "type": "separator",
            "margin": "xxl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": service
        }
        ]
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
    }
    return contents
def historyServices_flex(text,number, date,product): 
    
    contents ={
        "type": "bubble",
        "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "保單紀錄",
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
        },
        {
            "type": "text",
            "text": number,
            "weight": "bold",
            "color": "#1DB446",
            "size": "sm"
        },
        {
            "type": "text",
            "text": text,
            "weight": "bold",
            "size": "xxl",
            "margin": "md"
        },
        {
            "type": "separator",
            "margin": "xxl"
        },
        {
            "type": "box",
            "layout": "vertical",
            "margin": "xxl",
            "spacing": "sm",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": date,
                    "size": "sm",
                    "color": "#555555",
                    "flex": 0
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": product,
                    "size": "sm",
                    "color": "#555555"
                }
                ]
            },
            {
                "type": "button",
                "style": "link",
                "height": "sm",
                "action": {
                "type":"postback",
                "label":"申請理賠",
                "data":"apply&"+number,
                
                }
            }
            ]
        }
        ]
        },
        "styles": {
            "footer": {
            "separator": True
            }
        }
        }
    return contents    
def profitSharing_flex():
    content = {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": "https://i.imgur.com/dCmDaEZ.jpg",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "fit"
            }
        
        }
    return content
def comment_flex(name, img_url, rank, docs, url):
    
    star_ico = []
    goldStar = {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                }
    grayStar =  {
                "type": "icon",
                "size": "sm",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                }
    score = {
                "type": "text",
                "text": str(round(float(rank),1)),
                "size": "sm",
                "color": "#999999",
                "margin": "md",
                "flex": 0
            }
    
    for i in range(int(rank)):
        star_ico.append(goldStar)
    for i in range(5-int(rank)):
        star_ico.append(grayStar)
    star_ico.append(score)

    comment = []
    for i in docs:
        doc = i.to_dict()

        comment.append({
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": doc['name'],
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "sm",
                    "flex": 2
                    },
                    {
                    "type": "text",
                    "text": doc['comment'],
                    "wrap": True,
                    "color": "#666666",
                    "size": "sm",
                    "flex": 5
                    }
                ]
        })

    print (img_url)
    content = {
        "type": "bubble",
        "hero": {
        "type": "image",
        "url": img_url,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
            "type": "uri",
            "uri": url
        }
        },
        "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "text",
            "text": name,
            "weight": "bold",
            "size": "xl"
            },
            {
            "type": "box",
            "layout": "baseline",
            "margin": "md",
            "contents": star_ico
            },
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": comment 
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
            "style": "link",
            "height": "sm",
            "action": {
                "type": "uri",
                "label": "所有評論",
                "uri": url
            }
            },
            {
            "type": "spacer",
            "size": "sm"
            }
        ],
        "flex": 0
        }
    }
    return content



# Channel Access Token
line_bot_api = LineBotApi(line_channel_access_token)
# Channel Secret
handler = WebhookHandler(line_channel_secret)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text=event.message.text
    profile = line_bot_api.get_profile(event.source.user_id)
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        if text == "自傳":
            contents = welcome_flex()
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage('歡迎查看黃暉翔的履歷', contents)
            )
            
        elif text == "作品集":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="尚未完成喔")
            )
        elif text == "聯絡方式":
            pretty_text = "email: fly305z102@gmail.com"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=pretty_text)
            )
        elif text == "more":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="尚未完成喔")
            )
    
        

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    