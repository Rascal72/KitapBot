from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import time
import logging 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.command('temizle'))
async def deldirectory(bot, message):
    try:
        text = "DOWNLOADS"
        msg = await message.reply_text("`Siliyorum..`") 
        for files in os.listdir(text):
            os.remove(f"{text}/{files}")
        await msg.edit(f"`{text} Klasörü Başarıyla Silindi..`")
    except Exception as e:
        await message.reply_text(e) 

@Client.on_message(filters.command('indirilenler'))
async def get_directory(bot, message):
    try:
        directory = "DOWNLOADS"
        if 1 == 1:
            if not os.listdir(directory):
                await message.reply(f"{directory} klasörünüz boş")
            else:
                dsy = ""
                say = 0
                for files in os.listdir(directory):
                    say += 1
                    dsy = dsy + "  " + str(say) + "-) " + f"`{directory}/{files}`" + '\n'
                await message.reply_text(
                    f"{directory} Klasöründeki Dosyalar." + "\n\n" + dsy + "\n" + str(
                        say) + " Tane Dosya Var.")
    except Exception as e:
        await message.reply_text(e) 
