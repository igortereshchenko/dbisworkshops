from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
import json

Base = declarative_base()

from sqlalchemy.orm import relationship, sessionmaker
# создание таблиц
class Categories(Base):

    __tablename__ = 'dish_categories'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(50))

    styles = relationship('Dishes', backref='dish_categories', lazy=True)

class Dishes(Base):

    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    dish_name = Column(String(50))
    id_category = Column(Integer, ForeignKey("dish_categories.id"))
    text_recipe = Column(String(100))
    video_recept = Column(String(100))
    ingridients = Column(String(800))


class Clients(Base):

    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    client_username = Column(String(50))

class Marks(Base):

    __tablename__ = 'marks'

    id = Column(Integer, primary_key=True)
    mark_value = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))
    dish_id = Column(Integer, ForeignKey("dishes.id"))
    text_reviw = Column(String(100))
    user_name = Column(String(20))

    styles = relationship('Clients', backref='marks', lazy=True)
    styles_1 = relationship('Dishes', backref='marks', lazy=True)

Base.metadata.create_all(engine)

# добавления данных в бд
Session = sessionmaker(bind = engine)
session = Session()
# считывание данных с файла, на другом компьютере прийдеся вставить другой путь к файлам

categories = open("C:/Pyprojects/venv/categories.json",encoding="utf-8")
data_categories = json.load(categories)
dishes = open("C:/Pyprojects/venv/recipes.json",encoding="utf8")
data_dishes = json.load(dishes)
marks = open("C:/Pyprojects/venv/marks.json",encoding="utf8")
data_marks = json.load(marks)
clients = open("C:/Pyprojects/venv/clients.json",encoding="utf8")
data_clients = json.load(clients)

# добавление категорий блюд
session.add_all([
   Categories(id = data_categories['categories'][0]['id'], category_name = data_categories['categories'][0]['name']),
   Categories(id = data_categories['categories'][1]['id'], category_name = data_categories['categories'][1]['name']),
   Categories(id = data_categories['categories'][2]['id'], category_name = data_categories['categories'][2]['name']),
   Categories(id = data_categories['categories'][3]['id'], category_name = data_categories['categories'][3]['name'])]
)
session.commit()

# добавление рецептов и названий блюд
session.add_all([
    Dishes(id = data_dishes['dish'][0]['id'],
           dish_name = data_dishes['dish'][0]['name'],
           id_category=data_dishes['dish'][0]['id_category'],
           text_recipe = data_dishes['dish'][0]['text_recipe'],
           video_recept=data_dishes['dish'][0]['video_recipe'],
           ingridients=data_dishes['dish'][0]['ingridients']),
Dishes(id = data_dishes['dish'][1]['id'],
           dish_name = data_dishes['dish'][1]['name'],
           id_category=data_dishes['dish'][1]['id_category'],
           text_recipe = data_dishes['dish'][1]['text_recipe'],
           video_recept=data_dishes['dish'][1]['video_recipe'],
           ingridients=data_dishes['dish'][1]['ingridients']),
Dishes(id = data_dishes['dish'][2]['id'],
           dish_name = data_dishes['dish'][2]['name'],
           id_category=data_dishes['dish'][2]['id_category'],
           text_recipe = data_dishes['dish'][2]['text_recipe'],
           video_recept=data_dishes['dish'][2]['video_recipe'],
           ingridients=data_dishes['dish'][2]['ingridients']),
Dishes(id = data_dishes['dish'][3]['id'],
           dish_name = data_dishes['dish'][3]['name'],
           id_category=data_dishes['dish'][3]['id_category'],
           text_recipe = data_dishes['dish'][3]['text_recipe'],
           video_recept=data_dishes['dish'][3]['video_recipe'],
           ingridients=data_dishes['dish'][3]['ingridients']),
Dishes(id = data_dishes['dish'][4]['id'],
           dish_name = data_dishes['dish'][4]['name'],
           id_category=data_dishes['dish'][4]['id_category'],
           text_recipe = data_dishes['dish'][4]['text_recipe'],
           video_recept=data_dishes['dish'][4]['video_recipe'],
           ingridients=data_dishes['dish'][4]['ingridients']),
Dishes(id = data_dishes['dish'][5]['id'],
           dish_name = data_dishes['dish'][5]['name'],
           id_category=data_dishes['dish'][5]['id_category'],
           text_recipe = data_dishes['dish'][5]['text_recipe'],
           video_recept=data_dishes['dish'][5]['video_recipe'],
           ingridients=data_dishes['dish'][5]['ingridients']),
Dishes(id = data_dishes['dish'][6]['id'],
           dish_name = data_dishes['dish'][6]['name'],
           id_category=data_dishes['dish'][6]['id_category'],
           text_recipe = data_dishes['dish'][6]['text_recipe'],
           video_recept=data_dishes['dish'][6]['video_recipe'],
           ingridients=data_dishes['dish'][6]['ingridients']),
Dishes(id = data_dishes['dish'][7]['id'],
           dish_name = data_dishes['dish'][7]['name'],
           id_category=data_dishes['dish'][7]['id_category'],
           text_recipe = data_dishes['dish'][7]['text_recipe'],
           video_recept=data_dishes['dish'][7]['video_recipe'],
           ingridients=data_dishes['dish'][7]['ingridients']),
Dishes(id = data_dishes['dish'][8]['id'],
           dish_name = data_dishes['dish'][8]['name'],
           id_category=data_dishes['dish'][8]['id_category'],
           text_recipe = data_dishes['dish'][8]['text_recipe'],
           video_recept=data_dishes['dish'][8]['video_recipe'],
           ingridients=data_dishes['dish'][8]['ingridients']),
]
)
session.commit()

# Этот код следует запустить уже после первого запуска и поиска блюда в нем, эти данные добавляються искуственно, только для построения графика и добавления комментариев

# session.add_all([
#      Clients(id = data_clients['clients'][0]['id'],
#              client_username = data_clients['clients'][0]['name']),
#     Clients(id = data_clients['clients'][1]['id'],
#              client_username = data_clients['clients'][1]['name'])
# ]
# )
# session.commit()
#
# session.add_all([
#     Marks(id = data_marks['marks'][0]['id'],
#             mark_value = data_marks['marks'][0]['value'],
#           client_id = data_marks['marks'][0]['id_client'],
#           dish_id = data_marks['marks'][1]['id_dish'],
#           text_reviw = data_marks['marks'][1]['text_reviw'],
#           user_name = data_marks['marks'][1]['name'])]
# )
# session.commit()
# #

#
#
