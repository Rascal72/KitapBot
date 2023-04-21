from pyrogram import Client, filters
from sys import executable
import os
import asyncio

@Client.on_message(filters.command('onbellek'))
async def onbellek(bot, message):
    try:
        command = ["bash","onbellek.sh"]
        process = await asyncio.create_subprocess_exec(
            *command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            )
        await message.reply_text("Önbellek Silindi..")
    except Exception as e:
        await message.reply_text(e)
