from sqlalchemy import Column, Integer, Float,String, ForeignKey,Sequence
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price



class Risk(Base):
    __tablename__ = 'risk'

    name = Column(String(25), primary_key=True)
    description = Column(String(100), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description




class Meal(Base):
    __tablename__ = 'meal'

    meal_id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)
    taste = Column(String(15), nullable=False)                  # key word to be searched
    risk_name = Column(String(25), ForeignKey('risk.name'))        # any risks like allergic etc

    def __init__(self, meal_id, name, price, taste, risk_name):
        self.meal_id = meal_id
        self.name = name
        self.price = price
        self.taste = taste
        self.risk_name = risk_name



class MenuMeal(Base):
    __tablename__ = 'menu_meal'

    menu_id = Column(Integer, ForeignKey('menu.id'), primary_key=True)
    meal_id = Column(Integer, ForeignKey('meal.meal_id'), primary_key=True)

    def __init__(self, menu_id, meal_id):
        self.menu_id = menu_id
        self.meal_id = meal_id




class MealRisk(Base):
    __tablename__ = 'meal_risk'

    meal_id = Column(Integer, ForeignKey('meal.meal_id'), primary_key=True)
    risk_name = Column(String(25), ForeignKey('risk.name'), primary_key=True)

    def __init__(self, menu_id, meal_id):
        self.menu_id = menu_id
        self.meal_id = meal_id




class Test(Base):
    __tablename__ = 'test'

    col1 = Column(Integer, primary_key=True, nullable=False)
    col2 = Column(Integer, nullable=False)



Base.metadata.create_all(engine)