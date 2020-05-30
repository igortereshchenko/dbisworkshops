import config
import telebot
from telebot import types
import requests
import time
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from models_creation import User, Resources
from connections import engine
import random
import pandas as pd
import plotly.express as px
import numpy as np

Session = sessionmaker(bind=engine)
session = Session()


token = config.token
api_key = config.news_token
bot = telebot.TeleBot(token)
locations = {
    'Ukraine': 'ua',
    'Russia': 'ru',
    'United Kingdom': 'uk',
    'USA': 'us'
}
loc = 'ua'
cat = 'general'
category = ['business', 'entertainment', 'general', 'health', 'science', 'technology']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_1 = types.KeyboardButton(text="Ukraine")
button_2 = types.KeyboardButton(text="Russia")
button_4 = types.KeyboardButton(text="USA")
keyboard.add(button_1, button_2, button_4)
keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton(text="business")
button2 = types.KeyboardButton(text="entertainment")
button3 = types.KeyboardButton(text="health")
button4 = types.KeyboardButton(text="science")
button5 = types.KeyboardButton(text="technology")
button6 = types.KeyboardButton(text="general")
keyboard_1.add(button1, button2, button3, button4, button5, button6)



def news_api(cat, loc):
    url = f'https://newsapi.org/v2/top-headlines?country={loc}&category={cat}&pageSize=40&apiKey={api_key}'
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)
    info = response.json()
    ind = 0
    ind2 = 0
    if info['totalResults'] > 4:
        while ind2 - ind != 4:
            ind = random.randrange(0, info['totalResults'])
            ind2 = random.randrange(0, info['totalResults'])
    true_info = info['articles'][ind:ind2]
    for i in true_info:
        yield i['title'], i['url']


@bot.message_handler(commands=['start'])
def send_(message):
    global register
    register = 0
    bot.send_message(message.chat.id, "Hello, I am glad to see you {f}".format(f=message.chat.first_name))
    time.sleep(3)
    bot.send_message(message.chat.id, 'Send me your location, so i can sort news for your destination',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_(message):
    bot.send_message(message.chat.id, "Options that you can use \n /update_location  "
                                      "\n /stop  \n /update_category \n /news \n /stats")


@bot.message_handler(commands=['update_location'])
def send_(message):
    global flag
    flag = 1
    bot.send_message(message.chat.id, 'Choose your new location', reply_markup=keyboard)
    global register
    register = 1


@bot.message_handler(commands=['stats'])
def send_(message):
    q = '''
    Select count(distinct user_id) As dau, USER_DATE 
    from users
    group by USER_DATE
    '''

    result = session.execute(q)
    x = []
    y = []
    nfo = [row for row in result]
    for i in nfo:
        x.append(i[0])
        val = str(i[1]).split()[0]
        val = np.datetime64(val)
        y.append(val)

    df = pd.DataFrame({'Users': x, 'Date': y})
    df = df.groupby(by='Date', as_index=False).sum()
    fig = px.line(df, x='Date', y='Users')
    fig.show()
    query = '''
    Select count(DISTINCT users.user_id) as amount, resources.location_
    FROM users JOIN RESOURCES ON users.user_id = RESOURCES.USER_ID
    GROUP BY resources.location_
    '''
    res = session.execute(query)
    nfo = [row for row in res]
    x = []
    y = []
    for i in nfo:
        x.append(i[0])
        y.append(i[1])
    df_1 = pd.DataFrame({'Amount': x, 'Location': y})
    fig1 = px.pie(df_1, values='Amount', names='Location', title='Amount of users slided by countries')
    fig1.show()


@bot.message_handler(commands=['update_category'])
def send_(message):
    global flag
    flag = 1
    bot.send_message(message.chat.id, "Choose your new category", reply_markup=keyboard_1)
    global register
    register = 1


@bot.message_handler(commands=['stop'])
def send_(message):
    global flag
    flag = 1
    bot.send_message(message.chat.id, "I have stoped, thanks for using")
    try:
        session.query(Resources).filter(Resources.user_id == message.chat.id).delete(synchronize_session=False)
        session.commit()
        session.query(User).filter(User.user_id == message.chat.id).delete(synchronize_session=False)
        session.commit()
    except Exception as e:
        print(e)
    bot.stop_polling()


@bot.message_handler(commands=['news'])
def sendnews(message):
    chat = message.chat.id
    generate_news = news_api(cat, loc)
    try:
        for i in range(4):
            info = next(generate_news)
            bot.send_message(chat, info[1])
            time.sleep(5)
    except Exception as e:
        print(e)


@bot.message_handler(content_types=['text'])
def send_mess(message):
    if message.text in locations.keys():
        global loc
        loc = locations[message.text]
        print(loc)
        if register == 0:
            bot.send_message(message.chat.id, "Thanks, and now send me your favorite category", reply_markup=keyboard_1)
        else:
            bot.send_message(message.chat.id, "Get it")
            try:
                session.query(Resources).filter(Resources.user_id == message.chat.id).update({Resources.location_: loc.upper()})
                session.commit()
            except Exception as e:
                print(e)
    elif message.text in category:
        global cat
        cat = message.text
        print(cat)
        if register == 0:
            bot.send_message(message.chat.id, "You have finished, congrats! \nNow, whenever you need news \ntype /news")
            try:
                new_user = User(user_id=message.chat.id, user_name=message.chat.first_name, user_date=func.current_date())
                new_user_res = Resources(user_id=message.chat.id, category_=cat, location_=loc)
                for i in [new_user, new_user_res]:
                    session.add(i)
                    session.commit()
            except Exception as e:
                print(e)
        else:
            bot.send_message(message.chat.id, 'Get it')
            try:
                session.query(Resources).filter(Resources.user_id == message.chat.id).update({Resources.category_: cat})
                session.commit()
            except Exception as e:
                print(e)
    else:
        bot.send_message(message.chat.id, "Probably you /help or /news")


bot.polling(none_stop=True)