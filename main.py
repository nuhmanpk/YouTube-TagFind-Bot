# © BugHunterCodeLabs ™
# © bughunter0 | Nuhman Pk
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message
import YoutubeTags # https://pypi.org/project/youtubetags
from YoutubeTags import videotags
import os

SEARCH_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots')     
        ],
        [
        InlineKeyboardButton('Search Video Here',switch_inline_query_current_chat='')
        ]]
    )

bughunter0 = Client(
    "@BugHunterBots",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@bughunter0.on_message(filters.command(["start"]))
async def start(bot, message):
   await message.reply_text(text = "Join @BugHunterBots ",reply_markup=SEARCH_BUTTON) # Edit start text here
   
# Is there a better way ?? Add a pull
YOUTUBE = filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/")

@bughunter0.on_message(YOUTUBE & filters.private)
async def tag(bot, message):
    link = str(message.text)
    txt = await message.reply_text("Getting all Tags...")
    tags = videotags(link) # https://github.com/bughunter0/YoutubeTags
    await txt.edit(f"**These are the Tags that I Found** \n\n`{tags}` \n\n\n @BugHunterBots")
    await message.reply(text="Join @BugHunterBots" , reply_markup=SEARCH_BUTTON)
bughunter0.run()
