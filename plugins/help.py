from telethon.tl.custom import Button 
from telethon import events, client
from telethon import sync
import io, os
import config
from .important import CMD_HELP
from . import *




@events.register(events.NewMessage(outgoing=True , pattern=r'\!halp'))
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Unknown module type !halp to see all modules`")
    else:
        await event.edit(" Support Group for help & report bugs @simple_userbot ")
        string = (f"`Use !halp <module_name>`\n\n**Currently Loaded [{len(CMD_HELP)}] Modules **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
 
