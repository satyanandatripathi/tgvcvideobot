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
    plugins=dict(root="bot"),
)

bot.start()
print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
app.start()
print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
call_py.start()
print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
idle()
print("[STATUS]:❌ »» BOT STOPPED ««")
