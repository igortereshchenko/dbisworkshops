import telebot
from telebot import types

import config

from model import *
from student import Student
from register import Register
from group import Group
from OracleDb import OracleDb

import re
import datetime
from datetime import date
import pandas as pd
import uuid
import random


bot = telebot.TeleBot(config.TOKEN)
student = Student
register = Register
group = Group
db = OracleDb()
cl = db.execute('SELECT DISTINCT group_name FROM group')
clubs = [row[0] for row in cl]


@bot.message_handler(commands=['start'])
def welcome(message):
    msg = bot.send_message(message.chat.id, '''\
You are welcome!🇬🇧
Ми раді вітати Вас у нашій школі EasyEnglish!
Оберіть пункт меню, який Вас цікавить:
''')
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                       resize_keyboard=True,
                                       selective=True)
    markup.add('Записатися на курс', 'Записатися на speaking club', 'Переглянути ціни', 'Інформація про школу')
    bot.register_next_step_handler(msg, choise)



@bot.message_handler(commands=['text'])
def choise(message):
    try:
        msg = bot.reply_to(message, 'Для того, щоб записатися на курс, напишіть свої дані.
Прізвище, ім'я, по-батькові:')
        bot.register_next_step_handler(msg, process_name)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def process_name(message):
    try:
        msg = bot.reply_to(message, 'Скільки Вас років:')
        bot.register_next_step_handler(msg, process_age)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def process_age(message):

    try:
        age = message.text
        if not age.isdigit() or int(age) > 100 or int(age) < 0:
            msg = bot.reply_to(message, 'Вік має бути цифра. Скільки Вам років?')
            bot.register_next_step_handler(msg, process_age)
        else:
            student.age = age
            msg = bot.reply_to(message, 'Введіть свій email:', process_email)
            bot.register_next_step_handler(msg, process_email)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')

@bot.message_handler(commands=['text'])
def process_email(message):
    try:
        email = message.text
        rule = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
        if not re.search(rule, email):
            msg = bot.reply_to(message, 'Структура email невірна')
            bot.register_next_step_handler(msg, process_phone)
            return

        student.email = email
        msg = bot.reply_to(message, 'Введіть свій номер телефону:')
        bot.register_next_step_handler(msg, process_phone)
        return
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def process_phone(message):
    try:
        phone = message.text
        rule = re.compile(r'^\+?3?8?(0\d{9})$')
        if not re.search(rule, phone):
            msg = bot.reply_to(message, 'Введіть правильний номер телефону')
            bot.register_next_step_handler(msg, process_phone)
            return

        getter = db.execute("SELECT student_phone FROM student WHERE student_phone = {}".format(str(phone)))
        a = [row[0] for row in getter]
        if len(a) != 0:
            if a[0] == phone:
                bot.send_message(message.chat.id, 'Цей номер вже використовується')
                msg = bot.reply_to(message, 'Введіть правильний номер телефону')
                bot.register_next_step_handler(msg, process_phone)
                return
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def process_level(message):
    try:
        level_list = ['Starter', 'Elementary', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate']

        if (level := message.text) in level_list:
            student.level = level
            hideBoard = types.ReplyKeyboardRemove()
            msg = bot.reply_to(message, 'Введіть свій номер телефону:')
            bot.register_next_step_handler(msg, process_phone)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add(Starter', 'Elementary', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate')
            msg = bot.reply_to(message, 'Оберіть свій рівень знань англійської мови:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_level)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')

@bot.message_handler(commands=['text'])
def process_level(message):
    try:
        level_list = ['Starter', 'Elementary', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate']

        if (level := message.text) in level_list:
            student.level = level
            hideBoard = types.ReplyKeyboardRemove()
            msg = bot.reply_to(message, 'Введіть свій номер телефону:')
            bot.register_next_step_handler(msg, process_phone)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add(Starter', 'Elementary', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate')
            msg = bot.reply_to(message, 'Оберіть свій рівень знань англійської мови:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_level)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def student_group(message):

    try:
            answer = message.text

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add()
            msg = bot.reply_to(message, 'Оберіть групу, в якій хочете займатися:', reply_markup=markup)
            bot.register_next_step_handler(msg, choise_group)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


def choice_group(message):

    try:
        if (mm := message.text) in groups:
            m = db.execute("SELECT group_name, timetable FROM groups WHERE groups.level = student.level".format(str(mm)))
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add()
            msg = bot.reply_to(message, 'Оберіть групу, в якій хочете займатися:', reply_markup=markup)
            bot.register_next_step_handler(msg, student_group)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def process_pay(message):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                               resize_keyboard=True,
                                               selective=True)
            markup.add('Оплатити онлайн', 'Оплатити в офісі')
            msg = bot.send_message(call.message.chat.id, '''/
                                   'Ваше місце в групі зарезервоване😎

Детальну інформацію про обраний курс, групу ми надішлемо на Вашу пошту.

Тепер Вам необхідно сплатити за перший місяць навчання. Оплатити ви можете зараз онлайн або в офісі школи протягом 2 днів.
У разі неоплати протягом двох днів Вашу заявку на резерв буде скасовано.
Оберіть відповідний спосіб оплати:''',
                                   reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, 'Якась помилка!')

@bot.message_handler(commands=['text'])
def process_final_step(message):
    try:
        if message.text == 'Оплатити онлайн', 'Оплатити в офісі' :
            bot.send_message(message.chat.id, '''/Інформацію щодо оплати ми надіслали на Вашу електронну пошту💵

❗️Нагадуємо, оплату необхідно внести протягом двох днів.
Дякуємо, що обрали нашу школу!
Чекаємо Вас на навчанні📚''')
            msg = bot.send_message(message.chat.id, 'Повернутись до меню')
            bot.register_next_step_handler(msg, process_welcome)

    except Exception as e:
        bot.send_message(message.chat.id, 'Якась помилка!')


@bot.message_handler(commands=['text'])
def final_control(message):

    try:
        if message.text == 'Повернутись до меню':
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,
                                           resize_keyboard=True,
                                           selective=True)
            markup.add('Записатися на курс', 'Записатися на speaking club', 'Переглянути ціни', 'Інформація про школу')
            msg = bot.send_message(message.chat.id, 'Оберіть один пункт меню:', reply_markup=markup)
            bot.register_next_step_handler(msg, before_main_block)
    except Exception as e:
        bot.send_message(message.chat.id, 'Якась помилка!')


#bot.enable_save_next_step_handlers(delay=2)
#bot.load_next_step_handlers()
bot.polling()
