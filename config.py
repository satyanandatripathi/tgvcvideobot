from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", None)
API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
SESSION_NAME = getenv("SESSION_NAME", None)
BOT_USERNAME = getenv("BOT_USERNAME", None)


# Bolo shree krishna kaniya lal ki jai 
