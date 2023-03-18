#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28859709
API_HASH = c0ce6297f36cef47e540c1f506cef223
BOT_TOKEN = 6122544604:AAH-v5wNgvoZG0FMaIBv6uUx3iZakDUdDRg
SESSION = BQAHIkx-QXeZ0BYxxaMcnqpFUWRRt5oCkdqBfOmr3v1scibnEY6QVToVC-5bQ9X3wDt80eB3B62tZnL_B7OO02XkOKJDT_QCjU97tB6NKtv-G6LFQQsLO7ZaTf-4Lixedp3nd4tESo_fstUuU79w8dbTvrGxzaKNGETOLUhpVhcE-UcuycMuL_1rZiOAwIAL_TOu_ztphXKhvcT1g_ooEA8D2A1fptbGTlHX7PpGFA2SCecaOhWD_hi_Wq_D_oWggPaV_vkS-wTnimI1rPOuEVh3cY-Nlzn6vAtzG76nkT5bf43uxWYLIX9K4w71XfQSkSAdR0Br_GKCSyfrlOaeCepNaxydIAA
FORCESUB = config("FORCESUB", default=None)
AUTH = 1797037344
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
