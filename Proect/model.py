from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from OracleDb import *

Base = declarative_base()
db = OracleDb()


class app_user(Base):
    __tablename__ = 'app_user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    user_age = Column(Integer, nullable=False)
    user_phone = Column(String(30), unique=True)
    user_mail = Column(String(30), unique=True)
    user_bank = Column(Integer, unique=True)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, age, phone, mail, bank, orders_num, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = app_user(user_id=new_id,
                            user_name=name,
                            user_age=age,
                            user_phone=phone,
                            user_mail=mail,
                            user_bank=bank,
                            orders_num=orders_num)
        session.add(new_user)
        session.commit()


class orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('app_user.user_id'), nullable=False)
    dish_id = Column(Integer, ForeignKey('dishes.dish_id'), nullable=False)
    price = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, dish_name, phone, new_id=None, price=None):
        db = OracleDb()
        session = db.sqlalchemy_session

        ids = session.query(films).filter(dishes.dish_name == dish_name)
        id_dish = [row.dish_id for row in ids][0]
        idu = session.query(app_user).filter(app_user.user_phone == phone)
        id_user = [row.user_id for row in idu][0]
        new_order = orders(order_id=new_id,
                           user_id=id_user,
                           dish_id=id_dish,
                           price=(dish_price + snack_price)
                           )

        session.add(new_order)
        session.commit()


class dish(Base):
    __tablename__ = 'dishes'
    dish_id = Column(Integer, primary_key=True)
    dish_name = Column(String(30), nullable=False)
    dish_description = Column(String(30), nullable=True)
    dish_rate = Column(Integer, nullable=True)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, orders_num, new_id=None, description=None, rate=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_dish = dishes(dish_id=new_id,
                         dish_name=name,
                         dish_description=description,
                         dish_rate=rate,
                         orders_num=orders_num)
        session.add(new_film)
        session.commit()


class comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    film = Column(String(30), nullable=False)
    comment_text = Column(String(30), nullable=False)
    film_rate = Column(Integer, nullable=True)

    @classmethod
    def add_member(self, film, text, new_id=None, rate=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_comment = comments(comment_id=new_id,
                               film=film,
                               comment_text=text,
                               film_rate=rate)
        session.add(new_comment)
        session.commit()


Base.metadata.create_all(db.sqlalchemy_engine) 
