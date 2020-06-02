from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
from datetime import datetime

Base = declarative_base()

class Lessons(Base):
    __tablename__ = 'Lessons'
    id_lesson = Column(Integer, primary_key=True)
    name_of_lesson = Column(String(60), nullable=False)


class Groups(Base):
    __tablename__ = "Groups"
    Groups_id= Column(Integer, primary_key=True)
    name_g = Column(String(60), nullable=False)
    entrance_year = Column(Integer, nullable=False)
    grad_year = Column(Integer, nullable=False)

class Student(Base):
    __tablename__ = 'Student'
    st_id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    group = Column(Integer, ForeignKey('Groups.Groups_id'))



class Teacher(Base):
    __tablename__ = 'Teacher'
    t_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)

class Audience(Base):
    __tablename__ = 'Audience'
    building_num = Column(Integer, nullable=False)
    audience_num = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    Audience_id = Column(Integer, primary_key=True)

class Schedule(Base):
    __tablename__ = 'Schedule'
    lesson = Column(Integer, ForeignKey('Lessons.id_lesson'))
    audience = Column(Integer, ForeignKey('Audience.Audience_id'))
    date = Column(DateTime, primary_key=True, default = datetime.utcnow)
    term = Column(Integer, nullable=False)
    group = Column(Integer, ForeignKey('Groups.Groups_id'))
    teacher = Column(Integer, ForeignKey('Teacher.t_id'))




Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)
