import telebot
from telebot import  types
########
input_by_hand = types.InlineKeyboardButton(text='Внести витрату вручну', callback_data='hand_waste')
track = types.InlineKeyboardButton(text='Відстежування витрат', callback_data='seek_waste')
#########
food = types.InlineKeyboardButton(text='Їжа', callback_data='food')
clothes = types.InlineKeyboardButton(text='Одяг', callback_data='clothes')
transport= types.InlineKeyboardButton(text='Транспорт', callback_data='transport')
beauty = types.InlineKeyboardButton(text='Краса', callback_data='beauty')

def main_keyboard():
    markup = types.InlineKeyboardMarkup()
    # edit_system = types.InlineKeyboardButton(text='Редагування системи')
    # replenish_card = types.InlineKeyboardButton(text='Поповнення картки')
    markup.add(input_by_hand, track)
    return markup
#########
def choose_category():
    markup =  markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(food, clothes, transport, beauty)
    return markup




