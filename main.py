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

group = {}


def chose(update, context):
    id = update.effective_chat.id
    group[id].setchosen(context.args[0])
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="done")


chose_handler = CommandHandler('chose', chose)
dispatcher.add_handler(chose_handler)


def getchosen(update, context):
    id = update.effective_chat.id
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=group[id].getusername(group[id].getchosen()))


getchosen_handler = CommandHandler('getchosen', getchosen)
dispatcher.add_handler(getchosen_handler)


def calculate(update, context):
    id = update.effective_chat.id
    chosenone = group[id].getchosen()
    print(chosenone)
    sum = group[id].calculate()
    for i in range(group[id].people):  # i超過總借貸人數時會有KeyError
        if i != chosenone:
            if sum[i] > 0:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{group[id].getusername(chosenone)} 要給 {group[id].getusername(i)} {sum[i]}元")
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=f"{group[id].getusername(chosenone)} 要拿 {group[id].getusername(i)} {-sum[i]}元")


calculate_handler = CommandHandler('calculate', calculate)
dispatcher.add_handler(calculate_handler)


def add(update, context):
    id = update.effective_chat.id
    group[id].add(context.args[0],
                  update.effective_user.username, context.args[1])
    # 如果使用者未設定username，換成id會變成None
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="done")


add_handler = CommandHandler('add', add)
dispatcher.add_handler(add_handler)


def start(update, context):
    id = update.effective_chat.id
    number = context.bot.get_chat_members_count(id)
    print(number)
    if id not in group:
        group[id] = Calculate.Calculate(number)
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
