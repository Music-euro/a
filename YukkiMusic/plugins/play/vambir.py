import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
     command(["مبرمج السورس","اسكندر","المبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6cee33b2fb8d85c625c2d.jpg",
caption=f"""• الزرار الاول -> قناه السورس \n• الزرار الثاني -> هو مبرمج السورس""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "『𝙲𝙷𝙰𝙽𝙽𝙴𝙻』", url=f"https://t.me/E_U_R_O_1"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "𓂄𓆩ꪖ𝘴𝘬ꪖꪀᦔꫀ𝘳𓆪𓂁", url=f"https://t.me/DAD_A_S_K_A_N_D_E_R"),
                ],
            ]
        ),
    )
