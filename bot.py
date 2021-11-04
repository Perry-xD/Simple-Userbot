import plugins.alive, plugins.help
import config
import asyncio
import logging


from plugins import simple
from telethon import events




logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",level=logging.WARNING)














simple.start()
simple.run_until_disconnected()

