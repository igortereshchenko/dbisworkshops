from sqlalchemy import create_engine, Sequence, Column, Integer, String, Float, ForeignKey

from sqlalchemy.ext.declarative import declarative_base



oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(
    oracle_connection_string.format(

        username="SYS as sysdba",
        password="dbpass",
        sid="XE",
        host="laptop",
        port="1521",
        database="workshopDB"

    )
    , echo=True
)


Base = declarative_base()

class menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Meal(Base):
    __tablename__ = 'meal'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(15), nullable=False)
    price = Column(Float, nullable=False)
    taste = Column(String(15), nullable=False)                  # key word to be searched
    risk_name = Column(String(25), ForeignKey('risk.name'))        # any risks like allergic etc

    def __init__(self, id, name, price, meal_id, taste, risk_name):
        self.id = id
        self.name = name
        self.price = price
        self.meal_id = meal_id
        self.taste = taste
        self.risk_name = risk_name


class menu_meal(Base):
    __tablename__ = 'menu_meal'

    menu_id = Column(Integer, ForeignKey('menu.id'), primary_key=True)
    meal_id = Column(Integer, ForeignKey('meal.id'), primary_key=True)

    def __init__(self, menu_id, meal_id):
        self.menu_id = menu_id
        self.meal_id = meal_id



class risk(Base):
    __tablename__ = 'risk'

    name = Column(String(25), primary_key=True)
    description = Column(String(100), nullable=False)


    def __init__(self, name, description):
        self.name = name
        self.description = description


class meal_risk(Base):
    __tablename__ = 'meal_risk'

    meal_id = Column(Integer, ForeignKey('meal.id'), primary_key=True)
    risk_name = Column(String(25), ForeignKey('risk.name'), primary_key=True)

    def __init__(self, menu_id, meal_id):
        self.menu_id = menu_id
        self.meal_id = meal_id




Base.metadata.create_all(engine)
