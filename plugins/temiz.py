from pyrogram import Client, filters
from sys import executable
import os
import asyncio

@Client.on_message(filters.command('onbellek'))
async def onbellek(bot, message):
    try:
        msg = await message.reply_text("Önbellek Siliniyor..") 
        command = ["bash","onbellek.sh"]
        process = await asyncio.create_subprocess_exec(
            *command,
            # stdout must a pipe to be accessible as process.stdout
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            )
        await asyncio.wait([
            read_stderr(start,msg, process),
            process.wait(),
        ])
    
        if process.returncode == 0:
            await msg.edit('Önbellek Silindi..')
        else:
            await msg.edit('Önbellek Silinemedi..')
    except Exception as e:
        await message.reply_text(e)
