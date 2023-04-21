from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import time
import logging 

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

async def dosyasil(dosyaYolu, message, textim):
    for dosya in os.listdir(dosyaYolu):
        text = dosyaYolu
        dosyaYolu = os.path.join(text, dosya)
        try:
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
                textim += f"{dosyaYolu}"
            elif os.path.isdir(dosyaYolu):
                for i in os.listdir(dosyaYolu)
                    text = dosyaYolu
                    dosyaYolu = os.path.join(text, dosya)
                
        except Exception as hata:
            await message.reply_text(hata)
    return dosyaYolu

@Client.on_message(filters.command('diskisil'))
async def deldirecttory(bot, message):
    try:
        textim = ""
        text = "DOWNLOADS"
        msg = await message.reply_text("`Siliyorum..`") 
        for dosya in os.listdir(text):
            dosyaYolu = os.path.join(text, dosya)
            try:
                if os.path.isfile(dosyaYolu):
                    os.remove(dosyaYolu)
                elif os.path.isdir(dosyaYolu):
                    dosyaYolu = await dosyasil(dosyaYolu, message, textim)
                    if os.path.isfile(dosyaYolu):
                        os.remove(dosyaYolu)
                    elif os.path.isdir(dosyaYolu):
                        await dosyasil(dosyaYolu, message, textim)
            except Exception as hata:
                await message.reply_text(hata)
        await msg.edit(f"`{textim} Dosyaları Başarıyla Silindi..`")
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
