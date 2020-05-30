
import datetime
from sqlalchemy import create_engine, ForeignKey, Sequence, CheckConstraint
from sqlalchemy import Column, Date, Integer, String, Boolean, DateTime, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="SYSTEM",
        password="Oracle",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECT",

    )
    , echo=True
)

Base = declarative_base()

class Expenditure (Base):
    __tablename__ = 'expenditure'
    expend_id = Column(Integer, Sequence('id_seq'), primary_key=True)
    time = Column(String(50))
    cost_value = Column(Float, CheckConstraint('cost_value >= 1'))
    category_name = Column(String(50), ForeignKey('buy_category.category_name'), primary_key= True)
    card_number = Column(Integer, ForeignKey('card.card_number'), primary_key= True)

    def __init__(self, time, cost_value, category_name, card_number):
        """"""
        self.time = time
        self.cost_value = cost_value
        self.category_name = category_name
        self.card_number = card_number

class Category(Base):
    __tablename__ = 'buy_category'
    category_id = Column(Integer, Sequence('id_seq'))
    category_name = Column(String(50), primary_key=True)
    limit_value = Column(Float)

class Card(Base):
    __tablename__ = 'card'
    card_number = Column(Integer, CheckConstraint('card_number >=1000000000000000'), primary_key=True)
    money_amount = Column(Integer)

    def __init__(self, card_number, money_amount):
        """"""
        self.card_number = card_number
        self.money_amount = money_amount


# create tables
Base.metadata.create_all(engine)