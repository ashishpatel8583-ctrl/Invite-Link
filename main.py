from pyrogram import Client
from handlers.task import *
from handlers.join_track import *

app = Client(
    "bot",
    api_id=int(os.getenv("27194475")),
    api_hash=os.getenv("b9eaaeead349eb9c593bfe9ae04ded7d"),
    bot_token=os.getenv("BOT_TOKEN")
)

app.run()
