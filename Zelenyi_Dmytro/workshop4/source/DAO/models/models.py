from sqlalchemy import Integer, String, Text, Column, MetaData, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType
from Zelenyi_Dmytro.workshop4.source.database_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import re
Base = declarative_base()
meta = MetaData()


class photographers(Base):
    __tablename__ = 'photographers'

    email = Column(String(30), primary_key=True, nullable=False)
    user_password = Column(String(30), nullable=False)
    photographer_name = Column(String(30), nullable=False)
    photographer_surname = Column(String(30))
    gender = Column(String(20), nullable=False)
    about_photographer = Column(Text(), nullable=False)
    birthday = Column(DateTime)
    experience = Column(Integer, nullable=False)
    region = Column(String(30), nullable=False)
    city = Column(String, nullable=False)
    is_premium = Column(String(1))

    CheckConstraint('experience > 0', name='check_experience')







Base.metadata.create_all(engine)
