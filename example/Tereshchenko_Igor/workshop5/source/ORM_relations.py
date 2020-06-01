from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from root.source.db_connection import *

Base = declarative_base()
db = OracleDb()

class orm_users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_login = Column(String(20), nullable=False, unique=True)
    user_password = Column(String(30), nullable=False)
    user_type = Column(Integer, nullable=False)

    config_relationship = relationship('orm_config')
    items_relationship = relationship('orm_items')
    action_relationship = relationship('orm_actions')

    @classmethod
    def add(self, user_login, user_password, user_type):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = self(
            user_login=user_login,
            user_password=user_password,
            user_type=user_type,
        )
        session.add(new_user)
        session.commit()
        return new_user


class orm_config(Base):
    __tablename__ = 'user_config'

    id = Column(Integer, primary_key=True)
    user_id_fk = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)
    balance = Column(Integer, nullable=False)
    profit_percent = Column(Integer, nullable=False)
    min_price = Column(Integer, nullable=False)
    max_price = Column(Integer, nullable=False)
    daily_sales = Column(Integer, nullable=False)
    balance_to_stop = Column(Integer, nullable=False)
    max_items_in_inventory = Column(Integer, nullable=False)


    @classmethod
    def add(self, user_id_fk, balance, profit_percent, min_price, max_price, daily_sales, balance_to_stop,max_items_in_inventory):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_config = self(
            user_id_fk=user_id_fk,
            balance=balance,
            profit_percent=profit_percent,
            min_price=min_price,
            max_price=max_price,
            daily_sales=daily_sales,
            balance_to_stop=balance_to_stop,
            max_items_in_inventory=max_items_in_inventory,
        )
        session.add(new_config)
        session.commit()
        return new_config

class orm_items(Base):
    __tablename__ = 'user_items'

    id = Column(Integer, primary_key=True)
    user_id_fk = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)
    action = Column(String(20), nullable=False)

    @classmethod
    def add(self, user_id_fk, name, price, action):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_item = self(
            user_id_fk=user_id_fk,
            name=name,
            price=price,
            action=action,
        )
        session.add(new_item)
        session.commit()
        return new_item


class orm_actions(Base):
    __tablename__ = 'user_actions'

    id = Column(Integer, primary_key=True)
    user_id_fk = Column(Integer, ForeignKey('users.id'), nullable=False)
    action_type = Column(String(20), nullable=False)
    action_date = Column(Date, nullable=False)

    @classmethod
    def add(self, user_id_fk, action_type, action_date):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_action = self(
            user_id_fk=user_id_fk,
            action_type=action_type,
            action_date=action_date,
        )
        session.add(new_action)
        session.commit()
        return new_action

Base.metadata.create_all(db.sqlalchemy_engine)


