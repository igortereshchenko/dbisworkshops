from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine

Base = declarative_base()


class UserProfile(Base):

    __tablename__ = 'UserProfile'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    user_phone = Column(String(14), nullable=False, unique=True)
    user_email = Column(String(30), nullable=False, unique=True)


class Card(Base):

    __tablename__ = 'Card'

    user_id_fk = Column(Integer, ForeignKey('UserProfile.user_id'))
    card_number = Column(String(16), primary_key=True)
    card_name = Column(String(50))
    card_date = Column(Date, nullable=False)
    card_ccv = Column(String(3), nullable=False)


class Supply(Base):

    __tablename__ = 'Supply'

    user_id_fk = Column(Integer, ForeignKey('UserProfile.user_id'), primary_key=True)
    water_supply_id = Column(Integer, nullable=False, unique=True)
    power_supply_id = Column(Integer, nullable=False, unique=True)
    gas_supply_id = Column(Integer, nullable=False, unique=True)


class WaterSupply(Base):

    __tablename__ = 'WaterSupply'

    water_supply_id = Column(Integer, ForeignKey('Supply.water_supply_id'), primary_key=True)
    filling_date = Column(Date,  primary_key=True)

    water_hot_previous = Column(Float)
    water_hot_current = Column(Float)
    water_cold_previous = Column(Float)
    water_cold_current = Column(Float)


class PowerSupply(Base):

    __tablename__ = 'PowerSupply'

    power_supply_id = Column(Integer, ForeignKey('Supply.power_supply_id'), primary_key=True)
    filling_date = Column(Date,  primary_key=True)

    power_reading = Column(Float, nullable=False)


class GasSupply(Base):

    __tablename__ = 'GasSupply'

    gas_supply_id = Column(Integer, ForeignKey('Supply.gas_supply_id'), primary_key=True)
    filling_date = Column(Date,  primary_key=True)

    gas_reading = Column(Float, nullable=False)


Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)