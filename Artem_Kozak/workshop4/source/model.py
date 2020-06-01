from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from source.DB_WORKSHOPS import *

Base = declarative_base()
db = OracleDb()


class Users_list(Base):
    __tablename__ = 'users_list'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=True)
    purchased_items = relationship('Purchased_items_list', secondary='purchased_users')
    wish_items = relationship('Wish_items_list', secondary='wish_users')

    @classmethod
    def add(self, user_id, user_name, first_name, last_name):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = Users_list(
            user_id=user_id,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
        )
        session.add(new_user)
        session.commit()


class Purchased_items_list(Base):
    __tablename__ = 'purchased_items_list'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(30), nullable=False)
    photo_url = Column(String(100), nullable=False)
    item_price = Column(Integer, nullable=False)
    user = relationship('Users_list', secondary='purchased_users')

    @classmethod
    def add(self, item_id, item_name, photo_url, item_price):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_item = Purchased_items_list(
            item_id=item_id,
            item_name=item_name,
            photo_url=photo_url,
            item_price=item_price,
        )
        session.add(new_item)
        session.commit()


class Wish_items_list(Base):
    __tablename__ = 'wish_items_list'
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String(30), nullable=False)
    photo_url = Column(String(100), nullable=False)
    item_price = Column(Integer, nullable=False)
    user = relationship('Users_list', secondary='wish_users')

    @classmethod
    def add(self, item_id, item_name, photo_url, item_price):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_item = Wish_items_list(
            item_id=item_id,
            item_name=item_name,
            photo_url=photo_url,
            item_price=item_price,
        )
        session.add(new_item)
        session.commit()


class Purchased_users(Base):
    __tablename__ = 'purchased_users'
    item_id = Column(Integer, ForeignKey('purchased_items_list.item_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users_list.user_id'), primary_key=True)


class Expec_users(Base):
    __tablename__ = 'wish_users'
    item_id = Column(Integer, ForeignKey('wish_items_list.item_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users_list.user_id'), primary_key=True)


Base.metadata.create_all(db.sqlalchemy_engine)
