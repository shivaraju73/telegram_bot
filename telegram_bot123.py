import os


x = "shivaraj73" #ADAFRUIT_IO_USERNAME
y = "aio_hevN47NjCk7PEJ5CwwsDk5AGTICd"  #ADAFRUIT_IO_KE



from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud 
 

def get_url(): 
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth turned on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=1)
    value_send = aio.create_data('telebot',value)
 
def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth turned off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=0)
    value_send = aio.create_data('telebot',value)


u = Updater('1350574600:AAHmi8ThWTrYce8YlEVPMTfFPISiKF5dvJo')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()

