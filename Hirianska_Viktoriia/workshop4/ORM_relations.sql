from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sql_connection import engine
import json

from sqlalchemy.util import symbol

Base = declarative_base()

class U_USER(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_username = Column(String(50))


class SERIES(Base):

    __tablename__ = 'series'

    id = Column(Integer, primary_key=True)
    series_title = Column(String(128))
    series_genre = Column(String(128))
    series_year = Column(Integer)
    series_country = Column(String(128))
    series_amountofseasons = Column(Integer)
    series_duration = Column(Integer)
    series_description = Column(String(512))


class GRADE(Base):

    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True)
    grade_value = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    series_id = Column(Integer, ForeignKey("series.id"))
    reviw = Column(String(200))

    styles = relationship('U_USER', backref='grade', lazy=True)
    styles_ = relationship('SERIES', backref='grade', lazy=True)



Session = sessionmaker(bind = engine)
session = Session()

series = open("C:/Users/Strawika/Desktop/workshop4/series.json",encoding="utf-8")
data_series = json.load(series)

session.add_all([
    SERIES(id = data_series['series'][0]['id'],
           series_title = data_series['series'][0]['series_title'],
           series_genre = data_series['series'][0]['series_genre'],
           series_year = data_series['series'][0]['series_year'],
           series_country = data_series['series'][0]['series_country'],
           series_amountofseasons = data_series['series'][0]['series_amountofseasons'],
           series_duration=data_series['series'][0]['series_duration'],
           series_description = data_series['series'][0]['series_description']),

    SERIES(id = data_series['series'][1]['id'],
           series_title = data_series['series'][1]['series_title'],
           series_genre = data_series['series'][1]['series_genre'],
           series_year = data_series['series'][1]['series_year'],
           series_country = data_series['series'][1]['series_country'],
           series_amountofseasons = data_series['series'][1]['series_amountofseasons'],
           series_duration = data_series['series'][1]['series_duration'],
           series_description = data_series['series'][1]['series_description']),

    SERIES(id = data_series['series'][2]['id'],
           series_title = data_series['series'][2]['series_title'],
           series_genre = data_series['series'][2]['series_genre'],
           series_year = data_series['series'][2]['series_year'],
           series_country = data_series['series'][2]['series_country'],
           series_amountofseasons = data_series['series'][2]['series_amountofseasons'],
		   series_duration = data_series['series'][2]['series_duration'],
		   series_description = data_series['series'][2]['series_description']),
]
)

session.commit()