import telebot
from pandas.io.json import json_normalize
import json
import requests
from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import models

app = Flask(__name__)

db = SQLAlchemy(app)

TOKEN = '1245867811:AAGH1QJeO_zWGyTDPpKm2MhFKasxrYFult7'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

def find_series(film_features,page=1):
    request = requests.get(f'{MAIN_URL}/getMe')
    request = json.loads(request.text)
    request = json_normalize(request['results'])
    return request

def checkin_search_id(series_id):
    if series_id.data[-1]=='s':
        try:
            request = requests.get(f'https://api.telegram.org/bot/{series_id.data[0:-1]}')
            return True
        except:
            return False
    else:
        return False

def checkin_id(series_id):
    if series_id.data[-1]=='l':
        try:
            request = requests.get(f'https://api.telegram.org/bot/{series_id.data[0:-1]}')
            return True
        except:
            return False
    else:
        return False

df_param = pd.DataFrame([[1,2,3,4]],columns=['id','genre','year','grade'])

bot = telebot.TeleBot(token)


request = requests.get('https://api.telegram.org/bot{TOKEN}?api_key=my_key&language=en&page=1')
request = json.loads(request.text)
request = json_normalize(request['results'])
r = pd.DataFrame({'a':request['origin_language']=='en' ,'b':request['vote_count']>5000})

markup_start = telebot.types.ReplyKeyboardMarkup(True,None,True)
markup_start.row('Find series')
markup_series_option = telebot.types.ReplyKeyboardMarkup(True, None, True)
markup_series_option.row('Genre', 'Year', 'Grade')
markup_series_option.row('Back','Find series')

series_option = {'user_id':0,'series_id':0,'series_title':0,'genre':0,'year':0,'grade':0}

grades = [f'{i}-{i+1}' for i in range(10)]

genres = requests.get('https://api.telegram.org/bot{TOKEN}/genre/list?api_key=my_key&language=en')
genres = json.loads(genres.text)
genres = json_normalize(genres['genres'])
iter = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    msg = bot.send_message(message.chat.id)
    bot.register_next_step_handler(msg, process_name)

@bot.message_handler(content_types=['text'])
def send_info(message):
    print(message)
    if message.text.lower() == 'find series':
        bot.send_message(message.chat.id, "Choose series options", reply_markup=markup_series_option)
    elif message.text.lower() == 'genre':
        key_genre = telebot.types.InlineKeyboardMarkup()
        for genre in genres['name']:
            key = telebot.types.InlineKeyboardButton(text=genre, callback_data=genre)
            key_genre.add(key)
        bot.send_message(message.from_user.id, text='Choose genre of the series', reply_markup=key_genre)
    elif message.text.lower() == 'back':
        bot.send_message(message.chat.id, text='You can find series', reply_markup=markup_start)
    elif message.text.lower() == 'year':
        bot.send_message(message.chat.id, text='Choose year of the series release you want', reply_markup=markup_series_option)
    elif message.text.lower() == 'grade':
        key_grade = telebot.types.InlineKeyboardMarkup()
        for i in range(10):
            key = telebot.types.InlineKeyboardButton(text=f'{i}-{i+1}', callback_data=f'{i}-{i+1}')
            key_grade.add(key)
        bot.send_message(message.from_user.id, text='Choose rating of the series you want', reply_markup=key_grade)
    elif message.text.lower() == 'find series':
        try:
            findin_series = search(df_of_param[df_of_param['id']==message.from_user.id])
            key_series = telebot.types.InlineKeyboardMarkup()
            try:
                for title,id in np.array([findin_series['title'],findin_series['id']]).T:
                    key = telebot.types.InlineKeyboardButton(text=f"{title}", callback_data=f"{id}s")
                    key_series.add(key)
                bot.send_message(message.from_user.id, text='Series:',reply_markup=key_series)
            except KeyError:
                bot.send_message(message.from_user.id, text='There is no series with these options',reply_markup=markup_series_option)
        except IndexError:
            bot.send_message(message.from_user.id, text='Choose all options of the series',reply_markup=markup_series_option)
    else:
        bot.send_message(message.chat.id, 'Try some another commands', reply_markup=keyboard_start)

@bot.callback_query_handler(func=lambda call: call.data in list(genres['gname']))
def wrire_genre(call):
    global user_genre
    user_genre = call.data
    bot.send_message(call.from_user.id, text='You chose this genre: {}. You can try other options too'.format(call.data))
    df_param['genre'][df_param['id']==call.from_user.id] = int(genres[genres['gname']==call.data]['id'])
    series_option['genre'] = int(genres[genres['gname']==call.data]['id'])
    print(df_param)

@bot.callback_query_handler(func=lambda call: call.data in genres)
def write_grade(call):
    user_gade = call.data
    bot.send_message(call.from_user.id, text=f'You chose this rating: {user_rating}. You can try other options too')
    df_param['grade'][df_param['id']==call.from_user.id] = user_rating
    if (pd.isna(df_param[df_param['id'] == call.from_user.id]['genre'])[0]) or (pd.isna(df_param[df_of_param['id'] == call.from_user.id]['year'])[0]) or (pd.isna(df_of_param[df_of_param['id'] == call.from_user.id]['grade'])[0]):
        bot.send_message(call.from_user.id, text='Choose other options of the series'.format(call.data))
    else:
        bot.send_message(call.from_user.id, text='Now you can find series or go back'.format(call.data))

@bot.callback_query_handler(func=checkin_search_id)
def out_film(call):
    call.data = call.data[0:-1]
    keyback = telebot.types.ReplyKeyboardMarkup(True, None, True)
    keyback.row('Back')
    series = requests.get(f'https://api.telegram.org/bot/series{call.data}?api_key=my_key&language=en-US')
    series = json.loads(series.text)
    series_option['user_id'] = call.from_user.id
    series_option['series_id'] = series['id']
    series_option['series_title'] = series["title"]
    series_option['year'] = series['year']
    series_option['grade'] = film["grade"]
    bot.send_message(call.from_user.id, text=f'{film["series"]}\nhttps://api.telegram.org/bot/series{call.data}/',reply_markup=keyback)

if __name__ == '__main__':
    bot.polling()