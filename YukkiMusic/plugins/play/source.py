import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس اسكندر","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6cee33b2fb8d85c625c2d.jpg",
        caption=f"""[✨ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙼𝚄𝚂𝙸𝙲 𝙰𝚂𝙺𝙰𝙽𝙳𝙴𝚁 🎀](https://t.me/E_U_R_O_1)\n\n[✨ 𝙳𝙴𝚅 𝚂𝙾𝚄𝚁𝙲𝙴 𝙰𝚂𝙺𝙰𝙽𝙳𝙴𝚁 🎀](https://t.me/DAD_A_S_K_A_N_D_E_R)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝙲𝙷𝙰𝙽𝙽𝙴𝙻』", url=f"https://t.me/E_U_R_O_1"), 
                ],[
                    InlineKeyboardButton(
                        "𓂄𓆩ꪖ𝘴𝘬ꪖꪀᦔꫀ𝘳𓆪𓂁", url=f"https://t.me/DAD_A_S_K_A_N_D_E_R"),
                ],[
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك 🌐", url=f"https://t.me/Bot_JABWA_Bot?startgroup=true"),
                ],

            ]

        ),

    )
