from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import re
import requests


def GetAddress():
    object_received = requests.get('https://meme-api.herokuapp.com/gimme').json()
    address = object_received['url']
    return address


def GetImageAddress():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        address = GetAddress()
        file_extension = re.search("([^.]*)$", address).group(1).lower()
    return address


@run_async
def Meme(update, context):
    image_address = GetImageAddress()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=image_address)


def main():
    updater = Updater('1406466573:AAG8lo64WwyvavdRetxb7gtnp4Dj73ywc4I', use_context=True)
    dispatcher_ = updater.dispatcher
    dispatcher_.add_handler(CommandHandler('meme', Meme))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
