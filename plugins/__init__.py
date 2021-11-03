from telethon.sessions import StringSession
from telethon import TelegramClient as tg
from config import *
from . import *

CMD_HELP = {}

simple = tg(StringSession(config.SIMPLE_SESSION), api_id=config.API_ID, api_hash=config.API_HASH)
