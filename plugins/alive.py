from . import *


@Simple(pattern="alive")
async def alive_me(event):
  await event.edit(f"**Aha Meh Alive {simple.get_me(first_name)} Sir!**")


CMD_HELP.update({"alive": "alive your userbot"})
