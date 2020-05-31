from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
import db_classes
import json
from sqlalchemy.orm import relationship, sessionmaker
#
Session = sessionmaker(bind = engine)
session = Session()
# считывание данных с файла, на другом компьютере прийдеся вставить другой путь к файлам

categories = open("categories.json",encoding="utf-8")
data_categories = json.load(categories)
dishes = open("recipes.json",encoding="utf8")
data_dishes = json.load(dishes)
marks = open("marks.json",encoding="utf8")
data_marks = json.load(marks)
clients = open("clients.json",encoding="utf8")
data_clients = json.load(clients)

# # добавление категорий блюд
# session.add_all([
#    db_classes.Clients(id = data_clients['clients'][0]['id'], client_username = data_clients['clients'][0]['name']),
# db_classes.Clients(id = data_clients['clients'][1]['id'], client_username = data_clients['clients'][1]['name'])]
# )
# session.commit()
#
# session.add_all([
#     db_classes.Dishes(id = data_dishes['dish'][0]['id'],
#            dish_name = data_dishes['dish'][0]['name'],
#            id_category=data_dishes['dish'][0]['id_category'],
#            text_recipe = data_dishes['dish'][0]['text_recipe'],
#            video_recept=data_dishes['dish'][0]['video_recipe'],
#            ingridients=data_dishes['dish'][0]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][1]['id'],
#            dish_name = data_dishes['dish'][1]['name'],
#            id_category=data_dishes['dish'][1]['id_category'],
#            text_recipe = data_dishes['dish'][1]['text_recipe'],
#            video_recept=data_dishes['dish'][1]['video_recipe'],
#            ingridients=data_dishes['dish'][1]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][2]['id'],
#            dish_name = data_dishes['dish'][2]['name'],
#            id_category=data_dishes['dish'][2]['id_category'],
#            text_recipe = data_dishes['dish'][2]['text_recipe'],
#            video_recept=data_dishes['dish'][2]['video_recipe'],
#            ingridients=data_dishes['dish'][2]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][3]['id'],
#            dish_name = data_dishes['dish'][3]['name'],
#            id_category=data_dishes['dish'][3]['id_category'],
#            text_recipe = data_dishes['dish'][3]['text_recipe'],
#            video_recept=data_dishes['dish'][3]['video_recipe'],
#            ingridients=data_dishes['dish'][3]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][4]['id'],
#            dish_name = data_dishes['dish'][4]['name'],
#            id_category=data_dishes['dish'][4]['id_category'],
#            text_recipe = data_dishes['dish'][4]['text_recipe'],
#            video_recept=data_dishes['dish'][4]['video_recipe'],
#            ingridients=data_dishes['dish'][4]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][5]['id'],
#            dish_name = data_dishes['dish'][5]['name'],
#            id_category=data_dishes['dish'][5]['id_category'],
#            text_recipe = data_dishes['dish'][5]['text_recipe'],
#            video_recept=data_dishes['dish'][5]['video_recipe'],
#            ingridients=data_dishes['dish'][5]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][6]['id'],
#            dish_name = data_dishes['dish'][6]['name'],
#            id_category=data_dishes['dish'][6]['id_category'],
#            text_recipe = data_dishes['dish'][6]['text_recipe'],
#            video_recept=data_dishes['dish'][6]['video_recipe'],
#            ingridients=data_dishes['dish'][6]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][7]['id'],
#            dish_name = data_dishes['dish'][7]['name'],
#            id_category=data_dishes['dish'][7]['id_category'],
#            text_recipe = data_dishes['dish'][7]['text_recipe'],
#            video_recept=data_dishes['dish'][7]['video_recipe'],
#            ingridients=data_dishes['dish'][8]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][8]['id'],
#            dish_name = data_dishes['dish'][8]['name'],
#            id_category=data_dishes['dish'][8]['id_category'],
#            text_recipe = data_dishes['dish'][8]['text_recipe'],
#            video_recept=data_dishes['dish'][8]['video_recipe'],
#            ingridients=data_dishes['dish'][8]['ingridients']),
# ]
# )
# session.commit()
#
# session.add_all([
#    db_classes.Marks(id = data_marks['marks'][0]['id'], mark_value = data_marks['marks'][0]['value'], client_id = data_marks['marks'][0]['id_client'], dish_id = data_marks['marks'][0]['id_dish'], text_reviw = data_marks['marks'][0]['text_reviw'],user_name = data_marks['marks'][0]['name']),
#    db_classes.Marks(id = data_marks['marks'][1]['id'], mark_value = data_marks['marks'][1]['value'], client_id = data_marks['marks'][1]['id_client'], dish_id = data_marks['marks'][1]['id_dish'], text_reviw = data_marks['marks'][1]['text_reviw'],user_name = data_marks['marks'][1]['name'])]
# )
# session.commit()

# добавление рецептов и названий блюд
# session.add_all([
#     db_classes.Dishes(id = data_dishes['dish'][0]['id'],
#            dish_name = data_dishes['dish'][0]['name'],
#            id_category=data_dishes['dish'][0]['id_category'],
#            text_recipe = data_dishes['dish'][0]['text_recipe'],
#            video_recept=data_dishes['dish'][0]['video_recipe'],
#            ingridients=data_dishes['dish'][0]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][1]['id'],
#            dish_name = data_dishes['dish'][1]['name'],
#            id_category=data_dishes['dish'][1]['id_category'],
#            text_recipe = data_dishes['dish'][1]['text_recipe'],
#            video_recept=data_dishes['dish'][1]['video_recipe'],
#            ingridients=data_dishes['dish'][1]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][2]['id'],
#            dish_name = data_dishes['dish'][2]['name'],
#            id_category=data_dishes['dish'][2]['id_category'],
#            text_recipe = data_dishes['dish'][2]['text_recipe'],
#            video_recept=data_dishes['dish'][2]['video_recipe'],
#            ingridients=data_dishes['dish'][2]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][3]['id'],
#            dish_name = data_dishes['dish'][3]['name'],
#            id_category=data_dishes['dish'][3]['id_category'],
#            text_recipe = data_dishes['dish'][3]['text_recipe'],
#            video_recept=data_dishes['dish'][3]['video_recipe'],
#            ingridients=data_dishes['dish'][3]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][4]['id'],
#            dish_name = data_dishes['dish'][4]['name'],
#            id_category=data_dishes['dish'][4]['id_category'],
#            text_recipe = data_dishes['dish'][4]['text_recipe'],
#            video_recept=data_dishes['dish'][4]['video_recipe'],
#            ingridients=data_dishes['dish'][4]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][5]['id'],
#            dish_name = data_dishes['dish'][5]['name'],
#            id_category=data_dishes['dish'][5]['id_category'],
#            text_recipe = data_dishes['dish'][5]['text_recipe'],
#            video_recept=data_dishes['dish'][5]['video_recipe'],
#            ingridients=data_dishes['dish'][5]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][6]['id'],
#            dish_name = data_dishes['dish'][6]['name'],
#            id_category=data_dishes['dish'][6]['id_category'],
#            text_recipe = data_dishes['dish'][6]['text_recipe'],
#            video_recept=data_dishes['dish'][6]['video_recipe'],
#            ingridients=data_dishes['dish'][6]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][9]['id'],
#            dish_name = data_dishes['dish'][9]['name'],
#            id_category=data_dishes['dish'][9]['id_category'],
#            text_recipe = data_dishes['dish'][9]['text_recipe'],
#            video_recept=data_dishes['dish'][9]['video_recipe'],
#            ingridients=data_dishes['dish'][9]['ingridients']),
# db_classes.Dishes(id = data_dishes['dish'][10]['id'],
#            dish_name = data_dishes['dish'][10]['name'],
#            id_category=data_dishes['dish'][10]['id_category'],
#            text_recipe = data_dishes['dish'][10]['text_recipe'],
#            video_recept=data_dishes['dish'][10]['video_recipe'],
#            ingridients=data_dishes['dish'][10]['ingridients']),
# ]
# )




