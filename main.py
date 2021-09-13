# © BugHunterCodeLabs ™
# © bughunter0 | Nuhman Pk
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os
import pyrogram
from pyrogram import Client, filters
from youtubesearchpython import VideosSearch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags # https://pypi.org/project/youtubetags
from YoutubeTags import videotags


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

@bughunter0.on_message((filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/")) & filters.private)
async def tag(bot, message):
    link = str(message.text)
    try:
       tags = videotags(link) # https://github.com/bughunter0/YoutubeTags
       await message.reply_text(text=f"**These are the Tags that I Found** \n\n `{tags}` \n\n\n @BugHunterBots",reply_markup=SEARCH_BUTTON)
    except :
       await message.reply_text("**No Tags Found For This Video**")
    
# To enable Inline Search, make sure that You Turned on Inline Mode In Your Bot settings


@bughunter0.on_inline_query()
async def search(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Join ©BugHunterBots",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(search_query, limit=50)

        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=" {} .".format(
                       v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out",
                switch_pm_parameter="",
            )


bughunter0.run()
