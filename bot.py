import plugins.alive, plugins.help
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
















simple.start()
simple.run_until_disconnected()

