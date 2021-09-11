# Surprise MF

import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from tgvcvideo.tgvcvideoplayer import app
from tgvcvideo.tgvcvideoplayer import call_py

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="tgvcvideo"),
)

bot.start()
print("[STATUS]:✅ »» BOT Client has been successfully Started ««")
app.start()
print("[STATUS]:✅ »» USERBOT Client has been successfully Started ««")
call_py.start()
print("[STATUS]:✅ »» PYTGCALLS Client has been successfully Started ««")
