
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
import os
import time
from pytube import YouTube


dia='✅'
from collections import OrderedDict
os.environ['TZ'] = 'America/Buenos_Aires'
bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"Dev",
			url='https://t.me/dheeraj2324'
		),
        InlineKeyboardButton(
			"Channel",
			url='https://t.me/aboutdheeraj'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    print(chat_id)
    userid= info['username']
    text = f'Welcome @{userid}, to evideos iare'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return
####################################################################################################################################3
# help botstart botcmds botinfo bin

def help(update, context):
    chat_id = update.message.chat_id
    text = "Available cmds available:\n /botinfo \n /bin \n /botcmds \n /help \n /botstart \n MORE WILL BE UPDATED SOON"
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))
def botstart(update, context):
    chat_id = update.message.chat_id
    text = "Hey! I am a CC-Checker!"
    Sendmessage(chat_id, text)

################################################################################################################################
def yt(update,context):
    chat_id = update.message.chat_id
    info = update.effective_user
    chat_id = info.id
    tic = time.perf_counter()
    wdia ='❌'
    crs = '➟'
    dia='✅'
    text =  update.message.text.split(' ', 1)
    link=text[-1]
    url = YouTube(link)
    text="downloading...."
    Sendmessage(chat_id,text)
    video = url.streams.get_highest_resolution()
    path_to_download_folder = r"C:\Users\91889\Downloads"
    video.download(path_to_download_folder)
    text="Downloaded!"
    Sendmessage(chat_id,text)
    
    
######################################################################################################################

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("yt", yt))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
