from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import time
import shutil
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
        for dosya in os.listdir(text):
            dosyaYolu = os.path.join(text, dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    shutil.rmtree(dosyaYolu)
            except Exception as hata:
                await message.reply_text(hata)
        await msg.edit(f"`{text} Klasörleri Başarıyla Silindi..`")
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

@Client.on_message(filters.command('del'))
async def deldirectory(bot, message):
    try:
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n`/del downloads`") 
            return
        msg = await message.reply_text("`Siliyorum..`") 
        for files in os.listdir(text[1]):
            os.remove(f"{text[1]}/{files}")
        await msg.edit(f"`{text[1]} Klasörü Başarıyla Silindi..`")
    except Exception as e:
        await message.reply_text(e) 

@Client.on_message(filters.command('get'))
async def get_directoryyy(bot, message):
    try:
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n`/get downloads`") 
            return
        directory = text[1]
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

@Client.on_message(filters.command('delfile'))
async def delfilllee(bot, message):
    try:
        text = message.text.split(" ", 1)
        if len(text) < 2:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n`/del downloads/RTE Twerk Yapıyor.mp4`") 
            return
        msg = await message.reply_text("`Siliyorum..`") 
        os.remove(f"{text[1]}")
        await msg.edit(f"`{text[1]} Dosyası Başarıyla Silindi..`")
    except Exception as e:
        await message.reply_text(e)
