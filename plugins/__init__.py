from telethon.sessions import StringSession
from telethon import TelegramClient as tg

from . import *

CMD_HELP = {}

import os

API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
SIMPLE_SESSION = os.environ['SIMPLE_SESSION']

simple = tg(StringSession(SIMPLE_SESSION), api_id=API_ID, api_hash=API_HASH)
