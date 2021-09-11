# © BugHunterCodeLabs ™
# © bughunter0 | Nuhman Pk
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message
import YoutubeTags # https://pypi.org/project/youtubetags
from YoutubeTags import videotags
import os


bughunter0 = Client(
    "@BugHunterBots",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@bughunter0.on_message(filters.command(["start"]))
async def start(bot, message):
   await message.reply_text("Join @BugHunterBots") # Edit start text here
   

@bughunter0.on_message(filters.regex("https") | filters.regex("http") & filters.private)
async def tag(bot, message):
    link = str(message.text)
    txt = await message.reply_text("Getting all Tags...")
    tags = videotags(link) # https://github.com/bughunter0/YoutubeTags
    await txt.edit(f"These are the Tags that I Found \n\n\n{tags} \n @BugHunterBots")

bughunter0.run()