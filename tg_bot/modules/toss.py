import random
from telegram.ext import CommandHandler, run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher

@run_async
def toss(bot: Bot, update: Update):
    message = update.effective_message
    toss = bool(random.getrandbits(1))
    
    if toss:
        message.reply_to_message.reply_text("Heads.")
    else:
        message.reply_to_message.reply_text("Tails.")
    

TOSS_HANDLER = CommandHandler("toss", toss)
dispatcher.add_handler(TOSS_HANDLER)
