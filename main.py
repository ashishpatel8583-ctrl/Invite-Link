from pyrogram import Client
from handlers.task import *
from handlers.join_track import *

app = Client(
    "bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

app.run()
