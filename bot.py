import telebot
from telebot import types
import random
TOKEN = '1835122693:AAGvWIlOyfUY7T-jbybSgjDgPgasiB9Hk7A'
 
bot = telebot.TeleBot(TOKEN)
 
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('πΈ Tasodifiy raqam')
    item2 = types.KeyboardButton('π Valyuta kurslari')
    item3 = types.KeyboardButton('π Qo`shimcha')
    item4 = types.KeyboardButton('β‘οΈ Keyingisi')
 
    markup.add(item1, item2, item3, item4)
 
    bot.send_message(message.chat.id, 'Hayrli kun, {0.first_name}!'.format(message.from_user), reply_markup = markup)
 
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'πΈ Tasodifiy raqam':
            bot.send_message(message.chat.id, 'Sizning raqamingiz: ' + str(random.randint(0, 1000)))
        elif message.text == 'π Valyuta kurslari':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('πΊπΈ Dollar kursi')
            item2 = types.KeyboardButton('πͺπΊ Evro kursi')
            back = types.KeyboardButton('β¬οΈ Orqaga')
            markup.add(item1, item2, back)
 
            bot.send_message(message.chat.id, 'π Valyuta kurslari', reply_markup = markup)
        
        elif message.text == 'π Qo`shimcha':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('πΎ Bot haqida')
            item2 = types.KeyboardButton('βοΈ Burjlar haqida ma`lumot')
            back = types.KeyboardButton('β¬οΈ Orqaga')
            markup.add(item1, item2, back)
 
            bot.send_message(message.chat.id, 'πQo`shimcha', reply_markup = markup)
 
        elif message.text == 'β‘οΈ Keyingisi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('π  Sozlamalar')
            item2 = types.KeyboardButton('βοΈ Obuna')
            item3 = types.KeyboardButton('π§Έ Stiker')
            back = types.KeyboardButton('β¬οΈ Orqaga')
            markup.add(item1, item2, item3, back)
 
            bot.send_message(message.chat.id, 'β‘οΈ Keyingisi', reply_markup = markup)
        
        elif message.text == 'β¬οΈ Orqaga':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('πΈ Tasodifiy raqam')
            item2 = types.KeyboardButton('π Valyuta kurslari')
            item3 = types.KeyboardButton('π Qo`shimcha')
            item4 = types.KeyboardButton('β‘οΈ Keyingisi')
 
            markup.add(item1, item2, item3, item4)
 
            bot.send_message(message.chat.id, 'β¬οΈ Orqaga', reply_markup = markup)
        
        elif message.text == 'π§Έ Π‘ΡΠΈΠΊΠ΅Ρ':
            stick = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, stick)
 
 
 
bot.polling(none_stop = True)