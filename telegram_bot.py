from re import S
import telebot
import random
from gtts import gTTS
from telebot import types

bot = telebot.TeleBot("5173449174:AAHqmOa_HuI0LQSvTg2CnteEn0XRbsXLjqE")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    myname = message.from_user.first_name
    bot.reply_to(message,f"سلام {myname}به بات من خوش اومدی❤")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,"چه کمکی از دست من برمیاد جیگر؟!😉🤔")

@bot.message_handler(commands =['age'])
def send_age(message):
    bot.reply_to(message,f"سال تولد خود را وارد کنید.")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        year = int(message.text)
        now = 1401 - year
        bot.reply_to(message,f"تواکنون {now} ساله هستی.")


@bot.message_handler(commands=['newgame'])
def send_welcome(message):
    bot.reply_to(message,"عددی بین 1 تا 50 وارد کنید:")

a = random.randint(0,50)
@bot.message_handler(func= lambda m: True)
def echo(message):
    m = int(message.text)
    if a== m:
        bot.reply_to(message,'آفرین درست گفتی😊')
    elif m < a:
        bot.reply_to(message,'برو بالا')
    elif m > a:
        bot.reply_to(message,'برو پایین')

@bot.message_handler(commands=['fal'])
def send_welcome(message):
    fal_list =['به سفرخواهی رفت','به فنا خواهی رفت','به دیدار معشوق خواهی رفت']
    fal = random.choice(fal_list)
    bot.reply_to(message, fal)

@bot.message_handler(func=lambda m: True)
def send_welcome(message):
    if message.text == "سلام":
      bot.reply_to(message,"علیک سلام")  
    elif message.text =="چطوری؟":
        bot.reply_to(message,"مگه تو دکتری؟؟؟؟!!!")  
    elif message.text == "خوابم میاد":
        bot.reply_to(message,"شب بخیر")
    elif message.text == "دوست دارم":
        bot.reply_to(message,"منم دوست دارم عزیزم")
    elif message.text == "چی تنته عشقم؟":
        
        photo = open('set.jpg','rb')
        bot.send_photo(message.chat.id, photo)

    else:
        bot.reply_to(message,"نفهمیدم چی میگی!!")


     

bot.infinity_polling()
