from lunaBot import pbot
from pyrogram import filters


@pbot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2 :
            return await message.reply_text("Please give a text handwrite.")
    m = await message.reply_text(" Creating..")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("📤 Uploading ...")
    await pbot.send_chat_action(message.chat.id, "upload_photo")
    await message.reply_photo(hand, caption = "Made by @Miss_Akshi2_0_bot")


__mod_name__ = "HandWrite📝✍"
__help__ = """
❍ /write `[text / reply to text]`
"""
