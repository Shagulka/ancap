import requests

from random import randint, choice

import requests
import time

import numpy as np

import progressbar

from telethon import *
from telethon.tl.custom import *
from telethon.tl.functions.messages import *

bot = TelegramClient('bot', 1294596, '0f68b54cdb74e06bf2063ba36f8a1ede')


@bot.on(events.NewMessage())
async def start_command(event: Message):
    url = str(event.raw_text)

    try:
        r = requests.get(url, allow_redirects=True)
        await event.reply('Загрузка началась')
        name = url.split('/')[-1]

        open(name, 'wb').write(r.content)
        sender = await event.get_chat()
        await bot.send_file(force_document=True,
                            file=name,
                            entity=sender)
        os.remove(name)
    except:
        time.sleep(0.001)


def main():
    bot.start(bot_token='1786739642:AAHi7YBu_M2vJh-P-BkmsKGlj55fOCSoRq4')
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()







