import telebot
import config
import re
from sqlalchemy import func, and_
from database_connection import engine
from sqlalchemy.orm import sessionmaker
from model import UserProfile, Card, Supply, PowerSupply, WaterSupply, GasSupply, Payed

Session = sessionmaker(bind=engine)
session = Session()

TOKEN = config.TOKEN

botuseon = telebot.TeleBot(TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Зареєструватися')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Додати картку','Ввести дані')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Газопостачання', "Водопостачання")
keyboard3.row("Електропостачання")
keyboard3.row("Назад")
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row("Назад")
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row("Оплатити",'Ввести дані')
keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row("Додати/відмінити оплату елктропостачання")
keyboard6.row("Додати/відмінити оплату газопостачання")
keyboard6.row("Додати/відмінити оплату водопостачання")
keyboard6.row("Оплатити", "Назад")
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row("Підтвердити", "Відмінити")

class BotUser:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name= name
        self.phone = phone
        self.email = email
        self.state = 0

class BotCard:
    def __init__(self, id, number, name, date, cvv):
        self.id = id
        self.number = number
        self.name = name
        self.date = date
        self.cvv = cvv

class BotSupply:
    def __init__(self, id, water_supply_id, power_supply_id, gas_supply_id):
        self.id = id
        self.water_supply_id = water_supply_id
        self.power_supply_id = power_supply_id
        self.gas_supply_id = gas_supply_id

class BotWaterInput:
    def __init__(self, water_supply_id, water_hot_previous, water_hot_current, water_cold_previous, water_cold_current):
        self.water_supply_id = water_supply_id
        self.water_hot_previous = water_hot_previous
        self.water_hot_current = water_hot_current
        self.water_cold_previous = water_cold_previous
        self.water_cold_current = water_cold_current

class BotPay:
    def __init__(self, id):
        self.id = id
        self.water_sum = 0
        self.water_to_pay = 1
        self.gas_sum = 0
        self.gas_to_pay = 1
        self.power_sum = 0
        self.power_to_pay = 1

user = None
card = None
supply = None
bwi = None
bp = None

@botuseon.message_handler(commands=['start'])
def start_message(message):
    global user
    global card
    global supply
    global bp
    user = BotUser(message.from_user.id, None, None, None)
    card = BotCard(message.from_user.id, None, None, None, None)
    supply = BotSupply(message.from_user.id, None, None, None)
    bp = BotPay(message.from_user.id)
    if len((session.query(UserProfile).filter(UserProfile.user_id == user.id)).all()) == 0:
        botuseon.send_message(message.from_user.id, "Привіт, {0.first_name}! Я <b>{1.first_name}</b>, "
                     "<b>бот для внесення даних і оплати комунальних послуг.</b>"
                     "\nСпочатку зареєструйтеся.".format(message.from_user,
                                                             botuseon.get_me()),
                     parse_mode='html',
                     reply_markup=keyboard1)
    else:
        tempo = ((session.query(UserProfile).filter(UserProfile.user_id == user.id)).all())[0]
        user = BotUser(tempo.user_id, tempo.user_name, tempo.user_phone, tempo.user_email)
        del tempo
        tempo = ((session.query(Supply).filter(Supply.user_id_fk == user.id)).all())[0]
        supply = BotSupply(tempo.user_id_fk, tempo.water_supply_id, tempo.power_supply_id, tempo.gas_supply_id)
        del tempo
        user.state = 1
        if len((session.query(Card).filter(Card.user_id_fk == user.id)).all()) == 0:
            botuseon.send_message(message.from_user.id, "Привіт, {0}! Ви вже зареєстровані.".format(user.name),
                                  parse_mode='html',
                                  reply_markup=keyboard2)
        else:
            user.state = 2
            tempo = ((session.query(Card).filter(Card.user_id_fk == user.id)).all())[0]
            card = BotCard(tempo.user_id_fk, tempo.card_number, tempo.card_name, tempo.card_date, tempo.card_cvv)
            del tempo
            botuseon.send_message(message.from_user.id, "Привіт, {0}! Ви вже зареєстровані.".format(user.name),
                                  parse_mode='html',
                                  reply_markup=keyboard5)


def reg_check(message):
    global user
    global card
    global supply
    global bp
    if user == None:
        if len((session.query(UserProfile).filter(UserProfile.user_id == message.from_user.id)).all()) == 0:
            user = BotUser(message.from_user.id, None, None, None)
            supply = BotSupply(message.from_user.id, None, None, None)
        else:
            tempo = ((session.query(UserProfile).filter(UserProfile.user_id == message.from_user.id)).all())[0]
            user = BotUser(tempo.user_id, tempo.user_name, tempo.user_phone, tempo.user_email)
            del tempo
            tempo = ((session.query(Supply).filter(Supply.user_id_fk == message.from_user.id)).all())[0]
            supply = BotSupply(tempo.user_id_fk, tempo.water_supply_id, tempo.power_supply_id, tempo.gas_supply_id)
            del tempo
            user.state = 1
    if card == None:
        if len((session.query(Card).filter(Card.user_id_fk == message.from_user.id)).all()) == 0:
            card = BotCard(message.from_user.id, None, None, None, None)
        else:
            tempo = ((session.query(Card).filter(Card.user_id_fk == message.from_user.id)).all())[0]
            card = BotCard(tempo.user_id_fk, tempo.card_number, tempo.card_name, tempo.card_date, tempo.card_cvv)
            del tempo
            bp = BotPay(message.from_user.id)
            user.state = 2


@botuseon.message_handler(content_types=['text'])
def send_text(message):
    reg_check(message)
    if message.text.lower() == 'зареєструватися' and user.state==0:
        botuseon.send_message(message.from_user.id, "Введіть Ваше ім'я:")
        botuseon.register_next_step_handler(message, registr)
    elif message.text.lower() == 'додати картку' and user.state!=2:
        botuseon.send_message(message.from_user.id, 'Додаємо картку. \nВведіть номер картки', reply_markup=keyboard4)
        botuseon.register_next_step_handler(message, registr_kard)
    elif message.text.lower() == 'назад':
        if user.state != 2:
            botuseon.send_message(message.from_user.id, 'Оберіть дію',reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    elif message.text.lower() == 'ввести дані':
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?',
                              reply_markup=keyboard3)
    elif message.text.lower() == 'оплатити' and user.state==2:
        payment_calculate()
        botuseon.send_message(message.from_user.id, 'Суми до сплати:\nЕлктропостачання: {0} грн.'
                                                    '\nГазопостачання: {1} грн.\nВодопостачання: {2} грн.'
                                                    '\nЗагальна сума: {3} грн.'.format(bp.power_sum, bp.gas_sum,
                                                    bp.water_sum, round(bp.power_sum + bp.gas_sum + bp.water_sum, 2)),
                              reply_markup=keyboard6)
        botuseon.register_next_step_handler(message, pay)
    elif message.text.lower() == 'газопостачання':
        botuseon.send_message(message.from_user.id, 'Введіть покази лічильника', reply_markup=keyboard4)
        botuseon.register_next_step_handler(message, gas_input)
    elif message.text.lower() == 'електропостачання':
        botuseon.send_message(message.from_user.id, 'Введіть покази лічильника', reply_markup=keyboard4)
        botuseon.register_next_step_handler(message, power_input)
    elif message.text.lower() == 'водопостачання':
        botuseon.send_message(message.from_user.id, 'Введіть попередні покази лічильника гарячої води', reply_markup=keyboard4)
        botuseon.register_next_step_handler(message, water_input)
    elif user.state==0:
        botuseon.send_message(message.from_user.id, 'Почніть реєстрацію',reply_markup=keyboard1)
    else:
        if user.state != 2:
            botuseon.send_message(message.from_user.id, "Невідома команда", reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, "Невідома команда", reply_markup=keyboard5)

def gas_input(message):
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) >= 0:
        new_reading = GasSupply(gas_supply_id=supply.gas_supply_id, filling_date=func.current_timestamp(),
                                gas_reading=reading, payment_status = 0)
        session.add(new_reading)
        session.commit()
        botuseon.send_message(message.from_user.id, "Показ успішно збережено", reply_markup=keyboard3)
    elif message.text.lower() == 'назад':
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, gas_input)

def power_input(message):
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) >= 0:
        new_reading = PowerSupply(power_supply_id=supply.power_supply_id, filling_date=func.current_timestamp(),
                                  power_reading=reading, payment_status = 0)
        session.add(new_reading)
        session.commit()
        botuseon.send_message(message.from_user.id, "Показ успішно збережено", reply_markup=keyboard3)
    elif message.text.lower() == 'назад':
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, power_input)

def water_input(message):
    global bwi
    bwi = BotWaterInput(supply.water_supply_id, None, None, None, None)
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) >= 0:
        bwi.water_hot_previous = reading
        botuseon.send_message(message.from_user.id, "Показ збережено. Тепер введіть поточні покази лічильника гарячої води")
        botuseon.register_next_step_handler(message, water_input_2)
    elif message.text.lower() == 'назад':
        bwi = None
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, water_input)

def water_input_2(message):
    global bwi
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) < float(bwi.water_hot_previous):
        botuseon.send_message(message.from_user.id, "Попередній показ не має перевищувати поточний")
        botuseon.register_next_step_handler(message, water_input_2)
    elif re.match(regex, reading) != None and float(reading) >= float(bwi.water_hot_previous):
        bwi.water_hot_current = reading
        botuseon.send_message(message.from_user.id, "Показ збережено. Тепер введіть попередні покази лічильника холодної води")
        botuseon.register_next_step_handler(message, water_input_3)
    elif message.text.lower() == 'назад':
        bwi = None
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, water_input_2)

def water_input_3(message):
    global bwi
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) >= 0:
        bwi.water_cold_previous = reading
        botuseon.send_message(message.from_user.id, "Показ збережено. Тепер введіть поточні покази лічильника холодної води")
        botuseon.register_next_step_handler(message, water_input_4)
    elif message.text.lower() == 'назад':
        bwi = None
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, water_input_3)

def water_input_4(message):
    global bwi
    reading = message.text
    regex = '^-?\d+(?:\.\d+)?$'
    if re.match(regex, reading) != None and float(reading) < float(bwi.water_cold_previous):
        botuseon.send_message(message.from_user.id, "Попередній показ не має перевищувати поточний")
        botuseon.register_next_step_handler(message, water_input_4)
    elif re.match(regex, reading) != None and float(reading) >= float(bwi.water_cold_previous):
        bwi.water_cold_current = reading
        new_reading = WaterSupply(water_supply_id=supply.water_supply_id, water_hot_previous=bwi.water_hot_previous,
                                  water_hot_current=bwi.water_hot_current, water_cold_previous=bwi.water_cold_previous,
                                  water_cold_current=bwi.water_cold_current, filling_date=func.current_timestamp(),
                                  payment_status = 0)
        session.add(new_reading)
        session.commit()
        bwi = None
        botuseon.send_message(message.from_user.id, "Покази успішно збережено", reply_markup=keyboard3)
    elif message.text.lower() == 'назад':
        bwi = None
        botuseon.send_message(message.from_user.id, 'Які саме дані ви хочете занести?', reply_markup=keyboard3)
    else:
        botuseon.send_message(message.from_user.id, "Введіть коректний показ")
        botuseon.register_next_step_handler(message, water_input_4)

def registr(message):
    Name = message.text
    lname = [i.isalpha() for i in Name.split()]
    if all(lname) and len(lname) <= 3 and len(Name) > 1:
        user.name = Name
        botuseon.send_message(message.from_user.id, 'Тепер введіть номер телефона у форматі +38xxxxxxxxxx')
        botuseon.register_next_step_handler(message, registr_2)

    else:
        botuseon.send_message(message.from_user.id, "Введіть коректне ім'я")
        botuseon.register_next_step_handler(message, registr)

def registr_2(message):
    Number = message.text
    if len((session.query(UserProfile).filter(UserProfile.user_phone == Number)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей номер вже зайнятий')
        botuseon.register_next_step_handler(message, registr_2)
    elif Number[0] == '+' and Number[1] == '3' and Number[2] == '8' and Number[1:].isdigit() and len(Number) == 13:
        user.phone = Number
        botuseon.send_message(message.from_user.id, 'Тепер введіть емейл адресу')
        botuseon.register_next_step_handler(message, registr_3)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний номер телефона')
        botuseon.register_next_step_handler(message, registr_2)

def registr_3(message):
    email = message.text
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    if len((session.query(UserProfile).filter(UserProfile.user_email == email)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей емейл вже зайнятий')
        botuseon.register_next_step_handler(message, registr_3)
    elif re.search(regex, email) != None:
        user.email = email
        botuseon.send_message(message.from_user.id, 'Емейл адреса збережена. Тепер введіть номер особового рахунку водопостачання')
        botuseon.register_next_step_handler(message, registr_4)
        #state[0] = 1
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректну емейл адресу')
        botuseon.register_next_step_handler(message, registr_3)

def registr_4(message):
    water_supply_id = message.text
    if len((session.query(Supply).filter(Supply.water_supply_id == water_supply_id)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей номер вже зайнятий')
        botuseon.register_next_step_handler(message, registr_4)
    elif water_supply_id.isdigit():
        supply.water_supply_id = water_supply_id
        botuseon.send_message(message.from_user.id, 'Данні додані. Тепер введіть номер особового рахунку електропостачання')
        botuseon.register_next_step_handler(message, registr_5)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний номер особового рахунку водопостачання')
        botuseon.register_next_step_handler(message, registr_4)

def registr_5(message):
    power_supply_id = message.text
    if len((session.query(Supply).filter(Supply.power_supply_id == power_supply_id)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей номер вже зайнятий')
        botuseon.register_next_step_handler(message, registr_5)
    elif power_supply_id.isdigit():
        supply.power_supply_id = power_supply_id
        botuseon.send_message(message.from_user.id,
                              'Данні додані. Тепер введіть номер особового рахунку газопостачання')
        botuseon.register_next_step_handler(message, registr_6)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний номер особового рахунку електропостачання')
        botuseon.register_next_step_handler(message, registr_5)

def registr_6(message):
    gas_supply_id = message.text
    if len((session.query(Supply).filter(Supply.gas_supply_id == gas_supply_id)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей номер вже зайнятий')
        botuseon.register_next_step_handler(message, registr_6)
    elif gas_supply_id.isdigit():
        supply.gas_supply_id = gas_supply_id
        new_user = UserProfile(user_id=user.id, user_name=user.name, user_phone=user.phone, user_email=user.email)
        new_supply = Supply(user_id_fk=supply.id, water_supply_id=supply.water_supply_id,
                            power_supply_id=supply.power_supply_id, gas_supply_id=supply.gas_supply_id)
        session.add(new_user)
        session.commit()
        session.add(new_supply)
        session.commit()
        user.state = 1
        botuseon.send_message(message.from_user.id,
                              'Вітаємо з реестрацією. Далі Ви можете передати дані або додати картку',
                              reply_markup=keyboard2)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний номер особового рахунку газопостачання')
        botuseon.register_next_step_handler(message, registr_6)

"""
regex = '^-?\d+(?:\.\d+)?$'
if re.match(regex, water_supply_id) != None:

botuseon.send_message(message.from_user.id,
                      'Вітаємо з реестрацією. Далі ви можете передати дані або додати картку розрахунку',
                      reply_markup=keyboard2)
"""

def  registr_kard(message):
    number = message.text
    if len((session.query(Card).filter(Card.card_number == number)).all()) != 0:
        botuseon.send_message(message.from_user.id, 'Цей номер вже зайнятий')
        botuseon.register_next_step_handler(message, registr_kard)
    if number.isdigit() and len(number) == 16:
        card.number = number
        botuseon.send_message(message.from_user.id,
                          "Номер картки додано. Тепер введіть ім'я на карті\nЯкщо ім'я на карті не вказано, введіть '-'")
        botuseon.register_next_step_handler(message, registr_kard2)
    elif message.text.lower() == 'назад':
        if user.state != 2:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний номер картки'
                              )
        botuseon.register_next_step_handler(message, registr_kard)

def registr_kard2(message):
    name = message.text
    lname = [i.isalpha() for i in name.split()]
    if name == '-':
        name = None
        card.name = name
        botuseon.send_message(message.from_user.id,
                              "Ім'я записане. Тепер додайте дату на картці у форматі mm/yy")
        botuseon.register_next_step_handler(message, registr_kard3)
    elif all(lname) and len(lname) == 2 and len(name) > 1:
        card.name = name
        botuseon.send_message(message.from_user.id,
                              "Ім'я записане. Тепер додайте дату на картці у форматі mm/yy")
        botuseon.register_next_step_handler(message, registr_kard3)
    elif message.text.lower() == 'назад':
        if user.state != 2:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    else:
        botuseon.send_message(message.from_user.id, "Введіть корректне ім'я"
                              )
        botuseon.register_next_step_handler(message, registr_kard2)

def registr_kard3(message):
    date = message.text
    regex = '\d\d/\d\d'
    if len(date) == 5 and re.search(regex, date) != None and int(date[:2]) <= 12:
        card.date = date
        botuseon.send_message(message.from_user.id,
                          'Дата записана. Введіть <b>CVV/CVV2</b> код.', parse_mode='html')
        botuseon.register_next_step_handler(message, registr_kard4)
    elif message.text.lower() == 'назад':
        if user.state != 2:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректну дату')
        botuseon.register_next_step_handler(message, registr_kard3)

def registr_kard4(message):
    cvv = message.text
    if cvv.isdigit() and len(cvv) == 3:
        card.cvv = cvv
        new_card = Card(user_id_fk=card.id, card_number=card.number,
                            card_name=card.name, card_date=card.date, card_cvv=card.cvv)
        session.add(new_card)
        session.commit()
        user.state = 2
        botuseon.send_message(message.from_user.id,
                          'CVV записаний. Дякуємо за повну реєстрацію', reply_markup=keyboard5)
    elif message.text.lower() == 'назад':
        if user.state != 2:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard2)
        else:
            botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    else:
        botuseon.send_message(message.from_user.id, 'Введіть корректний <b>CVV/CVV2</b> код.', parse_mode='html')
        botuseon.register_next_step_handler(message, registr_kard4)

def payment_calculate():
    global bp
    if bp == None:
        bp = BotPay(user.id)
    water_bills = (session.query(WaterSupply).filter(and_(WaterSupply.water_supply_id == supply.water_supply_id,
                                                          WaterSupply.payment_status == 0))).all()
    power_bills = (session.query(PowerSupply).filter(and_(PowerSupply.power_supply_id == supply.power_supply_id,
                                                          PowerSupply.payment_status == 0))).all()
    gas_bills = (session.query(GasSupply).filter(and_(GasSupply.gas_supply_id == supply.gas_supply_id,
                                                      GasSupply.payment_status == 0))).all()

    if bp.power_to_pay == 1:
        summa = 0
        for i in power_bills:
            summa += i.power_reading
        if summa <= 100:
            summa *= 0.9
        else:
            summa = 90 + (summa - 100)*1.68
        summa = round(summa, 2)
        bp.power_sum = summa
        del summa
    else:
        bp.power_sum = 0.0

    if bp.gas_to_pay == 1:
        summa = 0
        for i in gas_bills:
            summa += i.gas_reading
        summa *= 2.94813
        summa = round(summa, 2)
        bp.gas_sum = summa
        del summa
    else:
        bp.gas_sum = 0.0

    if bp.water_to_pay == 1:
        summa1 = 0
        summa2 = 0
        for i in water_bills:
            summa1 += (i.water_hot_current - i.water_hot_previous)
            summa2 += (i.water_cold_current - i.water_cold_previous)
        summa1 *= 97.89
        summa2 *= 22.99
        bp.water_sum = round(summa1+summa2, 2)
        del summa1
        del summa2
    else:
        bp.water_sum = 0.0

def pay(message):
    option = message.text
    global bp
    if bp == None:
        bp = BotPay(message.from_user.id)
    if option.lower() == "додати/відмінити оплату елктропостачання":
        if bp.power_to_pay == 0:
            bp.power_to_pay = 1
        else:
            bp.power_to_pay = 0
        payment_calculate()
        botuseon.send_message(message.from_user.id, 'Суми до сплати:\nЕлктропостачання: {0} грн.'
                                                    '\nГазопостачання: {1} грн.\nВодопостачання: {2} грн.'
                                                    '\nЗагальна сума: {3} грн.'.format(bp.power_sum, bp.gas_sum,
                                                    bp.water_sum, round(bp.power_sum + bp.gas_sum + bp.water_sum, 2)),
                              reply_markup=keyboard6)
        botuseon.register_next_step_handler(message, pay)
    elif option.lower() == "додати/відмінити оплату газопостачання":
        if bp.gas_to_pay == 0:
            bp.gas_to_pay = 1
        else:
            bp.gas_to_pay = 0
        payment_calculate()
        botuseon.send_message(message.from_user.id, 'Суми до сплати:\nЕлктропостачання: {0} грн.'
                                                    '\nГазопостачання: {1} грн.\nВодопостачання: {2} грн.'
                                                    '\nЗагальна сума: {3} грн.'.format(bp.power_sum, bp.gas_sum,
                                                                                       bp.water_sum, round(
                bp.power_sum + bp.gas_sum + bp.water_sum, 2)),
                              reply_markup=keyboard6)
        botuseon.register_next_step_handler(message, pay)
    elif option.lower() == "додати/відмінити оплату водопостачання":
        if bp.water_to_pay == 0:
            bp.water_to_pay = 1
        else:
            bp.water_to_pay = 0
        payment_calculate()
        botuseon.send_message(message.from_user.id, 'Суми до сплати:\nЕлктропостачання: {0} грн.'
                                                    '\nГазопостачання: {1} грн.\nВодопостачання: {2} грн.'
                                                    '\nЗагальна сума: {3} грн.'.format(bp.power_sum, bp.gas_sum,
                                                    bp.water_sum, round(bp.power_sum + bp.gas_sum + bp.water_sum, 2)),
                              reply_markup=keyboard6)
        botuseon.register_next_step_handler(message, pay)
    elif option.lower() == "назад":
        botuseon.send_message(message.from_user.id, 'Оберіть дію', reply_markup=keyboard5)
    elif option.lower() == "оплатити":
        if bp.power_sum + bp.water_sum + bp.gas_sum != 0:
            botuseon.send_message(message.from_user.id, 'Підтвердіть оплату', reply_markup=keyboard7)
            botuseon.register_next_step_handler(message, confirm)
        else:
            botuseon.send_message(message.from_user.id, "Нічого не обрано для сплати", reply_markup=keyboard6)
            botuseon.register_next_step_handler(message, pay)
    else:
        botuseon.send_message(message.from_user.id, "Невідома команда", reply_markup=keyboard6)
        botuseon.register_next_step_handler(message, pay)


def confirm(message):
    global bp
    if bp == None:
        bp = BotPay(user.id)
    if message.text.lower() == "підтвердити":
        new_payment = Payed(user_id_fk=user.id, payment_time=func.current_timestamp(), gas_payed=bp.gas_sum,
                            power_payed=bp.power_sum, water_payed=bp.water_sum)
        session.add(new_payment)
        session.commit()
        if bp.gas_to_pay == 1:
            session.query(GasSupply).filter(and_(GasSupply.gas_supply_id == supply.gas_supply_id,
                                                      GasSupply.payment_status == 0)).update({'payment_status':1})
            session.commit()
        if bp.power_to_pay == 1:
            session.query(PowerSupply).filter(and_(PowerSupply.power_supply_id == supply.power_supply_id,
                                                 PowerSupply.payment_status == 0)).update({'payment_status': 1})
            session.commit()
        if bp.water_to_pay == 1:
            session.query(WaterSupply).filter(and_(WaterSupply.water_supply_id == supply.water_supply_id,
                                                 WaterSupply.payment_status == 0)).update({'payment_status': 1})
            session.commit()
        botuseon.send_message(message.from_user.id, 'Оплата успішно здійснена!', reply_markup=keyboard5)
    elif message.text.lower() == "відмінити":
        botuseon.send_message(message.from_user.id, 'Оплата відмінена', reply_markup=keyboard5)
    else:
        botuseon.send_message(message.from_user.id, 'Підтвердіть або відмініть оплату', reply_markup=keyboard7)
        botuseon.register_next_step_handler(message, confirm)


botuseon.polling()