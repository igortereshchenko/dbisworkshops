from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import func, update
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
    resources = relationship("Resources")

    def __init__(self, user_id, user_name, user_date):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date = user_date


class Resources(Base):
    __tablename__ = 'resources'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    location_ = Column(String(50), CheckConstraint('length(location_) > 0'), nullable=False)
    category_ = Column(String(50), CheckConstraint('length(category_) > 0'), nullable=False)

    def __init__(self, user_id, location_, category_):
        self.user_id = user_id
        self.location_ = location_
        self.category_ = category_


Base.metadata.create_all(engine)

if __name__ == '__main__':
    boban = User(user_id=12313, user_name="Boban", user_date=func.current_date()-1)
    bobovich = User(user_id=212321, user_name="Bobovich", user_date=func.current_date())
    bobenko = User(user_id=3333, user_name="Bobenko", user_date=func.current_date()-1)
    boban_res = Resources(user_id=12313, location_="Germany", category_="games")
    bobovich_res = Resources(user_id=212321, location_="UK", category_="business")
    bobenko_res = Resources(user_id=3333, location_='UK', category_='business')
    bober = User(user_id=666, user_name="bober", user_date=func.current_date()-2)
    bober_res = Resources(user_id=666, location_='ua', category_='general')

    try:
        new_users = [boban, bobovich, bobenko, bobovich_res, boban_res, bobenko_res, bober, bober_res]
        for i in new_users:
            session.add(i)
            session.commit()
    except Exception as e:
        print(e)

    q = '''
    Select count(distinct user_id) As dau, USER_DATE 
    from users
    group by USER_DATE
    '''

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
    df = df.groupby(by='Date', as_index=False).sum()
    print(df)
    fig = px.line(df, x='Date', y='Users')
    fig.show()
    query = '''
    Select count(DISTINCT users.user_id) as amount, resources.location_
    FROM users JOIN RESOURCES ON users.user_id = RESOURCES.USER_ID
    GROUP BY resources.location_
    '''
    res = session.execute(query)
    nfo = [row for row in res]
    print(nfo)
    x = []
    y = []
    for i in nfo:
        x.append(i[0])
        y.append(i[1])
    df_1 = pd.DataFrame({'Amount': x, 'Location': y})
    print(df_1)
    fig1 = px.pie(df_1, values='Amount', names='Location', title='Amount of users slided by countries')
    fig1.show()

