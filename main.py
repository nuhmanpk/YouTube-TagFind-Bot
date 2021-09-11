# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message
import os
from userbase import present_in_userbase, add_to_userbase, get_users, del_from_userbase
import time
from pyrogram.errors import (
    FloodWait,
    PeerIdInvalid,
    UserIsBlocked,
    InputUserDeactivated
)
import asyncio


bughunter0 = Client(
    "name",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_STRING_PRIVATE = """ Hi {}, I'm Youtube Video Tag Extractor,
 Send me a Youtube video Link to Get started
"""

ABOUT = """
● **BOT:** `YouTube Tag Extractor` 
● **AUTHOR :** [bughunter0](https://t.me/bughunter0) 
● **SERVER :** `Heroku` 
● **LIBRARY :** `Pyrogram` 
● **LANGUAGE :** `Python 3.9` 
● **SOURCE :** [BugHunterBots](https://t.me/BugHunterBots/93) 
"""
HELP = """

"""


CHANNEL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')
        ]]
    )

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📑 ABOUT 📑',callback_data='cbabout'),
        InlineKeyboardButton('📛 HELP 📛',callback_data='cbhelp')
        ],
        [
        InlineKeyboardButton('⭐ Rate Me Here ⭐', url='https://t.me/BugHunterBots'),
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')      
        ]]        
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('◀ Back ',callback_data='cbclose'),
        ]]
    )
DONATE_STRING = """ Happy To know that You are Willing to Donate!! Small Support in form of Donation is a little help to My Creator. All donation money goes straight to Host Bots On VPS(Dream), May The Dream come True. 
You can donate Me Here, (Currently for Indian Users Only)
"""

DONATE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ko-Fi' ,url='https://ko-fi.com/nuhmanpk'),
        ],
        [
        InlineKeyboardButton('₹25',url='https://paytm.me/fZ-PsaK'),
        InlineKeyboardButton('₹149',url='https://paytm.me/p-tPE0l'),
        InlineKeyboardButton('₹249',url='https://paytm.me/yoB-s0a'),
        ],
        [InlineKeyboardButton('₹499', url="https://paytm.me/8sRT-FA")
        ],
        [InlineKeyboardButton('Buy Me a Ko-Fi', url="https://ko-fi.com/nuhmanpk")
        ]]       
    )

@bughunter0.on_message((filters.command(["donate"])))
async def donate(bot, update):
    text = DONATE_STRING
    reply_markup = DONATE_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_callback_query() # callbackQuery()
async def cb_data(bot, update): 
           
           if update.data == "cbhelp":
              await update.message.edit_text(
              text=HELP,
              reply_markup=CLOSE_BUTTON,
              disable_web_page_preview=True
           )
           elif update.data == "cbdata":                
              await update.message.edit_text(
              text=dataurl.fulldata,
              reply_markup=BACK_BUTTON,
              disable_web_page_preview=True
           )
              return
           
           elif update.data == "cbabout":
              await update.message.edit_text(
              text=ABOUT,
              reply_markup=CLOSE_BUTTON,
              disable_web_page_preview=True
           ) 
           
           else:
              await update.message.edit_text(
              text=START_STRING_PRIVATE.format(update.from_user.mention),
              disable_web_page_preview=True,
              reply_markup=START_BUTTON
           )


@bughunter0.on_message(filters.private & filters.command('broadcast') & filters.user(778307700) & filters.reply)
async def broadcast(client: bughunter0, message: Message):
       broadcast_msg = str(message.reply_to_message.text)
       message = await message.reply(text = 'Staring....')        
       user_ids = await get_users()
       success = 0
       deleted = 0
       blocked = 0
       peerid = 0
       await message.edit(text = 'Broadcasting message, Please wait', reply_markup = None)   
       for user_id in user_ids:
          try:
            await bughunter0.send_message(text=broadcast_msg, chat_id=user_id)
            success += 1
            time.sleep(3)
          except FloodWait as e:
            await asyncio.sleep(e.x)
            success += 1
          except UserIsBlocked:
            blocked += 1
          except PeerIdInvalid:
            peerid += 1
          except InputUserDeactivated:
            deleted += 1                       
       text = f"""<b>Broadcast Completed</b>    
Total users: {str(len(user_ids))}
Blocked users: {str(blocked)}
Deleted accounts: {str(deleted)} (<i>Deleted from Database</i>)
Failed : {str(peerid)}"""
       await message.reply(text=text)
       await message.delete()
 

    


bughunter0.run()
