from sqlalchemy import Column, Integer, Float,String, ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from orm.database_connection import  engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Dishes(Base):
	__tablename__ = 'dishes'
	dish_id = Column(Integer, primary_key=True)
	dish_name = Column(String, nullable=False)
	dish_price = Column(Float, nullable=False)
	dish_describe = Column(String, nullable=False)

	order = relationship('Orders', back_populates = 'order_dish')


class Orders(Base):
	__tablename__ = 'orders'
	order_id = Column(Integer, primary_key=True)
	dish_id = Column(Integer, ForeignKey('dishes.dish_id'), nullable=False)
	user_phone = Column(String, nullable=False)
	user_name = Column(String, nullable=False)
	amount_dishes = Column(Integer, nullable=False)

	order_dish = relationship('Dishes', back_populates='order')


Base.metadata.create_all(engine)

