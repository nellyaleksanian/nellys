import telebot
from telebot import types
bot = telebot.TeleBot('6509829116:AAGjQ__-0hK0mJ5YcDb0-hCSKZwrh03Ks2k')


@bot.message_handler(commands=['start'])
def start(message):
    hellomessage = f'Привет, <b>{message.from_user.first_name}</b>\nЯ помогу вам познакомиться с Нелли!\nВот что я умею:'
    markup = types.InlineKeyboardMarkup()
    selfiebtn = types.InlineKeyboardButton('Показать селфи', callback_data='showselfie')
    hsbtn = types.InlineKeyboardButton('Показать фото из старшей школы', callback_data='showhs')
    postbtn = types.InlineKeyboardButton('Рассказать о главном увлечении', callback_data='post')
    voicebtn = types.InlineKeyboardButton('Отправить голосовые сообщения', callback_data='voicemsg')
    markup.row(selfiebtn)
    markup.row(hsbtn)
    markup.row(postbtn)
    markup.row(voicebtn)
    bot.send_message(message.chat.id, hellomessage, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'showselfie':
        photo = open("myselfie.jpg",'rb')
        bot.send_photo(callback.message.chat.id, photo=photo)
    elif callback.data == 'showhs':
        photo = open("highschool.jpg", 'rb')
        bot.send_photo(callback.message.chat.id, photo=photo)
    elif callback.data == 'post':
        posttext="Моим главным увлечением является музыка. С детства меня окружала музыкальная атмосфера – у меня музыкальная семья, где все играют на разных инструментах. Я пою с самого детства и начала играть на гитаре и пианино в 11 лет. Музыка для меня – это способ выразить свои эмоции и мысли, она помогает мне расслабляться и собирать мысли."
        bot.send_message(callback.message.chat.id, posttext)
    elif callback.data == 'voicemsg':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('GPT')
        btn2 = types.KeyboardButton('SQL')
        btn3 = types.KeyboardButton('Love')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        bot.send_message(callback.message.chat.id, 'Если вы хотите узнать о <i>GPT</i> напишите <b>GPT</b>\nЕсли вы хотите узнать о разнице между <i>SQL и NoSQL</i> напишите <b>SQL</b>\nЕсли вы хотите узнать про <i>историю первой любви</i> напишите <b>Love</b>', parse_mode='html', reply_markup=markup)

        bot.register_next_step_handler(callback.message, on_click)

@bot.message_handler(content_types=["text"])
def on_click(mess):
    if mess.text == 'GPT':
                audio = open("gpt.mp3", 'rb')
                bot.send_audio(mess.chat.id, audio=audio)
                audio.close()
    elif mess.text == 'SQL':
                    audio = open("sql.mp3", 'rb')
                    bot.send_audio(mess.chat.id, audio=audio)
                    audio.close()
    elif mess.text == 'Love':
                    audio = open("love.mp3", 'rb')
                    bot.send_audio(mess.chat.id, audio=audio)
                    audio.close()


bot.polling(none_stop=True)
