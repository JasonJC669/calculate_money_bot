
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from modules import Calculate
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

updater = Updater(
    token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def calculate(update, context):
    A = Calculate.Calculate()
    sum = A.calculate(credit=[[1, 2, 3, 4], [1, 2, 3, 4],
                              [1, 2, 3, 4], [1, 2, 3, 4]])
    for i in range(A.people):
        if i != A.chosen:
            if sum[i] > 0:
                #print(f"{A.chosen+1}號 要給 {i+1}號 {sum[i]}元")
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{A.chosen+1}號 要給 {i+1}號 {sum[i]}元")
            else:
                #print(f"{A.chosen+1}號 要拿 {i+1}號 {-sum[i]}元")
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{A.chosen+1}號 要拿 {i+1}號 {-sum[i]}元")


calculate_handler = CommandHandler('calculate', calculate)
dispatcher.add_handler(calculate_handler)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
