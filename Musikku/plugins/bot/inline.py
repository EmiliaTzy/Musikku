#
# Copyright (C) 2021-2022 by kenkansaja@Github, < https://github.com/kenkansaja >.
#
# This file is part of < https://github.com/kenkansaja/Musikku > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/kenkansaja/Musikku/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup,
                            InlineQueryResultPhoto)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS, MUSIC_BOT_NAME
from Musikku import app
from Musikku.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[
                0
            ]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Nonton Di Youtube",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
❇️**Judul:** [{title}]({link})

⏳**Durasi:** {duration} Menit
👀**Penonton:** `{views}`
⏰**Waktu Publikasi:** {published}
🎥**Nama Channel:** {channel}
📎**Tautan Channel:** [Kunjungi Dari Sini]({channellink})

__Balas dengan /play pada pesan yang dicari ini untuk mengalirkannya di obrolan suara.__

⚡️ ** Pencarian Inline Oleh {MUSIC_BOT_NAME} **"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(
                query.id, results=answers
            )
        except:
            return
