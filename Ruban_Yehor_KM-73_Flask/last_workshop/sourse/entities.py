from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from db_connection import engine


Base = declarative_base()


class Customers(Base):

    __tablename__ = 'Customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30))
    phone = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    UniqueConstraint(email)


class Restaurants(Base):

    __tablename__ = 'Restaurants'

    id = Column(String(30), nullable=False, primary_key=True)
    title = Column(String(30), nullable=False, primary_key=True)
    phone = Column(String(30), nullable=False)
    email = Column(String(30))
    adress = Column(String(30))
    UniqueConstraint(email)


class Menu(Base):

    __tablename__ = 'Menu'

    meal_title = Column(String(30), primary_key=True)
    restaurant = Column(String(30), primary_key=True)
    info = Column(Text())
    price = Column(Float)


class Orders(Base):

    __tablename__ = 'Orders'

    order_id = Column(String(30), nullable=False, primary_key=True)
    order_title = Column(String(30), nullable=False)
    order_name = Column(String(30))
    time = Column(DateTime())


class History(Base):

    __tablename__ = 'History'

    rest_title = Column(String(30), primary_key=True)
    name = Column(String(30), primary_key=True)
    date = Column(DateTime(), primary_key=True)
    details = Column(Text())




Base.metadata.create_all(engine)