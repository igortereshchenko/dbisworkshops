import telebot
from telebot import types

import check_function

API_TOKEN = '1240952041:AAGgpZ6C_-Ttga9fFgFKgdFImeV6GLcjd1s'

bot = telebot.TeleBot(API_TOKEN,threaded=False)
@bot.message_handler(commands=['start'])

def handle_text(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup()
    keyboard1.row('Поиск рецепта🥮')
    keyboard1.row('Правила использования📄')
    keyboard1.row('Помощь❓')

    bot.send_message(message.chat.id,
                     'Готовить стало ещё проще!\n'
                     'Добро пожаловать,' + str(message.from_user.username) + '\nЭтот бот предоставит вам возможность \nне только найти новые рецепты, но\nтакже сохранить их в кулинарную книгу\n Выберите одну из категорий ниже ',
                     reply_markup=keyboard1)

    result = check_function.check_user_exist(str(message.from_user.username))
    print(result)

#
@bot.message_handler(commands=['help'])

def handle_text(message):
    bot.send_message(message.from_user.id,
                     'Вы используете бот для поиска рецептов\n''Ниже представленны команды, которые существуют в боте:\n''/start - начало работы с ботом\n''/help - основные команды бота\n''/first_dishes - список доступных супов\n''/salads - список доступных салатов\n''/main_dishes - список доступных основніх блюд,\n''/desserts - список доступных дессертов,\n''/statistic - посмотреть статистику оценок,\n''/add_comment - добавить комментарий,\n''/see_comments - посмотреть комментарии других пользователей')


@bot.message_handler(commands=['first_dishes'])
def handle_text(message):
    result = check_function.see_all_soups()
    print(result)
    for i in range(len(result)):
        bot.send_message(message.from_user.id, result[i])

@bot.message_handler(commands=['salads'])
def handle_text(message):
    result = check_function.see_all_salads()
    for i in range(len(result)):
        bot.send_message(message.from_user.id, result[i])

@bot.message_handler(commands=['main_dishes'])
def handle_text(message):
    result = check_function.see_all_main_dishes()
    for i in range(len(result)):
        bot.send_message(message.from_user.id, result[i])

@bot.message_handler(commands=['desserts'])
def handle_text(message):
    result = check_function.see_all_desserts()
    for i in range(len(result)):
        bot.send_message(message.from_user.id, result[i])

@bot.message_handler(commands=['statistic'])
def handle_text(message):

    result = check_function.statistic_of_marks()
    print(type(result))
    bot.send_message(message.from_user.id,'Количество ценок "1" - '+ str(result[0])+'.')
    bot.send_message(message.from_user.id, 'Количество ценок "2" - ' + str(result[1]) + '.')
    bot.send_message(message.from_user.id, 'Количество ценок "3" - ' + str(result[2]) + '.')
    bot.send_message(message.from_user.id, 'Количество ценок "4" - ' + str(result[3]) + '.')
    bot.send_message(message.from_user.id, 'Количество ценок "5" - ' + str(result[4]) + '.')

    average = check_function.avarage_of_mark()
    bot.send_message(message.from_user.id, 'Средняя оценка - ' + str(average) + '.')

@bot.message_handler(commands=['add_comment'])
def handle_text(message):
    sent = bot.send_message(message.chat.id, 'Введите свой комментарий')
    bot.register_next_step_handler(sent, comments)

@bot.message_handler(commands=['see_comments'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Комментарии других пользователей: ')
    result = check_function.see_users_comments()
    print(result)
    for i in range(len(result)):
        bot.send_message(message.chat.id, str((list(result[i]))[0]) + ': ' + str((list(result[i]))[1]))

def comments(message):
        check_function.add_comments(message.text, str(message.from_user.username))
        print(message.text)
        bot.send_message(message.chat.id,'Спасибо, ваш комментарий был успешно добавлен!')

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == 'Правила использования📄':
        bot.send_message(message.from_user.id,
                         '1. Для начала работы с ботом, необходимо ввести команду /start\n''2.Для поиска рецепта нажмите клавишу "поиск рецепта"\n''3.Выберите категорию, к которой относится блюдо, которое вы хотите найти,ВАЖНО,бот сможет найти блюдо в заданой категории, только, если оно относится к этой категории\n''4.Вы можете просмотреть видео рецепт блюда или просто  прочиатть его,подтвердив свой выбор нажатием на соответствующюю клавишу\n''5.После окончания работы с ботом, вы можете поставить ем оценку и оставить комментарий.')
    elif message.text == 'Помощь❓':

        bot.send_message(message.from_user.id,
                         'Вы используете бот для поиска рецептов\n''Ниже представленны команды, которые существуют в боте:\n''/start - начало работы с ботом\n''/help - основные команды бота\n''/first_dishes - список доступных супов\n''/salads - список доступных салатов\n''/main_dishes - список доступных основніх блюд,\n''/desserts - список доступных дессертов,\n''/statistic - посмотреть статистику оценок')
    elif message.text == 'Поиск рецепта🥮':

        keyboard = types.InlineKeyboardMarkup()
        key_sup = types.InlineKeyboardButton(text='Первые блюда 🍲', callback_data='soups')
        # И добавляем кнопку на экран
        keyboard.add(key_sup)
        key_main = types.InlineKeyboardButton(text='Основные блюда 🥘', callback_data='main_dishes')
        keyboard.add(key_main)
        key_salad = types.InlineKeyboardButton(text='Салаты 🥗', callback_data='salads')
        keyboard.add(key_salad)
        key_sweet = types.InlineKeyboardButton(text='Дессерты 🍰', callback_data='sweets')
        keyboard.add(key_sweet)

        bot.send_message(message.from_user.id, "Выбери категорию.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'soups')
def callback_worker(call):

        keyboard = types.InlineKeyboardMarkup()
        key_text = types.InlineKeyboardButton(text='Посмотреть рецепт в текстовой формe', callback_data='text')
        keyboard.add(key_text)
        key_video = types.InlineKeyboardButton(text='Посмотреть видео рецепт', callback_data='video')
        keyboard.add(key_video)
        bot.send_message(call.message.chat.id, "Выберите один из возможных вариатнтов", reply_markup=keyboard)


        @bot.callback_query_handler(func=lambda call: call.data == 'text')
        def callback_worker(call):
                sent = bot.send_message(call.message.chat.id, 'Введите название супа 🍲')
                bot.register_next_step_handler(sent,text_recipe)

        @bot.callback_query_handler(func=lambda call: call.data == 'video')
        def callback_worker(call):
                sent = bot.send_message(call.message.chat.id, 'Введите название супа 🍲')
                bot.register_next_step_handler(sent, video_recipe)

@bot.callback_query_handler(func=lambda call: call.data == 'main_dishes')
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_text = types.InlineKeyboardButton(text='Посмотреть рецепт в текстовой формe', callback_data='text')
    keyboard.add(key_text)
    key_video = types.InlineKeyboardButton(text='Посмотреть видео рецепт', callback_data='video')
    keyboard.add(key_video)
    bot.send_message(call.message.chat.id, "Выберите один из возможных вариатнтов", reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data == 'text')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название основного блюда🥘')
        bot.register_next_step_handler(sent,text_recipe)

    @bot.callback_query_handler(func=lambda call: call.data == 'video')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название основного блюда🥘')
        bot.register_next_step_handler(sent, video_recipe)


@bot.callback_query_handler(func=lambda call: call.data == 'salads')
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_text = types.InlineKeyboardButton(text='Посмотреть рецепт в текстовой формe', callback_data='text')
    keyboard.add(key_text)
    key_video = types.InlineKeyboardButton(text='Посмотреть видео рецепт', callback_data='video')
    keyboard.add(key_video)
    bot.send_message(call.message.chat.id, "Выберите один из возможных вариатнтов", reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data == 'text')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название  салата🥗')
        bot.register_next_step_handler(sent, text_recipe)

    @bot.callback_query_handler(func=lambda call: call.data == 'video')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название салата🥗')
        bot.register_next_step_handler(sent, video_recipe)

@bot.callback_query_handler(func=lambda call: call.data == 'sweets')
def callback_worker(call):
    keyboard = types.InlineKeyboardMarkup()
    key_text = types.InlineKeyboardButton(text='Посмотреть рецепт в текстовой формe', callback_data='text')
    keyboard.add(key_text)
    key_video = types.InlineKeyboardButton(text='Посмотреть видео рецепт', callback_data='video')
    keyboard.add(key_video)
    bot.send_message(call.message.chat.id, "Выберите один из возможных вариатнтов", reply_markup=keyboard)


    @bot.callback_query_handler(func=lambda call: call.data == 'text')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название дессерта 🍰')
        bot.register_next_step_handler(sent,text_recipe)

    @bot.callback_query_handler(func=lambda call: call.data == 'video')
    def callback_worker(call):
        sent = bot.send_message(call.message.chat.id, 'Введите название дессерта 🍰')
        bot.register_next_step_handler(sent, video_recipe)


def text_recipe(message):

        add = check_function.check_is_dish_exist((message.text).upper())
        if bool(add) is False:
            result = check_function.if_not_exist_dish()
            list(result)
            print(result)
            bot.send_message(message.from_user.id, result[0])
            for i in range(len(result[1])):
                bot.send_message(message.from_user.id, result[1][i])


        else:
            result = check_function.result_of_search((message.text).upper())
            list(result)
            print(result)
            for i in range(len(result)):
                bot.send_message(message.from_user.id, result[i])
            evaluating(message)


def video_recipe(message):
    add = check_function.get_video_recipe((message.text).upper())
    if bool(add) is False:
        result = check_function.if_not_exist_dish()
        list(result)
        print(result)
        bot.send_message(message.from_user.id, result[0])
        for i in range(len(result[1])):
            bot.send_message(message.from_user.id, result[1][i])

    else:
        result = check_function.get_exsist_video_recipe((message.text).upper())
        print(result)
        bot.send_message(message.from_user.id, result)
        print(message)
        evaluating(message)
#
# def choos_dish(message):
#     check_function.check_dish_category(message.text)

def evaluating(message):
    keyboard3 = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='1', callback_data='one')
    # И добавляем кнопку на экран
    keyboard3.add(key_one)
    key_two = types.InlineKeyboardButton(text='2', callback_data='two')
    keyboard3.add(key_two)
    key_three = types.InlineKeyboardButton(text='3', callback_data='three')
    keyboard3.add(key_three)
    key_four = types.InlineKeyboardButton(text='4', callback_data='four')
    keyboard3.add(key_four)
    key_five = types.InlineKeyboardButton(text='5', callback_data='five')
    keyboard3.add(key_five)
    bot.send_message(message.chat.id, "Оцените,пожалуйста,работу бота", reply_markup=keyboard3)

    @bot.callback_query_handler(func=lambda call: call.data == 'one')
    def callback_worker(call):
        print(message.text)
        check_function.add_user_mark(1, str(message.from_user.username), (message.text).upper())
        continue_working_with_bot(message)

    @bot.callback_query_handler(func=lambda call: call.data == 'two')
    def callback_worker(call):
        print(message.text)
        check_function.add_user_mark(2, str(message.from_user.username), (message.text).upper())
        continue_working_with_bot(message)

    @bot.callback_query_handler(func=lambda call: call.data == 'three')
    def callback_worker(call):
        print(message.text)
        check_function.add_user_mark(3, str(message.from_user.username), (message.text).upper())
        continue_working_with_bot(message)

    @bot.callback_query_handler(func=lambda call: call.data == 'four')
    def callback_worker(call):
        print(message.text)
        check_function.add_user_mark(4, str(message.from_user.username), (message.text).upper())
        continue_working_with_bot(message)

    @bot.callback_query_handler(func=lambda call: call.data == 'five')
    def callback_worker(call):
        print(message.text)
        check_function.add_user_mark(5, str(message.from_user.username), (message.text).upper())
        continue_working_with_bot(message)


def continue_working_with_bot(message):
    keyboard4 = types.InlineKeyboardMarkup()
    key_one = types.InlineKeyboardButton(text='Оставить комментарий', callback_data='write_comment')
    # И добавляем кнопку на экран
    keyboard4.add(key_one)
    key_two = types.InlineKeyboardButton(text='Посмотреть комментарии пользователей', callback_data='see_comments')
    keyboard4.add(key_two)
    key_three = types.InlineKeyboardButton(text='Посмотреть статистику оценок', callback_data='see_rating')
    keyboard4.add(key_three)
    bot.send_message(message.chat.id, "Продолжите работу с ботом", reply_markup=keyboard4)

    @bot.callback_query_handler(func=lambda call: call.data == 'write_comment')
    def callback_worker(call):
        print(message.text)
        sent = bot.send_message(call.message.chat.id, 'Введите свой комментарий')
        bot.register_next_step_handler(sent,comments)

    @bot.callback_query_handler(func=lambda call: call.data == 'see_comments')
    def callback_worker(call):
        bot.send_message(call.message.chat.id, 'Отзывы другх пользователей')
        result = check_function.see_users_comments()
        print(result)
        for i in range(len(result)):
            bot.send_message(message.chat.id, str((list(result[i]))[0])+': '+str((list(result[i]))[1]))

    @bot.callback_query_handler(func=lambda call: call.data == 'see_rating')
    def callback_worker(call):
        bot.send_message(call.message.chat.id, 'Статистика оценок')
        result = check_function.statistic_of_marks()
        print(type(result))
        bot.send_message(message.from_user.id, 'Количество ценок "1" - ' + str(result[0]) + '.')
        bot.send_message(message.from_user.id, 'Количество ценок "2" - ' + str(result[1]) + '.')
        bot.send_message(message.from_user.id, 'Количество ценок "3" - ' + str(result[2]) + '.')
        bot.send_message(message.from_user.id, 'Количество ценок "4" - ' + str(result[3]) + '.')
        bot.send_message(message.from_user.id, 'Количество ценок "5" - ' + str(result[4]) + '.')

        average = check_function.avarage_of_mark()
        bot.send_message(message.from_user.id, 'Средняя оценка - ' + str(average) + '.')

# def comments(message):
#         check_function.add_comments(message.text, str(message.from_user.username))
#         print(message.text)
#         bot.send_message(message.chat.id,'Спасибо, ваш комментарий был успешно добавлен!')

if __name__ == '__main__':
     bot.polling()
#
