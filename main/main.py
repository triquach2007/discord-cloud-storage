import sys
sys.dont_write_bytecode = True

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

from bot import Upload_Bot, Download_Bot
from SECRET import TOKEN
import discord

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    b = Download_Bot("Coser@桜井宁宁 Vol.016.rar", intents=intents)
    # b = Upload_Bot(intents=intents)
    b.run(TOKEN)