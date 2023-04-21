from pyrogram import Client, filters
from sys import executable
import os

@Client.on_message(filters.command('onbellek'))
async def onbellek(bot, message):
    try:
        os.execl(executable, executable, "onbellek.sh")
        await message.reply_text("Önbellek Silindi..")
    except Exception as e:
        await message.reply_text(e)
