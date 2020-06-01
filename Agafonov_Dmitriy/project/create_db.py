import datetime
from sqlalchemy import create_engine, ForeignKey, Sequence, CheckConstraint
from sqlalchemy import Column, Date, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="PROJECTDB",
        password="oracle123",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECTDB",

    )
    , echo=True
)

Base = declarative_base()


class user_database(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_name = Column(String(100), nullable=False)
    user_mail = Column(String(100), nullable=False, unique=True)
    user_age = Column(Integer, CheckConstraint('user_age >= 18'), nullable=False)
    edrpou = Column(String(100), CheckConstraint('LENGTH(edrpou) = 6'), nullable=False, unique=True)
    user_pass = Column(String(100), CheckConstraint('LENGTH(user_pass) >= 5'), nullable=False)

    def __init__(self, user_name, user_mail, user_age, edrpou, user_pass):
        """"""
        self.user_name = user_name
        self.user_mail = user_mail
        self.user_age = user_age
        self.edrpou = edrpou
        self.user_pass = user_pass


class user_question(Base):
    __tablename__ = 'question_table'

    question_id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user_table.id'))
    question_reference = Column(String(20))
    question = Column(String(200))
    time_creating = Column(String(20), nullable=False)
    status = Column(Boolean, nullable=False)

    def __init__(self, user_id, question_reference, question, time_creating, status):
        """"""
        self.user_id = user_id
        self.question_reference = question_reference
        self.question = question
        self.time_creating = time_creating
        self.status = status


# create tables
Base.metadata.create_all(engine)