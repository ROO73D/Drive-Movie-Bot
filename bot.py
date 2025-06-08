from pymongo import *
import requests
from bs4 import BeautifulSoup
import re
import json
import humanize
from asyncio import events
import telebot
from telebot import types
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
import requests
import re
from bs4 import BeautifulSoup
from pymongo import *
import base64
import random
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from datetime import date
from urllib.parse import unquote
import datetime
from aiohttp import web
import asyncio
import os
import datetime 
import threading
import time
import string

client = MongoClient("mongodb+srv://notpointbreak:Password246M@cluster0.gzxc2sc.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('bifrost')
links = db.gdtot

client = MongoClient("mongodb+srv://yellowflash:Password246M@cluster0.nzv7x2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database('bifrost')
tokens_collection = db.token
users = db.users
settings = db.settings

client = MongoClient("mongodb+srv://yellowflash:Password246M@cluster0.nzv7x2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.get_database('bifrost')
ddlinks = db.bbg

TOKEN = '6530908059:AAHQwVCXO707ETbPrcnatwLoB0UqVaFYk-s'

bot = telebot.TeleBot(TOKEN)

img_link = ['https://i.pinimg.com/originals/2b/38/1e/2b381e29d6c14418cf104d07803403d5.jpg',
 'https://i.pinimg.com/originals/13/c5/72/13c572b686edd84fa16c0054da9c323d.jpg',
 'https://i.pinimg.com/originals/1f/bc/df/1fbcdf26cffe1f066edb2e4efed54d4a.jpg',
 'https://i.pinimg.com/originals/67/b4/c6/67b4c6e04a2c686076847241cd0cb88c.jpg',
 'https://i.pinimg.com/originals/d5/30/c9/d530c920c3a69d82744ea9586e2d8f38.jpg',
 'https://themighty.com/wp-content/uploads/2019/09/emotionalclub.png',
 'https://i.pinimg.com/originals/78/b1/30/78b13064c660fe2ebbe5224538f82d32.jpg',
 'https://i.pinimg.com/originals/7a/35/7b/7a357ba8fcb4d458e527a77b5af62a1a.jpg',
 'https://i.pinimg.com/originals/f7/7f/81/f77f811f65662f913ab0a727dfa5205a.jpg',
 'https://i.pinimg.com/originals/f7/7f/81/f77f811f65662f913ab0a727dfa5205a.jpg',
 'https://i.pinimg.com/originals/3b/8a/a7/3b8aa74a49e606ae1eaa46a25562dab1.jpg',
 'https://www.yatzer.com/sites/default/files/media/slideshow/15_s_daily_bat_stood_up_-photography_sebastian_magnani_yatzer.jpg',
 'https://i.pinimg.com/originals/fc/3a/da/fc3ada4114d5068067708a7d61e6354f.jpg',
 'http://www.teamjimmyjoe.com/wp-content/uploads/2016/01/street-sign-your-life-is-a-joke.jpg',
 'https://i.pinimg.com/originals/95/fe/9f/95fe9f2289ff1b5132320d94e8a7cd50.jpg',
 'https://i.pinimg.com/originals/71/94/58/71945842e6985f179772c11a65bfb3c9.jpg',
 'https://i.pinimg.com/originals/55/f0/05/55f0052e278d1f8615b42df235ff8836.jpg',
 'https://i.pinimg.com/originals/28/79/5c/28795cb77cc3fe6af94d8a73e023d1b3.jpg',
 'https://i.pinimg.com/originals/99/c8/13/99c813da11220eef9b1fcae3df9a5142.jpg',
 'https://i.pinimg.com/originals/c5/95/f1/c595f1e447ceec4cb09633cd915acf4c.jpg',
 'https://i.pinimg.com/originals/f6/bf/bc/f6bfbc8fdb2a5b3de5dc597c948ff072.jpg',
 'https://i.pinimg.com/originals/33/a8/cd/33a8cd881caa3774dc22f15cf92dc81c.jpg',
 'https://i.pinimg.com/originals/9e/7f/d9/9e7fd9fa9aba415f1b20b80ff112ca8a.jpg',
 'https://i.pinimg.com/originals/6d/1c/d5/6d1cd5db612dbfe80b894dacf137149a.jpg',
 'https://i.pinimg.com/originals/9d/b1/26/9db126488032b179abe1cb0e49daba8a.jpg',
 'https://i.pinimg.com/originals/06/12/4f/06124f2a2f848583488e74dbda1f4973.jpg',
 'https://i.pinimg.com/originals/51/f7/08/51f7086485a0be22204bfe1e29d03a59.jpg',
 'https://i.pinimg.com/originals/be/1d/b5/be1db592c185e35199bbb48389bcd89f.jpg',
 'https://i.pinimg.com/originals/12/b2/3a/12b23a8825c8da1efd80df53c57f9329.jpg',
 'https://i.pinimg.com/originals/a8/15/58/a81558911ddd07533e5909fa8f6f8df6.jpg',
 'https://i.pinimg.com/originals/71/38/78/7138781a8f72094f8f8e4e18b0142c37.jpg',
 'https://i.pinimg.com/originals/24/e8/ec/24e8ecb589aeb32759d8b5b94cf5e2a5.jpg',
 'https://i.pinimg.com/originals/a3/02/f4/a302f4a8b3521f6372ec8c173446e5f3.jpg',
 'https://i.pinimg.com/originals/da/6e/21/da6e2129e158411a76e13cc65f0674a6.jpg',
 'https://i.pinimg.com/originals/07/22/0a/07220ac0d1f16230e88e5c21c5681cc5.jpg',
 'https://i.pinimg.com/originals/ea/b6/20/eab6203681c0493206436b91bd376752.jpg',
 'https://i.pinimg.com/originals/5b/ee/5d/5bee5dd39a60d0b3206f80ac3a1a9811.jpg',
 'https://i.pinimg.com/originals/7c/b4/c5/7cb4c5a603a649e465941fc9beeb1f87.jpg',
 'https://i.pinimg.com/originals/cf/d0/e0/cfd0e0269e47bcf071a9dd9078fb20ca.png',
 'https://i.pinimg.com/originals/dc/51/23/dc5123da4d666664dfbd11a600452bb0.jpg',
 'https://i.pinimg.com/originals/e7/aa/5c/e7aa5c2d71a98e4fde49f239cb9a8c3b.jpg',
 'https://i.pinimg.com/originals/7d/ad/75/7dad755d702e44bae27d31ff6378d02c.jpg',
 'https://i.pinimg.com/originals/3a/5b/fd/3a5bfda3f15f7fee3aa25cee967585ab.jpg',
 'https://i.pinimg.com/originals/8e/50/71/8e5071f9d08d5c6ed492708ddce876a0.jpg',
 'https://i.pinimg.com/originals/cb/0b/d0/cb0bd072955cd85d45f601e0b0597852.jpg',
 'https://i.pinimg.com/originals/02/bb/ab/02bbab5852065e9c38c6fd879c41015f.jpg',
 'https://i.pinimg.com/originals/4b/82/28/4b82284995a7cb5a75085fa9fc1ae90e.jpg',
 'https://i.pinimg.com/originals/f4/48/25/f448259a5250c04d801b8f4a1feb5c86.jpg',
 'https://i.pinimg.com/originals/d9/e7/75/d9e775cbaba75d3473c4c1790bdda4dd.jpg',
 'https://i.pinimg.com/originals/bf/f5/14/bff514d1ba362d4892e7c0f338dc3183.jpg',
 'https://i.pinimg.com/originals/a0/d2/dd/a0d2ddb5f832b063bfc6a45618bbe721.jpg',
 'https://i.pinimg.com/originals/01/24/ff/0124ff9582214ffb5862dd8dadf8054d.jpg',
 'https://i.pinimg.com/564x/9d/06/ea/9d06ea5a3d3a2d38fa87e2e8e352654a.jpg',
 'https://i.pinimg.com/originals/48/9c/46/489c462dea830250c2e6a27a29d3a8ac.jpg',
 'https://i.pinimg.com/originals/85/fb/b4/85fbb425a8e15af17710454463690354.jpg',
 'https://i.pinimg.com/originals/71/59/4f/71594f065dc701387816e51edc35aea6.jpg',
 'https://i.pinimg.com/originals/ec/7f/7b/ec7f7b55ef735b86835f35b5997dcbd0.jpg',
 'https://i.pinimg.com/originals/6d/75/5c/6d755c5d3f8331bd85f055cf60b803d4.jpg',
 'https://i.pinimg.com/originals/6d/75/5c/6d755c5d3f8331bd85f055cf60b803d4.jpg',
 'https://i.pinimg.com/originals/bb/ad/ad/bbadad5ab61b6d17ac8c33ffee687129.jpg',
 'https://i.pinimg.com/originals/a1/fb/9a/a1fb9a2bb71dd25e2895298a63225b77.jpg',
 'https://i.pinimg.com/736x/e9/56/21/e9562142053e09048a54231e4ae4b138.jpg',
 'https://i.pinimg.com/originals/ef/d5/20/efd5204be4582beefabc2f59273673b7.jpg',
 'https://i.pinimg.com/originals/6b/0e/35/6b0e353d61f7f0f620cb5526561140a1.jpg']


 
def update_user_stats(user_id):
    return users.update_one(
        {'user_id': user_id},
        {'$set': {'last_login': datetime.datetime.now()}, '$inc': {'login_count': 1}},
        upsert=True
    )
    
def get_all_users():
    return users.find({})
  
def toggle_shortener():
    """Toggle link shortener status"""
    current_status = settings.find_one({'setting': 'shortener'})
    new_status = not current_status.get('enabled', True)
    
    settings.update_one(
        {'setting': 'shortener'},
        {'$set': {'enabled': new_status}},
        upsert=True
    )
    
    return f"✅ Link shortener has been {'enabled' if new_status else 'disabled'}"

def get_stats():
    return {
        'total_users': users.count_documents({}),
        'active_users': tokens_collection.count_documents({'valid':True})
    }
user_search_results = {}  # Format: {user_id: {'results': [...], 'timestamp': datetime}}


def appdrive(link,id,message):
  data = []
  url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://appdrive.pro/file/',link.strip())
  url1 = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://appdrive.cloud/file/',link.strip())
  html = requests.get(url1.strip())
  soup = BeautifulSoup(html.text,'lxml')
  if soup.title.text != 'AppDrive':
    if 'pack' in url:
      for i in soup.find_all('li',{'class':'list-group-item'}):
        for j in i.find_all('a'):
          print(f"https://appdrive.me{j['href']}")
          appdrive(f"https://appdrive.me{j['href']}",id)
          id+=1
    else:
      for i in soup.find_all('li',{'class':'list-group-item'}):
        data.append(i.text)
      title = data[0][7::]
      size = data[2][7::]
      try:
          m = re.split(r".[1-90]{4}",title)
          n = re.search(r"[1-90]{4}",title)
          k = re.sub("\.", " ", m[0])
          new_title = f"{k} {n.group(0)}"
      except:
          m = re.split(r".[1-90]{3}",title)
          k = re.sub("\.", " ", m[0])
          new_title = f"{k}"
      headers = {
      'authority': 'www.imdb.com',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'cache-control': 'max-age=0',
      # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
      'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
      }
    try:
      html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
      soup1 = BeautifulSoup(html.text,'lxml')
      print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
      bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
    except:
      try:
        html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
        soup1 = BeautifulSoup(html.text,'lxml')
        print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
        bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
      except:
        print(f"{id} : {url} : {new_title} : Nil")
        bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
    try:
      new_one = {
      "id":f"{id}",
      "title":f"{title}",
      "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
      "link":f"{url}",
      "size": f"{size}",
      "indexTitle":f"{new_title}"
      }
    except:
      new_one = {
      "id":f"{id}",
      "title":f"{title}",
      "imdbId":f"Nil",
      "link":f"{url}",
      "size": f"{size}",
      "indexTitle":f"{new_title}"
      }
    links.insert_one(new_one)
    id+=1

@bot.message_handler(commands=['stats'])
def show_stats(message):
    if not message.from_user.id == 385686409:
        bot.reply_to(message, "You don't have permission to use this command! ⛔")
        return
    try:
        # Get total count from MongoDB
        total_files = links.count_documents({})
        stats = get_stats()
        current_status = settings.find_one({'setting': 'shortener'})
        status = current_status.get('enabled', True)
        stats_text = f"""
            📊 <b>Bot Statistics</b> 📊
            ━━━━━━━━━━━━━━━━━━━━━
            📁 <b>Shortner Status:</b> <code>{status}</code>
            📁 <b>Total Files:</b> <code>{total_files}</code>
            👥 <b>Total Users:</b> <code>{stats['total_users']}</code>
            🔗 <b>Active Users:</b> <code>{stats['active_users']}</code>
            📅 <b>Last Updated:</b> <code>{time.strftime('%Y-%m-%d %H:%M:%S')} UTC</code>

            <i>🤖 Database is updated regularly!</i>
            ━━━━━━━━━━━━━━━━━━━━━
            """
        bot.reply_to(message, stats_text, parse_mode='html')
            
    except Exception as e:
        error_text = """
                    ❌ <b>Error Fetching Stats</b>
                    ━━━━━━━━━━━━━━━━━━━━━
                    Unable to fetch database statistics.
                    Please try again later.
                    """
        print(f"Stats Error: {e}")
        bot.reply_to(message, error_text, parse_mode='html')
        
@bot.message_handler(commands=['shortner'])
def handle_broadcast( message):
    if not message.from_user.id == 385686409:
        bot.reply_to(message, "You don't have permission to use this command! ⛔")
        return
    
    try:
      status = toggle_shortener()
      bot.reply_to(message, status)
    except Exception as e:
        bot.reply_to(message, f"Broadcast failed: {str(e)}")
        
@bot.message_handler(commands=['broadcast'])
def handle_broadcast( message):
    if not message.from_user.id == 385686409:
        bot.reply_to(message, "You don't have permission to use this command! ⛔")
        return

    try:
        try:
            image = message.reply_to_message.photo[-1].file_id  # Get the highest quality image
            caption = message.reply_to_message.caption.replace('.',"\.").replace("/","\/").replace("=","\=")
            caption = "||"+caption+"||"
        except Exception as e:
            broadcast_message = " ".join(message.text.split()[1:])

        users = get_all_users()
        success_count = 0
        fail_count = 0

        for user in users:
            try:
                try:
                    msg = bot.send_photo(user['user_id'],photo=image, caption=caption,parse_mode="MarkdownV2")
                    print(msg)
                except Exception as e:
                    print(e)
                    bot.send_message(user['user_id'], broadcast_message)
                success_count += 1
            except:
                fail_count += 1

        bot.reply_to(
            message,
            f"Broadcast completed!\n"
            f"✅ Success: {success_count}\n"
            f"❌ Failed: {fail_count}"
        )
    except Exception as e:
        bot.reply_to(message, f"Broadcast failed: {str(e)}")
        
@bot.message_handler(commands=['start']) 
def start(message):
    bplink = 'none'
    code = extract_arg(message.text)
    CHAT_ID = -1002161455712
    USER_ID = message.from_user.id
    update_user_stats(USER_ID)
    if code == []:
        bot.send_message(-1001975502922, text=f"#{message.chat.id}\n\nUsername : [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n\nStarted for fun", parse_mode='markdown', disable_web_page_preview=True)
        button = telebot.types.InlineKeyboardButton(text="⚡ Power House ", url=f"http://t.me/GdtotLinkz")
        keyboard = telebot.types.InlineKeyboardMarkup().add(button)
        bot.send_photo(chat_id=message.chat.id, photo=f"{random.choice(img_link)}", caption=f"Hey 👋🏻 `{str(message.chat.first_name)}`,\n\nThis 🤖 Bot is the Exclusive property of [Ye1lowFlash](https://t.me/Ye1lowFlash).\nIts a *Movie Search bot* , You'll get Movie as a google drive link\nTry searching `avengers` .\n\n*⚡️powered by* @GdtotLinkz", parse_mode="markdown", reply_markup=keyboard) 
    else:
        if False:
            pass
        else:
          if "Yellow" not in code[0]:
              if validate_short_token(message,code[0]):
                myquery = { "token": code[0] }
                newvalues = { "$set": { "valid": True } }
                tokens_collection.update_one(myquery, newvalues)
                user = message.from_user if message.from_user else None
                username = f"@{user.username}" if user.username else "No Username"
                user_mention = f"[{user.full_name}](tg://user?id={user.id})"
                bot.send_message(
                    -1001975502922,
                    text=(
                        f"🎉 **Verification Successful!** ✅\n\n"
                        f"👤 **User**: {user_mention if user_mention else None}"
                        f"🆔 **Chat ID**: `#{message.chat.id}`\n\n"
                        f"✨ Thank you for verifying. Welcome aboard!"
                    ),
                    parse_mode='markdown',
                    disable_web_page_preview=True
                )
          else:
            token_data = tokens_collection.find_one({'user_id': message.from_user.id})
            if token_data:
              print(token_data['expires_at'] > datetime.datetime.now())
              if token_data['expires_at'] > datetime.datetime.now() and token_data['valid'] == True:
                print("valid")
                try:
                    bot.delete_message(message.chat.id, message_id=message_id1)
                except Exception as e:
                    print(e)
                    pass
                message_ids = bot.reply_to(message, text=f"𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐋𝐢𝐧𝐤 🔄", parse_mode='markdown', disable_web_page_preview=True).message_id
                url = decrypt(code[0])
                print(url)
                data = list(links.find({"link": url}))
                print(data)
                link = data[0]['link']
                title = data[0]['title']
                if 'gdtot' in link:
                    link = link.replace('new6.gdtot.cfd', 'new19.gdtot.dad')
                elif 'filepress' in link:
                    link = link.replace('https://filepress.click', 'new3.filepress.live')
                elif 'appdrive' in link:
                    link = link.replace('.pro', '.fit')
                elif 'gdflix' in link:
                    link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://new8.gdflix.dad/file/',link)
                elif 'gofile' in link:
                    link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/d\/','https://gofile.io/d/',link)
                print(link)
                if 'http' in bplink:
                  try:
                    text = f"🎥\t*{title}*\n\n✂️ *size - {data[0]['size']}*\n\n🔗 {link}\n\n🌎*Bypassed Link :* ```{bplink}```\n\n*⚡powered by* @GdtotLinkz"
                  except Exception as e:
                    print(f"[bypass] {e}")
                    text = f"🎥\t*{title}*\n\n✂️ *size - {data[0]['size']}*\n\n🔗 {link}\n\n*⚡powered by* @GdtotLinkz"
                else:
                  text = f"🎥\t*{title}*\n\n✂️ *size - {data[0]['size']}*\n\n🔗 {link}\n\n*⚡powered by* @GdtotLinkz"
                bot.delete_message(chat_id=message.chat.id, message_id=message_ids)
                button1 = telebot.types.InlineKeyboardButton(text=f"Fast Dowload 🚀", url='https://gplinks.co/DDLHVN')
                keyboard = telebot.types.InlineKeyboardMarkup().add(button1)
                message_ids = bot.reply_to(message, text=text, parse_mode='markdown', disable_web_page_preview=True,reply_markup=keyboard)
                print(f"[STATUS] :{message.chat.id} got link {title}")
              else:
                tokens_collection.delete_many({'user_id': message.from_user.id})
                button1 = telebot.types.InlineKeyboardButton(text=f"verify ✅ ", url=f"{generate_adlink(message)}")
                button2 = telebot.types.InlineKeyboardButton(text=f"Retry 🔄", url=f"https://t.me/DriveMovie_bot?start={code[0]}")
                keyboard = telebot.types.InlineKeyboardMarkup().add(button1).add(button2)
                message_id1 = bot.reply_to(message, text=f"<code>Your token is expired,you need to verify before continuing !🤌</code> \n\n <b>click verify and then retry</b>", parse_mode="html", disable_web_page_preview=True,reply_markup=keyboard).message_id
            else:
              tokens_collection.delete_many({'user_id': message.from_user.id})
              button1 = telebot.types.InlineKeyboardButton(text=f"verify ✅ ", url=f"{generate_adlink(message)}")
              button2 = telebot.types.InlineKeyboardButton(text=f"Retry 🔄", url=f"https://t.me/DriveMovie_bot?start={code[0]}")
              keyboard = telebot.types.InlineKeyboardMarkup().add(button1).add(button2)
              bot.reply_to(message, text=f"<code>Your token is expired,you need to verify before continuing !🤌</code> \n\n <b>click verify and then retry</b>", parse_mode="html", disable_web_page_preview=True,reply_markup=keyboard)


 
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def handle_all_messages(message):
    movie = message.caption
    headers = {
        'authority': 'new.gdtot.dad',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        # 'cookie': 'PHPSESSID=0o1lcgl5du9ls9nfglf1mvfv7t',
        'referer': 'http://127.0.0.1:5000/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    if movie == None:
      movie = message.text
    if 'http' in movie:
      urls = re.findall(r'https:\/\/[a-zA-Z0-9._]+\/?[a-zA-Z0-9._]+\/?[a-zA-Z0-9._]+', movie)
      id=1
      for i in urls:
        link = i.strip()
        if 'gdtot' in link:
            link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://new6.gdtot.cfd/file/',link.strip())
        elif 'filepress' in link:
            link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://filepress.click/file/',link.strip())
        elif 'appdrive' in link:
            link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://appdrive.pro/file/',link.strip())
        elif 'gdflix' in link:
            link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://gdflix.lol/file/',link.strip())
        elif 'gofile' in link:
            link = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/d\/','https://gofile.io/d/',link.strip())
        elif 'hubcloud' in link:
            link = y
        data = list(links.find({"link": link}))
        if data:
          print(data)
          pass
        else:
          try:
            if 'hubcloud' in i:
              headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'if-modified-since': 'Sat, 07 Dec 2024 15:16:30 GMT',
                    'priority': 'u=0, i',
                    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                }
              url = re.sub(r'https:\/\/[a-zA-Z0-9._]+\/drive\/', 'https://hubcloud.day/drive/', i.strip())
              url1 = re.sub(r'https:\/\/[a-zA-Z0-9._]+\/drive\/', 'https://hubcloud.day/drive/', i.strip())
              response = requests.get(url1, headers=headers)
              print(response.status_code)
              soup = BeautifulSoup(response.text, 'html.parser')

              title = soup.title.text
              size = soup.find('i',{'id':'size'}).text
              try:
                  m = re.split(r".[1-90]{4}",title)
                  n = re.search(r"[1-90]{4}",title)
                  k = re.sub("\.", " ", m[0])
                  new_title = f"{k} {n.group(0)}"
              except:
                  m = re.split(r".[1-90]{3}",title)
                  k = re.sub("\.", " ", m[0])
                  new_title = f"{k}"
              headers = {
                  'authority': 'www.imdb.com',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                  'cache-control': 'max-age=0',
                  # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
                  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
              }
              try:
                html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                soup1 = BeautifulSoup(html.text,'lxml')
                print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
              except:
                try:
                  html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                  soup1 = BeautifulSoup(html.text,'lxml')
                  print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                except:
                  print(f"{id} : {url} : {new_title} : Nil")
              try:
                new_one = {
                "id":f"{id}",
                "title":f"{title}",
                "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                "link":f"{url}",
                "size": f"{size}",
                "indexTitle":f"{new_title}"
                }
                bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
              except:
                new_one = {
                "id":f"{id}",
                "title":f"{title}",
                "imdbId":f"Nil",
                "link":f"{url}",
                "size": f"{size}",
                "indexTitle":f"{new_title}"
                }
              links.insert_one(new_one)
              id+=1
              bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
            elif 'gdtot' in i:
              url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://new6.gdtot.cfd/file/',i.strip())
              url1 = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://new10.gdtot.dad/file/',i.strip())
              html = requests.get(f"{url1}",headers=headers)
              soup = BeautifulSoup(html.text,'lxml')
              title = soup.title.text[8::]
              if title != 'Simple Plot to Manage and Share Drive with your Friends':
                  size = soup.find('td',{'align':'right'}).text
                  try:
                      m = re.split(r".[1-90]{4}",title)
                      n = re.search(r"[1-90]{4}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k} {n.group(0)}"
                  except:
                      m = re.split(r".[1-90]{3}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k}"
                  headers = {
                      'authority': 'www.imdb.com',
                      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                      'cache-control': 'max-age=0',
                      # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
                      'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                      'sec-ch-ua-mobile': '?0',
                      'sec-ch-ua-platform': '"Windows"',
                      'sec-fetch-dest': 'document',
                      'sec-fetch-mode': 'navigate',
                      'sec-fetch-site': 'none',
                      'sec-fetch-user': '?1',
                      'upgrade-insecure-requests': '1',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                  }
                  try:
                    html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                    soup1 = BeautifulSoup(html.text,'lxml')
                    print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                    bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                  except:
                    try:
                      html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                      soup1 = BeautifulSoup(html.text,'lxml')
                      print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                      bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                    except:
                      print(f"{id} : {url} : {new_title} : Nil")
                      bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                  try:
                    new_one = {
                    "id":f"{id}",
                    "title":f"{title}",
                    "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                    "link":f"{url}",
                    "size": f"{size}",
                    "indexTitle":f"{new_title}"
                    }
                  except:
                    new_one = {
                    "id":f"{id}",
                    "title":f"{title}",
                    "imdbId":f"Nil",
                    "link":f"{url}",
                    "size": f"{size}",
                    "indexTitle":f"{new_title}"
                    }
                  links.insert_one(new_one)
                  id+=1

            elif 'filepress' in i:
              headers = {
                  'accept': 'application/json, text/plain, */*',
                  'accept-language': 'en-US,en;q=0.9',
                  'priority': 'u=1, i',
                  'referer': 'https://new1.filepress.life/file/65b2ade3869e1f441ca95579',
                  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
              }
              url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://filepress.click/file/',i.strip())
              match = re.findall(r"\/[1-9a-zA-Z0]+$",url.strip())
              code = match[0][1::]
              if code:
                html = requests.get(f"https://new1.filepress.life/api/file/get/{code}", headers=headers)
                soup = BeautifulSoup(html.text,'lxml')
                jk = json.loads(html.text)
                new_tit = jk['data']['name']
                size = jk['data']['size']
                new_size = humanize.naturalsize(int(size))
                try:
                    m = re.split(r".[1-90]{4}",new_tit)
                    n = re.search(r"[1-90]{4}",new_tit)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k} {n.group(0)}"
                except:
                    m = re.split(r".[1-90]{3}",new_tit)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k}"
                headers = {
                'authority': 'www.imdb.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                }
                try:
                  html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                  soup1 = BeautifulSoup(html.text,'lxml')
                  print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                  bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                except:
                  try:
                    html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                    soup1 = BeautifulSoup(html.text,'lxml')
                    print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                    bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                  except:
                    print(f"{id} : {url} : {new_title} : Nil")
                    bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                try:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{new_tit}",
                  "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                except:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{new_tit}",
                  "imdbId":f"Nil",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                links.insert_one(new_one)
                id+=1

            elif 'gdflix' in i:
              data = []
              url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://gdflix.lol/file/',i.strip())
              url1 = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://new6.gdflix.cfd/file/',i.strip())
              headers = {
                  'authority': 'new1.gdflix.cfd',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                  'cache-control': 'max-age=0',
                  # 'cookie': 'cf_chl_3=35c155dddfd27f1; cf_clearance=8LC5U.Ejlpu9V4Sr8ssWe6RlBnJUcek4VKNKnjI1jvU-1711195979-1.0.1.1-WQ22Qi6megEupgkldfUKOR.YTqnKczaQfEdMEdiDpdvUDEmRHwZH3Fbmlyyq4DIzuer3rWvBA8JX_0u81uDq1A; PHPSESSID=19885a6ca8dc997879ceed05797553c3',
                  'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                  'sec-ch-ua-arch': '"x86"',
                  'sec-ch-ua-bitness': '"64"',
                  'sec-ch-ua-full-version': '"122.0.6261.131"',
                  'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.131", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.131"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-model': '""',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-ch-ua-platform-version': '"15.0.0"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
              }
              html = requests.get(url1.strip(),headers=headers)
              soup = BeautifulSoup(html.text,'lxml')
              try:
                if soup.title.text != 'GDFlix | GDFlix':
                  for i in soup.find_all('li',{'class':'list-group-item'}):
                    data.append(i.text)
                  title = data[0][7::]
                  size = data[2][7::]
                  try:
                      m = re.split(r".[1-90]{4}",title)
                      n = re.search(r"[1-90]{4}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k} {n.group(0)}"
                  except:
                      m = re.split(r".[1-90]{3}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k}"
              except Exception as e:
                print(e)
                post_body = {
                  "cmd": "request.get",
                  "url":f"{url1}",
                  "maxTimeout": 120000
                }
                response = requests.post('https://flaresolverrmine.onrender.com/v1', headers={'Content-Type': 'application/json'}, json=post_body)
                try:
                  fsdata = json.loads(response.text)
                  soup = BeautifulSoup(fsdata['solution']['response'],'lxml')
                  if soup.title.text != 'GDFlix | GDFlix':
                    for i in soup.find_all('li',{'class':'list-group-item'}):
                      data.append(i.text)
                    title = data[0][7::]
                    size = data[2][7::]
                except:
                  post_body = {
                  "cmd": "request.get",
                  "url":f"{url1.replace('file','zfile')}",
                  "maxTimeout": 120
                  }
                  response = requests.post('https://flaresolverrmine.onrender.com/v1', headers={'Content-Type': 'application/json'}, json=post_body)
                  fsdata = json.loads(response.text)
                  soup = BeautifulSoup(fsdata['solution']['response'],'lxml')
                  size = soup.find('h5').text.strip().split('[')[-1][:-1].strip()
                  title = soup.find('h5').text.strip().split('[')[0].strip()
                try:
                    m = re.split(r".[1-90]{4}",title)
                    n = re.search(r"[1-90]{4}",title)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k} {n.group(0)}"
                except:
                    m = re.split(r".[1-90]{3}",title)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k}"
              headers = {
              'authority': 'www.imdb.com',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
              'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
              'cache-control': 'max-age=0',
              # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
              'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'sec-fetch-dest': 'document',
              'sec-fetch-mode': 'navigate',
              'sec-fetch-site': 'none',
              'sec-fetch-user': '?1',
              'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
              }
              try:
                html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                soup1 = BeautifulSoup(html.text,'lxml')
                print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
              except:
                try:
                  html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                  soup1 = BeautifulSoup(html.text,'lxml')
                  print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                  bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                except:
                  print(f"{id} : {url} : {new_title} : Nil")
                  bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
              try:
                new_one = {
                "id":f"{id}",
                "title":f"{title}",
                "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                "link":f"{url}",
                "size": f"{size}",
                "indexTitle":f"{new_title}"
                }
              except:
                new_one = {
                "id":f"{id}",
                "title":f"{title}",
                "imdbId":f"Nil",
                "link":f"{url}",
                "size": f"{size}",
                "indexTitle":f"{new_title}"
                }
              links.insert_one(new_one)
              id+=1
            elif 'appdrive' in i:
              data = []
              url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://appdrive.pro/file/',i.strip())
              url1 = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/file\/','https://appdrive.fit/file/',i.strip())
              html = requests.get(url1.strip())
              soup = BeautifulSoup(html.text,'lxml')
              if soup.title.text != 'AppDrive':
                if 'pack' in url:
                  for i in soup.find_all('li',{'class':'list-group-item'}):
                    for j in i.find_all('a'):
                      print(f"https://appdrive.me{j['href']}")
                      appdrive(f"https://appdrive.me{j['href']}",id,message)
                      id+=1
                else:
                  for i in soup.find_all('li',{'class':'list-group-item'}):
                    data.append(i.text)
                  title = data[0][7::]
                  size = data[2][7::]
                  try:
                      m = re.split(r".[1-90]{4}",title)
                      n = re.search(r"[1-90]{4}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k} {n.group(0)}"
                  except:
                      m = re.split(r".[1-90]{3}",title)
                      k = re.sub("\.", " ", m[0])
                      new_title = f"{k}"
                  headers = {
                  'authority': 'www.imdb.com',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                  'cache-control': 'max-age=0',
                  # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
                  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                  }
                try:
                  html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                  soup1 = BeautifulSoup(html.text,'lxml')
                  print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                  bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                except:
                  try:
                    html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                    soup1 = BeautifulSoup(html.text,'lxml')
                    print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                    bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                  except:
                    print(f"{id} : {url} : {new_title} : Nil")
                    bot.reply_to(message, text=f"Added {url1} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                try:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{title}",
                  "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                except:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{title}",
                  "imdbId":f"Nil",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                links.insert_one(new_one)
                id+=1
            elif 'gofile' in i:
              try:
                url = re.sub(r'https:\/\/[a-zA-Z1-90.]+\/d\/','https://gofile.io/d/',i.strip())
                contentID = i.split('/')[-1]
                headers = {
                     'accept': '*/*',
                     'accept-language': 'en-US,en;q=0.9',
                     'authorization': 'Bearer HK2I2WaNk1l9TWByyBU5SWaMLmNrmV7O',
                     'if-none-match': 'W/"315-C35DQMzRaLtPZYV9B6kfak5B8YI"',
                     'origin': 'https://gofile.io',
                     'priority': 'u=1, i',
                     'referer': 'https://gofile.io/',
                     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                     'sec-ch-ua-mobile': '?0',
                     'sec-ch-ua-platform': '"Windows"',
                     'sec-fetch-dest': 'empty',
                     'sec-fetch-mode': 'cors',
                     'sec-fetch-site': 'same-site',
                     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                 }

                params = {
                    'wt': '4fd6sg89d7s6',
                }

                response = requests.get(f"https://api.gofile.io/contents/{contentID}", params=params, headers=headers)
                title = response.json()['data']['children'][f"{list(response.json()['data']['children'].keys())[0]}"]['name']
                size = humanize.naturalsize(int(response.json()['data']['children'][f"{list(response.json()['data']['children'].keys())[0]}"]['size']))
                print(title)
                print(size)
                try:
                    m = re.split(r".[1-90]{4}",title)
                    n = re.search(r"[1-90]{4}",title)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k} {n.group(0)}"
                except:
                    m = re.split(r".[1-90]{3}",title)
                    k = re.sub("\.", " ", m[0])
                    new_title = f"{k}"
                headers = {
                'authority': 'www.imdb.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                # 'cookie': 'session-id=137-1418442-7241252; session-id-time=2082787201l; ubid-main=132-4293222-1837241; uu=eyJpZCI6InV1YTVkMDM5Y2MyMmQyNDhiM2E2MjgiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=XzBAGk2vd+ifdVA/sBvqo/8kPhLpAWkmAPr/2qUxoPii0cH2NAkCJ7RDHhHk0r8HTOiVmFA5td05R5jQGq1b6MbU8EeFosJ3bqCRSxGUdhGDluU7nZsQ53wmI5p4anJMnc/2om9uoZAFY/P2OQYgQFDNl4TaebDeMmSIN48mXo9ATJKjw1Gn0EKerQX+GXNB/XcLv8hroidvbLDdav8Xpw==; csm-hit=tb:P6R3VZ1QCD3ZJ1K0B0BR+s-T20E02TGW8B7GQ8ZQ4W5|1678378591458&t:1678378591461&adb:adblk_no',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                }
                try:
                  html = requests.get(f"https://www.imdb.com/find/?q={new_title.replace('Copy of ','')}&ref_=nv_sr_sm",headers=headers)
                  soup1 = BeautifulSoup(html.text,'lxml')
                  print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                  bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                except:
                  try:
                    html = requests.get(f"https://www.imdb.com/find/?q={new_title.split(' ')[0]}&ref_=nv_sr_sm",headers=headers)
                    soup1 = BeautifulSoup(html.text,'lxml')
                    print(f"{id} : {url} : {new_title} : {soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}")
                    bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                  except:
                    print(f"{id} : {url} : {new_title} : Nil")
                    bot.reply_to(message, text=f"Added {url} to DB , thank you !!", parse_mode="html", disable_web_page_preview=True)
                try:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{title}",
                  "imdbId":f"{soup1.find('a',{'class':'ipc-metadata-list-summary-item__t'})['href'][7:-19]}",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                except:
                  new_one = {
                  "id":f"{id}",
                  "title":f"{title}",
                  "imdbId":f"Nil",
                  "link":f"{url}",
                  "size": f"{size}",
                  "indexTitle":f"{new_title}"
                  }
                links.insert_one(new_one)
                id+=1
              except Exception as e:
                print(e)
                pass
          except Exception as e:
            print(e)
            print(f"{i}")

    else:
        text = "No Links found !"
        print(f"[STATUS] : {message.chat.id} started searching {message.text}")
        searching_text = (
            "🔍 *Searching Database*\n\n"
            "Please wait while I find the best matches..."
        )
        message_ids = bot.reply_to(message, text=searching_text, parse_mode="markdown").message_id
        send_status_message(message, 'link', message.text)
        result = links.aggregate([
            {
                "$search": {
                    "index": "default",
                    "text": {
                        "query": f"{message.text}",
                        "path": "indexTitle",
                        "fuzzy": {},
                    }
                }
            },
            {
                "$project": {
                    "title": 1,
                    "link": 1,
                    "size":1,
                    "score": {'$meta': 'searchScore'}
                }
            }
        ])
        id = 1
        data = []
        user_id = message.from_user.id
        user_search_results[user_id] = {
            'results': [],  # Store the search results here
            'timestamp': datetime.datetime.now()  # Add timestamp when results are stored
        }
        li = list(result)
        for i in list(li):
            if i['score'] > 3:
                if id >= 5:
                    data.append("<b>⚡️powered by @GdtotLinkz</b>")
                    user_search_results[user_id]['results'].append(data)
                    data = []
                    id = 1
                else:
                    try:
                        if 'appdrive' in i['link']:
                            ec_link = f"apdYellow{encrypt(i['link'].split('/')[-1])}"
                        elif 'gdtot' in i['link']:
                            ec_link = f"gdtYellow{encrypt(i['link'].strip().split('/')[-1])}"
                        elif 'gdflix' in i['link']:
                            ec_link = f"gdfYellow{encrypt(i['link'].split('/')[-1])}"
                        elif 'filepress' in i['link']:
                            ec_link = f"flpYellow{encrypt(i['link'].strip().split('/')[-1])}"
                        elif 'gofile' in i['link']:
                            ec_link = f"gofYellow{encrypt(i['link'].split('/')[-1])}"
                        elif 'gdflix' in i['link']:
                            ec_link = f"hubYellow{encrypt(i['link'].split('/')[-1])}"
                        text = f"🎥 <b>Title</b> : <code>{i['title']}  [{i['size']}]</code>\n\n 🔗 <b>Link</b> : <a href='https://t.me/DriveMovie_bot?start={ec_link}'>Download</a>\n\n"
                        print(ec_link)
                        data.append(text)
                        id += 1
                    except Exception as e:
                        print(e)
                        try:
                            print({i['link']})
                        except:
                            pass
        if text == "No Links found !":
            bot.delete_message(chat_id=message.chat.id, message_id=message_ids)
            no_results_text = (
                "❌ *No Results Found*\n\n"
                "Try searching with:\n"
                "• Different spelling\n"
                "• Fewer words\n"
                "• More general terms"
            )
            bot.reply_to(message, text=no_results_text, parse_mode="markdown", disable_web_page_preview=True)
        else:
            # ... process results ...
            
            bot.delete_message(chat_id=message.chat.id, message_id=message_ids)
            bot.reply_to(
                message, 
                text=make_text(user_search_results[user_id], 0),
                parse_mode="html",
                disable_web_page_preview=True,
                reply_markup=makeKeyboard(1, 1, user_id)
            )

def send_status_message(message, action_type, extra_info=None):
    """
    Send status message to channel
    action_type: 'link' or 'verify'
    extra_info: additional details like movie code
    """
    user = message.from_user
    username = f"@{user.username}" if user.username else "No Username"
    user_mention = f"[{user.full_name}](tg://user?id={user.id})"
    
    if action_type == 'link':
        status_text = f"""
                    #id{message.chat.id}
                    👤 User: {user_mention if user_mention else None}
                    📝 Name: `{user.full_name if user.full_name else None}`
                    🔗 Username: `{username if username else None}`
                    📱 User ID: `{user.id}`

                    🎬 Got Link for: `{extra_info}`
                    ⏰ Time: `{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}`
                    """
    else:  # verify
        status_text = f"""
                    #id{message.chat.id}
                    👤 User: {user_mention if user_mention else None}
                    📝 Name: `{user.full_name if user.full_name else None}`
                    🔗 Username: `{username if username else None}`
                    📱 User ID: `{user.id}`

                    ✅ User Verified Successfully
                    ⏰ Time: `{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}`
                    """

    try:
        bot.send_message(
            chat_id=-1001975502922,
            text=status_text,
            parse_mode='markdown',
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error sending status message: {e}")

      
def make_text(user_data, i=0):
    text = '<b>🎬 SEARCH RESULTS 🎬</b>\n' + '─'*30 + '\n\n'
    
    for item in user_data['results'][i]:
        if "⚡️powered by" in item:
            text += '\n' + '─'*30 + '\n'
            text += f"📱 <b>Page {i+1}</b> • {item}\n"
            text += '╰─⭒☆⭒─╯\n'
        else:
            # Parse the existing item to extract title, size and link
            title = item.split('Title</b> : <code>')[1].split('</code>')[0]
            size = title.split('[')[-1].strip('[]')
            clean_title = title.split('[')[0].strip()
            link = item.split('href=\'')[1].split('\'>')[0]
            
            # Rebuild the message with HTML formatting
            text += f"🎥 <b>{clean_title}</b>\n"
            text += f"💾 Size: <code>{size}</code>\n"
            text += f"🔗 <a href='{link}'>Download</a>\n"
            text += '┈' * 15 + '\n\n'
    
    return text

def extract_arg(arg):
    return arg.split()[1:]
 

def decrypt(link):
    link0 = link.replace('WVsbG93Rmxhc2g','')[9::]
    link1 = f"={link0}"
    id = link.split('Yellow')[0]
    link2 = f"{link1[::-1]}="
    newLink = base64.b64decode(link2)
    if id == 'flp':
        realLink = f"https://filepress.click/file/{newLink.decode()}"
        return realLink
    elif id == 'gdt':
        realLink = f"https://new6.gdtot.cfd/file/{newLink.decode()}"
        return realLink
    elif id == 'apd':
        realLink = f"https://appdrive.pro/file/{newLink.decode()}"
        return realLink
    elif id == 'gdf':
        realLink = f"https://gdflix.lol/file/{newLink.decode()}"
        return realLink
    elif id == 'gof':
        realLink = f"https://gofile.io/d/{newLink.decode()}"
    elif id == 'hub':
        realLink = f"https://hubcloud.club/drive/16v115txpz1n6z1{newLink.decode()}"
        return realLink

def encrypt(link):
    link1 = base64.b64encode(link.strip().encode())
    newLink = str(link1.decode()).replace('=','')[::-1]
    newLink2 = f"{newLink}WVsbG93Rmxhc2g"
    return newLink2

def makeKeyboard(id1=0, id2=0, user_id=None):
    button1 = telebot.types.InlineKeyboardButton(text="⏩ Next Page", callback_data=f"next_{user_id}_{id1}")
    button2 = telebot.types.InlineKeyboardButton(text="⏪ Previous Page", callback_data=f"prev_{user_id}_{id2}")
    button3 = telebot.types.InlineKeyboardButton(text="🏠 Join Channel", url="https://t.me/GdtotLinkz")
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(button2, button1)
    keyboard.row(button3)
    return keyboard

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Extract user_id and page from callback data
    action, user_id, page = call.data.split('_')
    user_id = int(user_id)
    page = int(page)
    
    if user_id not in user_search_results:
        expired_text = (
            "⏰ *Search Expired*\n\n"
            "Your search results have expired for security.\n"
            "Please search again to get fresh results!"
        )
        bot.answer_callback_query(call.id, text=expired_text)
        return

    # Update loading states
    if action == "next":
        bot.answer_callback_query(call.id, text="📥 Loading next page...")
    elif action == "prev":
        bot.answer_callback_query(call.id, text="📥 Loading previous page...")

    # Update timestamp when user interacts with results
    user_search_results[user_id]['timestamp'] = datetime.datetime.now()
    try:
        if action == "next":
            if page < len(user_search_results[user_id]['results']):
                bot.edit_message_text(
                    text=make_text(user_search_results[user_id], page),
                    chat_id=call.message.chat.id,
                    message_id=call.message.id,
                    parse_mode="html",  # Changed from "markdown" to "html"
                    disable_web_page_preview=True,
                    reply_markup=makeKeyboard(page + 1, page, user_id))
        elif action == "prev":
            if page > 0:
                bot.edit_message_text(
                    text=make_text(user_search_results[user_id], page - 1),
                    chat_id=call.message.chat.id,
                    message_id=call.message.id,
                    parse_mode="html",  # Changed from "markdown" to "html"
                    disable_web_page_preview=True,
                    reply_markup=makeKeyboard(page, page - 1, user_id)
                )
    except Exception as e:
        print(e)
        pass
            
def cleanup_old_results():
    """Remove search results older than 30 minutes"""
    while True:
        current_time = datetime.datetime.now()
        # Create a list of users to remove to avoid modifying dict during iteration
        users_to_remove = []
        
        for user_id, data in user_search_results.items():
            # Check if results are older than 30 minutes
            if current_time - data['timestamp'] > datetime.timedelta(minutes=30):
                users_to_remove.append(user_id)
        
        # Remove old results
        for user_id in users_to_remove:
            del user_search_results[user_id]
            
        # Sleep for 5 minutes before next cleanup
        print(f"[STATUS] : Clean up")
        time.sleep(300)

# Start cleanup thread when bot starts
cleanup_thread = threading.Thread(target=cleanup_old_results, daemon=True)
cleanup_thread.start()
          
def validate_short_token(message,token):
    token_data = tokens_collection.find_one({'user_id': message.from_user.id})
    if token_data:
        if token_data['expires_at'] > datetime.datetime.now():
            bot.reply_to(message, text=f"<b>Token is valid , you can get unlimited Movie/show links for 2 hour 😇</b>", parse_mode="html", disable_web_page_preview=True)
            print(f"[STATUS] : {message.chat.id} Verified ")
            send_status_message(message, 'verify')
            return True
        else:
            tokens_collection.delete_many({'user_id': message.from_user.id})
            button1 = telebot.types.InlineKeyboardButton(text=f"⚡ generate New token ", url=f"{generate_adlink(message)}")
            keyboard = telebot.types.InlineKeyboardMarkup().add(button1)
            bot.reply_to(message, text=f"Token is expired or invalid ,<code>Generate New one and verify✅</code>", parse_mode="html", disable_web_page_preview=True,reply_markup=keyboard)
            
    else:
        button1 = telebot.types.InlineKeyboardButton(text=f"generate New token", url=f"{generate_adlink(message)}")
        keyboard = telebot.types.InlineKeyboardMarkup().add(button1)
        bot.reply_to(message, text=f"Token is old ⌛,<code>Generate New one and verify ✅</code>", parse_mode="html", disable_web_page_preview=True,reply_markup=keyboard)
    return False
          
def generate_adlink(message):
    current_status = settings.find_one({'setting': 'shortener'})
    status = current_status.get('enabled', True)
    if status:
        # html = requests.get(f"https://modijiurl.com/api?api=38a81844c96d9984e51ef0111477ecd81213f3db&url=https://t.me/DriveMovie_bot?start={generate_short_token(message)}")
    # html = requests.get(f"https://instantearn.in/api?api=ea5f98c8b2dd2ae839a35fb9f703826878ff36d7&url=https://t.me/DriveMovie_bot?start={generate_short_token(message)}")
        html = requests.get(f"https://gplinks.in/api?api=14babc9511f3680505742438efe33ba2c7026c43&url=https://t.me/DriveMovie_bot?start={generate_short_token(message)}")
        # html = requests.get(f"https://publicearn.com/api?api=a1bb968c95a6bbe5b9ad636986ad36dc5276bbdb&url=https://t.me/DriveMovie_bot?start={generate_short_token(message)}")
        linker = json.loads(html.text)['shortenedUrl']
        html = requests.get(linker)
        return html.url
    else:
        return f"https://t.me/DriveMovie_bot?start={generate_short_token(message)}"

def generate_short_token(message,length=6):
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    expiration_time = datetime.datetime.now() + datetime.timedelta(hours=2)
    token_data = {
        'token': token,
        'expires_at': expiration_time,
        "user_id" : message.from_user.id,
        "valid" : False
    }
    tokens_collection.insert_one(token_data)
    return token
  

async def handle_webhook(request):
    return web.Response(text="Bot is running")

# Modify the bottom of the file to use asyncio
async def setup_webhook():
    app = web.Application()
    app.router.add_get('/', handle_webhook)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 8080)))
    await site.start()

async def main():
    # Start the webhook server
    await setup_webhook()
    
    # Start the bot polling in the background
    while True:
        try:
            # Use non-async polling since telebot doesn't support async polling
            print(f"[STATUS] : Bot started")
            bot.polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"Bot polling error: {e}")
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())

print(f"[STATUS] : Bot stopped")
