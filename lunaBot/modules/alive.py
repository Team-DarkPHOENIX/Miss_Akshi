from telethon import events, Button, custom
import re, os
from lunaBot.events import register
from lunaBot import telethn as tbot
from lunaBot import telethn as tgbot
PHOTO = "https://te.legra.ph/file/e22a86d0b5263d72fda15.jpg"
@register(pattern=("/alive"))
async def awake(event):
 godzilla = event.sender.first_name
 godzilla  = "♡ I,m Godzilla  \n\n"
 godzilla += "♡ I'm Working with awesome speed**\n\n"
 godzilla += "**godzilla  : 1.0 LATEST**\n\n"
 godzilla += "**♡ 𝘔𝘺 𝘰𝘸𝘯𝘦𝘳 : [Ajay](t.me/XXXTENTACION_forever)\n\n"
 godzilla  += "**♡ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔥", "https://t.me/godzilla_robot_Support"), Button.url("network", "https://t.me/godzilla_network")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
