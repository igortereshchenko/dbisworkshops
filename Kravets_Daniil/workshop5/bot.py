import telebot
from telebot import types
from models_create import OrderSong, Announcement, Broadcast, Chain, AnnouncementChain, feedback, Statistic
from sqlalchemy.orm import sessionmaker
from database_connection import engine
import datetime
from datetime import date
from sqlalchemy import and_
from sqlalchemy import func


Session = sessionmaker(bind=engine)
session = Session()

bot = telebot.TeleBot('1190148858:AAFrjHZHvQfVgFMsYRrrN1A3yBQ-eN7B8gI')

ordering = types.KeyboardButton('Замовлення')
order_song = types.KeyboardButton('Замовлення пісні')
order_ann = types.KeyboardButton('Замовлення оголошення')
tomorrow = types.KeyboardButton('Завтра')
after_tomorrow = types.KeyboardButton('Післязавтра')
after_tomorrow2 = types.KeyboardButton('Після післязавтра')
morning = types.KeyboardButton('Ранок\n8:00-11:00')
afternoon = types.KeyboardButton('День\n14:00-17:00')
evening = types.KeyboardButton('Вечір\n18:00-21:00')
schedule = types.KeyboardButton('Розклад ефірів')
helper = types.KeyboardButton('Допомога')
ordering_help = types.KeyboardButton('Особливості замовлення')
moderation = types.KeyboardButton('Модерація')
feedbackb = types.KeyboardButton('Зворотний зв`язок')
mainmenu = types.KeyboardButton('До головного меню')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard1.row(ordering)
keyboard1.row(schedule)
keyboard1.row(helper)

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard2.row(ordering_help)
keyboard2.row(moderation)
keyboard2.row(feedbackb)
keyboard2.row(mainmenu)

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row(order_song)
keyboard3.row(order_ann)
keyboard3.row(mainmenu)

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard4.row(tomorrow)
keyboard4.row(after_tomorrow)
keyboard4.row(after_tomorrow2)

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard5.row(morning)
keyboard5.row(afternoon)
keyboard5.row(evening)

to_main_menu = telebot.types.ReplyKeyboardMarkup(True)
to_main_menu.row(mainmenu)


if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Monday')).all()) == 0):
    day1_add = Statistic(statistic_day='Monday', statistic_time='8:00', statistic_count=30)
    day2_add = Statistic(statistic_day='Monday', statistic_time='14:00', statistic_count=31)
    day3_add = Statistic(statistic_day='Monday', statistic_time='18:00', statistic_count=35)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Tuesday')).all()) == 0):
    day1_add = Statistic(statistic_day='Tuesday', statistic_time='8:00', statistic_count=40)
    day2_add = Statistic(statistic_day='Tuesday', statistic_time='14:00', statistic_count=38)
    day3_add = Statistic(statistic_day='Tuesday', statistic_time='18:00', statistic_count=42)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Wednesday')).all()) == 0):
    day1_add = Statistic(statistic_day='Wednesday', statistic_time='8:00', statistic_count=31)
    day2_add = Statistic(statistic_day='Wednesday', statistic_time='14:00', statistic_count=37)
    day3_add = Statistic(statistic_day='Wednesday', statistic_time='18:00', statistic_count=39)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Thursday')).all()) == 0):
    day1_add = Statistic(statistic_day='Thursday', statistic_time='8:00', statistic_count=53)
    day2_add = Statistic(statistic_day='Thursday', statistic_time='14:00', statistic_count=43)
    day3_add = Statistic(statistic_day='Thursday', statistic_time='18:00', statistic_count=34)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Friday')).all()) == 0):
    day1_add = Statistic(statistic_day='Friday', statistic_time='8:00', statistic_count=51)
    day2_add = Statistic(statistic_day='Friday', statistic_time='14:00', statistic_count=49)
    day3_add = Statistic(statistic_day='Friday', statistic_time='18:00', statistic_count=44)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Saturday')).all()) == 0):
    day1_add = Statistic(statistic_day='Saturday', statistic_time='8:00', statistic_count=33)
    day2_add = Statistic(statistic_day='Saturday', statistic_time='14:00', statistic_count=35)
    day3_add = Statistic(statistic_day='Saturday', statistic_time='18:00', statistic_count=39)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

if (len((session.query(Statistic).filter(Statistic.statistic_day == 'Sunday')).all()) == 0):
    day1_add = Statistic(statistic_day='Sunday', statistic_time='8:00', statistic_count=36)
    day2_add = Statistic(statistic_day='Sunday', statistic_time='14:00', statistic_count=35)
    day3_add = Statistic(statistic_day='Sunday', statistic_time='18:00', statistic_count=40)
    session.add(day1_add)
    session.commit()
    session.add(day2_add)
    session.commit()
    session.add(day3_add)
    session.commit()

base = date.today()
for x in range(1, 4):
    dates = base + datetime.timedelta(days=x)
    if (len((session.query(Broadcast).filter(and_(Broadcast.broadcast_date == dates, Broadcast.broadcast_time != 'txt'))).all()) == 0):
        schedule_add1 = Broadcast(broadcast_date=dates, broadcast_time='8:00')
        schedule_add2 = Broadcast(broadcast_date=dates, broadcast_time='14:00')
        schedule_add3 = Broadcast(broadcast_date=dates, broadcast_time='18:00')
        session.add(schedule_add1)
        session.commit()
        session.add(schedule_add2)
        session.commit()
        session.add(schedule_add3)
        session.commit()


def audio_test(message):
    if type(message.text) != str:
        if message.audio.mime_type == 'audio/mpeg' or message.audio.mime_type == 'audio/mp3':
            song_name = OrderSong(song_name=message.audio.title, song_artist=message.audio.performer)
            session.add(song_name)
            session.commit()
            bot.send_message(message.chat.id,
                             'Оберіть день.',
                             reply_markup=keyboard4)
            bot.register_next_step_handler(message, day_choose)

        else:
            bot.send_message(message.chat.id,
                            'Будь-ласка, додайте файл відповідного формату.')
            bot.register_next_step_handler(message, audio_test)
    else:
        bot.send_message(message.chat.id,
                        'Будь-ласка, додайте файл відповідного формату.')
        bot.register_next_step_handler(message, audio_test)

def day_choose(message):
    global day_id
    global day_stat
    global time_stat
    if type(message.text) == str:
        if message.text == 'Завтра':
            day_id = 1
            bot.send_message(message.chat.id,
                             'Оберіть час.',
                             reply_markup=keyboard5)
            bot.register_next_step_handler(message, time_choose)
        elif message.text == 'Післязавтра':
            day_id = 2
            bot.send_message(message.chat.id,
                             'Оберіть час.',
                             reply_markup=keyboard5)
            bot.register_next_step_handler(message, time_choose)
        elif message.text == 'Післяпіслязавтра':
            day_id = 3
            bot.send_message(message.chat.id,
                             'Оберіть час.',
                             reply_markup=keyboard5)
            bot.register_next_step_handler(message, time_choose)
        else:
            bot.send_message(message.chat.id,
                             'Неправильно введено дані. Введіть, будь-ласка, день:',
                             reply_markup=keyboard4)
            bot.register_next_step_handler(message, day_choose)
    else:
        bot.send_message(message.chat.id,
                         'Неправильно введено дані. Введіть, будь-ласка, день:',
                         reply_markup=keyboard4)
        bot.register_next_step_handler(message, day_choose)

def time_choose(message):
    global day_id
    global day_stat
    global time_stat
    if type(message.text) == str:
        if message.text == 'Ранок\n8:00-11:00':
            day_stat = base + datetime.timedelta(days=day_id)
            time_stat = 1
            stat_insert(day_stat, time_stat)
            broad_id = (session.query(Broadcast).filter(
                and_(Broadcast.broadcast_date == (base + datetime.timedelta(days=day_id)),
                     Broadcast.broadcast_time == '8:00'))[0]).broadcast_id
            maximum = session.query(func.max(OrderSong.song_id)).scalar()
            s_id = (session.query(OrderSong).filter(OrderSong.song_id == maximum)[0]).song_id
            chain_in = Chain(broadcast_id_fk=broad_id, song_id_fk=s_id)
            session.add(chain_in)
            session.commit()
            bot.send_message(message.chat.id,
                             'Ваше замовлення відправлено на модерацію',
                             reply_markup=to_main_menu)
        elif message.text == 'День\n14:00-17:00':
            day_stat = base + datetime.timedelta(days=day_id)
            time_stat = 2
            stat_insert(day_stat, time_stat)
            broad_id = (session.query(Broadcast).filter(
                and_(Broadcast.broadcast_date == (base + datetime.timedelta(days=day_id)),
                     Broadcast.broadcast_time == '14:00'))[0]).broadcast_id
            maximum = session.query(func.max(OrderSong.song_id)).scalar()
            s_id = (session.query(OrderSong).filter(OrderSong.song_id == maximum)[0]).song_id
            chain_in = Chain(broadcast_id_fk=broad_id, song_id_fk=s_id)
            session.add(chain_in)
            session.commit()
            bot.send_message(message.chat.id,
                             'Ваше замовлення відправлено на модерацію',
                             reply_markup=to_main_menu)
        elif message.text == 'Вечір\n18:00-21:00':
            day_stat = base + datetime.timedelta(days=day_id)
            time_stat = 3
            stat_insert(day_stat, time_stat)
            broad_id = (session.query(Broadcast).filter(
                and_(Broadcast.broadcast_date == (base + datetime.timedelta(days=day_id)),
                     Broadcast.broadcast_time == '18:00'))[0]).broadcast_id
            maximum = session.query(func.max(OrderSong.song_id)).scalar()
            s_id = (session.query(OrderSong).filter(OrderSong.song_id == maximum)[0]).song_id
            chain_in = Chain(broadcast_id_fk=broad_id, song_id_fk=s_id)
            session.add(chain_in)
            session.commit()
            bot.send_message(message.chat.id,
                             'Ваше замовлення відправлено на модерацію.',
                             reply_markup=to_main_menu)
        else:
            bot.send_message(message.chat.id,
                             'Неправильно введено дані. Введіть, будь-ласка, час:',
                             reply_markup=keyboard5)
            bot.register_next_step_handler(message, time_choose)
    else:
        bot.send_message(message.chat.id,
                         'Неправильно введено дані. Введіть, будь-ласка, час:',
                         reply_markup=keyboard5)
        bot.register_next_step_handler(message, time_choose)

def announcement(message):
    Name = message.text
    for i in range(1, 8):
        dayweek = base + datetime.timedelta(days=i)
        if (dayweek.isoweekday() == 2):
            break
    if (len((session.query(Broadcast).filter(and_(Broadcast.broadcast_date == dayweek, Broadcast.broadcast_time == 'txt'))).all()) == 0):
        announ_add = Broadcast(broadcast_date=dayweek, broadcast_time='txt')
        session.add(announ_add)
        session.commit()
    if (type(Name) == str):
        ann = Announcement(announcement_text=Name)
        session.add(ann)
        session.commit()
        maximum = session.query(func.max(Announcement.announcement_id)).scalar()
        announ_id = (session.query(Announcement).filter(Announcement.announcement_id == maximum)[0]).announcement_id
        broad_id = (session.query(Broadcast).filter(and_(Broadcast.broadcast_date == dayweek, Broadcast.broadcast_time == 'txt'))[0]).broadcast_id
        announ_insert = AnnouncementChain(broadcast_id_fk=broad_id, announcement_id_fk=announ_id)
        session.add(announ_insert)
        session.commit()
        bot.send_message(message.chat.id,
                         'Ваше оголошення на '+str(dayweek)+'. Оголошення відправлено на модерацію.',
                         reply_markup=to_main_menu)
    else:
        bot.send_message(message.chat.id,
                         'Будь-ласка, введіть оголошення коректно.',
                         reply_markup=to_main_menu)
        bot.register_next_step_handler(message, announcement)

def feedback_to(message):
    Name = message.text
    if (type(Name) == str):
        feed = feedback(feedback_text=Name)
        session.add(feed)
        session.commit()
        bot.send_message(message.chat.id,
                         'Дякуємо за Ваш відгук.',
                         reply_markup=keyboard2)

def stat_insert(day, timing):
    num = day.isoweekday()
    if (num == 1):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Monday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 2):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Tuesday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 3):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Wednesday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 4):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Thursday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 5):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Friday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 6):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Saturday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()
    elif (num == 7):
        if (timing == 1):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '8:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '8:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 2):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '14:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '14:00')).update({'statistic_count':count_now})
            session.commit()
        elif (timing == 3):
            count_now = (session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '18:00'))[0]).statistic_count
            count_now = count_now + 1
            session.query(Statistic).filter(and_(Statistic.statistic_day == 'Sunday', Statistic.statistic_time == '18:00')).update({'statistic_count':count_now})
            session.commit()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Вас вітає Radio Bot - бот, призначений для роботи з користувачем на радіо')
    bot.send_message(message.chat.id, 'Оберіть, будь ласка, потрібну функцію у меню',
                     reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    global day_id
    global day_stat
    global time_stat
    if message.text == 'Замовлення':
        bot.send_message(message.chat.id,
                         'Оберіть, будь ласка, потрібне замовлення.',
                         reply_markup=keyboard3)
    elif message.text == 'Замовлення пісні':
        bot.send_message(message.chat.id,
                         'Будь ласка, завантажте файл з піснею.')
        bot.register_next_step_handler(message, audio_test)
    elif message.text == 'Розклад ефірів':
        bot.send_message(message.chat.id,
                         'Музичні ефіри відбуваються 3 рази на день кожного дня.\nРанковий ефір: 8:00-11:00\nДенний ефір: 14:00-17:00\nВечірній ефір: 18:00-21:00',
                         reply_markup=keyboard1)
    elif message.text == 'Замовлення оголошення':
        for i in range(1, 8):
            tuesday = base + datetime.timedelta(days=i)
            if (tuesday.isoweekday() == 2):
                break
        bot.send_message(message.chat.id,
                         'Найближчий день озвучування вашого оголошення - '+str(tuesday)+'. Напишіть, будь ласка, Ваше повідомлення')
        bot.register_next_step_handler(message, announcement)
    elif message.text == 'Допомога':
        bot.send_message(message.chat.id,
                         'Оберіть, будь ласка, цікавлючу Вас тему.',
                         reply_markup=keyboard2)
    elif message.text == 'Особливості замовлення':
        bot.send_message(message.chat.id,
                        'Для того, щоб замовити пісню, користувач повинен завантажити файл та вибрати день та час, коли пісня повинна зіграти.\nНа наступний вівторок користувач має можливість замовити оголошення.',
                        reply_markup=keyboard2)
    elif message.text == 'Модерація':
        bot.send_message(message.chat.id,
                         'Можливо замовити лише одну пісню за одне замовлення. Також замовлена пісня не повинна містити у собі нецензурної лексики російською або українською мовою та повинна мати тривалість 7 хвилин і менше.'+
                         '\nЩо стосується замовлення оголошень, то воно не повинно бути комерційним, містити нецензурну лексику, мати за мету образити когось. Оголошення повинно бути російською або українською мовою.'+
                         '\nМодератори мають право без пояснення причин не допустити пісню або замовлення до ефіру.',
                         reply_markup=keyboard2)
    elif message.text == 'Зворотний зв`язок':
        bot.send_message(message.chat.id,
                         'Ви можете залишити свій відгук прямо тут, написавши нам. Ми будемо вдячні за будь які пропозиції.')
        bot.register_next_step_handler(message, feedback_to)
    elif message.text == 'До головного меню':
        bot.send_message(message.chat.id,
                         'Оберіть, будь ласка, потрібну функцію у меню',
                         reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id,
                         'Невідома команда. Повернення до головного меню. Будь-ласка, оберіть правильну команду.',
                         reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)