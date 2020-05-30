from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from oracledb import *

Base = declarative_base()
db = OracleDb()

class Users(Base):

    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))

class Country(Base):

    __tablename__ = 'Country'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class NumbersAid(Base):

    __tablename__ = 'NumbersAid'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))


class Hospital(Base):

    __tablename__ = 'Hospital'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    adres = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))
    
    
class Symptom(Base):

    __tablename__ = 'Symptom'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    Description = Column(String(1000), nullable=False)
    
    
class Note(Base):

    __tablename__ = 'Note'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    Description = Column(String(1000), nullable=False)
    
    def _repr_(self):
        return '<Note %r>' % self.id

    
Base.metadata.create_all(db.sqlalchemy_engine)