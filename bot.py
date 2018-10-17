from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

updater = Updater(token='735217499:AAEF0neKtozPpvrxrxlcY_vFxA86pboQw3E')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
                     
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
