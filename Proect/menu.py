import telebot
from telebot import types

import config

from model import *
from user import User
from order import Order
from comment import Comment
from OracleDb import OracleDb

import re
import datetime
from datetime import date
import pandas as pd
import uuid
import random


bot = telebot.TeleBot(config.TOKEN)
user = User()
order = Order()
comment = Comment()
db = OracleDb()
thres = db.execute('SELECT DISTINCT dish_name FROM menu')
restaurant = [row[0] for row in res]
mv = db.execute('SELECT DISTINCT dish_name FROM dishes')
book = [row[0] for row in mv]
times = ['{}:00'.format(10+i) for i in range(0, 12, 2)]
sn = db.execute('SELECT snack_name FROM snack')
snacks = [row[0] for row in sn]
snacks.append('No thanks')

@bot.message_handler(commands=['start'])
def welcome(message):
    msg = bot.send_message(message.chat.id, '''\
Hi! Welcome to the chat! I am Kafe bot
Let's complete a few registration steps
to get started with lanche🎟🎟
Enter your name👶🏻👧🏻
''')
    bot.register_next_step_handler(msg, process_name)


@bot.message_handler(commands=['text'])
def process_name(message):
    try:
        user.name = message.text
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_age(message):

    try:
        age = message.text
        if not age.isdigit() or int(age) > 100 or int(age) < 0:
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age)
        else:
            user.age = age
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Kyiv', 'Dnipro', 'Odessa', 'Other')
            msg = bot.reply_to(message, 'What is your city?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_city)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_city(message):
    try:
        city_list = ['Kyiv', 'Dnipro', 'Odessa']

        if (city := message.text) in city_list:
            user.city = city
            hideBoard = types.ReplyKeyboardRemove()
            msg = bot.reply_to(message, 'Now, enter your phone number📱')
            bot.register_next_step_handler(msg, process_phone)
        else:
            bot.send_message(message.chat.id, 'Sorry, we are not support other cities.')
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Kyiv', 'Dnipro', 'Odessa', 'Other')
            msg = bot.reply_to(message, 'Select one of the variants presented in buttons. What is your city?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_city)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_phone(message):
    try:
        phone = message.text
        rule = re.compile(r'^\+?3?8?(0\d{9})$')
        if not re.search(rule, phone):
            msg = bot.reply_to(message, 'Enter valid phone number📱')
            bot.register_next_step_handler(msg, process_phone)
            return

        getter = db.execute("SELECT user_phone FROM app_user WHERE user_phone = {}".format(str(phone)))
        a = [row[0] for row in getter]
        if len(a) != 0:
            if a[0] == phone:
                bot.send_message(message.chat.id, 'This number is already used!')
                msg = bot.reply_to(message, 'Enter valid phone number📱')
                bot.register_next_step_handler(msg, process_phone)
                return

        user.phone = phone
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                           resize_keyboard=True,
                                           selective=True)
        markup.add('Student', 'Not student')
        msg = bot.reply_to(message, 'And know, enter your status', reply_markup=markup)
        bot.register_next_step_handler(msg, process_status)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_status(message):
    try:
        sts = ['Student', 'Not student']
        status = message.text
        if status not in sts:
            msg = bot.reply_to(message, 'Enter one of variants presented in buttons', reply_markup=markup)
            bot.register_next_step_handler(msg, process_status)
            return

        user.status = status
        msg = bot.reply_to(message, 'And know, enter your email📨')
        bot.register_next_step_handler(msg, process_email)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_email(message):
    try:
        email = message.text
        rule = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        if not re.search(rule, email):
            msg = bot.reply_to(message, 'Enter valid email📨')
            bot.register_next_step_handler(msg, process_phone)
            return

        user.mail = email
        msg = bot.reply_to(message, 'Enter bank card number💳, card lenght should be 16 symbols 🗿')
        bot.register_next_step_handler(msg, process_bank)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def process_bank(message):

    try:
        bank = message.text
        gett = db.execute("SELECT user_bank FROM app_user WHERE user_bank = {}".format(int(bank)))
        a = [row[0] for row in gett]
        if len(a) != 0:
            if a[0] == int(bank):
                bot.send_message(message.chat.id, 'This number is already used!')
                msg = bot.reply_to(message, 'Enter valid bank number💳')
                bot.register_next_step_handler(msg, process_bank)
        elif len(bank) != 16 or not bank.isdigit():
            msg = bot.reply_to(message, 'Enter valid bank card number, card lenght should be 16 symbols 🗿')
            bot.register_next_step_handler(msg, process_bank)
            return
        else:
            user.bank = bank
            msg = bot.send_message(message.chat.id, 'Nice to meet you ' + user.name)

            new_member = app_user.add_member(name=str(user.name),
                                             age=int(user.age),
                                             phone=str(user.phone),
                                             mail=str(user.mail),
                                             bank=int(user.bank),
                                             status=str(user.status),
                                             city=str(user.city)
                                            )

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Comments menu🗣', 'Buy dish 📽')
            bot.send_message(message.chat.id, 'Select one variant to continue.', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def before_main_block(message):

    try:
        answer = message.text
        if answer == 'Comments menu🗣':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Show 3 random comments🗣', 'Write a comment👀')
            msg = bot.send_message(message.chat.id, 'Choose one option 🗿', reply_markup=markup)
            bot.register_next_step_handler(msg, process_comment)
        elif answer == 'Buy dish📽':
            markup = types.InlineKeyboardMarkup(row_width=1)
            for i in theatres:
                b1 = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(b1)

            bot.send_message(message.chat.id, 'Cost of dish is equals to 5$🍿📽')
            bot.send_message(message.chat.id, 'OK, choose one theatre presented in buttons🍿📽', reply_markup=markup)

        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Comments menu🗣', 'Buy dish📽')
            msg = bot.reply_to(message, 'Select one of the variants presented in buttons🗿', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


def process_comment(message):
    try:
        answer = message.text
        if answer == 'Show 3 random comments🗣':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            for i in movies:
                markup.add(i)
            msg = bot.send_message(message.chat.id, 'Choose movie to display comments 📱', reply_markup=markup)
            bot.register_next_step_handler(msg, random_comments)
        elif answer == 'Write a comment👀':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            for i in movies:
                markup.add(i)
            msg = bot.send_message(message.chat.id, 'Choose movie to write a comment 📱', reply_markup=markup)
            bot.register_next_step_handler(msg, comment_write)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Show 3 random comments🗣', 'Write a comment👀')
            msg = bot.reply_to(message, 'Select one of the variants presented in buttons🗿', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


def comment_write(message):

    try:
        if (movie := message.text) in movies:
            comment.movie = movie
            msg = bot.send_message(message.chat.id, 'Write a comment I am ready 🗿')
            bot.register_next_step_handler(msg, new_comment)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            for i in movies:
                markup.add(i)
            msg = bot.send_message(message.chat.id, 'Choose movie to display comments 📱', reply_markup=markup)
            bot.register_next_step_handler(msg, comment_write)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


def new_comment(message):

    try:
        if (co := message.text):
            comment.comm = co
            if len(co) > 30:
                bot.send_message(message.chat.id, 'Your comment is too long!(max lenght is 30)')
                msg = bot.send_message(message.chat.id, 'Enter new, I am listening!')
                bot.register_next_step_handler(msg, new_comment)
                return

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Сomments menu🗣', 'Buy dish')
            new_comm = comments.add_member(dish=comment.dish,
                                              text=comment.comm)
            msg = bot.send_message(message.chat.id, 'I got it!', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


def random_comments(message):

    try:
        if (mm := message.text) in movies:
            m = db.execute("SELECT comment_text FROM comments WHERE dish = '{}'".format(str(mm)))
            comms = [row[0] for row in m][:3]
            for i in comms:
                bot.send_message(message.chat.id, i)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Comments menu🗣', 'Buy dish')
            msg = bot.reply_to(message, 'Select one of the variants presented in buttons🗿', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            for i in movies:
                markup.add(i)
            msg = bot.send_message(message.chat.id, 'Choose movie to display comments 📱', reply_markup=markup)
            bot.register_next_step_handler(msg, random_comments)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.callback_query_handler(func=lambda call: True)
def processor_of_queries(call):
    try:
        base = date.today()
        dates = [str(base + datetime.timedelta(days=x)) for x in range(1, 6)]
        thres = db.execute('SELECT DISTINCT restaurant_name FROM restaurant')
        theatres = [row[0] for row in thres]
        mv = db.execute('SELECT DISTINCT dish_name FROM dishes')
        movies = [row[0] for row in mv]
        times = ['{}:00'.format(10+i) for i in range(0, 12, 2)]
        seats = ['{}'.format(i+1) for i in range(7)]
        sn = db.execute('SELECT snack_name FROM snack')
        snacks = [row[0] for row in sn]
        snacks.append('No thanks')
        if (theatre := call.data) in theatres:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Theatre was choosen!',
                                  reply_markup=None)
            order.theatre = theatre

            markup = types.InlineKeyboardMarkup(row_width=1)
            for i in movies:
                b1 = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(b1)

            bot.send_message(call.message.chat.id, 'OK, choose one movie presented in buttons🍿📽', reply_markup=markup)
        elif (movie := call.data) in movies:

            phone = user.phone
            getter = db.execute("SELECT user_age FROM app_user WHERE user_phone = {}".format(str(phone)))
            us_age = [row[0] for row in getter][0]
            go_data2 = db.execute("SELECT age_limit FROM dishes WHERE dish_name = '{}'".format(str(movie)))
            age_lim = [int(row[0]) for row in go_data2][0]

            if us_age < age_lim:
                bot.send_message(call.message.chat.id, 'You are too young buying that, choose other option')
                return

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Movie was choosen!',
                                  reply_markup=None)
            order.movie = movie

            markup = types.InlineKeyboardMarkup(row_width=3)
            for i in times:
                b1 = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(b1)

            bot.send_message(call.message.chat.id, 'OK, choose visit time🍿📽', reply_markup=markup)
        elif (time := call.data) in times:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Time was choosen!',
                                  reply_markup=None)
            order.time = time

            markup = types.InlineKeyboardMarkup(row_width=2)
            for i in dates:
                b1 = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(b1)

            bot.send_message(call.message.chat.id, 'OK, choose visit date🍿📽', reply_markup=markup)
        elif (date1 := call.data) in dates:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Date was choosen!',
                                  reply_markup=None)
            order.date = date1

            go_data = db.execute(f" SELECT seat FROM orders INNER JOIN app_user ON orders.user_id = app_user.user_id WHERE datte = '{order.date}' AND time = '{order.time}' AND city ='{user.city}'")
            taken_seats = [row[0] for row in go_data]

            markup = types.InlineKeyboardMarkup(row_width=7)

            for j in range(7):
                group = []
                for i in seats:
                    if '{}-{}'.format(i, j+1) in taken_seats:
                        group.append(types.InlineKeyboardButton('z', callback_data='z'))
                    else:
                        group.append(types.InlineKeyboardButton(str(i), callback_data='{}-{}'.format(i, j+1)))
                markup.row(*group)

            bot.send_message(call.message.chat.id, 'OK, choose your seat🍿📽(first row is closest to the screen)', reply_markup=markup)
        elif (seat := call.data)[0] in seats:
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Seat was choosen!',
                                  reply_markup=None)
            order.seat = seat
            order.price = 5

            markup = types.InlineKeyboardMarkup(row_width=1)
            for i in snacks:
                b1 = types.InlineKeyboardButton(i, callback_data=i)
                markup.add(b1)

            bot.send_message(call.message.chat.id, 'Cost of every snack is equals to 7$')
            bot.send_message(call.message.chat.id, 'OK, choose snack(if you want)🍿📽', reply_markup=markup)
        elif (snack := call.data) in snacks:
            phone = user.phone
            getter = db.execute("SELECT user_age FROM app_user WHERE user_phone = {}".format(str(phone)))
            us_age = [row[0] for row in getter][0]
            go_data2 = db.execute("SELECT age_limit FROM snack WHERE snack_name = '{}'".format(str(snack)))
            age_lim = [int(row[0]) for row in go_data2]

            if len(age_lim) > 0:
                if us_age < age_lim[0]:
                    bot.send_message(call.message.chat.id, 'You are too young buying that, choose other option')
                    return

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Snack was choosen!',
                                  reply_markup=None)
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Pay💸', 'Cancel❌')
            msg = bot.send_message(call.message.chat.id,
                                   'All data about your order is stored, now choose one of the options🤴',
                                   reply_markup=markup)

            if snack != 'No thanks':
                order.snack = snack
                order.price = order.price + 7
            else:
                order.snack = None

            bot.register_next_step_handler(msg, process_final_step)
        else:
            if call.data == 'z':
                bot.send_message(call.message.chat.id, 'This seat is already taken')
                return
            bot.send_message(call.message.chat.id, 'Select one of the variants presented in buttons🗿')

    except Exception as e:
       bot.send_message(call.message.chat.id, 'Something gone wrong! 🗿')


def my_random_string(string_length=12):
    """
        Функція для створення секретного коду
    """
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length] 


@bot.message_handler(commands=['text'])
def process_final_step(message):
    try:
        if message.text == 'Pay💸':
            order.code = my_random_string()
            bot.send_message(message.chat.id, 'Thank you for your order!')
            msg = bot.send_message(message.chat.id, 'To continue, enter your phone number📱')
            bot.register_next_step_handler(msg, verify_phone)
        elif message.text == 'Cancel❌':
            bot.send_message(message.chat.id, 'Thats a pity, but if you want you can order a new dish, or leave a comment.')
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Go to menu👣🍿')
            msg = bot.send_message(message.chat.id,
                                   'Choose one of presented options🗿',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, final_control)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Pay💸', 'Cancel❌')
            msg = bot.send_message(message.chat.id,
                                   'Choose one of presented options🗿',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, process_final_step)
    except Exception as e:
        bot.send_message(message.chat.id, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def verify_phone(message):
    try:
        phone = message.text
        rule = re.compile(r'^\+?3?8?(0\d{9})$')
        if not re.search(rule, phone):
            msg = bot.reply_to(message, 'Enter valid phone number📱')
            bot.register_next_step_handler(msg, verify_phone)
            return

        getter = db.execute("SELECT user_phone FROM app_user WHERE user_phone = '{}'".format(str(phone)))
        a = [row[0] for row in getter]
        getter2 = db.execute("SELECT status FROM app_user WHERE user_phone = '{}'".format(str(phone)))
        b = [row[0] for row in getter2]
        if len(a) == 0:
            bot.send_message(message.chat.id, 'This number is not used!')
            msg = bot.reply_to(message, 'Enter valid phone number📱')
            bot.register_next_step_handler(msg, process_phone)
            return
        if b[0] == 'Student':
            new_order = orders.add_member(dish=str(order.movie),
                                          restaurant=str(order.restaurant),
                                          phone=str(a[0]),
                                          seat=str(order.seat),
                                          date=str(order.date),
                                          time=str(order.time),
                                          price=int(order.price * 0.5),
                                          city=str(user.city))
        else:
            new_order = orders.add_member(dish=str(order.movie),
                                          restaurant=str(order.restaurant),
                                          phone=str(a[0]),
                                          seat=str(order.seat),
                                          date=str(order.date),
                                          time=str(order.time),
                                          price=int(order.price),
                                          city=str(user.city))
        bot.send_message(message.chat.id, 'Your secret code is: {}'.format(order.code))
        bot.send_message(message.chat.id, 'If you want you can buy a new 
        et or write a comment.')
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                           resize_keyboard=True,
                                           selective=True)
        markup.add('Go to menu👣🍿')
        msg = bot.send_message(message.chat.id, 'Choose one of presented options🗿',
                               reply_markup=markup)
        bot.register_next_step_handler(msg, final_control)
    except Exception as e:
        bot.reply_to(message, 'Something gone wrong! 🗿')


@bot.message_handler(commands=['text'])
def final_control(message):

    try:
        if message.text == 'Go to menu👣🍿':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                           resize_keyboard=True,
                                           selective=True)
            markup.add('Comments menu🗣', 'Buy dish📽')
            msg = bot.send_message(message.chat.id, 'Select one variant to continue.', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Go to menu👣🍿')
            msg = bot.send_message(message.chat.id,
                                   'Choose one button🗿',
                                   reply_markup=markup)
            bot.register_next_step_handler(msg, final_conrol)
    except Exception as e:
        bot.send_message(message.chat.id, 'Something gone wrong! 🗿')


#bot.enable_save_next_step_handlers(delay=2)
#bot.load_next_step_handlers()
bot.polling()
