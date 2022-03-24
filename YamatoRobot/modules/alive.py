import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YamatoRobot.events import register
from YamatoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/8636589aac0d6c10f8db0.jpg"

@register(pattern=("/halive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Yamato Nice to Meet you💖💜** \n\n"
  TEXT += "💠 **I'm Working Properly** \n\n"
  TEXT += f"💠 **My Master : [Kazutora Hanemiya](https://t.me/zerohisoka)** \n\n"
  TEXT += f"💠 **Library Version :** `{telever}` \n\n"
  TEXT += f"💠 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💠 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/BoaHancock_Robot?start=help"), Button.url("ᴀɴɪᴍᴇ ᴄʜᴀᴛ", "https://t.me/straydogs")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
