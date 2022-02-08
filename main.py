import telebot
import random

from telebot import types

def tre(corzina):
    a = ''
    total = 0
    for i, j in corzina.items():
        print(i, j)
        a += str(i)
        a += '   ' + str(j) + '$' + '\n'
        total += j
        print(a, total)
    a += '\n' + 'Сумма: ' + str(total)+ "$"
    return a


bot = telebot.TeleBot("5058513599:AAGLVTYW4CyrPHc8xZsZUWgKcx-coFs_OSA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
corzina = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ноутбуки 💻')
    itembtn2 = types.KeyboardButton('Стационарки 🖥')
    itembtn3 = types.KeyboardButton('Корзина 🛒')

    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id,
                     "Выберите компьютер: ",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':

        if message.text == 'Ноутбуки 💻':
            markup = types.InlineKeyboardMarkup(row_width=2)
            nout1 = telebot.types.InlineKeyboardButton("Macbook",  callback_data = 'mac')
            nout2 = telebot.types.InlineKeyboardButton("Dell inspiron", callback_data = 'dell')
            nout3 = telebot.types.InlineKeyboardButton("Lenovo", callback_data = 'lenovo')
            nout4 = telebot.types.InlineKeyboardButton("Acer", callback_data = 'acer')
            nout5 = telebot.types.InlineKeyboardButton("HP", callback_data = 'hp')
            markup.add(nout1, nout2, nout5, nout4, nout3)
            bot.send_message(message.chat.id,
                             "Выберите какой нутбук 💻",
                             reply_markup=markup)
        elif message.text == 'Корзина 🛒':
            if corzina == {}:
                bot.send_message(message.chat.id, 'Корзина пуста 🛒')
            else:
                print('1')
                korzin = types.InlineKeyboardMarkup(row_width=1)
                print('2')
                cor = telebot.types.InlineKeyboardButton('Очистить корзину 🛒', callback_data = 'clear_bin')
                print('3')
                korzin.add(cor)
                print('4')
                bot.send_message(message.chat.id, tre(corzina), reply_markup=korzin)
                print('5')

        elif message.text == 'Стационарки 🖥':
            markup = types.InlineKeyboardMarkup(row_width=2)
            nout1 = telebot.types.InlineKeyboardButton("Видеокарта",  callback_data = 'gpu')
            nout2 = telebot.types.InlineKeyboardButton("Процессор", callback_data = 'cpu')
            nout3 = telebot.types.InlineKeyboardButton("Оперативная память", callback_data = 'ram')
            nout4 = telebot.types.InlineKeyboardButton("Память", callback_data = 'ssd')
            nout5 = telebot.types.InlineKeyboardButton("Материнская плата", callback_data = 'plata')
            nout6 = telebot.types.InlineKeyboardButton("Блок питания", callback_data = 'pitanie')
            markup.add(nout1, nout2, nout3, nout4, nout5, nout6)
            bot.send_message(message.chat.id,
                             "Выберите комплектующие",
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id,
                             "Обратитесь к консультанту 👨‍💼")





@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'mac':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_mac')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '1050$', reply_markup=markup)
        if call.data == 'dell':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_dell')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '850$', reply_markup=markup)

        if call.data == 'lenovo':

            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_len')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '500$', reply_markup=markup)

        if call.data == 'clear_bin':
            global corzina
            print(7)
            corzina = {}


        if call.data == 'acer':

            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_acer')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)

            bot.send_message(call.message.chat.id, '350$', reply_markup=markup)

        if call.data == 'hp':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_hp')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)

        if call.data == 'gpu':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_gpu')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
        if call.data == 'cpu':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_cpu')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
        if call.data == 'ram':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_ram')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
        if call.data == 'ssd':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_ssd')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
        if call.data == 'pitanie':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_pitanie')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
        if call.data == 'plata':
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину? 🛒', callback_data='corzina_plata')
            btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
            markup.add(btn1, btn2)
            bot.send_message(call.message.chat.id, '150$', reply_markup=markup)



        if call.data == 'corzina_hp':
            corzina['HP'] = 150
            print(corzina)
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
            # return corzina
        if call.data == 'corzina_len':
            corzina['Lenovo'] = 500
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
            # return corzina
        if call.data == 'corzina_acer':
            corzina['Acer'] = 350
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
            # return corzina
        if call.data == 'corzina_dell':
            corzina['Dell inspiron'] = 850
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
            # return corzina
        if call.data == 'corzina_mac':
            corzina['MacBook Pro'] = 1050
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
            # return corzina

        if call.data == 'back':
            pass


        if call.data == 'corzina_gpu':
            corzina['Видеокарта'] = 300
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
        if call.data == 'corzina_cpu':
            corzina['Процессор'] = 160
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
        if call.data == 'corzina_ram':
            corzina['Оперативная память'] = 20
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
        if call.data == 'corzina_ssd':
            corzina['Жесткий диск'] = 50
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
        if call.data == 'corzina_pitanie':
            corzina['Блок питания'] = 20
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')
        if call.data == 'corzina_plata':
            corzina["Материнская плата"] = 50
            bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину 🛒\nПроверьте свою корзину!')



# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     try:
#         if call.message:
#             if call.data == 'mac':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_mac')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '1050$', reply_markup=markup)
#             if call.data == 'dell':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_dell')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '850$', reply_markup=markup)
#
#             if call.data == 'lenovo':
#
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_len')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '500$', reply_markup=markup)
#
#             if call.data == 'acer':
#
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_acer')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#
#                 bot.send_message(call.message.chat.id, '350$', reply_markup=markup)
#
#             if call.data == 'hp':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_hp')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#
#             if call.data == 'gpu':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_gpu')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#             if call.data == 'cpu':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_cpu')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#
#             if call.data == 'ram':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_ram')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#             if call.data == 'ssd':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_ssd')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#             if call.data == 'plata':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_plata')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#             if call.data == 'pitanie':
#                 markup = types.InlineKeyboardMarkup(row_width=2)
#                 btn1 = telebot.types.InlineKeyboardButton('Добавить товар в корзину?', callback_data='corzina_pitanie')
#                 btn2 = telebot.types.InlineKeyboardButton('Назад...', callback_data="back")
#                 markup.add(btn1, btn2)
#                 bot.send_message(call.message.chat.id, '150$', reply_markup=markup)
#
#
#             bot.edit_message_text(
#                 chat_id=call.message.chat.id,
#                 message_id=call.message.message_id
#             )
#             if call.data == 'back':
#                 bot.send_message(call.message.chat.id, 'asdasdsa')
#     except:
#         print('Error1')
#
# @bot.callback_query_handler(func= lambda call: True)
# def korzina(call):
#     try:
#         if call.message:
#             if call.data == 'corzina_hp':
#                 corzina['hp'] = '150$'
#                 bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину\nПроверьте свою корзину!')
#                 # return corzina
#             if call.data == 'corzina_len':
#                 corzina['lenovo'] = '500$'
#                 bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину\nПроверьте свою корзину!')
#                 # return corzina
#             if call.data == 'corzina_acer':
#                 corzina['acer'] = '350$'
#                 bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину\nПроверьте свою корзину!')
#                 # return corzina
#             if call.data == 'corzina_dell':
#                 corzina['dell'] = '850$'
#                 bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину\nПроверьте свою корзину!')
#                 # return corzina
#             if call.data == 'corzina_mac':
#                 corzina['mac'] = '1050$'
#                 bot.send_message(call.message.chat.id, 'Товар успешно был добавлен в корзину\nПроверьте свою корзину!')
#                 # return corzina
#     except:
#         print('Error')
#
#
#
#
#
#
#
#


bot.polling(none_stop=True)





# @bot.message_handler(commands=['start'])
# def welcome(message):
#
#     # keyboard
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton("🎲 Рандомное число")
#     item2 = types.KeyboardButton("😊 Как дела?")
#
#     markup.add(item1, item2)
#
#     bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
#         parse_mode='html', reply_markup=markup)
#
# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     if message.chat.type == 'private':
#         if message.text == '🎲 Рандомное число':
#             bot.send_message(message.chat.id, str(random.randint(0,100)))
#         elif message.text == '😊 Как дела?':
#
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
#             item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
#
#             markup.add(item1, item2)
#
#             bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
#
#             markup = types.ReplyKeyboardRemove(selective=False)
#             bot.send_message(message.chat.id, 'qwe' ,reply_markup=markup)
#         else:
#             bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'good':
#                 bot.send_message(call.message.chat.id, 'Вы: Хорошо')
#                 bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
#                 call.data = 'Отлично, сам как?'
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Вы: Не очень')
#                 bot.send_message(call.message.chat.id, 'Бывает 😢')
#                 call.data = 'Отлично, сам как?'
#
#             # remove inline buttons
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.data,
#                 reply_markup=None)
#
#
#     except Exception as e:
#         print(repr(e))
#
# # RUN
# bot.polling(none_stop=True)
