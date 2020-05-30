from sqlalchemy import Column, Integer, Float,String, ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Cafes(Base):
    __tablename__ = 'cafes'

    cafe_id = Column(Integer, primary_key=True)
    cafe_name = Column(String, nullable=False)
    cafe_popularity = Column(Float, nullable=False)

    order = relationship('Orders', back_populates = 'cafes')

    def __init__(self, name, pop):
        self.cafe_name = name
        self.cafe_popularity = pop


class Dishes(Base):
    __tablename__ = 'dishes'

    dish_id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer, ForeignKey('cafes.cafe_id'), nullable=False)
    dish_name = Column(String, nullable=False)
    dish_price = Column(Float, nullable=False)
    dish_describe = Column(String, nullable=False)
    dish_avg_time = Column(Float, nullable=False)

    order = relationship('Orders', back_populates = 'dish')

    def __init__(self, name, cafe, price, desc, time):
        self.dish_name = name
        self.cafe_id = cafe
        self.dish_price = price
        self.dish_describe = desc
        self.dish_avg_time = time


class Orders(Base):
    __tablename__ = 'orders'

    row_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    dish_id = Column(Integer, ForeignKey('dishes.dish_id'), nullable=False)
    cafe_id = Column(Integer, ForeignKey('cafes.cafe_id'), nullable=False)
    amount_dishes = Column(Integer, nullable=False)
    avg_time = Column(Float, nullable=False)

    dish = relationship('Dishes', back_populates='order')
    queue = relationship('Queue', back_populates='orders')
    cafes = relationship('Cafes', back_populates='order')

    def __init__(self, order_id, dish_id, cafe_id, amount_dishes, avg_time):
        self.order_id = order_id
        self.dish_id = dish_id
        self.cafe_id = cafe_id
        self.amount_dishes = amount_dishes
        self.avg_time = avg_time


class Queue(Base):
    __tablename__ = 'queue'

    queue_index = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    order_time = Column(Integer, nullable=False)

    orders = relationship('Orders', back_populates='queue')

    def __init__(self, order_id, time):
        self.order_id =  order_id
        self.order_time = time



Base.metadata.create_all(engine)