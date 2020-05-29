import telebot
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
import requests
import datetime
import time
from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


# for local run
os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
os.environ['DATABASE_URL'] = 'postgresql://postgres:alim1234@localhost/postgres'


# for HEROKU
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


import models


def search(film_features,page=1):
    request = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key=my_key&language=en-US&sort_by=vote_average.desc&include_adult=false&include_video=false&page={page}&primary_release_year={int(film_features['year'][0])}&vote_count.gte=1000&vote_average.gte={int(film_features['rating'][0][0])}&vote_average.lte={int(film_features['rating'][0][2])}&with_genres={int(film_features['genre'][0])}")
    request = json.loads(request.text)
    request = json_normalize(request['results'])
    return request

def check_search_id(movie_id):
    if movie_id.data[-1]=='s':
        try:
            request = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id.data[0:-1]}?api_key=my_key&language=en-US')
            return True
        except:
            return False
    else:
        return False

def check_liked_id(movie_id):
    if movie_id.data[-1]=='l':
        try:
            request = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id.data[0:-1]}?api_key=my_key&language=en-US')
            return True
        except:
            return False
    else:
        return False

df_of_param = pd.DataFrame([[1,2,3,4]],columns=['id','genre','year','rating'])


bot = telebot.TeleBot('token')

secret = 'token'
# bot.remove_webhook()
# time.sleep(1)
# bot.set_webhook(url="mycinematelegrambot.herokuapp.com/{}".format(secret))

request = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=my_key&language=RU&page=1')
request = json.loads(request.text)
request = json_normalize(request['results'])
a = pd.DataFrame({'a':request['original_language']=='en' ,'b':request['vote_count']>5000})
top_10 = request[a.all(axis=1)]
top_10 = [(title,id) for title,id in zip(list(top_10['title']),list(top_10['id']))]

keyboard_start = telebot.types.ReplyKeyboardMarkup(True,None,True)
keyboard_start.row('Топ 10 популярных фильмов', 'Поиск фильма')
keyboard_start.row('Посмотреть список понравившихся фильмов')
keyboard_film_param = telebot.types.ReplyKeyboardMarkup(True, None, True)
keyboard_film_param.row('Жанр', 'Год выпуска', 'Рейтинг')
keyboard_film_param.row('Назад','Найти фильм')

now = datetime.datetime.now()

param_of_choosed_film = {'user_id':0,'film_id':0,'film_name':0,'genre':0,'release_date':0,'rating':0}
del_film_id = 0


# создание списка уникальных жанров

ratings = [f'{i}-{i+1}' for i in range(10)]

genres = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=my_key&language=RU')
genres = json.loads(genres.text)
genres = json_normalize(genres['genres'])
iterr = 0
@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    models.Bot_user.add(message.from_user.id,message.from_user.username,message.from_user.first_name,message.from_user.last_name)
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard_start)
    global iterr
    if (df_of_param['id']!=message.chat.id).all():
        df_of_param.loc[iterr] = [message.chat.id,None,None,None]
        iterr+=1
    print(df_of_param)

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text.lower() == 'поиск фильма':
        bot.send_message(message.chat.id, "Выбери параметры фильма.", reply_markup=keyboard_film_param)
    elif message.text.lower() == 'топ 10 популярных фильмов':
        keyboard_top10 = telebot.types.InlineKeyboardMarkup()
        for title,id in top_10:
            key = telebot.types.InlineKeyboardButton(text=title, url=f'https://www.themoviedb.org/movie/{id}/')
            keyboard_top10.add(key)
        bot.send_message(message.from_user.id, text='Можешь фильмец выбрать, вот 10 лучших:', reply_markup=keyboard_top10)
    elif message.text.lower() == 'жанр':
        keyboard_genre = telebot.types.InlineKeyboardMarkup()
        for genre in genres['name']:
            key = telebot.types.InlineKeyboardButton(text=genre, callback_data=genre)
            keyboard_genre.add(key)
        bot.send_message(message.from_user.id, text='Выбери жанр фильма:', reply_markup=keyboard_genre)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, 'Ты в начале, что делаем?', reply_markup=keyboard_start)
    elif len(message.text)==4:
        try:
            if (int(message.text)>1960 and int(message.text)<now.year):
                user_year = int(message.text)
                bot.send_message(message.from_user.id, text='Окей, {}, записали. Может быть ещё что-то?'.format(user_year),reply_markup=keyboard_film_param)
                df_of_param['year'][df_of_param['id'] == message.from_user.id] = user_year
                print(df_of_param)
        except:
            pass
    elif message.text.lower() == 'год выпуска':
        bot.send_message(message.chat.id, "Напиши год выпуска фильма который хочешь найти.\nФильм должен быть выпущен позже 1960 года.", reply_markup=keyboard_film_param)
    elif message.text.lower() == 'рейтинг':
        keyboard_rating = telebot.types.InlineKeyboardMarkup()
        for i in range(10):
            key = telebot.types.InlineKeyboardButton(text=f'{i}-{i+1}', callback_data=f'{i}-{i+1}')
            keyboard_rating.add(key)
        bot.send_message(message.from_user.id, text='Выбери интервал в который входит желвемый рейтинг фильма:', reply_markup=keyboard_rating)
    elif message.text.lower() == 'найти фильм':
        try:
            found_films = search(df_of_param[df_of_param['id']==message.from_user.id])
            keyboard_films = telebot.types.InlineKeyboardMarkup()
            try:
                for title,id in np.array([found_films['title'],found_films['id']]).T:
                    key = telebot.types.InlineKeyboardButton(text=f"{title}", callback_data=f"{id}s")
                    keyboard_films.add(key)
                bot.send_message(message.from_user.id, text='Фильмы:',reply_markup=keyboard_films)
            except KeyError:
                bot.send_message(message.from_user.id, text='К сожалению, по таким параметрам не было найдено фильма((',reply_markup=keyboard_film_param)
        except IndexError:
            bot.send_message(message.from_user.id, text='Вы не ввели все необходимые параметры для фильма!',reply_markup=keyboard_film_param)
    elif message.text.lower() == 'добавить фильм в список понравившихся':
        # добавление записи в базу данных
        models.Liked_film_list.add(param_of_choosed_film['film_id'],param_of_choosed_film['film_name'],param_of_choosed_film['genre'],param_of_choosed_film['release_date'],param_of_choosed_film['rating'])
        models.Liked_users.add(param_of_choosed_film['film_id'],message.from_user.id)
        bot.send_message(message.chat.id, 'Готово!', reply_markup=keyboard_start)
    elif message.text.lower() == 'посмотреть список понравившихся фильмов' or message.text.lower() == 'вернуться к списку понравившихся':
        keyboard_liked_films = telebot.types.InlineKeyboardMarkup()
        list_of_user_films = db.session.query(models.Liked_users,models.Liked_film_list).join(models.Liked_film_list).filter(models.Liked_users.film_id==models.Liked_film_list.film_id).filter(models.Liked_users.user_id==message.from_user.id).all()
        if len(list_of_user_films) != 0:
            for film in list_of_user_films:
                key = telebot.types.InlineKeyboardButton(text=f"{film[1].film_name}", callback_data=f"{film[1].film_id}l")
                keyboard_liked_films.add(key)
            bot.send_message(message.from_user.id, text='Список понравившихся фильмов:', reply_markup=keyboard_liked_films)
        else:
            bot.send_message(message.from_user.id, text='Ваш список понравившихся фильмов пуст.',reply_markup=keyboard_liked_films)
    elif message.text.lower() == 'удалить фильм из списка понравившихся':
        # delete = models.Liked_users.query.filter_by(db.and_(models.Liked_users.film_id == del_film_id, models.Liked_users.user_id == message.from_user.id)).first()
        print(del_film_id)
        delete = db.session.query(models.Liked_users).get((del_film_id,message.from_user.id))
        print(delete)
        db.session.delete(delete)
        db.session.commit()
        bot.send_message(message.chat.id, 'Готово!', reply_markup=keyboard_start)
    else:
        bot.send_message(message.chat.id, 'Команда не была распознана.', reply_markup=keyboard_start)
@bot.callback_query_handler(func=lambda call: call.data in list(genres['name']))
def genre_wrote(call):
    global user_genre
    user_genre = call.data
    bot.send_message(call.from_user.id, text='Окей, {}, записали. Может быть ещё что-то?'.format(call.data))
    df_of_param['genre'][df_of_param['id']==call.from_user.id] = int(genres[genres['name']==call.data]['id'])
    param_of_choosed_film['genre'] = int(genres[genres['name']==call.data]['id'])
    print(df_of_param)

@bot.callback_query_handler(func=lambda call: call.data in ratings)
def rating_wrote(call):
    user_rating = call.data
    bot.send_message(call.from_user.id, text=f'Окей, рейтинг: {user_rating}, записали. Может быть ещё что-то?')
    df_of_param['rating'][df_of_param['id']==call.from_user.id] = user_rating

@bot.callback_query_handler(func=check_search_id)
def print_film(call):
    call.data = call.data[0:-1]
    keyboard_add_to_liked = telebot.types.ReplyKeyboardMarkup(True, None, True)
    keyboard_add_to_liked.row('Добавить фильм в список понравившихся')
    keyboard_add_to_liked.row('Назад')
    film = requests.get(f'https://api.themoviedb.org/3/movie/{call.data}?api_key=my_key&language=en-US')
    film = json.loads(film.text)
    param_of_choosed_film['user_id'] = call.from_user.id
    param_of_choosed_film['film_id'] = film['id']
    param_of_choosed_film['film_name'] = film["title"]
    param_of_choosed_film['release_date'] = int(time.mktime(datetime.datetime.strptime(film["release_date"], "%Y-%m-%d").timetuple()))
    param_of_choosed_film['rating'] = film["vote_average"]
    bot.send_message(call.from_user.id, text=f'{film["title"]}\nhttps://www.themoviedb.org/movie/{call.data}/',reply_markup=keyboard_add_to_liked)


@bot.callback_query_handler(func=check_liked_id)
def del_liked_film(call):
    global del_film_id
    del_film_id = int(call.data[0:-1])
    print(del_film_id)
    keyboard_del_film = telebot.types.ReplyKeyboardMarkup(True, None, True)
    keyboard_del_film.row('Удалить фильм из списка понравившихся')
    keyboard_del_film.row('Вернуться к списку понравившихся')
    bot.send_message(call.from_user.id, text='Хотите удалить фильм из списка понравившихся?',reply_markup=keyboard_del_film)

# @app.route('/{}'.format(secret), methods=["POST"])
# def webhook():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     print("Message")
#     return "ok", 200




if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)