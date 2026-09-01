from Fareel import *
from BEAPI import BEAPI
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from FareelBots.ttypes import Message
from FareelBots.ttypes import ContentType as Type
from FareelBots.ttypes import TalkException
from datetime import datetime
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback, livejson
from googletrans import Translator
from threading import Thread,Event
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
_session = requests.session()
botStart = time.time()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2 
#=========================================================
#=========================================================
try:
    with open('token1.txt','r') as tokens:
        token = tokens.read()
    print(str(token))
except Exception as e:
    cl = LINE()
cl = LINE(token)
cl.log("Auth Token : " + str(cl.authToken))
time.sleep(1)
ajs = LINE("tmamd223@gmail.com","tm1234567",appName="DESKTOPWIN\t7.9.1\tFareel OS\t11")
#=========================================================
oepoll = OEPoll(cl)
clProfile = cl.getProfile()
clSettings = cl.getSettings()
#=========================================================
clMID = cl.profile.mid
mid = cl.getProfile().mid
Zmid = ajs.getProfile().mid
creator = [clMID]
owner = [clMID]
admin = [clMID]
staff = [clMID]
KAC = [cl]
ABC = [cl,ajs]
Bots = [clMID,Zmid]
FareelBots = creator + owner+ admin + staff 
#=========================================================
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
leave = []
msg_dict = {}
msg_dict1 = {}
#=========================================================
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeCover":{},
    "autoJoinTicket":False,
    "readerPesan": "Gw @!, Kang Sider",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

read = { 
    "readMember": {},
    "readPoint": {}
}

tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}

wait = {
    "Limit": 50,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "respontag":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    'autoBlock':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":5},
    'autoAdd':True,
    'autotext':True,
    'autoLeave':False,
    'Timeline':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "stickerOn":False,
    "sticker":False,
    "smule": True,
    "changevp": False,
    "changeFoto": {},
    "changeFoto": False,
    "likeOn": False,
    "stickers": {},
    "apikey" : "Ryansbot",
    "dark" : True,
    "apkTikel": True,
    "AddstickerSider": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerPesan": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerWelcome": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "AddstickerLeave": {
        "sid": "",
        "spkg": "",
        "status": False
    },
    "stk":{},
    "selfbot":True,
    "token":True,
    "responGc":True,
    "Images":{},
    "Img":{},
    "Addimage":{},
    "Videos":{},
    "Video":{},
    "Addvideo":{},
    "laranganOn":True,
    "responsalam":False,
    "link":"https://i.gifer.com/7CJk.gif",
    "link":"https://www.smule.com",
    "amdb":"#bypass",
    "amda":"nukeall",
    "mention":"ngintip loh😎 ",
    "Tag":"Jones tag gwee hh",
    "leave":"See you next time kaka",
    "welcome":"Welcome to my room",
    "order":"""
╭────────────────
│• OPEN ORDER BOTS
├────────────────
├ ▣ SB FOOTER
├ ▣ SB TEMLATE
├ ▣ SB TEMPLATE + AJS
├────────────────
│• BOT PROTECTION
├────────────────
├ ▣ PROTECT GC SMULE
├ ▣ PROTECT GC EVENT
├ ▣ PROTECT GC CHAT
├────────────────
│• GOLANG BOT
├────────────────
├ ▣ BOT GOLANG CL
├ ▣ BOT WAR MULTI
├────────────────
│• VIP - SONGBOOK
├────────────────
├ ▣ SONGBOK 10K
├ ▣ 25 VIP ANDROID 150K
├ ▣ 1 VIP ANDROID 25K 
╰────────────────    
    """,
    "comment":"""
╭────────────────
│• Done Like & Comment
│• Numpang promo kk
├────────────────
│• OPEN ORDER BOTS
├────────────────
├ ▣ SB FOOTER
├ ▣ SB TEMLATE
├ ▣ SB TEMPLATE + AJS
├────────────────
│• BOT PROTECTION
├────────────────
├ ▣ PROTECT GC SMULE
├ ▣ PROTECT GC EVENT
├ ▣ PROTECT GC CHAT
├────────────────
│• GOLANG BOT
├────────────────
├ ▣ BOT GOLANG CL
├ ▣ BOT WAR MULTI
├────────────────
│• VIP - SONGBOOK
├────────────────
├ ▣ SONGBOK 10K
├ ▣ 25 VIP ANDROID 150K
├ ▣ 1 VIP ANDROID 25K 
╰────────────────""",
    "unsend":False,
    "message":"""
╭────────────────
│• OPEN ORDER BOTS
├────────────────
├ ▣ SB FOOTER
├ ▣ SB TEMLATE
├ ▣ SB TEMPLATE + AJS
├────────────────
│• BOT PROTECTION
├────────────────
├ ▣ PROTECT GC SMULE
├ ▣ PROTECT GC EVENT
├ ▣ PROTECT GC CHAT
├────────────────
│• GOLANG BOT
├────────────────
├ ▣ BOT GOLANG CL
├ ▣ BOT WAR MULTI
├────────────────
│• VIP - SONGBOOK
├────────────────
├ ▣ SONGBOK 10K
├ ▣ 25 VIP ANDROID 150K
├ ▣ 1 VIP ANDROID 25K 
╰────────────────
▣ Langsung gasken link bawah ini
▣ line.me/ti/p/~Tm_bots
▣ Wa 081213332385""",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

comd = {
    "help": "help",
    "speed": "speed",
    "kick": "kick",
    "tagall": "hay",
    "cban": "cban",
    "siderOn": "sider on",
    "siderOff": "sider off",
    "bye": "@bye",
    "unsend": "unsend"
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

temptag = {
    "stealtag":False
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('sticker.json', 'r') as fp:
    stickers = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)

mulai = time.time()

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def runtime2(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Menit %02d Detik' % (mins, secs)
   
def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': cl.authToken,
        'X-Line-Application': cl.server.APP_NAME,
        'X-Line-ChannelId': '1653691907',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)

def flex3(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    scover = cl.getProfileCoverURL(mid)
    data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co/QJ230By/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
    sendTemplate(to, data)

def flexvian(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    scover = cl.getProfileCoverURL(mid)
    data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co/QJ230By/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
    sendTemplate(to, data)

def flex2(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    scover = cl.getProfileCoverURL(mid)
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True }, { "type": "image", "url": "https://i.ibb.co/QJ230By/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": text, "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "139.5px", "height": "17.5px", "cornerRadius": "2px", "offsetTop": "9px", "offsetStart": "10.5px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
    sendTemplate(to, data)         

def flextext(to, text):
    contact = cl.getProfile()
    mids = [contact.mid]
    status = cl.getContact(mid)
    scover = cl.getProfileCoverURL(mid)
    data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pnTLnnn/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "SELFBOT LINE", "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "10px", "offsetTop": "21.5px", "offsetStart": "22px" }, { "type": "text", "text": text, "size": "8px", "color": "#00ff00", "wrap": True, "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/pnTLnnn/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:1", "animated": True, "backgroundColor": "#000000" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "LINE CORPOROTATION", "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "115px", "height": "10px", "offsetStart": "22px", "offsetBottom": "21.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } ] } }
    sendTemplate(to, data)                  

def modflex(to, text):
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    contact = cl.getContact(mid)
    data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "image", "url": "https://i.ibb.co/Fz5jYwQ/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "USER : {}".format(contact.displayName), "size": "8px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "129px", "height": "12px", "offsetTop": "82px", "offsetStart": "18px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "8px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "82px", "height": "12px", "offsetTop": "58px", "offsetEnd": "12px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
    sendTemplate(to, data)

def sendFlexVideo(to, videoUrl, thumbnail='dark'):
    main = ["dark","red","cyan","yellow","green","white"]
    if thumbnail in main:
       thumbnail = f"https://i.ibb.co/DY8GgVm/IMG-20220805-WA0007.jpg"
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s' % token.accessToken}
    data = {'messages': [{'type': 'video','originalContentUrl': videoUrl,'previewImageUrl': thumbnail,}]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendFlexAudio(to, link):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer %s' % token.accessToken}
    data = {'messages': [{'type': 'audio','originalContentUrl': link,'duration': 250000}]}
    requests.post(url, headers=headers, data=json.dumps(data))


def sendFlexImage(to, imageUrl, animated=False):
    main = ["dark","red","cyan","yellow","green","white"]
    color = random.choice(main)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % token.accessToken
        }
    data = {
            'messages': [{
                'type': 'image',
                'originalContentUrl': imageUrl,
                'previewImageUrl': imageUrl,
                'animated': animated,
                'extension': 'jpg'
            }]
        }
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate2(friend, data):
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def sendCarousel2(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = cl.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)

def sendFoter(to, text):
    data = {
        "type": "text",
        "text": text,
        "sentBy": {
             "label": "• Tuman Bots •",
             "iconUrl": "https://s20.directupload.net/images/210719/mrc6uorh.gif",
             "linkUrl": "line://nv/profilePopup/mid=ube9340d43361f4d904cd574c7a2ad308"
         }
     }
    sendTemplate(to, data)

def failOverAPI():
    try:
        result = requests.get("https://api.boteater.xyz",timeout=0.5)
        if result.status_code == 200:
            return "https://api.boteater.xyz"
        else:
            return "https://api.boteater.us"
    except:
        return "https://api.boteater.us"

def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+cl.google_url_shorten(links)
    
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "update profile failed"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("vp.mp4")

def changeProfileVideo(to):
    if settings['changevp']['picture'] == None:
        return cl.sendReplyMessage(msg_id, to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == None:
        return cl.sendReplyMessage(msg_id, to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendReplyMessage(msg_id, to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def FakeStickerV2(to, spkg,sid, mids=[]): #DONE
    if clMID in mids: mids.remove(clMID)
    parsed_len = len(mids)//140+1
    result = '「 Mention Members 」\n'
    mention = '@netizent...\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*140:(point+1)*140]:
            no += 1
            result += ' %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += ''
        if result:
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees}),'STKPKGID':spkg,'STKID':sid}, 7)
        result = ''

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╭─「 Daftar anggota 」\n├↘\n├↘1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n├↘\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├↘ {}. ".format(str(no))
            else:
                textx += "╰─「 Mentions {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Result {} Sider 」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Welcome:  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\n"+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Bye :".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact("u176ef6889643e290ba5801bffc83457b").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def khieMention(to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Mmk "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 5
                else:slen = len(textx);elen = len(textx) + 5
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def FareelKiller(to, mid):
    try:
        aa = '{"S":"0","E":"5","M":'+json.dumps(mid)+'}'
        text_ = '@Khiez'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers2(to, mids=[]):
    if clMID in mids: mids.remove(clMID)
    parsed_len = len(mids)//20+1
    result = '╭───「 Mention 」\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 TM_BOTS」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	#if Setmain["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
def helpjs():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "╭─╼Help Js \n"+\
                  "├⌬ " + key + "nukeall\n" + \
                  "├⌬ " + key + "bantai: no\n" + \
                  "├⌬ " + key + "sapu: no\n" + \
                  "├⌬ " + key + "#bypass\n" + \
                  "├⌬ " + key + "#cancel\n" + \
                  "├⌬ " + key + "Set js\n" + \
                  "├⌬ " + key + "Set bypass\n" + \
                  "├⌬ " + key + "js in\n" + \
                  "├⌬ " + key + "js lv\n" + \
                  "├⌬ " + key + "js cl\n" + \
                  "├⌬ " + key + "stay\n" + \
                  "├⌬ " + key + "#bye\n" + \
                  "╰╼─┅tuman bots"
    return helpMessage1
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return        
        if op.type in [11,122]:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass                    
        if op.type in [13,124]:
            if clMID in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            time.sleep(5)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            contact = cl.getContact(op.param2)
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            data = {"type": "flex","altText": "Tuman Bots","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co/brwBdv2/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "Thanks for invite me dan salam kenal semuanya", "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                            sendTemplate(op.param1, data)           
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        data = {"type": "flex","altText": "Tuman Bots","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co/brwBdv2/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "Thanks for invite me dan salam kenal semuanya", "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                        sendTemplate(op.param1, data)           
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace(" ",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if clMID in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)                      
        if op.type in [13,124]:
            if op.param1 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    babi = op.param3.replace("",',')
                    memek = babi.split(",")
                    for sodok in memek:
                       cl.cancelGroupInvitation(op.param1,[sodok])
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       wait["blacklist"][op.param2] = True
        if op.type in [13,124]:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    babi = op.param3.replace("",',')
                    memek = babi.split(",")
                    for sodok in memek:
                       cl.cancelGroupInvitation(op.param1,[sodok])
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       wait["blacklist"][op.param2] = True
        if op.type in [19,133]:
            if clMID in op.param3:
            	if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ajs.acceptGroupInvitation(op.param1)
                        ajs.kickoutFromGroup(op.param1,[op.param2])
                        ajs.inviteIntoGroup(op.param1,[clMID])
                        cl.acceptGroupInvitation(op.param1)
                        ajs.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        wait["blacklist"][op.param2] = True
                    except:pass
        if op.type in [32,126]:
            if op.param3 in Zmid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                          wait["blacklist"][op.param2] = True
                          cl.inviteIntoGroup(op.param1,[Zmid])
                  except:pass
        if op.type in [19,133]:
            if Zmid in op.param3:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:ajs.kickoutFromGroup(op.param1,[op.param2]);ajs.inviteIntoGroup(op.param1,[clMID])
                  except:pass
        if op.type in [19,133]:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.findAndAddContactsByMid(op.param3);cl.kickoutFromGroup(op.param1,[op.param2]);cl.inviteIntoGroup(op.param1,[op.param3])
                  except:pass
        if op.type in [19,133]:
            if op.param3 in Bots:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          cl.findAndAddContactsByMid(op.param3);cl.kickoutFromGroup(op.param1,[op.param2]);cl.inviteIntoGroup(op.param1,[op.param3])
                  except:pass
 
        if op.type in [17,130]:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = { "type": "flex", "altText": "Tm Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "34px", "height": "34px", "offsetTop": "10px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co/PzBdQ6W/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "22px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "35px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["welcome"], "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "142px", "height": "20px", "offsetBottom": "9.5px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                sendTemplate(op.param1, data)                                                
                sid = str(wait["AddstickerWelcome"]["sid"])
                spkg = str(wait["AddstickerWelcome"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)

        if op.type in [15,128]:
            if op.param1 in leave:
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                cover = cl.getProfileCoverURL(op.param2)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                data = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "34px", "height": "34px", "offsetTop": "10px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co/PzBdQ6W/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "22px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "73px", "height": "11px", "offsetTop": "35px", "offsetStart": "43px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["leave"], "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "142px", "height": "20px", "offsetBottom": "9.5px", "offsetStart": "9px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                sendTemplate(op.param1, data)                                                
                sid = str(wait["AddstickerLeave"]["sid"])
                spkg = str(wait["AddstickerLeave"]["spkg"])
                cl.sendSticker(op.param1, spkg, sid)                 
                  
        if op.type in [17,130]:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl.kickoutFromGroup(op.param1,[op.param2])
                    except:pass
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)
                    cl.kickoutFromGroup(op.param1,[op.param2])                        
                return
        if op.type == 0:
            return
        if op.type in [5]:
              if wait["autoAdd"] == True:
                  cl.sendMentionV2(op.param1, "Haii Kak @!\nThanks For add me\n" +wait["message"]+ "", [op.param1])
                  sid = str(wait["AddstickerPesan"]["sid"])
                  spkg = str(wait["AddstickerPesan"]["spkg"])
                  cl.sendSticker(msg.to, spkg, sid)

        if op.type in [5]:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
                cl.sendMentionV2(op.param1, "Haii Kak @!\nThanks For add me\nTapi Mohon maaf auto blok aktiff", [op.param1])
        if op.type in [19,133]:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type in [32,126]:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:pass                        
                return
        if op.type in [55]:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:pass

            if op.param1 in Setmain["RAreadPoint"]:
                if op.param2 in Setmain["RAreadMember"][op.param1]:
                    pass
                else:
                    Setmain["RAreadMember"][op.param1][op.param2] = True
            else:
                pass
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭─「 Gambar Dihapus 」\n│ Pengirim : "
                                ret_ = "│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╭─「 Pesan Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n│ Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                flextext(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╭─「 Sticker Dihapus 」\n"
                                ret_ += "│ Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n│ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n│ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╰───────────"
                                flextext(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type in [55]:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        contact = cl.getContact(op.param2)
                        tz = pytz.timezone("Asia/Jakarta")
                        cover = cl.getProfileCoverURL(op.param2)
                        timeNow = datetime.now(tz=tz)
                        data = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co/brwBdv2/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["mention"], "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                        sendTemplate(op.param1, data)
                        sid = str(wait["AddstickerSider"]["sid"])
                        spkg = str(wait["AddstickerSider"]["spkg"])
                        cl.sendSticker(op.param1, spkg, sid)
			
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
   
        if op.type == 25 or op.type == 26:
            try:
                print ("[ 25 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to = msg.to
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != cl.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return

            except:
                pass
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
              if wait["respontag"] == True:
                contact = cl.getContact(msg._from)
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                cover = cl.getProfileCoverURL(sender)
                name = re.findall(r'@(\w+)', msg.text)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                mentionees = mention['MENTIONEES']
                for mention in mentionees:
                     if mention ['M'] in clMID:
                        XFUCK = {"type": "flex","altText": "Tm Bots","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "6px", "offsetStart": "60.5px", "cornerRadius": "2px" }, { "type": "image", "url": "https://i.ibb.co/ZY7B0Bb/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "6.5px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "52px", "height": "11px", "offsetTop": "12px", "offsetStart": "6px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "6.5px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "47px", "height": "11px", "offsetTop": "32px", "offsetEnd": "11px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": wait["Tag"], "size": "7px", "color": "#00ff00", "align": "center", "wrap": True } ], "position": "absolute", "width": "136px", "height": "22px", "offsetBottom": "10px", "offsetStart": "12px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                        sendTemplate(to, XFUCK)
                        sid = str(wait["AddstickerTag"]["sid"])
                        spkg = str(wait["AddstickerTag"]["spkg"])
                        cl.sendSticker(msg.to, spkg, sid)  
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
                     
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if temptag["stealtag"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention["M"] in clMID:
                           contact = cl.getContact(msg._from)
                           anu = contact.displayName
                           cl.sendReplyMessage(msg.id,to, " " +anu+ " {}".format(wait["Tag"]))
                           sid = str(wait["AddstickerTag"]["sid"])
                           spkg = str(wait["AddstickerTag"]["spkg"])
                           cl.sendSticker(msg.to, spkg, sid)
                           break
                                                                                                    
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in clMID:
                           cl.sendMessage(msg.to, "Don't Tag Me !!")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    flextext(msg.to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        flextext(msg.to,"╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n├↘ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            stickername = str(text)
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            flextext(to, str(ret_))

               if msg.contentType == 16:
                    if wait["likeOn"] == True:
                        url = msg.contentMetadata["postEndUrl"]
                        cl.likePost(url[25:58], url[66:], likeType = 1001)
                        cl.createComment(url[25:58], url[66:], wait["comment"])
                        contact = cl.getContact(sender)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        data = {"type": "flex","altText": "Tuman Bots","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "39px", "height": "39px", "offsetTop": "13px", "offsetEnd": "13.5px" }, { "type": "image", "url": "https://i.ibb.co/brwBdv2/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "87px", "height": "10px", "offsetBottom": "12px", "offsetEnd": "10px", "cornerRadius": "2px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1.5px" } ], "position": "absolute", "width": "44px", "height": "12px", "offsetBottom": "11px", "offsetStart": "12px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "DONE LIKE DAN COMMENT JANGAN LUPA LIKE BACK", "size": "7px", "color": "#00ffff", "wrap": True, "align": "center" } ], "position": "absolute", "width": "90px", "height": "24.5px", "offsetTop": "13px", "offsetStart": "12.5px" } ], "paddingAll": "0px", "backgroundColor": "#000000" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                        sendTemplate(to, data)
                        
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerTag"]["status"] == True:
                        wait["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        flexvian(msg.to, "Add Stickers Tag Succes ♪")
                        wait["AddstickerTag"]["status"] = False     
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerSider"]["status"] == True:
                        wait["AddstickerSider"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerSider"]["spkg"] = msg.contentMetadata['STKPKGID']
                        flexvian(msg.to, "Add stickers sider ♪")
                        wait["AddstickerSider"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerPesan"]["status"] == True:
                        wait["AddstickerPesan"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerPesan"]["spkg"] = msg.contentMetadata['STKPKGID']
                        flexvian(msg.to, "Succes add Stickers ♪")
                        wait["AddstickerPesan"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerWelcome"]["status"] == True:
                        wait["AddstickerWelcome"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerWelcome"]["spkg"] = msg.contentMetadata['STKPKGID']
                        flexvian(msg.to, "Succes add Stickers ♪")
                        wait["AddstickerWelcome"]["status"] = False                   
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["AddstickerLeave"]["status"] == True:
                        wait["AddstickerLeave"]["sid"] = msg.contentMetadata['STKID']
                        wait["AddstickerLeave"]["spkg"] = msg.contentMetadata['STKPKGID']
                        flexvian(msg.to, "Succes add Stickers Leave ♪")
                        wait["AddstickerLeave"]["status"] = False                   
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
               if msg.contentType == 7:
                   if msg._from in admin:
                       try:
                           if wait["sticker"] == True:
                               wait["stickers"][wait["stk"]] = msg.contentMetadata
                               wait["stk"] = {}
                               wait["sticker"] = False
                               f=codecs.open("wait.json","w","utf-8")
                               json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                               flexvian(msg.to,"Tersimpan")
                       except Exception as e:
                           sendFoter(msg.to,"{}".format(str(e)))
                       
               if msg.contentType == 7:
                 if wait["stickerOn"] == True:
                    msg.contentType = 0
                    flextext(msg.to,"╭─「 Cek ID Sticker 」\n├↘ STKID : " + msg.contentMetadata["STKID"] + "\n├↘ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n├↘ STKVER : " + msg.contentMetadata["STKVER"]+ "\n├↘\n╰─「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        flextext(msg.to," ╭─「 Contact Info 」\n├↘ Nama : " + msg.contentMetadata["displayName"] + "\n├↘ MID : " + msg.contentMetadata["mid"] + "\n├↘ Status Msg : " + contact.statusMessage + "\n╰─ 「Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        flextext(msg.to,"Sudah dalam daftar bot\nSilahkan ketik refresh")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        flextext(msg.to,"Masuk dalam daftar bots\nSilahkan ketik refresh")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        flextext(msg.to,"Berhasil menghapus dari anggota bot\nSilahkan ketik refresh")
                    else:
                        wait["dellbots"] = True
                        flextext(msg.to,"Contact itu bukan anggota bot\nSilahkan ketik refresh")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        flextext(msg.to,"Contact itu sudah jadi staff\nSilahkan ketik refresh")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        flextext(msg.to,"Berhasil menambahkan ke staff\nSilahkan ketik refresh")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        flextext(msg.to,"Berhasil menghapus dari staff\nSilahkan ketik refresh")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        flextext(msg.to,"Contact itu bukan staff\nSilahkan ketik refresh")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        flextext(msg.to,"Contact itu sudah jadi admin\nSilahkan ketik refresh")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        flextext(msg.to,"Berhasil menambahkan ke admin\nSilahkan ketik refresh")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        flextext(msg.to,"Berhasil menghapus dari admin\nSilahkan ketik refresh")
                    else:
                        wait["delladmin"] = True
                        flextext(msg.to,"Contact itu bukan admin\nSilahkan ketik refresh")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        flextext(msg.to,"Contact itu sudah ada di blacklist\nSilahkan ketik refresh")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        flextext(msg.to,"Masuk daftar blacklist\nSilahkan ketik refresh")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        flextext(msg.to,"Unbaned blacklist\nSilahkan ketik refresh")
                    else:
                        wait["dblacklist"] = True
                        flextext(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        flextext(msg.to,"Contact itu sudah ada di Talkban\nSilahkan ketik refresh")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        flextext(msg.to,"Berhasil menambahkan ke Talkban user\nSilahkan ketik refresh")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        flextext(msg.to,"Berhasil menghapus dari Talkban user\nSilahkan ketik refresh")
                    else:
                        wait["Talkdblacklist"] = True
                        flextext(msg.to,"Contact itu tidak ada di Talkban\nSilahkan ketik refresh")
#UPDATE FOTO
               if msg.contentType == 1:
                if msg._from in admin:
                  if wait["Addimage"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        flextext(msg.to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}                
                        wait["Addimage"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataFoto/'+wait["Img"]+'.jpg')
                        flextext(msg.to, "Berhasil menambahkan gambar")
                        wait["Img"] = {}
                        wait["Addimage"] = False
               if msg.contentType == 2:
                if msg._from in admin:
                  if wait["Addvideo"] == True:
                    try:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        flextext(msg.to, "Berhasil menambahkan video")
                        wait["Video"] = {}                
                        wait["Addvideo"] = False
                    except Exception as e:
                        cl.downloadObjectMsg(msg.id,'path','dataVideo/'+wait["Video"]+'.mp4')
                        flextext(msg.to, "Berhasil menambahkan video")
                        wait["Video"] = {}
                        wait["Addvideo"] = False
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     flexvian(msg.to, "Success")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if clMID in wait["changeFoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del wait["changeFoto"][clMID]
                            cl.updateProfilePicture(path)
                            flexvian(msg.to,"Foto berhasil dirubah")
                   if msg._from in admin:
                       if Zmid in wait["changeFoto"]:
                            path = ajs.downloadObjectMsg(msg_id)
                            del wait["changeFoto"][Zmid]
                            ajs.updateProfilePicture(path)
                            ajs.sendMessage(msg.to,"Foto Succes ajs")
                   if msg._from in admin:
                       if clMID in settings["changeCover"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del settings["changeCover"][clMID]
                            cl.updateProfileCover(path)
                            flexvian(to, "Updated")                                                            

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "chatbot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                ret = "Chatbot Enable."
                                flexvian(msg.to, str(ret))

                        elif cmd == comd["help"]:
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            name = contact.displayName
                            modflex(msg.to,"GROUP")
                                
                        elif cmd == "chatbot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                ret = "Chatbot Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "clear":
                            if msg._from in admin:
                                process = os.popen('cd /tmp/ && rm -r *')
                                a = process.read()
                                ret = "Cleared Temp File"
                                flexvian(msg.to, str(ret))
    
                        elif cmd == "remote":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Tag: (numb)\n"
                                ret += "• Gurl (numb)\n"
                                ret += "• Bye: (numb)\n"
                                ret += "• Close(numb)\n"
                                ret += "• Infogrup (numb)\n"
                                ret += "• Infomem (numb)\n"
                                ret += "• Bantai: (numb)"
                                flextext(msg.to, str(ret))    
    
                        elif cmd == "group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Me\n"
                                ret += "• Mid\n"
                                ret += "• Addfriend @\n"
                                ret += "• Block @\n"
                                ret += "• Cek @\n"
                                ret += "• Find @\n"
                                ret += "• Rename @\n"
                                ret += "• Mid @\n"
                                ret += "• Speed|Sp\n"
                                ret += "• Stag\n"
                                ret += "• Tag\n"
                                ret += "• Tagall sticker\n"
                                ret += "• Ginfo\n"
                                ret += "• Buka qr\n"
                                ret += "• Tutup qr\n"
                                ret += "• @bye\n"
                                ret += "• Url\n"
                                ret += "• Idline (idline)\n"
                                ret += "• Gruplist\n"
                                ret += "• Gnamegrup (text)\n"
                                ret += "• Call @\n"
                                ret += "• Fotgbc (Text)\n"
                                ret += "• Fotfbc (Text)\n"
                                ret += "• Flexgbc (Text)\n"
                                ret += "• Flexfbc (Text)\n"
                                ret += "• Clearallfriend\n"
                                ret += "• Clearchat\n"
                                ret += "• Refresh\n"
                                ret += "• Sider (on|off)\n"
                                ret += "• Broadcast: (Text)\n"
                                ret += "• Setkey (key)\n"
                                ret += "• Mykey\n"
                                ret += "• Resetkey\n"
                                ret += "• Unsend (numb)\n"
                                ret += "• Jumlah: (jumlh)\n"
                                ret += "• Spamtag (jumlh)\n"
                                ret += "• Spamtag @ (jumlh)\n"
                                ret += "• Spamcall (numb)\n"
                                ret += "• Spamcall: (jumlh)\n"
                                ret += "• Spamcall\n"
                                ret += "• Gift: (mid)(jumlh)\n"
                                ret += "• Spam: (mid)(jumlh)\n"
                                ret += "• Spam on|jumlah|text\n"
                                ret += "• Tag (jumlah di pm)"
                                flextext(msg.to, str(ret))

                        elif cmd == "profile":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Myname\n"
                                ret += "• Mybio\n"
                                ret += "• Mypict\n"
                                ret += "• Myvideo\n"
                                ret += "• Steal @\n"
                                ret += "• Video @\n"
                                ret += "• Pict @\n"
                                ret += "• Cover\n"
                                ret += "• Bio\n"
                                ret += "• Name:\n"
                                ret += "• Cvp: (link yt)"
                                flextext(msg.to, str(ret))

                        elif cmd == "admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Blc\n"
                                ret += "• Bot:on\n"
                                ret += "• Bot:repeat\n"
                                ret += "• Staff:on\n"
                                ret += "• Staff:repeat\n"
                                ret += "• Admin:on\n"
                                ret += "• Admin:repeat\n"
                                ret += "• Botadd @\n"
                                ret += "• Botdell @\n"
                                ret += "• Staffadd @\n"
                                ret += "• Staffdell @\n"
                                ret += "• Adminadd @\n"
                                ret += "• Admindell @\n"
                                ret += "• Kick @\n"
                                ret += "• Ulti @"
                                flextext(msg.to, str(ret))

                        elif cmd == "banned":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Blc\n"
                                ret += "• Banlist\n"
                                ret += "• Clearban\n"
                                ret += "• Ban:on\n"
                                ret += "• Unban:on\n"
                                ret += "• Ban @\n"
                                ret += "• Unban @\n"
                                ret += "• Talkban @\n"
                                ret += "• Untalkban @\n"
                                ret += "• Talkbanlist @"
                                flextext(msg.to, str(ret))

                        elif cmd == "setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• CekSider\n"
                                ret += "• CekSpam\n"
                                ret += "• CekPesan\n"
                                ret += "• CekRespon\n"
                                ret += "• clfoto\n"
                                ret += "• ajsfoto\n"
                                ret += "• mename:\n"
                                ret += "• ajsname:\n"
                                ret += "• Sticker sider\n"
                                ret += "• Sticker pesan\n"
                                ret += "• Sticker Welcome\n"
                                ret += "• Sticker Leave\n"
                                ret += "• Setsider: (Text)\n"
                                ret += "• Setcomment: (Text)\n"
                                ret += "• Setreject: (jumlah)\n"
                                ret += "• Setwelcome: (Text)\n"
                                ret += "• Setleave: (Text)\n"
                                ret += "• Setrespon: (Text)\n"
                                ret += "• Setpesan: (Text)\n"
                                ret += "• Setcban: (Text)\n"
                                ret += "• Setbye: (Text)\n"
                                ret += "• Sethelp: (Text)\n"
                                ret += "• Setspeed: (Text)\n"
                                ret += "• Setsider on: (Text)\n"
                                ret += "• Setsider off: (Text)\n"
                                ret += "• Setkick: (Text)\n"
                                ret += "• Settagall: (Text)\n"
                                ret += "• Setunsend: (Text)\n"
                                ret += "• Myname: (Text)\n"
                                ret += "• ajsname:\n"
                                ret += "• clfoto\n"
                                ret += "• ajsfoto\n"
                                ret += "• Updategrup\n"
                                ret += "• Autojoin (On|Off)\n"
                                ret += "• Autochat (On|Off)\n"
                                ret += "• Autoleave (On|Off)\n"
                                ret += "• Autoread (On|Off)\n"
                                ret += "• Autoblock (On|Off)\n"
                                ret += "• Autolike (On|Off)\n"
                                ret += "• Respon (On|Off)\n"
                                ret += "• Respon2 (On|Offa)\n"
                                ret += "• Responcall (On|Off)\n"
                                ret += "• Sticker (On|Off)\n"
                                ret += "• Unsend (On|Off)\n"
                                ret += "• Timeline (On|Off)\n"
                                ret += "• Contact: (On|Off)\n"
                                ret += "• Autoadd (On|Off)\n"
                                ret += "• Jointicket (On|Off\n"
                                ret += "• Welcomemsg (On|Off)\n"
                                ret += "• Leavemsg (On|Off)\n"
                                ret += "• Smule (On|Off)\n"
                                ret += "• Tiktok url (On|Off)\n"
                                ret += "• Yt url (On|Off)"
                                flextext(msg.to, str(ret))

                        elif cmd == "media":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "• Addsticker: (Text)\n"
                                ret += "• Dellsticker: (Text)\n"
                                ret += "• Stickerlist\n"
                                ret += "• Addtext: (Text)\n"
                                ret += "• Deltext: (Text)\n"
                                ret += "• List text\n"
                                ret += "• Bitcoin\n"
                                ret += "• Corona\n"
                                ret += "• Info bmkg\n"
                                ret += "• Acara tv\n"
                                ret += "• Info loker\n"
                                ret += "• Ciname xx1\n"
                                ret += "• Fs (text)\n"
                                ret += "• Cctv code\n"
                                ret += "• Cctv (number)\n"
                                ret += "• Github (search)\n"
                                ret += "• Ytmp3 (query)\n"
                                ret += "• Ytmp4 (query )\n"
                                ret += "• Porn (search)\n"
                                ret += "• Randomname\n"
                                ret += "• Lyrik (search)\n"
                                ret += "• Joox: (search)\n"
                                ret += "• Cuaca (wilayah)\n"
                                ret += "• Sholat (wilayah)\n"
                                ret += "• Surahlist\n"
                                ret += "• Surah (ayat)\n"
                                ret += "• Fancytext (text)\n"
                                ret += "• Acaratv (search)\n"
                                ret += "• Zodiak (bintang)\n"
                                ret += "• Instagram (search)\n"
                                ret += "• Ponsel (type)\n"
                                ret += "• Google (search)\n"
                                ret += "• Resi-jnt: (resi)\n"
                                ret += "• Resi-pos: (resi)\n"
                                ret += "• Resi-rex: (resi)\n"
                                ret += "• Resi-ninja: (resi)\n"
                                ret += "• Resi-sicepat: (resi)\n"
                                ret += "• Anime: (search)\n"
                                flextext(msg.to, str(ret))

                        elif cmd == "protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret += "• Notag On|Off\n"
                                ret += "• Pinvite On|Off\n"
                                ret += "• Pqr On|Off\n"
                                ret += "• Pjoin On|Off \n"
                                ret += "• Pkick On|Off\n"
                                ret += "• Pcancell On|Off"
                                flextext(msg.to, str(ret))

                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ret = "❑ Indo: Text\n"
                                ret += "❑ Jawa: Text\n"
                                ret += "❑ Jp: Text\n"
                                ret += "❑ Thai: Text\n"
                                ret += "❑ Eng: Text\n"
                                ret += "❑ Arab: Text\n"
                                ret += "❑ Korea: Text\n"
                                ret += "❑ India: Text\n"
                                ret += "❑ China: Text\n"
                                ret += "❑ Rusia: Text\n"
                                ret += "❑ Spanyol: Text\n"
                                ret += "❑ Franchis: Text\n"
                                ret += "❑ Malay: Text\n"
                                ret += "❑ Itali: Text\n"
                                ret += "❑ Filipin: Text\n"
                                ret += "❑ Turki: Text\n"
                                ret += "❑ Vietnam: Text\n"
                                ret += "❑ Belanda: Text\n"
                                ret += "❑ German: Text"
                                flextext(msg.to, str(ret))

                        elif cmd == "cmd list":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                vian = "╭─「👥 Cmd List 👥」\n"
                                for u in comd:
                                    vian += "├❑ {} : {}\n".format(u,comd[u])
                                vian += '╰────────'
                                flextext(msg.to, str(vian))
                            
                        elif cmd.startswith("footgbc"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                khie = text.split(" ")
                                hey = text.replace(khie[0] + " ", "")
                                text = "{}".format(hey)
                                groups = cl.getGroupIdsJoined()
                                for gr in groups:
                                    flextext(gr, text)
 
                        elif cmd.startswith("textgbc "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                bc = text.replace(sep[0] + " ","")
                                saya = cl.getGroupIdsJoined()
                                for rom in saya:
                                    cl.sendMessage(rom," BROADCAST \n\n"+bc)
                                cl.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(saya))))
 
                        elif cmd.startswith("flexgbc "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                rah = text.split(" ")
                                matt = text.replace(rah[0] + " ","")
                                chat = "{}".format(matt)
                                groups = cl.getGroupIdsJoined()
                                for gr in groups:
                                    flextext(gr, chat)
                                
                        elif cmd.startswith("flexfbc "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                rah = text.split(" ")
                                matt = text.replace(rah[0] + " ","")
                                chat = "{}".format(matt)
                                friends = cl.getAllContactIds()
                                for friend in friends:
                                    flextext(friend, chat)
                                    time.sleep(1)
                                cl.sendReplyMessage(msg.id,to, "Succes friend cast to {} friend ".format(str(len(friends))))
                            
                        elif cmd.startswith("fotfbc"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                khie = text.split(" ")
                                hey = text.replace(khie[0] + " ", "")
                                text = "{}".format(hey)
                                groups = cl.getGroupIdsJoined()
                                for friend in friends:
                                    flextext(friend, text)
                              
                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                #tz = pytz.timezone("Asia/Jakarta")
                                #timeNow = datetime.now(tz=tz)
                                md = "╭─「 STATUS BOTS 」\n"
                                if wait["yturl"] == True: md+="├ ✓  ❑ Youtube Url\n"
                                else: md+="├ ✗  ❑ Youtube Url\n"
                                if wait["tiktok"] == True: md+="├ ✓  ❑ Tiktok Url\n"
                                else: md+="├ ✗  ❑ Tiktok Url\n"
                                if wait["smule"] == True: md+="├ ✓  ❑ Smule\n"
                                else: md+="├ ✗  ❑ Smule\n"
                                if wait["sticker"] == True: md+="├ ✓  ❑ Sticker\n"
                                else: md+="├ ✗  ❑ Sticker\n"
                                if wait["contact"] == True: md+="├ ✓  ❑ Contact\n"
                                else: md+="├ ✗  ❑ Contact\n"
                                if wait["unsend"] == True: md+="├ ✓  ❑ Unsend\n"
                                else: md+="├ ✗  ❑ Unsend\n"
                                if wait["Timeline"] == True: md+="├ ✓  ❑ Timeline\n"
                                else: md+="├ ✗  ❑ Timeline\n"
                                if wait["respontag"] == True: md+="├ ✓  ❑ Respon\n"
                                else: md+="├ ✗  ❑ Respon\n"
                                if temptag["stealtag"] == True: md+="├ ✓  ❑ Respon2\n"
                                else: md+="├ ✗  ❑ Respon2\n"
                                if wait["autoBlock"] == True: md+="├ ✓  ❑ Auto Block\n"
                                else: md+="├ ✗  ❑ Auto Block\n"
                                if wait["talkban"] == True: md+="├ ✓  ❑ Talkban\n"
                                else: md+="├ ✗  ❑ Talkban\n"
                                if wait["Mentionkick"] == True: md+="├ ✓  ❑ Notag\n"
                                else: md+="├ ✗  ❑ Notag\n"
                                if wait["detectMention"] == True: md+="├ ✓  ❑ Respon2\n"
                                else: md+="├ ✗  ❑ Respon2\n"
                                if wait["autoJoin"] == True: md+="├ ✓  ❑ Autojoin\n"
                                else: md+="├ ✗  ❑ Autojoin\n"
                                if wait["autoCancel"]["on"] == True: md+="├ ✓  ❑ AutoReject : " + str(wait["autoCancel"]["members"]) + "\n"
                                else: md+="├ ✗  ❑ AutoReject\n"
                                if wait["autoAdd"] == True: md+="├ ✓  ❑ Autoadd\n"
                                else: md+="├ ✗  ❑ Autoadd\n"
                                if wait["likeOn"] == True: md+="├ ✓  ❑ Autolike\n"
                                else: md+="├ ✗  ❑ Autolike\n"
                                if wait["responGc"] == True: md+="├ ✓  ❑ Respon Gc\n"
                                else: md+="├ ✗  ❑ Respon Gc\n"
                                if msg.to in welcome: md+="├ ✓  ❑ Welcome\n"
                                else: md+="├ ✗  ❑ Welcome\n"
                                if wait["autoLeave"] == True: md+="├ ✓  ❑ Autoleave\n"
                                else: md+="├ ✗  ❑ Autoleave\n"
                                if msg.to in leave: md+="├ ✓  ❑ LeaveMsg\n"
                                else: md+="├ ✗  ❑ LeaveMsg\n"
                                if msg.to in protectqr: md+="├ ✓  ❑ Protectqr\n"
                                else: md+="├ ✗  ❑ Protectqr\n"
                                if msg.to in protectjoin: md+="├ ✓  ❑ ProtectJoin\n"
                                else: md+="├ ✗  ❑ ProtectJoin\n"
                                if msg.to in protectkick: md+="├ ✓  ❑ ProtectKick\n"
                                else: md+="├ ✗  ❑ ProtectKick\n"
                                if msg.to in protectcancel: md+="├ ✓  ❑ ProtectCancell\n"
                                else: md+="├ ✗  ❑ ProtectCancell\n"
                                if msg.to in protectinvite: md+="├ ✓  ❑ ProtectInvite\n╰─❑ Tuman-Bots ❑"
                                else: md+="├ ✗  ❑ ProtectInvite\n╰───────────────"
                                flextext(msg.to, str(md))
                                                                
                        elif cmd == "rejectall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    flex2(to, "Rejected {} Group Invite".format(str(len(ginvited))))
                                else:
                                    flex2(to, "Nothing")
                                
                        elif cmd == "cancelall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                        flexvian(to, "Nothing")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for inv in invitee:
                                            cl.cancelGroupInvitation(to, [inv])
                                        flex2(to, "Cancelled {} Group Pending".format(str(len(invitee))))
                                
                        elif cmd == "accept:all":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                    group = cl.getGroup(to)
                                    if group.invitee is None or group.invitee == []:
                                        flex2(to, "No Have Groups Invitation.")
                                    else:
                                        invitee = [contact.mid for contact in group.invitee]
                                        for acc in invitee:
                                            cl.acceptGroupInvitation(to, [acc])
                                        flex2(to, "Join {} Groups".format(str(len(invitee))))
                              
                        elif cmd == "logout":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                flexvian(msg.to, "Logout Success ♪")
                                sys.exit("Logout")
                               
                        elif cmd == "help js":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpjs()
                               flextext(msg.to, str(helpMessage1))
                              
                        elif cmd == "about":
                            if wait["selfbot"] == True:
                                if msg._from in admin:
                                    try:
                                        arr = []
                                        today = datetime.today()
                                        thn = 2018 
                                        bln = 8    #isi bulannya yg sewa
                                        hr = 9   #isi tanggalnya yg sewa
                                        future = datetime(thn, bln, hr)
                                        days = (str(future - today))
                                        comma = days.find(",")
                                        days = days[:comma]
                                        h = cl.getContact(clMID)
                                        groups = cl.getGroupIdsJoined()
                                        contactlist = cl.getAllContactIds()
                                        kontak = cl.getContacts(contactlist)
                                        favorite = cl.getFavoriteMids()
                                        fil = cl.getSettings().privacyReceiveMessagesFromNotFriend
                                        seal = cl.getSettings().e2eeEnable
                                        blockedlist = cl.getBlockedContactIds()
                                        src = cl.getSettings().privacySearchByUserid
                                        kontak2 = cl.getContacts(blockedlist)
                                        status = {"kick": "", "invite": ""}
                                        peler = {"receivercount": 0, "sendcount": 0}
                                        try:cl.kickoutFromGroup(to, [clMID]);status["kick"] = "Normal"
                                        except:status["kick"] = "Limit"
                                        try:cl.inviteIntoGroup(to, [clMID]);status["invite"] = "Normal"
                                        except:status["invite"] = "Limit"
                                        if src == True:alid = "Add From LineID : True"
                                        else:alid = "Add From LineID : False"                            
                                        if seal == True:letsel = "Letter Sealing : True"
                                        if seal == False:letsel = "Letter Sealing : False"
                                        if fil == True:fpes = "Filter Message : False"
                                        if fil == False:fpes = "Filter Message : True"
                                        kontol = "╭── • ABOUT SELFBOT • ──"
                                        kontol += "\n├ ◌ User : {}".format(h.displayName)
                                        kontol += "\n├ ◌ Group : {}".format(str(len(groups)))
                                        kontol += "\n├ ◌ Friend : {}".format(str(len(kontak)))
                                        kontol += "\n├ ◌ Favorite: {}".format(str(len(favorite)))
                                        kontol += "\n├ ◌ Blocked : {}".format(str(len(kontak2)))
                                        kontol += "\n├ ◌ Chat send : {}".format(str(peler["sendcount"]))
                                        kontol += "\n├ ◌ Chat received : {}".format(str(peler["receivercount"]))
                                        kontol += "\n├ ◌ {}".format(alid)
                                        kontol += "\n├ ◌ {}".format(letsel)
                                        kontol += "\n├ ◌ {}".format(fpes)
                                        kontol += "\n├ ◌ Kick : %s" % status["kick"]
                                        kontol += "\n├ ◌ Invite : %s" % status["invite"]
                                        kontol += "\n├ ◌ Type : Selfbot"
                                        kontol += "\n├ ◌ Version : TM V2\n╰────────────────"
                                        flextext(to, str(kontol))
                                    except Exception as e:
                                        cl.sendReplyMessage(msg.id,to, str(e))
                               
                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendReplyMessage(msg.id,to, "╭─「 Contact Info 」\n│ Nama : "+str(mi.displayName)+"\n│ Mid : " +key1+"\n│ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif ("/ti/g/" in msg.text):
                           if msg._from in admin or msg._from in staff:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    flex2(msg.to, "Masuk : %s" % str(group.name))

                        elif text.lower() == "clearchat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   flexvian(msg.to, "Cleared messages")
                               except:
                                   pass
                                
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:  
                                sep = text.split(" ")
                                txt = text.replace(sep [0] + " ","")
                                groups = cl.getGroupIdsJoined()
                                for group in groups:
                                    cl.sendMessage(group, "{}".format(str(txt)))
                                flex2(msg.to, "Broadcast {} Group".format(str(len(groups))))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               flex2(msg.to, "Setkey Anda: " + str(Setmain["keyCommand"]))
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flex2(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   flex2(msg.to, "Update to {}".format(str(key).lower()))

                        elif cmd.startswith("setsider: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendReplyMesage(msg.id,to, "Gagal mengganti key")
                               else:
                                   wait["mention"] = str(key).lower()
                                   flex2(msg.to, "Update to {}".format(str(key).lower()))

                        elif cmd.startswith("setreject: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flex2(msg.to, "Failed..!!")
                               else:
                                   wait["autoCancel"]["members"] = str(key).lower()
                                   flex2(msg.to, "Auto reject set to {}".format(str(key).lower()))

                        elif cmd.startswith("setapikey: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flex2(msg.to, "Gagal mengganti key")
                               else:
                                   wait["apikey"] = str(key).lower()
                                   flex2(msg.to, "Success update apikey")

                        elif cmd.startswith("setwelcome: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flex2(msg.to, "Failed..!!")
                               else:
                                   wait["welcome"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setleave: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flex2(msg.to, "Failed..!!")
                               else:
                                   wait["leave"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               flex2(msg.to, "Succes")

                        elif cmd == "1reboot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               flexvian(msg.to, "Waitting 1 second")
                               time.sleep(5)
                               Setmain["restartPoint"] = msg.to
                               flexvian(msg.to, "Be reboot to pee.")
                               restartBot()
                                                          
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                flexvian(msg.to, bot)
                               
                        elif cmd == "blocklist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="「 Blocked List 」\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                flextext(msg.to, msgs)
                                
                        elif cmd.startswith("delfriend "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.deleteContact(ls)
                                flex2(to, "Success Remove " + str(contact.displayName) + " to Friendlist")
                                
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃┃ " + str(a) + ". " +G.displayName+ "\n"
                               flextext(msg.id,to,"┏━━[ FRIEND LIST ]\n┃┃\n"+ma+"┃┃\n┗━━[ Total「"+str(len(gid))+"」Friends ]")
                               
                        elif cmd.startswith("bye:"):
                            if wait["selfbot"] == True:
                              if msg._from in admin:
                                  separate = cmd.split(":")
                                  number = cmd.replace(separate[0] + ":","")
                                  groups = cl.getGroupIdsJoined()
                                  try:
                                      group = groups[int(number)-1]
                                      G = cl.getGroup(group)
                                      try:
                                          cl.leaveGroup(G.id)
                                      except:
                                          cl.leaveGroup(G.id)
                                      flex2(msg.to, "Leave Group : " + G.name)
                                  except Exception as error:
                                      sendFoter(msg.to, str(error))

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendReplyMessage(msg.id,to, "╭─「 Group Info 」\n├↘ Nama Group : {}".format(G.name)+ "\n├↘ ID Group : {}".format(G.id)+ "\n├↘ Pembuat : {}".format(G.creator.displayName)+ "\n├↘ Waktu Dibuat : {}".format(str(timeCreated))+ "\n├↘ Jumlah Member : {}".format(str(len(G.members)))+ "\n├↘ Jumlah Pending : {}".format(gPending)+ "\n├↘ Group Qr : {}".format(gQr)+ "\n├↘ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendFoter(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╭───「 Group Info 」───"
                                ret_ += "\n├↘ Nama Group : {}".format(G.name)
                                ret_ += "\n├↘ ID Group : {}".format(G.id)
                                ret_ += "\n├↘ Pembuat : {}".format(gCreator)
                                ret_ += "\n├↘ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n├↘ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n├↘ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n├↘ Group Qr : {}".format(gQr)
                                ret_ += "\n├↘ Group Ticket : {}".format(gTicket)
                                ret_ += "\n├↘ Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += "\n╰──────────────"
                                flextext(msg.to, str(ret_))
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd.startswith("gurl "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("close "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "├↘ "+ str(no) + ". " + mem.displayName
                                flextext(msg.to,"├↘ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               flextext(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "buka qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   flexvian(msg.to, "Open Link Groups")

                        elif cmd == "tutup qr":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   flexvian(msg.to, "Blocked Url Groups")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendReplyMessage(msg.id,to, "Nama : "+str(x.name)+ "\nUrl : http://line.me/R/ti/g/"+gurl)
   
                        elif cmd == "order" or cmd == "promo":
                          if wait["selfbot"] == True:
                                kontol = wait["order"]
                                flextext(to, str(kontol))
                             
                        elif cmd == "creator" or cmd == "developer":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(sender)
                                data = { "type": "flex", "altText": "Tuman Bots", "contents":{ "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "image", "url": "https://i.ibb.co/YyDR7TM/ezgif-com-gif-maker-22.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                                sendTemplate(to, data)
                                                        
                        elif cmd == "me" or cmd == "aku":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                cover = cl.getProfileCoverURL(sender)
                                data = { "type": "flex", "altText": "Tuman Bots", "contents":{ "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover" } ], "position": "absolute", "width": "51px", "height": "51px", "offsetTop": "18px", "offsetEnd": "13px" }, { "type": "image", "url": "https://i.ibb.co/p2hgtcL/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute", "offsetStart": "1px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "75px", "height": "16px", "offsetTop": "54px", "offsetStart": "16px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "75px", "height": "16px", "offsetBottom": "49px", "offsetEnd": "14px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(status.statusMessage), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "136px", "height": "62px", "offsetTop": "76px", "offsetStart": "12px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute", "offsetStart": "1px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                                sendTemplate(to, data)
                                                      
                        elif cmd == "randomtiktok":
                          if msg._from in admin:
                            contact = cl.getContact(sender)
                            data = {
                                "type": "video",
                                "originalContentUrl": "https://rest.farzain.com/api/tiktok.php?apikey=fn",
                                "previewImageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                }
                            sendTemplate(to, data)
                            
                        elif cmd == "myliff":
                          if msg._from in admin:
                            if wait["selfbot"] == True:
                              ret_ = []
                              ret_.append({"thumbnailImageUrl": 'https://2.bp.blogspot.com/-_5b81bKClC4/XAEXlpG7PwI/AAAAAAAAAZ4/6MhJlHfSBrUdcn1vJngYvxP1sUZp-L3OQCLcBGAs/s1600/IMG_20181130_175412.JPG',"imageSize": "contain","imageAspectRatio": "square","title": 'FAKE EMAIL GENERATOR',"text": 'LIFF TYPE',"actions": [{"type": "uri","label": "👉 LIVE HERE 👈","uri": 'line://app/1623679774-bQ0ELEkW'}]})
                              ret_.append({"thumbnailImageUrl": 'https://1.bp.blogspot.com/-cmRUZ6qFAj4/VPF9oa5mU0I/AAAAAAAAiBw/YxFCYkmFZ6A/s728-e100/facebook-acccount-password.png',"imageSize": "contain","imageAspectRatio": "square","title": 'FACEBOOK.COM',"text": 'LIFF TYPE',"actions": [{"type": "uri","label": "👉 LIVE HERE 👈","uri": 'line://app/1609524990-mpvZ5xv5'}]})
                              ret_.append({"thumbnailImageUrl": 'https://topesdegama.com/app/uploads/2018/04/play-store-logo-color-750x400.jpg',"imageSize": "contain","imageAspectRatio": "square","title": 'PLAY STORE',"text": 'LIFF TYPE',"actions": [{"type": "uri","label": "👉 LIVE HERE 👈","uri": 'line://app/1623679774-qmmXPXJ5'}]})
                              ret_.append({"thumbnailImageUrl": 'https://www.youredm.com/wp-content/uploads/2015/08/soundcloud-ad.png',"imageSize": "contain","imageAspectRatio": "square","title": 'SOUNDCLOUD',"text": 'LIFF TYPE',"actions": [{"type": "uri","label": "👉 LIVE HERE 👈","uri": 'line://app/1623679774-lGOq9q3G'}]})
                              ret_.append({"thumbnailImageUrl": 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTM6fb1xTcHlkyD9LH-dw03naHyZcHVLAosv9R1A2es1RqC0QTr',"imageSize": "contain","imageAspectRatio": "square","title": 'HIGHWAY',"text": 'LIFF TYPE',"actions": [{"type": "uri","label": "👉 LIVE HERE 👈","uri": 'line://app/1623679774-j4rZkZ51'}]})
                              k = len(ret_)//5
                              for aa in range(k+1):
                                  data = {
                                      "type": "template",
                                      "altText": "💻Tuman Bots Team💻",
                                      "template": {
                                          "type": "carousel",
                                          "columns": ret_[aa*5 : (aa+1)*5]
                                      }
                                  }
                                  sendTemplate(to,data)       

                        elif cmd.startswith(comd["unsend"]):
                            if msg._from in admin:
                                sep = text.split(" ")
                                args = text.replace(sep[0] + " ", "")
                                mes = 0
                                try:
                                    mes = int(args[1])
                                except:
                                    mes = 1
                                M = cl.getRecentMessagesV2(to, 101)
                                MId = []
                                for ind, i in enumerate(M):
                                    if ind == 0:
                                        pass
                                    else:
                                        if i._from == cl.profile.mid:
                                            MId.append(i.id)
                                            if len(MId) == mes:
                                                break

                                def unsMes(id):
                                    cl.unsendMessage(id)

                                for i in MId:
                                    thread1 = threading.Thread(target=unsMes, args=(i,))
                                    thread1.start()
                                    thread1.join()
                                flexvian(to, "Unsend Message")       
                                                                                                                                    
                        elif cmd == "tag":
                          if msg._from in admin:
                            group = cl.getGroup(to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "「 Mention member 」\n"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n{}. @!".format(str(no))
                                ret_ += "\n\n「 Jumlah {} member 」".format(str(len(dataMid)))
                                khieMention(to, ret_, dataMid)    
   
                        elif cmd == comd["tagall"]:
                          if msg._from in admin:
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(to)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getCompactGroup(to)
                                members = [mem.mid for mem in group.members]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                mentionMembers2(to, members)
        
                        elif cmd.startswith("tag: "):
                          if msg._from in admin:
                            separate = msg.text.split(":")
                            number = msg.text.replace(separate[0] + ":"," ")
                            groups = cl.getGroupIdsJoined()
                            gid = groups[int(number)-1]                                                                                                      
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(gid)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getCompactGroup(gid)
                                members = [mem.mid for mem in group.members]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                mentionMembers2(gid, members)
                                flex2(msg.to, "Remote Mentions Group: " + str(group.name))                      
                        elif cmd == "tagall sticker":
                          if msg._from in admin:
                            members = []
                            if msg.toType == 1:
                                room = cl.getCompactRoom(to)
                                members = [mem.mid for mem in room.contacts]
                            elif msg.toType == 2:
                                group = cl.getCompactGroup(to)
                                members = [mem.mid for mem in group.members]
                            else:
                                return cl.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
                            if members:
                                FakeStickerV2(to,"11537" ,"52002736", members)
               
                        elif "https://www.smule.com" in msg.text.lower():
                            if wait["smule"] == True:
                                Ancok = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                Bikfareel = re.findall(Ancok, text)
                                Pokeh = []
                                for Nyaman in Bikfareel:
                                    if Nyaman not in Pokeh:
                                        Pokeh.append(Nyaman)
                                for Lottok in Pokeh:
                                    PokenahRengmadureh = Lottok
                                    headers = {
                                            }
                                    api = imjustgood(wait["apikey"])
                                    kontol = api.smuledl(Lottok)
                                    caption ="{}".format(kontol["result"]["caption"])
                                    title ="{}".format(kontol["result"]["title"])
                                    pict ="{}".format(kontol["result"]["thumbnail"])
                                    type ="Type : {}".format(kontol["result"]["type"])
                                    data = {"type": "flex","altText": "Tuman Bots ","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(pict), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/C0yjDzt/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(type), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(caption), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                                    sendTemplate(to, data)
                                if kontol["result"]["type"] == "video":
                                    sendFlexVideo(to, "{}".format(kontol["result"]["mp4Url"]))
                                else:
                                    sendFlexAudio(to, "{}".format(kontol["result"]["mp3Url"]))

                        elif "https://vt.tiktok.com/" in msg.text.lower():
                            if wait["tiktok"] == True:
                                Ancok = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                Bikfareel = re.findall(Ancok, text)
                                Pokeh = []
                                for Nyaman in Bikfareel:
                                    if Nyaman not in Pokeh:
                                        Pokeh.append(Nyaman)
                                for Lottok in Pokeh:
                                    PokenahRengmadureh = Lottok
                                    headers = {
                                            }
                                    kontol = requests.get("https://minz-restapi.xyz/tiktokdl?url={}".format(Lottok))
                                    main = kontol.text
                                    main = json.loads(main)
                                    sendFlexVideo(to, main["result"]["no_watermark"])

                        elif "https://youtu.be/" in msg.text.lower():
                            if wait["tiktok"] == True:
                                Ancok = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                                Bikfareel = re.findall(Ancok, text)
                                Pokeh = []
                                for Nyaman in Bikfareel:
                                    if Nyaman not in Pokeh:
                                        Pokeh.append(Nyaman)
                                for Lottok in Pokeh:
                                    PokenahRengmadureh = Lottok
                                    headers = {
                                            }
                                    kontol = requests.get("https://minz-restapi.xyz/youtubeurl?url={}".format(Lottok))
                                    main = kontol.text
                                    main = json.loads(main)
                                    cl.sendReplyMessage(msg.id,to, "{}".format(main["result"]["tittle"])) 
                                    sendFlexVideo(to, main["result"]["videoUrl"])
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                flexvian (msg.to,"Send a Picture ♪")
                                
                        elif cmd == "updatecover":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changeCover"][clMID] = True
                                flexvian(msg.to,"Send a Picture ♪")

                        elif cmd == "clfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["changeFoto"][clMID] = True
                                flexvian(msg.to,"Send a Picture ♪")

                        elif cmd == "ajsfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["changeFoto"][Zmid] = True
                                ajs.sendReplyMessage(msg.id,to,"Send a Picture ♪")
                               
                                
                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                flex2(msg.id,to,"Update to " + string + "")
                               
                                
                        elif cmd.startswith("ajsname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ajs.getProfile()
                                profile.displayName = string
                                ajs.updateProfile(profile)
                                ajs.sendReplyMessage(msg.id,to,"Update to " + string + "")

                        elif cmd.startswith("cek "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            mid = msg.text.replace(separate[0] + " ","")
                            if mid is not None:
                                listMid = mid.split("*")
                                if len(listMid) > 1:
                                    for a in listMid:
                                        cl.sendContact(to,a)
                                else:
                                    cl.sendContact(to,mid)

                        elif cmd.startswith("stag"):
                            if msg._from in admin:
                                gname = cl.getGroup(msg.to)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_RFU\n'
                                            atas = '\n╭───────────────\n│Mention {} '.format(str(gname.name))
                                            atas += '\n│Total {} Members\n╰───────────────'.format(str(len(local)))
                                        cl.sendMessage(to, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(to, str(error)) 

                        elif cmd.startswith("addtext "):
                            if msg._from in admin:
                                sep = text.split(" ")
                                apl = text.replace(sep[0] + " ","")
                                sam = apl.split("/")
                                chat1 = sam[0]
                                chat2 = sam[1]
                                apk = ""+chat1
                                tes["Message"][apk] = chat2
                                tes["msg"] = chat1
                                anu = tes["msg"]+'.'
                                cl.sendReplyMessage(msg.id,to,"Command %s created."%chat1)
                                tes["msg"] = {}

                        elif cmd == "list text":
                            if msg._from in admin:
                                if tes["Message"] == {}:
                                    cl.sendMessage(to,"empty text")
                                else:
                                    mc = ""
                                    jml = 1
                                    for listword in tes["Message"]:
                                        mc += "\n"+str(jml)+". "+listword+""
                                        jml += 1
                                    cl.sendReplyMessage(msg.id,to,"List text :\n"+str(mc))

                        elif cmd.startswith("deltext "):
                            	if msg._from in admin:
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in tes["Message"]:
                                        del tes["Message"][xres]                                        
                                        cl.sendReplyMessage(msg.id,to,"Command %s has been removed."%tetx)
                                    else:
                                        cl.sendReplyMessage(msg.id,to,"Command %s does not exist."%tetx)
                            
                        elif cmd == "screen -ls":
                          if msg._from in admin:
                              process = os.popen('screen -list')
                              a = process.read()
                              flextext(to, "{}".format(a))
                              process.close()

                        elif cmd == "myname":
                          if msg._from in admin:
                            h = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id,to,"「 Name 」\n"+str(h.displayName))
                            
                        elif cmd == "mybio":
                          if msg._from in admin:
                            h = cl.getContact(sender)
                            cl.sendReplyMessage(msg.id,to,"「 Status 」\n"+str(h.statusMessage))
                            
                        elif cmd == "mypict":
                          if msg._from in admin:
                            h = cl.getContact(sender)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            sendFlexImage(msg.to, str(image))     

                        elif cmd == "myvideo":
                          if msg._from in admin:
                            h = cl.getContact(sender)
                            if h.videoProfile == None:
                            	return cl.sendMessage(to, "「 Video 」\nNone")
                            sendFlexVideo(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")       
#===========BOT UPDATE============#                                                     
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                flextext(msg.to,"╭─「 User botlist」\n│\n│"+ma+"\n╰──「 Total「%s」User Botlist 」" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n│"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n│"
                                flextext(msg.to,"╭─「 List Admin Selfbot 」\n│\n│Owner:\n│"+ma+"\n│Admin:\n│"+mb+"\n│Staff:\n│"+mc+"\n╰──「Total「%s」Team 」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n│'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n│'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n│'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n│'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n│"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n│'
                                    me += str(e) + ". " +cl.getGroup(group).name + "\n"
                                flextext(msg.to,"╭─「 Setting Protection List 」\n│\n│ PROTECT URL :\n│"+ma+"\n│ PROTECT KICK :\n│"+mb+"\n│ PROTECT JOIN :\n│"+md+"\n│ PROTECT CANCEL:\n│"+mc+"\n│ PROTECT INVITE:\n│"+me+"\n╰──「 Total「%s」Protect 」" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))


                        elif cmd == comd["bye"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                flexvian(msg.to, "Selamat Tinggall..")
                                cl.leaveGroup(msg.to)

                        elif cmd == "respontime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                flextext(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == comd["speed"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                start = time.time()
                                cl.sendMessage("u0a94a68c058d99a72f95b420a0b7a493", "test speed")
                                speed = time.time() - start
                                ping = speed * 1000
                                flexvian(to, "Time {} Ms !".format(str(speedtest(ping))))
                                  
                             
                        elif cmd == comd["siderOn"]:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  flexvian(msg.to, "Sider Enable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == comd["siderOff"]:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  flexvian(msg.to, "Sider Disable ♪") #\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  flexvian(msg.to, "None Active..!!")
                             
                        elif cmd.startswith("find "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                a = cl.getGroupIdsJoined();i = cl.getGroups(a)
                                c = []
                                for h in i:
                                    g = [c.append(h.name[0:20]+',.s/'+str(len(h.members))) for d in h.members if key1 in d.mid]
                                h = "╭「 Find Contact 」─"
                                no = 0
                                for group in c:
                                    no += 1
                                    h+= "\n│{}. {} | {}".format(no, group.split(',.s/')[0], group.split(',.s/')[1])
                                flextext(msg.to,h+"\n╰─「 {} Groups I Found it 」".format(len(c)))                                
                                
                        elif cmd.startswith("tag "):
                          if msg._from in admin:
                            text = removeCmd("tag", text)
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ", text)
                            cond = text.split(" ")
                            jml = int(cond[0])
                            for x in range(jml):
                                name = cl.getContact(to)
                                FareelKiller(to, name.mid)
                                
                        elif cmd.startswith("spam "):
                          if msg._from in admin:
                            dzin = removeCmd("spam", text)
                            line = dzin.split("|")
                            count = int(line[1])
                            text1 = removeCmd("spam"+str(line[0])+"|"+str(count)+"|", text)
                            text2 = count * (text1+"\n")
                            if line[0] == "on":
                                if count <= 1000:
                                    for a in range(count):
                                        cl.sendMessage(msg.to, str(text1))
                                else:
                                    cl.sendMessage(msg.to, "Max 1000.")
                            if line[0] == "off":
                                if count <= 1000:
                                    cl.sendMessage(msg.to, str(text2))
                                else:
                                    cl.sendMessage(msg.to, "Max 1000.")
                            
                        elif cmd == "bitcoin":
                          if msg._from in admin:
                            r=requests.get("https://xeonwz.herokuapp.com/bitcoin.api")
                            data=r.text
                            data=json.loads(data)
                            hasil = "「 Bitcoin 」\n" 
                            hasil += "\n• Price : " +str(data["btc"])
                            hasil += "\n• Expensive : " +str(data["high"])
                            hasil += "\n• Cheap : " +str(data["low"])
                            flextext(msg.to, str(hasil))                            

                        elif cmd.startswith('github '):
                          if msg._from in admin:
                           args = text.split(" ")
                           search = text.replace(args[0] + " ","")
                           kontol = requests.get("http://dolphinapi.herokuapp.com/api/github?name={}".format(search))
                           data = kontol.text
                           data = json.loads(data)
                           kontol = "GITHUB SEARCH"
                           for b in data["result"]["repository"]:
                               kontol += "\n•{} \n{}".format(str(b["title"]), str(b["url"]))
                           kontol += "GITHUB SEARCH"
                           cl.sendReplyMessage(msg.id,to, str(kontol))

                        elif cmd == "cctv code":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data = api.cctv_code()
                           kontol = "RESULT CCTV"
                           for b in data["result"]["active"]:
                               kontol += "\n• {} {}".format(b,data["result"]["active"][b])
                           kontol += "{}\nExample : Cctv (number)"
                           flextext(msg.to, str(kontol))
                        elif cmd.startswith('cctv '):
                          if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.cctvSearch(userId)
                                  kontol = "DETAIL CCTV INFO"
                                  kontol += "\nArea : {}".format(data["result"]["area"])
                                  kontol += "\nWilayah : {}".format(data["result"]["wilayah"])
                                  flextext(msg.to, str(kontol))
                                  sendFlexVideo(to, "{}".format(data["result"]["video"]))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith('lyrik '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.lyric(userId)
                           vian = "Title : {}".format(data["result"]["title"])
                           vian += "\nArtist : {}".format(data["result"]["artist"])
                           vian += "\n{}".format(data["result"]["lyric"])
                           cl.sendReplyMessage(msg.id,to, str(vian))         

                        elif cmd == "clearallfriend":
                          if msg._from in admin:
                            n = len(cl.getAllContactIds())
                            try:
                                cl.clearContacts()
                            except: 
                                pass
                            t = len(cl.getAllContactIds())
                            flextext(msg.to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
#===========Hiburan============#
                        elif cmd.startswith("eng:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('en', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("indo:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('id', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jp:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ja', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("india:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('hi', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("sunda:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('su', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("china:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('zh-cn', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("arab:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ar', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("rusia:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ru', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("thai:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('th', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("spanyol:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('es', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("franchis:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('fr', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("korea:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ko', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("malay:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('ms', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("turki:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('tr', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("jawa:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('jw', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("itali:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('it', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("belanda:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('nl', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("filipin:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('tl', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("german:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('de', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("vietnam:"):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                res = api.translate('vi', query)
                                vian = "{}".format(res["result"]["translate"])
                                cl.sendReplyMessage(msg.id,to, str(vian))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("joox:"):
                           if msg._from in admin:
                                set = text.split(" ")
                                userId = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.joox(userId)
                                title = "{}".format(data["result"]["title"])
                                durasi = "{}".format(data["result"]["duration"])
                                artis = "{}".format(data["result"]["singer"])
                                size = "{}".format(data["result"]["size"])
                                img = "{}".format(data["result"]["thumbnail"])
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                KONTOL = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/C0yjDzt/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(artis), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                                sendTemplate(to, KONTOL)  
                                sendFlexAudio(to, "{}".format(data["result"]["mp3Url"]))

                        elif cmd.startswith('ytmp3 '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.youtube(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           autor = "{}".format(data["result"]["author"])
                           audio = "{}".format(data["result"]["audioUrl"])
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           KONTOL = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/C0yjDzt/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(autor), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexAudio(to, "{}".format(data["result"]["audioUrl"]))

                        elif cmd.startswith('porn '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.porn(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           quality = "Quality : {}".format(data["result"]["quality"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           KONTOL = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/C0yjDzt/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(quality), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('ytmp4 '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api  = imjustgood(wait["apikey"])
                           data = api.youtube(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           autor = "{}".format(data["result"]["author"])
                           audio = "{}".format(data["result"]["audioUrl"])
                           durasi = "Durasi : {}".format(data["result"]["duration"])
                           img = "{}".format(data["result"]["thumbnail"])
                           title = "{}".format(data["result"]["title"])
                           wath = "{}".format(data["result"]["watched"])
                           KONTOL = { "type": "flex", "altText": "Tuman Bots", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(img), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "40px", "height": "40px", "offsetTop": "12px", "offsetEnd": "13.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/GdyLZ5d/ezgif-com-gif-maker-69.png", "size": "100px", "aspectRatio": "2:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "100px", "height": "40px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/C0yjDzt/ezgif-com-gif-maker-21.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(autor), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "13px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(durasi), "size": "7px", "color": "#00ffff", "align": "center" } ], "position": "absolute", "width": "94px", "height": "11px", "offsetTop": "26.5px", "offsetStart": "10px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(title), "size": "7px", "color": "#00ffff", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "131.5px", "height": "11px", "offsetBottom": "15.5px", "offsetEnd": "13.5px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                           sendTemplate(to, KONTOL)         
                           sendFlexVideo(to, "{}".format(data["result"]["videoUrl"]))

                        elif cmd.startswith('cuaca '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.cuaca(userId)
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           kontol = "╭───「 INFO CUACA 」───"
                           kontol += "\n├⌬ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')
                           kontol += "\n├⌬ Tanggal : "+datetime.strftime(timeNow,'%d-%m-%Y')
                           kontol += "\n├⌬ Lokasi : {}".format(data["result"]["location"])
                           kontol += "\n├⌬ Cuaca : {}".format(data["result"]["description"])
                           kontol += "\n├⌬ Suhu : {}".format(data["result"]["humidity"])
                           kontol += "\n├⌬ Tempratur : {}".format(data["result"]["temperature"])
                           kontol += "\n├⌬ Angin : {}".format(data["result"]["wind"])
                           kontol += "\n╰───────────────"         
                           flextext(msg.to, str(kontol))

                        elif cmd.startswith('sholat '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.adzan(userId)
                           kontol = "╭───「 INFO SHOLAT 」───"
                           kontol += "\n├⌬ Date : {}".format(data["result"]["tanggal"])
                           kontol += "\n├⌬ Wilayah : {}".format(data["result"]["wilayah"])
                           kontol += "\n├⌬ Ashar : {}".format(data["result"]["adzan"]["ashar"])
                           kontol += "\n├⌬ Duha : {}".format(data["result"]["adzan"]["dhuha"])
                           kontol += "\n├⌬ Dzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
                           kontol += "\n├⌬ Imsyak : {}".format(data["result"]["adzan"]["imsyak"])
                           kontol += "\n├⌬ Isya : {}".format(data["result"]["adzan"]["isya"])
                           kontol += "\n├⌬ Mag'rib : {}".format(data["result"]["adzan"]["maghrib"])
                           kontol += "\n├⌬ Subuh : {}".format(data["result"]["adzan"]["subuh"])
                           kontol += "\n├⌬ Fajar : {}".format(data["result"]["adzan"]["terbit"])
                           kontol += "\n╰────────────────"         
                           flextext(msg.to, str(kontol))       

                        elif cmd == "corona":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data = api.corona()
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           kontol = "╭──「 CORONA VIRUS 」──"
                           kontol += "\n├⌬ TIME : "+datetime.strftime(timeNow,'%H:%M:%S')
                           kontol += "\n├⌬ DATE : {}".format(data["result"]["date"])
                           kontol += "\n├⌬─────────────⌬"
                           kontol += "\n├⌬ INDONESIA"
                           kontol += "\n├⌬ TERJANGKIT : {}".format(data["result"]["indonesia"]["case"])
                           kontol += "\n├⌬ SEMBUH : {}".format(data["result"]["indonesia"]["fit"])
                           kontol += "\n├⌬ MENINGGAL : {}".format(data["result"]["indonesia"]["rip"])
                           kontol += "\n├⌬─────────────⌬"
                           kontol += "\n├⌬ SELURUH DUNIA"
                           kontol += "\n├⌬ TERJANGKIT : {}".format(data["result"]["world"]["case"])
                           kontol += "\n├⌬ SEMBUH : {}".format(data["result"]["world"]["fit"])
                           kontol += "\n├⌬ MENINGGAL : {}".format(data["result"]["world"]["rip"])
                           kontol += "\n╰────────────────"         
                           flextext(msg.to, str(kontol))        

                        elif cmd == "surahlist":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data = api.alquran()
                           vian  = "LIST SURAH AL-QUR'AN"
                           for qs in data:
                               vian += "\n{}".format(qs)
                           flextext(to, str(vian))

                        elif cmd.startswith('surah '):
                          if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.alquranQS(userId) 
                                  audioUrl = data["result"]["audio"]
                                  vian = "Di Turunkan Di :{}\n".format(data["result"]["place"])
                                  vian += "{}".format(data["result"]["desc"])
                                  cl.sendReplyMessage(msg.id,to, (vian))
                                  sendFlexAudio(to, str(audioUrl))
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to, "ERROR!\nText Terlalu Panjang!!")         

                        elif cmd == "info bmkg":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data = api.bmkg()
                           kontol = "╭──「 INFO BMKG 」──"
                           kontol += "\n├⌬ Time : {}".format(data["result"]["pukul"])
                           kontol += "\n├⌬ Date : {}".format(data["result"]["tanggal"])
                           kontol += "\n├⌬ Wilayah : {}".format(data["result"]["wilayah"])
                           kontol += "\n├⌬ Kekuatan : {}".format(data["result"]["kekuatan"])
                           kontol += "\n├⌬ Kedalaman : {}".format(data["result"]["kedalaman"])
                           kontol += "\n├⌬ Kordinat : {}".format(data["result"]["kordinat"])
                           kontol += "\n├⌬ Lokasi : {}".format(data["result"]["lokasi"])
                           kontol += "\n├⌬ Arhan : {}".format(data["result"]["arahan"])
                           kontol += "\n├⌬ Saran : {}".format(data["result"]["saran"])
                           kontol += "\n╰─────────────"         
                           flextext(msg.to, str(kontol))        

                        elif cmd.startswith('fancytext '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.fancy(userId) 
                           vian = "FANCY RESULT :\n"
                           for s in data["result"]:
                               vian += "\n{}\n".format(s)
                           cl.sendReplyMessage(msg.id,to, str(vian))         

                        elif cmd.startswith('acaratv '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.acaratv_channel(userId) 
                           vian = "Jadwal Acara TV"
                           for a in data["result"]:
                               vian += "\n{}".format(a)
                           flextext(msg.to, str(vian))    

                        elif cmd == "acara tv":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data   = api.acaratv()
                           result = "ACARA TV"
                           for a in data["result"]:
                               for b in a:
                                   result += "\n\nChannel : {}".format(b)
                                   for c in a[b]:
                                       result += "\n{}".format(c)
                           flextext(msg.to, str(result))      

                        elif cmd == "info loker":
                          if msg._from in admin:
                           api = imjustgood(wait["apikey"])
                           data   = api.karir()
                           number = 0
                           apkbot = "INFO LOWONGAN KERJA"
                           for a in data["result"]:
                               number += 1
                               apkbot += "\n\n{}. {}".format(number,a["perusahaan"])
                               apkbot += "\nLokasi : {}".format(a["lokasi"])
                               apkbot += "\nProfesi : {}".format(a["profesi"])
                               apkbot += "\nBagian : {}".format(a["bagian"])
                               apkbot += "\nJabatan : {}".format(a["jabatan"])
                               apkbot += "\nGaji : {}".format(a["gaji"])
                               apkbot += "\nPendidikan : {}".format(a["pendidikan"])
                               apkbot += "\nPengalaman : {}".format(a["pengalaman"])
                               apkbot += "\nSyarat : {}".format(a["syarat"])
                               apkbot += "\nDeskirpsi : {}".format(a["deskripsi"])
                               apkbot += "\nSumber : {}".format(a["sumber"])
                           cl.sendReplyMessage(msg.id,to, str(apkbot))     

                        elif cmd.startswith("zodiak"):
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.zodiac(search)
                                vian = "╭─── • ZODIAK • ──"
                                vian += "\n├≽ Sign : {}".format(data["result"]["zodiac"])
                                vian += "\n├≽ Couple : {}".format(data["result"]["couple"])
                                vian += "\n├≽ Date Range : {}".format(data["result"]["date"])
                                vian += "\n├≽ Lucky Color : {}".format(data["result"]["color"])
                                vian += "\n├≽ Lucky Time : {}".format(data["result"]["time"])
                                vian += "\n├≽ Lucky Number : {}".format(data["result"]["number"])
                                vian += "\n├≽ Public : {}".format(data["result"]["public"])
                                vian += "\n├≽ Money : {}".format(data["result"]["money"])
                                vian += "\n├≽ Love Couple : {}".format(data["result"]["love"]["couple"])
                                vian += "\n├≽ Love Single : {}".format(data["result"]["love"]["single"])
                                vian += "\n╰── • TM_BOTS • ──"
                                cl.sendReplyMessage(msg.id,to, str(vian)) 

                        elif cmd.startswith('instagram '):
                          if msg._from in admin:
                              try:
                                  args = text.split(" ")
                                  userId = text.replace(args[0] + " ","")
                                  api = imjustgood(wait["apikey"])
                                  data = api.instagram(userId) 
                                  user = "{}".format(data["result"]["username"])
                                  folwer = "{}".format(data["result"]["follower"])
                                  folwing = "{}".format(data["result"]["following"])
                                  post = "{}".format(data["result"]["post"])
                                  bio = "{}".format(data["result"]["biography"])
                                  pict = "{}".format(data["result"]["picture"])
                                  INSTA = {"type": "flex","altText": "𝐌𝐎𝐍𝐒𝐓𝐄𝐑_𝐁𝐎𝐓𝐒","contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/vz3vV2G/ezgif-com-gif-maker-16.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(pict), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "102px", "height": "102px", "offsetTop": "20px", "offsetStart": "29px" }, { "type": "image", "url": "https://i.ibb.co/rfj2q51/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "3:4", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(user), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "113px", "height": "10px", "offsetTop": "7px", "offsetStart": "24px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(folwer), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "127px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(folwing), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "142px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(post), "size": "7px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "90px", "height": "10px", "offsetTop": "156px", "offsetStart": "35px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(bio), "size": "7px", "color": "#00ff00", "wrap": True, "align": "center" } ], "position": "absolute", "width": "130px", "height": "30px", "offsetBottom": "16px", "offsetStart": "15px" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u1c5233bdc0da4800d07131656e106068" } } }
                                  sendTemplate(to, INSTA)           
                              except Exception as error:
                                  cl.sendReplyMessage(msg.id,to,str(error))

                        elif cmd.startswith('google '):
                          if msg._from in admin:
                           args = text.split(" ")
                           userId = text.replace(args[0] + " ","")
                           api = imjustgood(wait["apikey"])
                           data = api.search(userId) 
                           pretyPrintJson(data)
                           number = 0
                           result = "GOOGLE SEARCH RESULT :"
                           for s in data["result"]:
                               number += 1
                               result += "\n{}. {}".format(number,s["title"])
                               result += "\n{}".format(s["snippet"])
                               result += "\n{}".format(s["url"])
                           cl.sendReplyMessage(msg.id,to, str(result))                  

                        elif cmd.startswith("ponsel"):
                            if msg._from in admin:
                                set = text.split(" ")
                                search = text.replace(set[0] + " ","")
                                api = imjustgood(wait["apikey"])
                                data = api.cellular(search)
                                pretyPrintJson(data)
                                number = 0
                                vian = "SPESIFIKASI PONSEL\n"
                                for a in data["result"]:
                                    number += 1
                                    vian += "\n• {}. {}\n".format(number,a["brands"])
                                    vian += "\n• Release : {}".format(a["release"])
                                    vian += "\n• Chipset : {}".format(a["chipset"])
                                    vian += "\n• Screen : {}".format(a["screen"])
                                    vian += "\n• Battery : {}".format(a["battery"])
                                    vian += "\n• Display : {}".format(a["display"])
                                    vian += "\n• Ram : {}".format(a["ram"])
                                    vian += "\n• Storage : {}\n".format(a["storage"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
 
                        elif cmd.startswith("resi-sicepat:"):
                          if msg._from in admin:
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"sicepat")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))
 
                        elif cmd.startswith("resi-pos:"):
                          if msg._from in admin:
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"pos")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-rex:"):
                          if msg._from in admin:
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"rex")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-jnt:"):
                          if msg._from in admin:
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"jnt")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))

                        elif cmd.startswith("resi-ninja:"):
                          if msg._from in admin:
                            try:
                                memek = text.split(" ")
                                ngewe = text.replace(memek[0] + " ","")
                                api = BEAPI(wait["apikey2"])
                                kontol = api.trackingResi(ngewe,"ninja")
                                vian  = "{}\n".format(kontol["result"]["summary"]["courier_name"])
                                vian += "Resi : {}\n".format(kontol["result"]["summary"]["waybill_number"])
                                vian += "Tanggall : {}\n".format(kontol["result"]["delivery_status"]["pod_date"])
                                vian += "Jam : {}\n".format(kontol["result"]["delivery_status"]["pod_time"])
                                vian += "Penerima : {}\n".format(kontol["result"]["delivery_status"]["pod_receiver"])
                                vian += "Status : {}\n".format(kontol["result"]["delivery_status"]["status"])
                                for a in kontol["result"]["manifest"]:
                                    vian += "\n\n{}".format(a["manifest_description"])
                                    vian += "\nJam : {}".format(a["manifest_time"])
                                    vian += "\nTanggal :{}".format(a["manifest_date"])
                                    vian += "\nTanggal :{}".format(a["city_name"])
                                cl.sendReplyMessage(msg.id,to, str(vian)) 
                            except Exception as error:
                                cl.sendReplyMessage(msg.id,to, str(error))
                                                                                    
                        elif cmd.startswith("gnamegrup"):
                          if msg._from in admin:
                            if msg.toType == 2:
                                X = cl.getGroup(to)
                                X.name = text.split(" ")
                                cl.updateGroup(X)
                                                               
                        elif cmd.startswith("spamtag "):
                          if msg._from in admin:
                            text_ = cmd.replace("spamtag ", "")
                            cond = text_.split(" ")
                            text = text_.replace(cond[0] + " ", "")
                            jml = int(cond[0])
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    text = text.replace("@{}".format(str(contact.displayName)),"")
                                if "|" in text:
                                    cond = text.split("|")
                                    fm = cond[0]
                                    lm = cond[1]
                                else:
                                    fm = ""
                                    lm = text
                                for ls in lists:
                                    for x in range(jml):
                                        sendMention(to, ls, str(fm), str(lm))
                                cl.sendReplyMessage(msg.id,to, "「 Succes tag {} user , with amount {} tags 」".format(str(len(lists)), str(jml)))
                                return
                            else:
                                flexvian(msg.to, "Nothing user :v")
                                return
                                    
                        elif cmd.startswith("call "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                group = cl.getGroup(to)
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,500):                                        	
                                        cl.acquireGroupCallRoute(to)                                            
                                        members = [ls for ls in lists]
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                    try:
                                        flex2(msg.to,"Success 500 invite call group")
                                        break
                                    except Exception as error:
                                        logError(error)                     
                                                       
                             
                        elif cmd.startswith("block "):
                          if msg._from in admin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.blockContact(ls)
                                flex2(msg.to, "Success block " + str(contact.displayName) + " to Blocklist")


                        elif cmd == "change vp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["changevp"] = True
                                flexvian(msg.to, "Kirim Video ny")

                        elif cmd.startswith("cvp: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sep = text.split(" ")
                                FckVeza = text.replace(sep[0] + " ","")
                                FckVezaGans = cl.getContact(sender)
                                flexvian(msg.to, "Loading...")
                                pic = "http://dl.profile.line-cdn.net/{}".format(FckVezaGans.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output vp.mp4 {}'.format(FckVeza))
                                pict = cl.downloadFileURL(pic)
                                vids = "vp.mp4"
                                changeVideoAndPictureProfile(pict, vids)
                                flexvian(msg.to, "Dual Profile Video ♪")
                                os.remove("vp.mp4")
                                
                        elif cmd.startswith("scall "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            num = int(sep[1])
                            try:                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            group = cl.getGroup(to)
                                            members = [ls]
                                            kunkun = cl.getContact("u176ef6889643e290ba5801bffc83457b").displayName
                                            cl.acquireGroupCallRoute(to)
                                            cl.inviteIntoGroupCall(to, contactIds=members)
                                        flex2(msg.to, "Success Invite Groups Call")
                            except Exception as error:
                                flexvian(to, str(error))
                                      
                        elif cmd == "cinema xx1":
                          if msg._from in admin:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "[ Cinema XX1 ]\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            flextext(to, str(hasil))
                                        
                        elif cmd.startswith("fs "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=nda12345&text={}".format(txt)
                            cl.sendImageWithURL(to, url)             

                        elif cmd.startswith("anime: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            judul = msg.text.replace(sep[0] + " ","")
                            tahun = msg.text.replace(sep[1] + " ","")
                            r=requests.get('https://www.omdbapi.com/?t='+judul+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                            data=r.text
                            data=json.loads(data)
                            ret_ = "「 Anime Search 」"
                            ret_ += "\nTitle : " +str(data["Title"])  + " ("+str(data["Year"])+ ")"
                            ret_ += "\n\n " + str(data["Plot"])
                            ret_ += "\n\nSumber Info: https://myanimelist.net/anime"                       
                            img = data["Poster"]
                            sendFlexImage(msg.to,str(img))
                            cl.sendReplyMessage(msg.id,to, str(ret_))
                                                                                             
                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                flexvian(msg.to,"Changed to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                flexvian(msg.to,"Changed to " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
        
                        elif cmd.startswith('pict '):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               res = '╭───「 Picture Status 」'
                               no = 0
                               if 'MENTION' in msg.contentMetadata.keys():
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       profile = cl.getContact(mentions['MENTIONEES'][0]['M'])
                                       if profile.pictureStatus:
                                           path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                                           cl.sendImageWithURL(to, path)
                                       else:
                                           flex2(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                
                        elif cmd.startswith('cover '):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                               res = '╭───「 Picture Cover 」'
                               no = 0
                               if 'MENTION' in msg.contentMetadata.keys():
                                   mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   if len(mentions['MENTIONEES']) == 1:
                                       mid = mentions['MENTIONEES'][0]['M']
                                       cover = cl.getProfileCoverURL(mid)
                                       cl.sendImageWithURL(to, cover)
                                   else:
                                       flex2(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                                    
                        elif cmd.startswith("video "):
                          if msg._from in admin:  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    if contact.videoProfile == None:
                                    	continue
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "/vp"
                                    cl.sendVideoWithURL(to, str(path))
                                                                            
                        elif cmd.startswith("name "):
                          if msg._from in admin:  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMesage(msg.id,to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                                    
                        elif cmd.startswith("bio "):
                          if msg._from in admin:  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendReplyMesage(msg.id,to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                                
                        elif cmd.startswith("addfriend "):
                          if msg._from in admin:  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.findAndAddContactsByMid(ls)
                                flex2(msg.to, "Success Add " + str(contact.displayName) + " to Friendlist")
                                
                        elif cmd.startswith("ulti "):
                          if msg._from in admin:  
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        cl.kickoutFromGroup(to, [ls])
                                        cl.inviteIntoGroup(to, [ls])
                                        cl.cancelGroupInvitation(to, [ls])
                                    except:
                                       flexvian(msg.to, "Limited !")
      
                        elif cmd.startswith("invite "):
                                if msg._from in creator or msg._from in owner or msg._from in admin:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:                                                                            
                                        try:      
                                            cl.findAndAddContactsByMid(target)
                                            cl.inviteIntoGroup(to,[target])                                             
                                        except:
                                            pass

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                flexvian(msg.to, "Success {} Call Groups".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendReplyMesage(msg.id,to, str(e))
                                else:
                                    cl.sendReplyMesage(msg.id,to, "Jumlah melebihi batas")

                        elif cmd.startswith("spamcall "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                flexvian(msg.to,"Success {} Call Groups".format(str(strnum)))
                                jumlah = int(strnum)
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           cl.acquireGroupCallRoute(to)
                                           cl.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendReplyMesage(msg.id,to, str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'idline: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('idline: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendReplyMesage(msg.id,to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif msg.text.lower() in tes["Message"]:
                            if wait["autotext"] == True:
                                sid = tes["Message"][msg.text.lower()]
                                cl.sendReplyMessage(msg.id, to, sid)     
                                    
                        elif msg.text.lower() in wait["stickers"]:
                           if wait["apkTikel"] == True:
                             if msg.text.lower() in wait["stickers"]:
                                 sid = wait["stickers"][msg.text.lower()]["STKID"]
                                 data = {
                                     "type": "template",
                                     "altText": "Sticker",
                                     "baseSize": { #
                                         "height": 1040, #
                                         "width": 1040 #
                                     }, #
                                     "template": {
                                         "type": "image_carousel",
                                         "columns": [{
                                             "imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid), 
                                             "action": {
                                                 "type": "uri",
                                                 "uri": "line://ti/p/~tm_bots",
                                                 "area": {
                                                     "x": 520,
                                                     "y": 0,
                                                     "width": 520,
                                                     "height": 1040
                                                 }
                                             }
                                         }]
                                     }
                                 }
                                 sendTemplate(to, data)      
                                    
                        elif cmd.startswith("dellsticker: "):
                          if msg._from in admin:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama not in wait["stickers"]:
                                        flexvian(msg.to,"List Sticker Kosong.")
                                    else:
                                        del wait["stickers"][nama]
                                        f=codecs.open("sticker.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexvian(msg.to,"Hapus Sticker ✓")
                                except Exception as e:
                                    cl.sendReplyMessage(msg.id,to,"{}".format(str(e)))
                                    
                        elif cmd.startswith("stickerlist"):
                          if msg._from in admin:
                                if wait["stickers"] == {}:
                                    flex3(msg.to,"Nothing sticker")
                                else:
                                    no = 0
                                    ret_ = "List\n"
                                    for a in wait["stickers"]:
                                        no += 1
                                        ret_ += "\n" +str(no)+". " +str(a)
                                    ret_ += "\n\nList %i Sticker" % len(wait["stickers"])
                                    cl.sendReplyMessage(msg.id,to, str(ret_))  
  
                        elif cmd.startswith("addsticker: "):
                          if msg._from in admin:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama in wait["stickers"]:
                                        flexvian(msg.to,"Sudah ada dalam list")
                                    else:
                                        wait["stk"] = nama
                                        wait["sticker"] = True
                                        f=codecs.open("sticker.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexvian(msg.to,"Send a stickers ✓")
                                except Exception as e:
                                    cl.sendMessage(msg.to,"{}".format(str(e)))
                   
#===========Protection============#
                        elif cmd.startswith("welcomemsg "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Sudah Aktif ♪"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  flexvian(msg.to, "Welcome Enable ✓")
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    flexvian(msg.to, "Welcome Disable ✓")

                                
                        elif cmd.startswith("leavemsg "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in leave:
                                       msgs = "Leave Msg sudah aktif"
                                  else:
                                       leave.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Leave Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  flexvian(msg.to, "Leave Msg Enable ✓")
                              elif spl == 'off':
                                    if msg.to in leave:
                                         leave.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Leave Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Leave Msg sudah tidak aktif"
                                    flexvian(msg.to, "Leave Msg Disable ✓")

                        elif cmd.startswith("pqr "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  flex2(msg.to, "Protect qr enable")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    flex2(msg.to, "Protect qr disable")

                        elif cmd.startswith("pkick "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  flex3(msg.to, "Protect kick enable")
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    flex2(msg.to, "Protect kick disable")

                        elif cmd.startswith("pjoin "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  flex2(msg.to, "Protect join enable")
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    flex2(msg.to, "Protect join disable")

                        elif cmd.startswith("pcancell "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  flex2(msg.to, "Protect cancel enable")
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    flex2(msg.to, "Protect cancel disable")
                        
                        elif cmd == "!cek":
                            if msg._from in admin:
                               try:cl.inviteIntoGroup(to, ["u02049c241027dcb7c16e6263746f6025"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u02049c241027dcb7c16e6263746f6025"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Normal 💯"
                               else:sil = "limit"
                               if has1 == "OK":sil1 = "Norma 💯l"
                               else:sil1 = "limit"
                               cl.sendReplyMessage(msg.id,to,"Kick: {} \nInvite: {}".format(sil1,sil))                                                                               
                               try:ajs.inviteIntoGroup(to, ["u02049c241027dcb7c16e6263746f6025"]);has = "OK"
                               except:has = "NOT"
                               try:ajs.kickoutFromGroup(to, ["u02049c241027dcb7c16e6263746f6025"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "Normal 💯"
                               else:sil = "limit"
                               if has1 == "OK":sil1 = "Normal 💯"
                               else:sil1 = "limit"
                               ajs.sendReplyMessage(msg.id,to,"Kick: {} \nInvite: {}".format(sil1,sil))

                        elif cmd.startswith("pinvite "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect in : " +str(ginfo.name)
                                  flex2(msg.to, "Protect invite enable")
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    flex2(msg.to, "Protect invite disable")

                        elif cmd.startswith("maxpro "):
                           if msg._from in admin:
                              vian = text.split(" ")
                              spl = text.replace(vian[0] + " ","")
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Max protection enable "
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Max protection allready On"
                                  flex2(msg.to, "All protection enable")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Max protection Disable"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Max protection allready disble"
                                    flex2(msg.to, "All protection disable")

#===========KICKOUT============#

                        elif cmd.startswith(comd["kick"]):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.sendMentionV2(msg.to,"@! \nMinggat kau fuck..", [target])
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#

                        elif cmd.startswith("staffadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMentionV2(msg.to,"@! \nPromote to staff ✓", [target])
                                       except:
                                           pass

                        elif cmd.startswith("botadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMentionV2(msg.to,"@! \nSucces add bots ✓", [target])
                                       except:
                                           pass

                        elif cmd.startswith("adminadd "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMentionV2(msg.to,"@! \nPromote to admin ✓", [target])
                                       except:
                                           pass

                        elif cmd.startswith("staffdell "):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in FareelBots:
                                       try:
                                           staff.remove(target)
                                           cl.sendMentionV2(msg.to,"@! \nHas ben removed staff ✓", [target])
                                       except:
                                           pass

                        elif cmd.startswith("botdell "):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in FareelBots:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMentionV2(msg.to,"@! \nBotlist removed ✓", [target])
                                       except:
                                           pass

                        elif cmd.startswith("admindell "):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in FareelBots:
                                       try:
                                           admin.remove(target)
                                           cl.sendMentionV2(msg.to,"@! \nHas ben removed admin ✓", [target])
                                       except:
                                           pass
                                           
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                flexvian(msg.to,"Send Contact ✓")

                        elif cmd == "refresh" or text.lower() == 'abort':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                flexvian(msg.to,"Command Aborted")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif "assalamualaikum" in msg.text.lower():
                             if wait["responsalam"] == True:  
                                cl.sendReplyMessage(msg.id,to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif cmd == "notag on":
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                ret = "Notag Enable ✓"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "notag off":
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                ret = "Notag Disable ✓"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "respon on":
                            if msg._from in admin:
                                wait["respontag"] = True
                                ret = "Auto Respon Enable ✓"
                                flexvian(msg.to, str(ret))
                           
                        elif cmd == "respon off":
                            if msg._from in admin:
                                wait["respontag"] = False
                                ret = "Auto Respon Disable ✓"
                                flexvian(msg.to, str(ret))
                           
                        elif cmd == "autoread on":
                            if msg._from in admin:
                                Setmain["autoRead"] = True
                                ret = "Auto Read Enable ✓"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autoread off":
                            if msg._from in admin:
                                Setmain["autoRead"] = False
                                ret = "Auto Read Disable ✓"
                                flexvian(msg.to, str(ret))

                        elif cmd == "contact on":
                            if msg._from in admin:
                                wait["contact"] = True
                                ret = "Detail contact Enable ✓"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "contact off":
                            if msg._from in admin:
                                wait["contact"] = False
                                ret = "Detail Contact Disable ✓"
                                flexvian(msg.to, str(ret))

                        elif cmd == "autotext on":
                            if msg._from in admin:
                                wait["autotext"] = True
                                ret = "Autotext Enable ✓"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autotext off":
                            if msg._from in admin:
                                wait["autotext"] = False
                                ret = "Autotext Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "autoblock on":
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                ret = "Auto Block Enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autoblock off":
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                ret = "Auto Block Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                ret = "Unsend Chat Enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                ret = "Unsend Chat Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "timeline on":
                            if msg._from in admin:
                                wait["Timeline"] = True
                                ret = "Detail Post Enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "timeline off":
                            if msg._from in admin:
                                wait["Timeline"] = False
                                ret = "Detail Post Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "autojoin on":
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                ret = "Auto Join Enable."
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autojoin off":
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                ret = "Auto Join Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "autoleave on":
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                ret = "Auto Leave Enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autoleave off":
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                ret = "Auto Leave Disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "autoadd on":
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                ret = "Auto Add Enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autoadd off":
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                ret = "Auto Add Disable"
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "tikelgede on":
                            if msg._from in admin:
                                wait["apkTikel"] = True
                                ret = "Sticker Temp On."
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "tikelgede off":
                            if msg._from in admin:
                                wait["apkTikel"] = False
                                ret = "Sticker Temp Off"
                                flexvian(msg.to, str(ret))

                        elif cmd == "sticker on":
                            if msg._from in admin:
                                wait["sticker"] = True
                                ret = "Detail Sticker On"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "sticker off":
                            if msg._from in admin:
                                wait["sticker"] = False
                                ret = "Detail sticker Off"
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "smule on":
                            if msg._from in admin:
                                wait["smule"] = True
                                ret = "Detect smule On"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "smule off":
                            if msg._from in admin:
                                wait["smule"] = False
                                ret = "Detect smule Off"
                                flexvian(msg.to, str(ret))

                        elif cmd == "tiktok url on":
                            if msg._from in admin:
                                wait["tiktok"] = True
                                ret = "Tiktok url enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "tiktok url off":
                            if msg._from in admin:
                                wait["tiktok"] = False
                                ret = "Tiktok url disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "yt url on":
                            if msg._from in admin:
                                wait["yturl"] = True
                                ret = "youtube url enable"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "yt url off":
                            if msg._from in admin:
                                wait["yturl"] = False
                                ret = "youtube url disable"
                                flexvian(msg.to, str(ret))

                        elif cmd == "jointicket on":
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                ret = "Join Ticket On."
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "jointicket off":
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                ret = "Join Ticket Off."
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "autolike on":
                            if msg._from in admin:
                                wait["likeOn"] = True
                                ret = "Auto Like Enable."
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "autolike off":
                            if msg._from in admin:
                                wait["likeOn"] = False
                                ret = "Auto like Disable."
                                flexvian(msg.to, str(ret))                                
        
                        elif cmd == "responsalam on":
                            if msg._from in admin:
                                wait["responsalam"] = True
                                ret = "Auto salam On."
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "responsalam off":
                            if msg._from in admin:
                                wait["responsalam"] = False
                                ret = "Auto salam Off."
                                flexvian(msg.to, str(ret))
  
                        elif cmd == "token on":
                            if msg._from in admin:
                                wait["token"] = True
                                ret = "Cek Token On."
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "token off":
                            if msg._from in admin:
                                wait["token"] = False
                                ret = "Cek Token Off."
                                flexvian(msg.to, str(ret))
                          
                        elif cmd == "autolike off":
                            if msg._from in admin:
                                wait["likeOn"] = False
                                ret = "Auto like Disable."
                                flexvian(msg.to, str(ret))                                
                    
                        elif cmd == "respon2 on":
                            if msg._from in admin:
                                temptag["stealtag"] = True
                                ret = "Respon 2 Enable !"
                                flexvian(msg.to, str(ret))
                                                        
                        elif cmd == "respon2 off":
                            if msg._from in admin:
                                temptag["stealtag"] = False
                                ret = "Respon 2 Disable !"
                                flexvian(msg.to, str(ret))
                                
                        elif cmd == "responcall on":
                            if msg._from in admin:
                                wait["responGc"] = True
                                ret = "Detect call enable"
                                flexvian(msg.to, str(ret))
                                                        
                        elif cmd == "responcall off":
                            if msg._from in admin:
                                wait["responGc"] = False
                                ret = "Detect call disable"
                                flexvian(msg.to, str(ret))
                                                                                      
                        elif cmd == "sticker sider":
                            if msg._from in admin:
                                wait["AddstickerSider"]["status"] = True
                                ret = "Send a stickers ♪"
                                flexvian(msg.to, str(ret))
                            
                        elif cmd == "sticker tag":
                            if msg._from in admin:
                                wait["AddstickerTag"]["status"] = True
                                ret = "Send a stickers ♪"
                                flexvian(msg.to, str(ret))

                        elif cmd == "sticker pesan":
                            if msg._from in admin:
                                wait["AddstickerPesan"]["status"] = True
                                ret = "Send a stickers ♪"
                                flexvian(msg.to, str(ret))

                        elif cmd == "sticker welcome":
                            if msg._from in admin:
                                wait["AddstickerWelcome"]["status"] = True
                                ret = "Send a stickers ♪"
                                flexvian(msg.to, str(ret))

                        elif cmd == "sticker leave":
                            if msg._from in admin:
                                wait["AddstickerLeave"]["status"] = True
                                ret = "Send a stickers ♪"
                                flexvian(msg.to, str(ret))
       
                        elif cmd == comd["cban"]:
                          if wait["selfbot"] == True:  
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                   ret = "Blacklist Empty"
                                   flexvian(msg.to, str(ret))
                              else:
                                   ret = "Cleared {} Blacklist".format(str(len(wait["blacklist"])))
                                   flexvian(msg.to, str(ret))
                                   wait["blacklist"] = {}
                    
#===========COMMAND BLACKLIST============#
                        elif cmd.startswith("talkban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           flexvian(msg.to,"Added Blacklist")
                                       except:
                                           pass

                        elif cmd.startswith("untalkban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           flexvian(msg.to,"Clear Blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                flexvian(msg.to,"Send Contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                flexvian(msg.to,"Send Contact")

                        elif cmd.startswith("ban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           flexvian(msg.to,"Added To Blacklist")
                                       except:
                                           pass

                        elif cmd.startswith("unban "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           flexvian(msg.to,"Unbaned Blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                flexvian(msg.to,"Send Contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                flexvian(msg.to,"Send Contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                flexvian(msg.to,"No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                flextext(msg.to,"↘Blacklist User↘\n\n"+ma+"\n↘Total「%s」Blacklist User↘" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                flexvian(msg.to,"No Body Is Banned")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                flextext(msg.to,"↘Talkban User↘\n\n"+ma+"\n↘Total「%s」Talkban User↘" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    flexvian(to,"No body is baned")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
#===========COMMAND SET============#
                        elif cmd.startswith("setpesan: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   wait["pesan"] = str(key).lower()
                                   flextext(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setcomment: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   wait["comment"] = str(key).lower()
                                   flextext(msg.to, "{}".format(str(key).lower()))

                                  
                        elif cmd.startswith("setspeed: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["speed"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))
                                  
                        elif cmd.startswith("setbye: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["bye"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setkick: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["kick"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setsideron: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["siderOn"] = str(key).lower()
                                   flexvian(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setsideroff: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["siderOff"] = str(key).lower()
                                   flexvian(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("settagall: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["tagall"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))
                        elif 'Set js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set js ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan amda")
                              else:
                                  wait["amda"] = spl
                                  cl.sendMessage(msg.to, "「amda」\namda diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set bypass ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set bypass ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan amdb")
                              else:
                                  wait["amdb"] = spl
                                  cl.sendMessage(msg.to, "「amdb」\namdb diganti jadi :\n\n「{}」".format(str(spl)))
                        elif cmd.startswith("sethelp: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["help"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setcban: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["cban"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))
                        elif cmd == "#bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "See you next again "+str(G.name))
                                cl.cancelGroupInvitation(msg.to, [Zmid])
                                ajs.leaveGroup(msg.to)

                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"[ ɴᴀᴍᴀ ɢʀᴏᴜᴘ ]\n"+str(ginfo.name)+"\nᴅᴏɴᴇ ᴋɪᴄᴋᴇʀ ᴀᴋᴛɪᴠᴇ ᴊs")
                                except:pass                          

                        elif cmd == "js lv":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                G = cl.getGroup(msg.to)
                                ajs.leaveGroup(msg.to);cl.inviteIntoGroup(msg.to, [Zmid])

                        elif cmd == "js in":
                            if msg._from in admin or msg._from in owner:
                                anggota = [Zmid]
                                cl.inviteIntoGroup(msg.to, anggota)
                                ajs.acceptGroupInvitation(msg.to)

                        elif cmd == "js cl":
                            if msg._from in admin or msg._from in owner:
                                G = cl.getGroup(msg.to)
                                cl.cancelGroupInvitation(msg.to, [Zmid])
                        
                        elif cmd == "addasis":
                            try:
                                cl.sendMessage(msg.to, "⏳ᴛᴜɴɢɢᴜ sᴇʟᴀᴍᴀ 5 ᴍᴇɴɪᴛ")
                                cl.findAndAddContactsByMid(Zmid)
                                time.sleep(5)
                                ajs.findAndAddContactsByMid(clMID)
                                time.sleep(5)
                                ajs.sendMessage(to, "✓sᴜᴄᴄᴇss")
                            except:
                                ajs.sendMessage(to, "✓sᴜᴄᴄᴇss")

                        elif cmd.startswith("setrespon: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFlex(msg.to, "Failed..!!")
                               else:
                                   wait["Tag"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setspam: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendFlex(msg.to, "Failed..!!")
                               else:
                                   Setmain["RAmessage1"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd.startswith("setunsend: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   flexvian(msg.to, "Failed..!!")
                               else:
                                   comd["unsend"] = str(key).lower()
                                   flex2(msg.to, "{}".format(str(key).lower()))

                        elif cmd == "cekpesan":
                            if msg._from in admin:
                               flextext(msg.to, "Pesan anda\n"+ str(wait["pesan"]))
                               
                        elif cmd == "cekwelcome":
                            if msg._from in admin:
                               flextext(msg.to, "Msg Welcome\n" + str(wait["welcome"]))
                               
                        elif cmd == "cekcomment":
                            if msg._from in admin:
                               flextext(msg.to, "Msg Comment\n" + str(wait["comment"]))                               

                        elif cmd == "cekrespon":
                            if msg._from in admin:
                               flex2(msg.to, "Msg Respon\n" + str(wait["Tag"]))

                        elif cmd == "cekspam":
                            if msg._from in admin:
                               flex2(msg.to, "Msg Spam\n" + str(Setmain["RAmessage1"]))

                        elif cmd == "ceksider":
                            if msg._from in admin:
                               flex2(msg.to, "Msg Sider\n" + str(wait["mention"]))
                               
                        elif cmd == "cekcomment":
                            if msg._from in admin:
                               flextext(msg.to, "Msg Comment\n" + str(wait["comment"]))

                        elif cmd == "cekleave":
                            if msg._from in admin:
                               flex2(msg.to, "Msg Leave\n" + str(wait["leave"]))

                        elif cmd.startswith("lefft: "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        flexvian(i, "Waitting for notifed success")
                                        cl.leaveGroup(i)
                                        flexvian(to,"Leave all group " +h)

                        elif cmd.startswith("sapu: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                separate = msg.text.split(":")
                                number = msg.text.replace(separate[0] + ":"," ")
                                groups = cl.getGroupIdsJoined()
                                gid = groups[int(number)-1]                             
                                xyz = cl.getGroup(gid)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(gid, cl.authToken, "DESKTOPWIN\t7.9.1\tWindowns\t11")
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif text.lower() == wait["amda"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(to, cl.authToken,"DESKTOPWIN\t7.9.1\tWindowns\t11")
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif cmd.startswith("bantai: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                separate = msg.text.split(":")
                                number = msg.text.replace(separate[0] + ":"," ")
                                groups = cl.getGroupIdsJoined()
                                gid = groups[int(number)-1]                             
                                xyz = cl.getGroup(gid)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(gid, cl.authToken, "DESKTOPWIN\t7.9.1\tWindowns\t11")
                                for x in targp:lolz += ' uid={}'.format(x)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif text.lower() == wait["amdb"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                xyz = cl.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                mems = [c.mid for c in xyz.members]
                                targk = []
                                for x in mems:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targk.append(x)
                                lolz = 'dual.js gid={} token={}'.format(to, cl.authToken,"DESKTOPWIN\t7.9.1\tWindowns\t11")
                                for x in targp:lolz += ' uid={}'.format(x)
                                for x in targk:lolz += ' uik={}'.format(x)
                                execute_js(lolz)
                        elif cmd == "#cl" or text.lower() == "#cencel":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                FarelKiller = cl.getGroup(to)
                                if FarelKiller.invitee == None:pends = []
                                else:pends = [c.mid for c in FarelKiller.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in Bots and x not in cl.profile.mid:targp.append(x)
                                pokeh = 'cancel.js gid={} token={}'.format(to, cl.authToken, "DESKTOPWIN\t7.9.1\tWindowns\t11")
                                for x in targp:pokeh += ' uid={}'.format(x)
                                execute_js(pokeh)
               if msg.contentType == 6:
                 if wait["responGc"] == True:
                     a = cl.getContact(sender)
                     if msg.toType == 2:
                         b = msg.contentMetadata['GC_EVT_TYPE']
                         c = msg.contentMetadata["GC_MEDIA_TYPE"]
                         if c == "VIDEO" and b == "S":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             cover = cl.getProfileCoverURL(sender)
                             data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "20px", "height": "20px", "offsetTop": "19px", "offsetStart": "20px" }, { "type": "image", "url": "https://i.ibb.co/n7HMKLv/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "MEMULAI PANGGILAN", "size": "6px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "80px", "height": "10px", "offsetTop": "29px", "offsetEnd": "27.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "8px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "98px", "height": "10px", "offsetBottom": "24px", "offsetEnd": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "22.5px", "offsetStart": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), "size": "6.5px", "color": "#00ff00", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "12.5px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                             sendTemplate(to, data)
                         if c == "VIDEO" and b == "E":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             cover = cl.getProfileCoverURL(sender)
                             data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "20px", "height": "20px", "offsetTop": "19px", "offsetStart": "20px" }, { "type": "image", "url": "https://i.ibb.co/n7HMKLv/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "PANGGILAN BERAKHIR", "size": "6px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "80px", "height": "10px", "offsetTop": "29px", "offsetEnd": "27.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "8px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "98px", "height": "10px", "offsetBottom": "24px", "offsetEnd": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "22.5px", "offsetStart": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), "size": "6.5px", "color": "#00ff00", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "12.5px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                             sendTemplate(to, data)
                             sendTemplate(to, data)
                         if c == "AUDIO" and b == "S":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             cover = cl.getProfileCoverURL(sender)
                             data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "20px", "height": "20px", "offsetTop": "19px", "offsetStart": "20px" }, { "type": "image", "url": "https://i.ibb.co/n7HMKLv/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "MEMULAI PANGGILAN", "size": "6px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "80px", "height": "10px", "offsetTop": "29px", "offsetEnd": "27.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "8px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "98px", "height": "10px", "offsetBottom": "24px", "offsetEnd": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "22.5px", "offsetStart": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), "size": "6.5px", "color": "#00ff00", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "12.5px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                             sendTemplate(to, data)
                         if c == "AUDIO" and b == "E":
                             tz = pytz.timezone("Asia/Jakarta")
                             timeNow = datetime.now(tz=tz)
                             contact = cl.getContact(sender)
                             cover = cl.getProfileCoverURL(sender)
                             data = { "type": "flex", "altText": "TUMAN BOTS", "contents": { "type": "bubble", "size": "micro", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/pJvKcvX/ezgif-com-gif-maker-19.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus), "size": "full", "aspectRatio": "1:1", "aspectMode": "cover", "animated": True } ], "position": "absolute", "width": "20px", "height": "20px", "offsetTop": "19px", "offsetStart": "20px" }, { "type": "image", "url": "https://i.ibb.co/n7HMKLv/ezgif-com-gif-maker-18.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "PANGGILAN BERAKHIR", "size": "6px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "80px", "height": "10px", "offsetTop": "29px", "offsetEnd": "27.5px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(contact.displayName), "size": "8px", "color": "#00ff00", "align": "center" } ], "position": "absolute", "width": "98px", "height": "10px", "offsetBottom": "24px", "offsetEnd": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%H:%M:%S'), "size": "7px", "color": "#00ff00", "align": "center", "offsetTop": "0.5px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "22.5px", "offsetStart": "8px" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": " "+datetime.strftime(timeNow,'%d-%m-%Y'), "size": "6.5px", "color": "#00ff00", "align": "center", "offsetTop": "1px" } ], "position": "absolute", "width": "45px", "height": "10px", "offsetBottom": "12.5px", "offsetStart": "8px" }, { "type": "image", "url": "https://i.ibb.co/GWvB4Fj/ezgif-com-gif-maker-20.png", "size": "full", "aspectMode": "cover", "aspectRatio": "2:1", "animated": True, "position": "absolute" } ], "paddingAll": "0px" }, "action": { "type": "uri", "label": "action", "uri": "line://nv/profilePopup/mid=u40815093b2aa87290893929e0d7abdc0" } } }
                             sendTemplate(to, data)
    except Exception as error:
        print (error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        pass
