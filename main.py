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


def start(update, context):
    id = update.effective_chat.id
    number = context.bot.get_chat_members_count(id)
    if id not in group:
        group[id] = Calculate.Calculate(number)
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="借貸機器人在此為您服務！")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def lend(update, context):
    id = update.effective_chat.id
    if update.effective_user.username is None:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="您沒有username，請填寫完username後再使用此機器人喔！")
    else:
        try:
            group[id].lend(context.args[0],
                           update.effective_user.username, context.args[1])
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="已加入")
        except KeyError:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="機器人尚未啟動，請輸入/start來啟動機器人")


lend_handler = CommandHandler('lend', lend)
dispatcher.add_handler(lend_handler)


def clear(update, context):
    id = update.effective_chat.id
    group[id].clear()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="已將資料清除")


clear_handler = CommandHandler('clear', clear)
dispatcher.add_handler(clear_handler)


def getchosen(update, context):
    id = update.effective_chat.id
    try:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"{group[id].getusername(group[id].getchosen())}為______")
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="目前沒有任何資料喔！")


getchosen_handler = CommandHandler('getchosen', getchosen)
dispatcher.add_handler(getchosen_handler)


def chose(update, context):
    id = update.effective_chat.id
    if context.args is not list:
        getchosen(update, context)
    else:
        group[id].setchosen(context.args[0])
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"已將{context.args[0]}設為______")


chose_handler = CommandHandler('chose', chose)
dispatcher.add_handler(chose_handler)


def calculate(update, context):
    id = update.effective_chat.id
    chosenone = group[id].getchosen()
    sum = group[id].calculate()
    try:
        for i in range(group[id].people): 
            if i != chosenone:
                if sum[i] > 0:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=f"{group[id].getusername(chosenone)} 要給 {group[id].getusername(i)} {sum[i]}元")
                else:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text=f"{group[id].getusername(chosenone)} 要拿 {group[id].getusername(i)} {-sum[i]}元")
    except KeyError:
        pass


calculate_handler = CommandHandler('calculate', calculate)
dispatcher.add_handler(calculate_handler)


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="您可以...")


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="不好意思，我不清楚您的指令，可以查看/help以獲得更多資訊")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()
