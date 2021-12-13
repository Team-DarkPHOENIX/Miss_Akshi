from telethon import events, Button, custom
import re, os
from lunaBot.events import register
from lunaBot import telethn as tbot
from lunaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/0d239215b8e4382f970ab.mp4"
@register(pattern=("/alive"))
async def awake(event):
 Miss_Akshi = event.sender.first_name
 Miss_Akshi = "♡ I,m Miss_Akshi💕 \n\n"
 Miss_Akshi += "♡ I'm Working with awesome speed**\n\n"
 Miss_Akshi += "**♡Miss_Akshi : 1.0 LATEST**\n\n"
 Miss_Akshi += "**♡ 𝘔𝘺 𝘰𝘸𝘯𝘦𝘳 : [𝘈𝘴𝘩𝘶👑](t.me/Professer_Ashu)\n\n"
 Miss_Akshi += "**♡ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔥", "https://t.me/Miss_AkshiV1_Support"), Button.url("𝘜𝘱𝘥𝘢𝘵𝘦𝘴", "https://t.me/Miss_AkshiV1_Updates")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
