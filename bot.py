from plugins import *
import config
import asyncio
import logging

from telethon import TelegramClient as tg
from telethon.sessions import StringSession
import glob
import importlib
import sys
from pathlib import Path

from telethon import events




logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",level=logging.WARNING)


simple = tg(StringSession(str(config.SIMPLE_SESSION)), api_id=config.API_ID, api_hash=config.API_HASH)
simpleBot = tg("bot", api_id=config.API_ID, api_hash=config.API_HASH).start(bot_token=config.BOT_TOKEN)







CMD_HANDLER = "."


def Simple(**args):
    args["pattern"] = "^{}".format(CMD_HANDLER) + args["pattern"]

    def decorator(func):
        async def wrapper(c):
            try:
                await func(c)
            except:
                return

        simple.add_event_handler(wrapper, events.NewMessage(**args))

    return decorator







loop = asyncio.get_event_loop()
simple.start()
simpleBot.start()
loop.run_forever()
print("DONE!")
