import random
from telegram.ext import CommandHandler, run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher

@run_async
def flip(bot: Bot, update: Update):
    message = update.effective_message
    flip = bool(random.getrandbits(1))
    
    if flip:
        message.reply_to_message.reply_text("Heads.")
    else:
        message.reply_to_message.reply_text("Tails.")
    

FLIP_HANDLER = CommandHandler("flip", flip)
dispatcher.add_handler(FLIP_HANDLER)
