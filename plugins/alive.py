from . import *
from plugins import CMD_HELP
from telethon import events, client


@events.register(events.NewMessage(outgoing=True , pattern=r'\!jinda'))
async def alive_me(event):
  await event.edit(f"**Aha Meh Alive {client.get_me(first_name)} Sir!**")


CMD_HELP.update({"alive": "alive your userbot"})
