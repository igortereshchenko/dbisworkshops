from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import func
import plotly.express as px
import pandas as pd
import numpy as np

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/?service_name={database}'

engine = create_engine(
    oracle_connection_string.format(
        username="MYDATABASE",
        password="qwert123",
        hostname="localhost",
        port='1521',
        database='XE'
    )
)


Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(40), nullable=False)
    user_date = Column(Date, nullable=True)
    age = Column(Integer, CheckConstraint('age > 14', name='check_age'), nullable=True)
    resources = relationship("Resources")

    def __init__(self, user_id, user_name, user_date, age):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date = user_date
        self.age = age


class Resources(Base):
    __tablename__ = 'resources'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    location_ = Column(String(50), CheckConstraint('length(location_) > 0'), nullable=False)
    category_ = Column(String(50), CheckConstraint('length(category_) > 0'), nullable=False)

    def __init__(self, location_, category_):
        self.location_ = location_
        self.category_ = category_


Base.metadata.create_all(engine)


boban = User(user_id=12313, user_name="Boban", user_date=func.current_date()-2, age=15)
bobovich = User(user_id=212321, user_name="Bobovich", user_date=func.current_date(), age=17)
bobenko = User(user_id=3333, user_name="Bobenko", user_date=func.current_date()-3, age=18)
Boba = User(user_id=666, user_name="Boba", user_date=func.current_date(), age=23)
boban_res = Resources(location_="Germany", category_="games")
bobovich_res = Resources(location_="UK", category_="business")
bobenko_res = Resources(location_='LA', category_='general')
borb_res = Resources(location_="LO", category_='general')
bobenko.resources.append(bobenko_res)
boban.resources.append(bobovich_res)
bobovich.resources.append(boban_res)
Boba.resources.append(borb_res)

try:
    new_users = [boban, bobovich, bobenko, Boba]
    for i in new_users:
        session.add(i)
        session.commit()
except Exception as e:
    print(e)
session.query(Resources).filter(Resources.user_id == 12313).delete()
session.commit()
session.query(User).filter(User.user_id == 12313).delete()
session.commit()
session.query(Resources).filter(Resources.user_id == 3333).update({Resources.category_: 'general',
                                                                   Resources.location_: 'ua'})
session.commit()

q = '''Select count(distinct user_id) As dau, USER_DATE 
from users
group by USER_DATE'''
result = session.execute(q)
x = []
y = []
nfo = [row for row in result]
for i in nfo:
    x.append(i[0])
    val = str(i[1]).split()[0]
    val = np.datetime64(val)
    y.append(val)

df = pd.DataFrame({'Users': x, 'Date': y})
print(df)
fig = px.line(df, x='Date', y='Users')
fig.show()

