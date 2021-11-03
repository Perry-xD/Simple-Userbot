import plugins.alive, plugins.help
from . import *
import asyncio
import sys


from telethon import events
from plugins import simple





if __name__=="__main__":
    simple.start()
    simple.run_until_disconnected()
