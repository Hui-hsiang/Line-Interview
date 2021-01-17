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


def resume_flex():
    
    content = {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "hero": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/idkgenq.jpg",
                    "aspectMode": "cover",
                    "size": "full"
                }
                ],
                "spacing": "none",
                "height": "250px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/jUSHZll.jpg",
                            "aspectMode": "fit",
                            "size": "full"
                        }
                        ],
                        "cornerRadius": "100px",
                        "width": "72px",
                        "height": "72px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "contents": [
                            {
                                "type": "span",
                                "weight": "bold",
                                "color": "#000000",
                                "text": "黃暉翔\n"
                            },
                            {
                                "type": "span",
                                "text": "年齡:21 歲\n ⽬前就讀 \n 台灣科技⼤學資訊⼯程系\n 畢業於 \n 大安⾼⼯電⼦科  "
                            }
                            ],
                            "size": "sm",
                            "wrap": true
                        }
                        ]
                    }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "contents": [
                        {
                            "type": "span",
                            "text": "程式技術 \n",
                            "size": "xxs",
                            "weight": "regular",
                            "style": "italic",
                            "color": "#0000008F"
                        },
                        {
                            "type": "span",
                            "text": "Visual Studio、C、C++、Java、\nSwift、python、JavaSript、HTML \n"
                        },
                        {
                            "type": "span",
                            "text": "熟悉並瞭解\n",
                            "size": "xs",
                            "color": "#0000008F",
                            "weight": "regular",
                            "style": "italic"
                        },
                        {
                            "type": "span",
                            "text": " line bot api 、Android app 開發\n、 iOS app 開發"
                        }
                        ],
                        "wrap": true
                    }
                    ],
                    "margin": "none",
                    "spacing": "none",
                    "borderWidth": "none",
                    "cornerRadius": "none",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "offsetStart": "none",
                    "offsetEnd": "none",
                    "offsetBottom": "lg"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "hero": {
                "separator": false
                }
            }
            },
            {
            "type": "bubble",
            "hero": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/idkgenq.jpg",
                    "aspectMode": "cover",
                    "size": "full"
                }
                ],
                "spacing": "none",
                "height": "250px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "contents": [
                        {
                            "type": "span",
                            "text": " 有修過",
                            "size": "md"
                        },
                        {
                            "type": "span",
                            "text": "機器學習，深度學習，資料分析，android app 與 ios app開發",
                            "size": "md",
                            "weight": "bold",
                            "decoration": "underline"
                        },
                        {
                            "type": "span",
                            "text": "相關課程。並且接觸",
                            "size": "md"
                        },
                        {
                            "type": "span",
                            "text": " c , c++ , python , java , c# , javascript ",
                            "size": "md",
                            "weight": "bold",
                            "decoration": "underline"
                        },
                        {
                            "type": "span",
                            "text": "等程式語⾔。能夠理解並接續開發他⼈程式碼，並能夠進⾏專案團隊合作。",
                            "size": "md"
                        },
                        {
                            "type": "span",
                            "text": "我有問題處理的能⼒",
                            "size": "md",
                            "weight": "bold",
                            "decoration": "underline"
                        },
                        {
                            "type": "span",
                            "text": "，同時豐富的活動及比賽經驗培養我更能找出被忽略的問題，並提供解決⽅案，對於⾃⼰份內的事有責任感，同時有領導跟錯誤檢討能⼒，可以調整⾃⼰更加融入團隊。",
                            "size": "md"
                        }
                        ],
                        "size": "sm",
                        "wrap": true,
                        "offsetTop": "none",
                        "offsetStart": "none",
                        "offsetEnd": "none"
                    }
                    ],
                    "offsetStart": "xxl",
                    "borderWidth": "normal",
                    "cornerRadius": "none",
                    "margin": "none",
                    "spacing": "none",
                    "width": "250px",
                    "offsetTop": "xl"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "hero": {
                "separator": false
                }
            }
            },
            {
            "type": "bubble",
            "hero": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/idkgenq.jpg",
                    "aspectMode": "cover",
                    "size": "full"
                }
                ],
                "spacing": "none",
                "height": "250px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "contents": [
                            {
                                "type": "span",
                                "weight": "bold",
                                "color": "#000000",
                                "text": "特殊經歷\n",
                                "style": "italic",
                                "size": "xl"
                            },
                            {
                                "type": "span",
                                "text": "46屆全國技能競賽北區 ⼯業電⼦職類 第五名\n",
                                "size": "sm",
                                "color": "#538F53",
                                "weight": "bold",
                                "decoration": "none",
                                "style": "normal"
                            },
                            {
                                "type": "span",
                                "text": "46屆全國技能競賽暨44屆國際技能競賽國⼿選拔賽 ⼯業電⼦職類 佳作\n",
                                "color": "#5000FF",
                                "size": "sm",
                                "style": "normal",
                                "weight": "bold"
                            },
                            {
                                "type": "span",
                                "text": "全國⾼級中等學校專業群科106年專題及創意製作競賽 專題組電機與電⼦群佳作\n ",
                                "color": "#538F53",
                                "size": "sm",
                                "weight": "bold"
                            },
                            {
                                "type": "span",
                                "text": "LINE FRESH 2020校園競賽 ⿊客松組 季軍\n",
                                "color": "#5000FF",
                                "size": "sm",
                                "weight": "bold"
                            },
                            {
                                "type": "span",
                                "text": "2020放視⼤賞 ⾏動應⽤類——軟體內容組 銀獎 未來式互動盆栽與植物交友盒\n",
                                "color": "#538F53",
                                "size": "sm",
                                "weight": "bold"
                            },
                            {
                                "type": "span",
                                "text": "戰國策競賽 資誠數位創新組-最佳學⽣組",
                                "color": "#5000FF",
                                "size": "sm",
                                "weight": "bold"
                            }
                            ],
                            "size": "sm",
                            "wrap": true
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [],
                            "spacing": "sm",
                            "margin": "md"
                        }
                        ]
                    }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "hero": {
                "separator": false
                }
            }
            }
        ]
        }
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
            contents = resume_flex()
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
        elif text == "MORE":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="尚未完成喔")
            )
    
        

    

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    