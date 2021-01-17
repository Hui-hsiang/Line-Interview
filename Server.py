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
                                "text": "年齡:21 歲\n⽬前就讀 \n台灣科技⼤學資⼯系\n畢業於 \n大安⾼⼯電⼦科  "
                            }
                            ],
                            "size": "sm",
                            "wrap": True
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
                            "text": "Visual Studio,C,C++,Java,\nSwift,python,JavaSript,HTML \n"
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
                            "text": " line bot api ,Android app 開發\n, iOS app 開發 ,Node.js"
                        }
                        ],
                        "wrap": True
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
                    "offsetBottom": "lg",
                    "offsetTop": "sm"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "hero": {
                "separator": False
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
                            "color": "#5000FF",
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
                            "color": "#5000FF",
                            "decoration": "underline"
                        },
                        {
                            "type": "span",
                            "text": "等程式語⾔。能夠理解並接續開發他⼈程式碼，並能夠進⾏專案團隊合作。",
                            "size": "md"
                        },
                        {
                            "type": "span",
                            "text": "我具備問題處理的能⼒",
                            "size": "md",
                            "weight": "bold",
                            "color": "#5000FF",
                            "decoration": "underline"
                        },
                        {
                            "type": "span",
                            "text": "，同時豐富的活動及比賽經驗培養我更能找出被忽略的問題，並提供解決⽅案，對於⾃⼰份內的事有責任感，同時有領導跟錯誤檢討能⼒，可以調整⾃⼰更加融入團隊。",
                            "size": "md"
                        }
                        ],
                        "size": "sm",
                        "wrap": True,
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
                    "offsetTop": "xxl"
                }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "hero": {
                "separator": False
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
                                "size": "md"
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
                                "text": "戰國策競賽 數位創新組-最佳學⽣組",
                                "color": "#5000FF",
                                "size": "sm",
                                "weight": "bold"
                            }
                            ],
                            "size": "sm",
                            "wrap": True
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
                "separator": False
                }
            }
            }
        ]
        }
    return content

    
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

    