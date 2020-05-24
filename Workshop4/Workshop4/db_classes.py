from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
import json

Base = declarative_base()

from sqlalchemy.orm import relationship, sessionmaker

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

    styles = relationship('Clients', backref='marks', lazy=True)
    styles_1 = relationship('Dishes', backref='marks', lazy=True)



Session = sessionmaker(bind = engine)
session = Session()

categories = open("C:/Pyprojects/venv/categories.json",encoding="utf-8")
data_categories = json.load(categories)

dishes = open("C:/Pyprojects/venv/recipes.json",encoding="utf8")
data_dishes = json.load(dishes)

session.add_all([
   Categories(id = data_categories['categories'][0]['id'], category_name = data_categories['categories'][0]['name']),
   Categories(id = data_categories['categories'][1]['id'], category_name = data_categories['categories'][1]['name']),
   Categories(id = data_categories['categories'][2]['id'], category_name = data_categories['categories'][2]['name']),
   Categories(id = data_categories['categories'][3]['id'], category_name = data_categories['categories'][3]['name'])]
)

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
           ingridients=data_dishes['dish'][3]['ingridients'])]
)

session.commit()


