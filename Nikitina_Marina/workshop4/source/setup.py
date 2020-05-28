from sqlalchemy import create_engine, ForeignKey, Sequence, CheckConstraint
from sqlalchemy import Column, Date, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="SYSTEM",
        password="bars",
        sid="XE",
        host="localhost",
        port="1521",
        database="XE",

    )
    , echo=True
)

Base = declarative_base()

class clients(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, Sequence('id_seq'), nullable=False, unique=True)
    client_phone = Column(String(13), CheckConstraint('length(client_phone) = 13'), primary_key=True)
    client_nickname = Column(String(30), nullable=False, unique=True)
    client_pass = Column(String(30), nullable=False)
    client_age = Column(Integer, CheckConstraint('client_age >= 18'), nullable=False)

    def __init__(self,  phone, nickname, client_pass, age, new_id=None):
        self.client_phone = phone
        self.client_nickname = nickname
        self.client_pass = client_pass
        self.client_age = age

class events(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, nullable=False)
    event_name = Column(String(30), nullable=False,  primary_key=True)
    event_tag = Column(String(30), nullable=False)
    reg_date_start = Column(DateTime, nullable=False)
    reg_date_finish = Column(DateTime, nullable=False)
    quantity_tic = Column(Integer,  nullable=False)
    event_time = Column(DateTime,  nullable=False)
    price = Column(Integer, nullable=False)

    def __init__(self, name, tag, date_start, date_finish, quantity_tic, event_time, price, new_id=None):
        self.event_name = name
        self.event_tag = tag
        self.reg_date_start = date_start
        self.reg_date_finish = date_finish
        self.quantity_tic = quantity_tic
        self.event_time = event_time
        self.price = price

class guests(Base):
    __tablename__ = 'guests'
    client_phone = Column(String(13), ForeignKey('clients.client_phone'), nullable=False, primary_key=True)
    event_name = Column(String(30), ForeignKey('events.event_name'), nullable=False, primary_key=True)
    event_time = Column(DateTime, nullable=False, primary_key=True)

    def __init__(self, client_phone, event_name, event_time):
        self.client_phone = client_phone
        self.event_name = event_name
        self.event_time = event_time


# create tables
Base.metadata.create_all(engine)